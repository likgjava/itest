import requests

payload = {'a': '1', 'b': '2', 'key2': ['value2', 'value3']}

# r = requests.get('http://httpbin.org/get', params=payload)
r = requests.get('http://127.0.0.1:8000/add/', params=payload)
print(dir(r))
print(r.url)
print(r.headers)
print(r.content.decode())
