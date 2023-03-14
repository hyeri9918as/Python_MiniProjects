####### 텍스트를 음성으로 변환 후 바로 실행하는 코드 만들기 #######

from gtts import gTTS    # gtts 라이브러리로부터 gTTS 기능만 불러오기 
from playsound import playsound  #playsound 라이브러리로부터 playsound 기능만 불러오기
import os   # 경로 이동시 꼭 필요한 os 라이브러리 

# 경로를 .py 파일의 현재 실행 경로로 이동 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# text 변수에 문자열 바인딩
text = "오늘은 2023년 02월 16일입니다."  

# text 변수 문자열을 ko(한글)로 변환하여 tts 변수에 바인딩
tts = gTTS(text=text, lang='ko')

# 현재 경로 안에 date_guide2.mp3 파일 저장 
tts.save("date_guide2.mp3")
playsound("date_guide2.mp3")
