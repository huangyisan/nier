from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from nier import settings_ecs

def gen_machine():
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(20)
    client = settings_ecs.client
    response = client.do_action_with_exception(request)
    return response
