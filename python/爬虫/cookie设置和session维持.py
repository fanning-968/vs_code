import requests as rq

# r = rq.get('https://www.baidu.com')
# print(r.cookies)

# for key, value in r.cookies.items():
#     print(key + '=' + value)

# headers = {
#     'Cookie' : '_octo=GH1.1.607249668.1741915894; _device_id=b824e0a0680566f0a02c50d7b647bfe7; saved_user_sessions=65838411%3ACU-DN0aVF7O7NtgvIs7KcZE6TJQq3lYyJCP9aKcGl_iXBZqN; user_session=CU-DN0aVF7O7NtgvIs7KcZE6TJQq3lYyJCP9aKcGl_iXBZqN; __Host-user_session_same_site=CU-DN0aVF7O7NtgvIs7KcZE6TJQq3lYyJCP9aKcGl_iXBZqN; logged_in=yes; dotcom_user=fanning-968; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=lg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=JpSHEDS3ikoG0VWx%2FWIb7TwlbAd3fqyEYXXvNLp7L47dVr4CDvxWIZsxN2fYpRKgYjN2SIkCfQkDwYYTg2%2Bz6BaIHSk7ahkRThCZ9%2F4LsKdZC64ilOth0CpWD4FkUpWNrxfC4UbUyu1vJcS9J12lFtEe3FZD2q2KnS3yuvWbQSqxvHBw7XTFofDzVthvqsuyf72i8zoNg0d6QtWlvSanBGdxn5%2FWEtOstfSxcDSTindVtRbY5VvpeSBgoZf%2BFRnr5dBkN0lXCLdhxfx%2BUWrcMVX%2BaomlsLugWHRgN3QR%2BZmItUB%2BnrWMoMrwZAnhM4ssdq%2Ft%2Fli8Z4H5HxEKGoZH2PXu4GBI4g5YOF1sC4tfxT0qmGLnYZUJnTMUqEKiqHOD--vyrElH9Tykgoaedu--rWYh8vNB6f%2FMGUNcxfSPfA%3D%3D'
# }

# r = rq.get('https://github.com/', headers=headers)
# print(r.text)

s = rq.Session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)


