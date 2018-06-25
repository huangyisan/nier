from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User

class UserInfo(models.Model):
    create_by_role = (
        (1, '未激活'),
        (2, '激活'),
    )

    user = models.OneToOneField(User)
    # role  1 admin 2 normal
    role = models.IntegerField(default=2, choices=create_by_role)
    group = models.CharField(max_length=64, default='')
    createtime = models.DateField()
    logintime = models.DateField(default='1970-01-01')
    validkey = models.CharField(max_length=256)
    # role status   0:no active 1:active 2:ban
    status = models.IntegerField(default=0)
    avatar = models.CharField(max_length=256, default='')

    def get_user_info(self,username):
        User.objects.get(username=username)

    def get_role(self):
        if self.role == 1:
            return '超级用户'
        else:
            return '普通用户'

    def get_status(self):
        if self.role == 0:
            return '未激活'
        else:
            return '激活'



