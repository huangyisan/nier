from django.conf.urls import url

from .views import AddAssetView, RemoveAssetView, DelAssetView, get_ecslist

app_name = 'assets'

urlpatterns = [
url(r'addasset/', AddAssetView.as_view(), name="addasset"),
url(r'removeasset/', RemoveAssetView.as_view(), name="removeasset"),
url(r'delasset/', DelAssetView.as_view(), name="delasset"),
# ajax 请求ecs数据保留地址
url(r'get_ecslist/', get_ecslist, name="get_ecslist"),
        ]