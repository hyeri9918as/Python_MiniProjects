#######  외부 사이트에 접속하고 접속된 정보를 바탕으로 외부 IP 확인하는 방법  #######

import requests   # python 용 http 라이브러리 
import re    # 정규 표현식 라이브러리 

req = requests.get("http://ipconfig.kr")    # 사이트 주소 열기 

# r string = raw string : escape 문이 작동하지 않고 문자열 그대로 출력하는 함수 
# \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) : \.는 . 문자를 나타내는 것이고 \d{1, 3}는 1에서 3사이의 단일 문자 출력을 의미한다. 
# req.text는 문자열 객체를 반환 
out_address = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print(out_address)