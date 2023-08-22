# 라이브러리 불러오기
import datetime

# 오늘 날짜 가져오기
today = datetime.datetime.now()

# 요일에 따라 다른 메세지 출력하기 (0 ~ 6)
if today.weekday() == 5 or today.weekday() == 6 :
# if today.weekday() in [5, 6] :
    print("주말입니다.")
elif today.weekday() == 4 :
    print("금요일입니다.")
else :
    print("주말이 아닙니다.")