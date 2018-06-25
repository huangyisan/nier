from django.shortcuts import render
from django.views.generic import View, FormView, ListView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from .models import UserInfo
from .forms import RegisterForm, LoginForm, AccountInfoForm

from tools.timestamp import gen_currenttime
from tools.validkey import gen_validkey
from tools.ecs import gen_machine

from nier import settings_email



import json


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        return self._register(form)

    def _register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            email = form.cleaned_data.get('email', '')
            validkey = gen_validkey()
            try:
                with transaction.atomic():
                    new_user = User.objects.create(username=username, password=make_password(password=password, salt='yorha'), email=email)
                    UserInfo.objects.create(user=new_user, createtime=gen_currenttime(), validkey=validkey)

                    # send mail

                    send_mail(
                        'Active email',
                        'active url is http://172.16.90.104:8000/account/active/?username={0}&validkey={1}'.format(username, validkey),
                        settings_email.EMAIL_HOST_USER,
                        ['huangyisan@qmtv.com'],

                    )

                    return JsonResponse({'status': 200})
            except BaseException as e:
                return JsonResponse({'status':500, 'errors':{'server': [{'message': '服务器内部异常'}]}})
        else:
            return JsonResponse({'status': 400, 'errors':json.loads(form.errors.as_json())})

class ActiveView(View):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')

        try:
            active_user = User.objects.get(username=username)
            active_user_status = active_user.userinfo.status

            if active_user_status == 1:
                return JsonResponse({'status':400, 'message':'has been actived'})
            elif active_user_status == 2:
                return JsonResponse({'status':400, 'message':'has been baned'})
            elif active_user_status == 0 and active_user.userinfo.validkey != validkey:
                return JsonResponse({'status':400, 'message':'validkey error'})
            elif active_user_status == 0 and active_user.userinfo.validkey == validkey:
                active_user.userinfo.status = 1
                active_user.userinfo.save()
                return JsonResponse({'status':200, 'message':'active success'})
        except ObjectDoesNotExist as e:
            return JsonResponse({'status':400, 'message':'server error'})

class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        return self._login(request, form)

    def _login(self, request,form):
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user.userinfo.status)
                if user.userinfo.status == 0:
                    # 201,redirect user info page
                    return JsonResponse({'status':201})
                login(request, user)
                return JsonResponse({'status':200, 'errors':{}})
            else:
                return JsonResponse({'status': 403, 'errors': {'messages': [{'message': 'authen faild'}]}})
        else:

            return JsonResponse({'status':400, 'errors':json.loads(form.errors.as_json())})

class UserListView(ListView):
    model = UserInfo
    template_name = "table_userlist.html"

class AccountInfoView(View):
    template_name = 'userinfo.html'
    form_class = AccountInfoForm


