#######  내부, 외부 IP 한번에 출력하는 방법  #######

import socket  # socket 모듈 : 컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈 
import requests   # python 용 http 라이브러리 
import re   # 정규표현식 라이브러리

# socket 연결 / AF_INET : IP version 4 사용 
# SOCK_STREAM : 소켓에 TCP 패킷을 받겠다는 의미 
ip_address = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# goole 사이트로 연결, https 기본 접속 포트 443
ip_address.connect(("www.google.co.kr", 443))   

# 구글에서 반환한 현재 내부 IP 주소값 출력 
print("내부 IP : ", ip_address.getsockname()[0])

req = requests.get("http://ipconfig.kr")    # 사이트 주소 열기 

# r string = raw string : escape 문이 작동하지 않고 문자열 그대로 출력하는 함수 
# \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) : \.는 . 문자를 나타내는 것이고 \d{1, 3}는 1에서 3사이의 단일 문자 출력을 의미한다. 
# req.text는 문자열 객체를 반환 
out_address = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print("외부 IP : ", out_address)
