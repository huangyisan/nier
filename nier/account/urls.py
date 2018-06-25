from django.conf.urls import url
from django.views.generic import TemplateView

from .views import RegisterView, ActiveView, LoginView, UserListView, AccountInfoView

app_name = 'account'

urlpatterns = [
url(r'^register/', RegisterView.as_view(), name="register"),
url(r'^active/', ActiveView.as_view(), name="active"),
url(r'^login/', LoginView.as_view(), name="login"),
url(r'^info/', TemplateView.as_view(template_name="account_info.html"), name="account_info"),
# url(r'^account_info/', AccountInfoView.as_view(), name="account_i1nfo"),
]