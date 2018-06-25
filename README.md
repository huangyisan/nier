### pythen version 3.6.0

### django version 1.11.0

### 数据库准备：
> CREATE DATABASE `nier_db` /*!40100 DEFAULT CHARACTER SET utf8 */

### 需要pymysql支持

### 假数据
>python3 manage.py shell

>from django.contrib.auth.models import User

>User.objects.create_user('admin', '861987227@qq.com', '123456')

* 扩展数据
>from account.models import UserInfo

>import datetime

>createtime=datetime.date(1970,1,1)

>from django.utils import timezone

>u = User.objects.get(username='admin')

>UserInfo.objects.create(user=u, role=1, createtime=createtime, logintime=timezone.now(), validkey='123456', status=1)


### account
* 注册
    * active url: http://x.x.x.x/active/?username='xxx'&validkey='yyy'
    * todo:
        * 验证码过期时间
        * 重新验证
* 登陆
    * 成功跳转到index.html，根据权限展现内容
    * 未激活则跳转到userinfo.html，需要进行重新邮件验证
* 退出
