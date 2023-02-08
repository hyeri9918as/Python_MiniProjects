#######  외부 사이트에 접속하고 접속된 정보를 바탕으로 내부 IP 확인하는 방법  #######

# socket 모듈 : 컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈 
import socket   

# socket 연결 / AF_INET : IP version 4 사용 
# SOCK_STREAM : 소켓에 TCP 패킷을 받겠다는 의미 
ip_address = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# goole 사이트로 연결, https 기본 접속 포트 443
ip_address.connect(("www.google.co.kr", 443))   

# 구글에서 반환한 현재 내부 IP 주소값 출력 
print(ip_address.getsockname()[0])