#######  외부 사이트에 접속하고 접속된 정보를 바탕으로 외부 IP 확인하는 방법  #######

import requests
import re

req = requests.get("http://ipconfig.kr")
out_address = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print(out_address)