# 라이브러리 불러오기
import datetime

# 오늘 날짜와 시간 가져오기
today = datetime.datetime.now()
print(type(today))

# 오늘의 연도, 월, 일 출력하기 - today 클래스 사용
print("지금은", today.year, "년입니다.")
print("지금은", today.month, "월입니다.")
print("지금은", today.day, "일입니다.")
print("지금은", today.hour, "시입니다.")
print("지금은", today.minute, "분입니다.")