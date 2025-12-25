import re 

content = 'Hello 123 4567 World_This is a Regex Demo'
print(content)
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# result = re.match('^Hello\s(\d+)\sWorld', content)
result = re.match('^Hello.*?Demo$', content)
print(result)
print(result.group())
print(result.span())