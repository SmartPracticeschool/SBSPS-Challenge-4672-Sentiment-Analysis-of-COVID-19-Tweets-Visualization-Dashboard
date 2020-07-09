import requests

url='http://127.0.0.1:8000/upload'
data={
    'name':'aksh'
}
r=requests.post(url,data=data)
print(r)