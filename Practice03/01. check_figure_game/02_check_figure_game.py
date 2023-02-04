# 숫자 맞추는 게임 만들기 

import random

# random_number 변수에 1~100 사이의 임의의 값을 정수형태로 바인딩
random_number = random.randint(1, 100)   

# 게임 횟수를 세기 위한 변수를 생성하고 1 값을 대입(바인딩)
game_count = 1 

while True :      # while의 조건이 True이기 때문에 break를 만나기 전까지 계속 반복됨. 
    my_number = int(input("1~100 사이의 숫자를 입력하세요. :"))   # 입력 값을 정수형으로 변환 후 my_number 변수에 저장 
    
    if my_number > random_number :  # 입력값이 임의의 수보다 크다면 
        print("down")               # down을 출력 
        
    elif my_number < random_number :  # 입력값이 임의의 수보다 작다면 
        print("up")                   # up을 출력 
            
    elif my_number == random_number :  # 입력값과 임의의 수 값이 같다면 (일치한다면)
        print(f"축하합니다. {game_count}회 만에 맞췄습니다.")   # 맞춘 횟수 출력 (f'string)
        break    # while 문 종료 
    
    game_count = game_count + 1   # while 문 반복 수행 시 count 값 1씩 증가 50
    