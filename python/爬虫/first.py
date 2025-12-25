import requests as rq

data = {
    'name' : 'germy',
    'age' : 25
} 
url = 'https://www.httpbin.org/post'

response = rq.post(url, data=data)

print(response.text)
print(response.headers)
# print(response.cookies)
print(response.status_code)



