# -*- coding: gbk -*-
import json

# Python �ֵ�����ת��Ϊ JSON ����
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

# json.dumps(): �����ݽ��б��롣
json_str = json.dumps(data1)
print ("Python ԭʼ���ݣ�", repr(data1))
print ("JSON ����", json_str)

# json.loads(): �����ݽ��н��롣
# �� JSON ����ת��Ϊ Python �ֵ�
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])