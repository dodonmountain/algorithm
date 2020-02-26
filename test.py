import sys
import requests
client_id = "nn7epvorby"
client_secret = "d3bZaPLgytjnQO6Ak4qhdQI4wh0cZ3xsWQYQED8u"
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
data = open('iu.jpeg', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "multipart/form-data"
}
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)