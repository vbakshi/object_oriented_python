from config_dict import *

a = ConfigDict('conf_test')
a['username'] = 'vinayak'
a['kerberos'] = 'bakshv'
print(a)
b = ConfigDict('conf_test')
print(b)