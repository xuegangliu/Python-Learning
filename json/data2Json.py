# -*- coding: gbk -*-
import json

# Python �ֵ�����ת��Ϊ JSON ����
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

# json.dumps(): �����ݽ��б��롣
json_str = json.dumps(data)
print ("Python ԭʼ���ݣ�", repr(data))
print ("JSON ����", json_str)