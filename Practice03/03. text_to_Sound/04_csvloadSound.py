####### csv 파일을 불러와 음성으로 변환 후 바로 실행하는 코드 만들기 #######

from gtts import gTTS    # gtts 라이브러리로부터 gTTS 기능만 불러오기 
from playsound import playsound  #playsound 라이브러리로부터 playsound 기능만 불러오기
import os   # 경로 이동시 꼭 필요한 os 라이브러리 

# 경로를 .py 파일의 현재 실행 경로로 이동 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 자료.csv 경로를 바인딩  
file_path='자료.csv'

# 파일 이름을 f로 오픈, 
# 공공데이터는 cp949나 euc-kr 방식으로 인코딩이 되어 있기 때문에 
# encoding을 cp949로 설정해준다. 
with open(file_path,'rt',encoding='CP949')as f:
    read_file=f.read()

# csv 데이터 터미널에 출력 
print(read_file)

# text 변수 문자열을 ko(한글)로 변환하여 tts 변수에 바인딩
tts=gTTS(text=read_file,lang='ko')

# 현재 경로 안에 csvSound.mp3 파일 저장 & 바로 실행 
tts.save("csvSound.mp3")
playsound("csvSound.mp3")