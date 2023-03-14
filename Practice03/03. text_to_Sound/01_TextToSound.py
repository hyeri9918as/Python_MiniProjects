####### 텍스트를 음성으로 변환하는 코드 만들기 #######

from gtts import gTTS    # gtts 라이브러리로부터 gTTS 기능만 불러오기 

text = "오늘은 2023년 02월 16일입니다."  # text 변수에 문자열 바인딩

# text 변수 문자열을 ko(한글)로 변환하여 tts 변수에 바인딩
tts = gTTS(text=text, lang='ko')

# 프로젝트 폴더 안에 date_guide.mp3 파일 저장 
tts.save(r"03. text_to_Sound\date_guide.mp3")
