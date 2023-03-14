####### 파일 텍스트를 불러와 음성으로 변환 후 바로 실행하는 코드 만들기 #######

from gtts import gTTS    # gtts 라이브러리로부터 gTTS 기능만 불러오기 
from playsound import playsound  #playsound 라이브러리로부터 playsound 기능만 불러오기
import os   # 경로 이동시 꼭 필요한 os 라이브러리 

# 경로를 .py 파일의 현재 실행 경로로 이동 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 나의 텍스트.txt 경로를 바인딩  
file_path = "나의텍스트.txt"

# 파일 이름을 f로 오픈, 한글 파일 오픈시 글자가 깨지지 않게 지정 
with open(file_path, 'rt', encoding='UTF8') as f :
    read_file = f.read()

# text 변수 문자열을 ko(한글)로 변환하여 tts 변수에 바인딩
tts = gTTS(text=read_file, lang='ko')

# 현재 경로 안에 myText.mp3 파일 저장 & 바로 실행 
tts.save("myText.mp3")
playsound("myText.mp3")
