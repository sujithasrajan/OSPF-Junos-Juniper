from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import RpcError
from jnpr.junos.utils.config import Config
from lxml import etree as etree
import time


device = Device(host='192.168.1.21', user='labuser', password='Labuser', normalize=True)
if_config = {'ge-0/0/1':'72.114.255.3/19', 'ge-0/0/2':'72.114.255.34/19', 'ge-0/0/3':'72.114.196.0/19'}
if_config_check = {'ge-0/0/1': '', 'ge-0/0/2':'passive', 'ge-0/0/3' : '' }
if_area = {'ge-0/0/1':'area 0.0.0.20', 'ge-0/0/2':'area 0.0.0.20', 'ge-0/0/3':'area 0.0.0.20'}
var_dict = {'if_config':if_config, 'if_config_check': if_config_check, 'if_area' : if_area}

try:
	device.open()
	device.bind(conf=Config)
	device.conf.load(template_path='template_ospf.conf', template_vars = var_dict, merge = True)
	success = device.conf.commit()
	print("Success : {}".format(success))

except (RpcError, ConnectError) as err:
	print("\nError: " + repr(err))

finally:
	device.close()
