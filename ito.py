import requests

response = requests.get('https://kpk.kss45.ru')

print(requests)

print(type(response))
print(dir(response))
print(response.status_code)
print(response.content.decode('utf-8'))

