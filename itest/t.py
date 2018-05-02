import json
import re

import sys


list2 = []
s = '数学&英语'
print(s.split('&'))
list2.append(s.split('&'))
print('list=', list2)
print(re.split(r'[&,]', s))

a = 'hello' in ['hello3', 'hello2']
print(a)

print(re.match('t', 'abc'))

line = '<response[0].sum>'
# matchObj = re.match(r'(.*) are (.*?) .*', line)
matchObj = re.match(r'<response\[(.*)\]\.(.*)>', line)
# matchObj = re.match(r'<response(.*)>', line)

if matchObj:
    print("matchObj.group() : ", matchObj.group())

    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match!!")

obj = json.loads('{"sum":1}')
print(obj.get('sum2', 'ok'))

d = obj
if isinstance(d, dict):
    print("d is dict")
else:
    print('d is not dict...')


print('max===', sys.maxsize)