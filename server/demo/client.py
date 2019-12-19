import requests

user_info = {'name': 'lala', 'password': '123'}
file_data = {'image': open('123.jpg', 'rb')}
# r = requests.post('http://127.0.0.1:5000/register', data=user_info)
r = requests.post('http://127.0.0.1:5000/upload', json=user_info, files=file_data)

print(r.headers)
print(r.text)
