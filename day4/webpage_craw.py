# 웹페이지 가져오기
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com') # 네이버 웹페이지 요청
# res = urlopen(req)

# print(res.status)

# 외부 request 패키지 추가 설치
# pip install requests

import requests

url = 'https://www.naver.com'
res = requests.get(url)

print(res.text)
