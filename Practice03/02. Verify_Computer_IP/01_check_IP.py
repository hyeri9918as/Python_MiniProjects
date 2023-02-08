#######  컴퓨터의 외부 및 내부 IP 확인하기 #######

# socket 모듈 : 컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈 
import socket   

ip_address = socket.gethostbyname(socket.gethostname())  

print(ip_address)