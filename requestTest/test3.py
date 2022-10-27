import requests

response = requests.get('http://httpbin.org/get')
print(response.text)