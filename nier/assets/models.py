from django.db import models
from django.forms import ModelForm

# Create your models here.

class Asset(models.Model):
    '''总资产'''
    asset_type_choice = (
        ('server', '服务器'),
        ('slb', '负载均衡'),
        ('rds', '阿里云rds'),
        ('other', '阿里云其他资产'),
        ('company', '公司资产'),
    )

    asset_region_choice = (
        ('cn-qingdao', '华北1'),
        ('cn-beijing', '华北2'),
        ('cn-zhangjiakou', '华北3'),
        ('cn-huhehaote', '华北5'),
        ('cn-hangzhou', '华东1'),
        ('cn-shanghai', '华东2'),
        ('cn-shenzhen', '华南1'),
        ('company', '公司'),
    )

    asset_networktype_choice = (
        ('classic', '经典网络'),
        ('vpc', '专有网络'),
        ('inner', '公司内网'),
    )

    asset_status_choice = (
        ('running', '在线'),
        ('stop', '下线'),
        ('unknow', '未知'),
    )

    show_status_choice = (
        (1, '确认'),
        (0, '待确认'),
        (2, '删除'),
    )


    asset_type = models.CharField(max_length=64, default='server', choices=asset_type_choice, verbose_name='资产类型')
    region = models.CharField(max_length=64, default='cn-shanghai', choices=asset_region_choice, verbose_name='所属地域')
    instance_id = models.CharField(max_length=64,unique=True, null=True, blank=True, verbose_name='实例ID')
    instance_type = models.CharField(max_length=16, null=True, blank=True, verbose_name='实例类型')
    name = models.CharField(max_length=64, null=True, blank=True, verbose_name='资产名称')
    status = models.CharField(max_length=16, default='running', choices=asset_status_choice, verbose_name='资产状态')
    create_day = models.DateField(null=True, blank=True, verbose_name='创建日期')
    expire_day = models.DateField(null=True, blank=True, verbose_name='过期日期')
    show_status = models.IntegerField(default=0, choices=show_status_choice, verbose_name='确认状态')
    # 备注
    memo = models.TextField(null=True, blank=True, verbose_name='备注信息')

    def __str__(self):
        info = '<Asset:[type={type}, region={region}, instance_id={instance_id}, status={status}>'
        return info.format(asset_type = self.asset_type, region = self.region, instance_id = self.instance_id, status = self.status)



    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '资产总表'
        ordering = ['-create_day']


class Server(models.Model):
    '''服务器资产'''
    created_by_choice = (
        ('auto', '自动'),
        ('manual', '手工'),
    )

    asset = models.OneToOneField('Asset')
    created_by = models.CharField(max_length=16, default='auto',choices=created_by_choice, verbose_name='添加方式')
    in_ipaddr = models.CharField(max_length=32, null=True, blank=True, verbose_name='内网ip')
    ou_ipaddr = models.CharField(max_length=32, null=True, blank=True, verbose_name='外网ip')
    os_type = models.CharField(max_length=16, null=True, blank=True, verbose_name='操作系统类型')
    os_info = models.CharField(max_length=16, null=True, blank=True, verbose_name='操作系统信息')
    cpu_info = models.CharField(max_length=16, null=True, blank=True, verbose_name='cpu信息')
    memory_info = models.CharField(max_length=16, null=True, blank=True, verbose_name='内存信息')
    business_unit = models.CharField(max_length=128,null=True, blank=True, verbose_name='服务器用途')

    def __str__(self):
        info = '<Server:[name={name}, os_type={os_type}, os_info={os_info}, region={region}, instance_id={instance_id}]>'
        return info.format(name = self.asset.name, os_type=self.os_type, os_info=self.os_info, region=self.asset.region, instance_id=self.asset.instance_id)

    def as_dict(self):
       return {'asset_type': self.asset.get_asset_type_display(), 'name': self.asset.name, 'instance_id': self.asset.instance_id, \
                'in_ipaddr': self.in_ipaddr, 'ou_ipaddr': self.ou_ipaddr, 'os_info': self.os_info, 'cpu_info': self.cpu_info, \
                'memory_info': self.memory_info, 'region': self.asset.get_region_display(), 'status': self.asset.get_status_display(), \
                'expire_day': self.asset.expire_day.strftime('%Y-%m-%d'), 'created_by':self.get_created_by_display(), 'show_status': \
               self.asset.show_status}

    class Meta:
        verbose_name = '服务器资产表'
        verbose_name_plural = '服务器资产表'

