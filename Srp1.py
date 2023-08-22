# 라이브러리 불러오기
import random

choices = ["가위", "바위", "보"]

# 컴퓨터의 선택
cChoice = random.choice(choices)

# 사용자 선택
print("가위, 바위, 보?")
uChoice = input("가위, 바위, 보 중 하나를 고르세요.")
uChoice = uChoice.strip()

# 테스트하기
print("사용자 : " + uChoice)
print("컴퓨터 : " + cChoice)

# 선택 비교하기
if cChoice == uChoice :
    print("무승부입니다!")
elif cChoice == "가위" and uChoice == "바위" :
    print("사용자가 이겼습니다.")
elif cChoice == "가위" and uChoice == "보" :
    print("컴퓨터가 이겼습니다.")
elif cChoice == "바위" and uChoice == "가위" :
    print("컴퓨터가 이겼습니다.")
elif cChoice == "바위" and uChoice == "보" :
    print("사용자가 이겼습니다.")
elif cChoice == "보" and uChoice == "바위" :
    print("컴퓨터가 이겼습니다.")
elif cChoice == "보" and uChoice == "가위" :
    print("사용자가 이겼습니다.")
else :
    print("잘못 입력하였습니다. 다시 입력해주세요.")
