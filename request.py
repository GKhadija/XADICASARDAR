import requests
count = 100
succes_request=0
url= "https://www.youtube.com/"
for i in range(count):
    response=requests.get(url)
    if response.status_code==200:
        succes_request+=1
print(succes_request)