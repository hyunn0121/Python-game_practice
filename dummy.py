print("3" * 5)
print(3 * 5)

# 05-1
name = " Ben "

# 대문자로 변경
name = name.upper()
# 공백 없애기
name = name.strip()
# 합치기
name = name.upper().strip()

# 결과 출력하기
print(name)

# 리스트 만들기
animals = ["개", "개미", "고양이", "박쥐", "장어"]
# 리스트 요소 출력하기
print(animals[1])
# 리스트 크기
print(len(animals))
# 아이템 추가하기
animals.append("여우")

# 리스트 합치기
list2 = ["염소", "이구아나", "하마"]
animals.extend(list2)

# 리스트 삭제
animals.pop(5)
# animals.remove("여우")

# 리스트 내 같은 요소 개수 세기
animals.count("암소")