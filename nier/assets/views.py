from django.shortcuts import render

# Create your views here.
from .models import Asset, Server
from django.views.generic import View, ListView
from django.http import JsonResponse,HttpResponse

from django.core.exceptions import ObjectDoesNotExist

from tools.ecs import gen_machine

import json
from addict import Dict

class GetEcsInfoView(View):
    def get(self, request, *args, **kwargs):
        # ajax get ecsinfo
        if request.is_ajax():
            contents = Server.objects.order_by('-asset')
            contents = [content.as_dict() for content in contents]
            return JsonResponse({'status': 200, 'contents': contents})
        else:
            machine_list = gen_machine()
            ecs_dict = json.loads(machine_list.decode())

            #ecs_dict = {'PageNumber': 1, 'TotalCount': 3, 'PageSize': 10, 'RequestId': '3C87091C-E928-4B55-91B2-3D6375990B00', 'Instances': {'Instance': [{'InnerIpAddress': {'IpAddress': ['10.29.91.139']}, 'ImageId': 'centos_6_08_64_20G_alibase_20170824.vhd', 'InstanceTypeFamily': 'ecs.sn1', 'VlanId': '', 'InstanceId': 'i-m5ejbgrhjw5mqtyctikn', 'EipAddress': {'IpAddress': '', 'AllocationId': '', 'InternetChargeType': ''}, 'InternetMaxBandwidthIn': -1, 'ZoneId': 'cn-qingdao-b', 'InternetChargeType': 'PayByTraffic', 'SpotStrategy': 'NoSpot', 'StoppedMode': 'Not-applicable', 'SerialNumber': '7dea7192-ea38-4386-a3f0-b361f0d807b0', 'IoOptimized': True, 'Memory': 16384, 'Cpu': 8, 'VpcAttributes': {'NatIpAddress': '', 'PrivateIpAddress': {'IpAddress': []}, 'VSwitchId': '', 'VpcId': ''}, 'InternetMaxBandwidthOut': 10, 'DeviceAvailable': True, 'SecurityGroupIds': {'SecurityGroupId': ['sg-28l4uu3bw']}, 'SaleCycle': '', 'SpotPriceLimit': 0.0, 'AutoReleaseTime': '', 'StartTime': '2017-12-22T02:13Z', 'InstanceName': '广告外部', 'Description': '', 'ResourceGroupId': '', 'OSType': 'linux', 'OSName': 'CentOS  6.8 64位', 'InstanceNetworkType': 'classic', 'PublicIpAddress': {'IpAddress': ['114.215.108.225']}, 'HostName': 'iZm5ejbgrhjw5mqtyctiknZ', 'InstanceType': 'ecs.sn1.xlarge', 'CreationTime': '2017-06-14T09:35Z', 'Status': 'Running', 'ClusterId': '', 'Recyclable': False, 'RegionId': 'cn-qingdao', 'GPUSpec': '', 'DedicatedHostAttribute': {'DedicatedHostId': '', 'DedicatedHostName': ''}, 'OperationLocks': {'LockReason': []}, 'InstanceChargeType': 'PrePaid', 'GPUAmount': 0, 'ExpiredTime': '2018-06-14T16:00Z'}, {'InnerIpAddress': {'IpAddress': ['10.31.95.48']}, 'ImageId': 'centos_6_08_64_20G_alibase_20170824.vhd', 'InstanceTypeFamily': 'ecs.n4', 'VlanId': '', 'InstanceId': 'i-m5e89mz6bd3rb1l035wj', 'EipAddress': {'IpAddress': '', 'AllocationId': '', 'InternetChargeType': ''}, 'InternetMaxBandwidthIn': -1, 'ZoneId': 'cn-qingdao-b', 'InternetChargeType': 'PayByTraffic', 'SpotStrategy': 'NoSpot', 'StoppedMode': 'Not-applicable', 'SerialNumber': 'ebf30d2b-9c41-4f83-b9d1-dc0e6354340c', 'IoOptimized': True, 'Memory': 16384, 'Cpu': 8, 'VpcAttributes': {'NatIpAddress': '', 'PrivateIpAddress': {'IpAddress': []}, 'VSwitchId': '', 'VpcId': ''}, 'InternetMaxBandwidthOut': 10, 'DeviceAvailable': True, 'SecurityGroupIds': {'SecurityGroupId': ['sg-28l4uu3bw']}, 'SaleCycle': '', 'SpotPriceLimit': 0.0, 'AutoReleaseTime': '', 'StartTime': '2017-12-22T02:20Z', 'InstanceName': '广告内部_登陆入口_测试机', 'Description': '', 'ResourceGroupId': '', 'OSType': 'linux', 'OSName': 'CentOS  6.8 64位', 'InstanceNetworkType': 'classic', 'PublicIpAddress': {'IpAddress': ['121.42.139.27']}, 'HostName': 'iZm5e89mz6bd3rb1l035wjZ', 'InstanceType': 'ecs.n4.2xlarge', 'CreationTime': '2017-01-11T09:52Z', 'Status': 'Running', 'ClusterId': '', 'Recyclable': False, 'RegionId': 'cn-qingdao', 'GPUSpec': '', 'DedicatedHostAttribute': {'DedicatedHostId': '', 'DedicatedHostName': ''}, 'OperationLocks': {'LockReason': []}, 'InstanceChargeType': 'PrePaid', 'GPUAmount': 0, 'ExpiredTime': '2018-06-11T16:00Z'}, {'InnerIpAddress': {'IpAddress': ['10.45.19.78']}, 'ImageId': 'centos6u5_64_40G_cloudinit_20160427.raw', 'InstanceTypeFamily': 'ecs.c2', 'VlanId': '', 'InstanceId': 'i-28emmoscr', 'EipAddress': {'IpAddress': '', 'AllocationId': '', 'InternetChargeType': ''}, 'InternetMaxBandwidthIn': -1, 'ZoneId': 'cn-qingdao-b', 'InternetChargeType': 'PayByTraffic', 'SpotStrategy': 'NoSpot', 'StoppedMode': 'Not-applicable', 'SerialNumber': '0f0a2ffe-94a7-448a-acb7-edd2020927c5', 'IoOptimized': True, 'Memory': 16384, 'Cpu': 16, 'VpcAttributes': {'NatIpAddress': '', 'PrivateIpAddress': {'IpAddress': []}, 'VSwitchId': '', 'VpcId': ''}, 'InternetMaxBandwidthOut': 10, 'DeviceAvailable': True, 'SecurityGroupIds': {'SecurityGroupId': ['sg-28l4uu3bw']}, 'SaleCycle': '', 'SpotPriceLimit': 0.0, 'AutoReleaseTime': '', 'StartTime': '2016-08-08T16:28Z', 'InstanceName': 'qm-hb1b-cdnscript-01', 'Description': '', 'ResourceGroupId': '', 'OSType': 'linux', 'OSName': 'CentOS  6.5 64位', 'InstanceNetworkType': 'classic', 'PublicIpAddress': {'IpAddress': ['139.129.196.57']}, 'HostName': 'iZ28emmoscrZ', 'InstanceType': 'ecs.c2.medium', 'CreationTime': '2016-08-08T15:25Z', 'Status': 'Running', 'ClusterId': '', 'Recyclable': False, 'RegionId': 'cn-qingdao', 'GPUSpec': '', 'DedicatedHostAttribute': {'DedicatedHostId': '', 'DedicatedHostName': ''}, 'OperationLocks': {'LockReason': []}, 'InstanceChargeType': 'PrePaid', 'GPUAmount': 0, 'ExpiredTime': '2019-01-08T16:00Z'}]}}
            mapping = Dict(ecs_dict)
            instances = mapping.Instances.Instance
            print(instances)
            for i in instances:
                region = i.get('RegionId', 'null')
                instance_id = i.get('InstanceId', 'null')
                name = i.get('InstanceName', 'null')
                status = i.get('Status', 'null')
                create_day = i.get('CreationTime', 'null')[0:10]
                expire_day = i.get('ExpiredTime', 'null')[0:10]

                InnerIpAddress = i.get('InnerIpAddress', None)
                try:
                    in_ipaddr = InnerIpAddress.get('IpAddress', None)[0]
                except IndexError:
                    in_ipaddr = i.get('VpcAttributes', None).get('PrivateIpAddress',None).get('IpAddress',None)[0]

                PublicIpAddress = i.get('PublicIpAddress', None)
                if PublicIpAddress:
                    try:
                        ou_ipaddr = PublicIpAddress.get('IpAddress', None)[0]
                    except IndexError:

                        ou_ipaddr = i.get('EipAddress',None).get('IpAddress',None)
                else:
                    ou_ipaddr = PublicIpAddress
                os_type = i.get('OSType', 'null')
                os_info = i.get('OSName', 'null')
                cpu_info = i.get('Cpu', None)
                if cpu_info:
                    cpu_info = str(cpu_info) + 'C'

                memory_info = i.get('Memory', None)
                if memory_info:
                    memory_info = str(int(memory_info/1024)) + 'G'

                try:
                    check_instance = Asset.objects.get(instance_id=instance_id)
                except ObjectDoesNotExist:
                    new_instance = Asset.objects.create(region=region, instance_id=instance_id, instance_type='server',  \
                                                        name=name, status=status, create_day=create_day, expire_day=expire_day)
                    Server.objects.create(asset=new_instance, in_ipaddr=in_ipaddr, ou_ipaddr=ou_ipaddr, os_type=os_type, \
                                          os_info=os_info, cpu_info=cpu_info, memory_info=memory_info)
            return JsonResponse({'status':200})

class EcsListView(ListView):
    model = Server
    template_name = 'table_ecslist.html'

class EcsWaitListView(ListView):
    model = Server
    template_name = 'table_ecswaitlist.html'


# asset action class
class AddAssetView(View):
    def post(self,request, *args, **kwargs):
        instance_id = request.POST.get('instance_id')

        addasset = Asset.objects.get(instance_id=instance_id)
        addasset.show_status = 1
        addasset.save()
        return JsonResponse({'status': 200})

class RemoveAssetView(View):
    pass

class DelAssetView(View):
    pass


# ajax
def get_ecslist(request):
    print(request.is_ajax() == True)
    contents = Server.objects.order_by('-asset')
    contents = [content.as_dict() for content in contents]
    return JsonResponse({'status':200, 'contents':contents})

