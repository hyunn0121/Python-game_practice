# 사용할 아스키 범위 - 이 범위를 벗어나면 오류가 발생할 수 있습니다.
asciiMin = 32 # 공백 문자를 나타냄 - ""
asciiMax = 126 # 물결표 문자를 나타냄 - "~"

# 암호화 키
key = 314159
key = str(key)  # 각 문자에 접근할 수 있도록 문자열로 변환

# 암호화할 메세지 입력받기
message = input("암호화할 메세지를 입력하세요: ")

# 암호화 메세지용 변수 초기화
messEncr = ""

# 메세지 루프
for index in range (0, len(message)) :
    # 해당 문자의 아스키값 가져오기
    char = ord(message[index])
    # 이 문자가 범위 밖인지 확인
    if char < asciiMin or char > asciiMax :
        # 밖이라면 암호화하지 않고 사용
        messEncr += message[index]
    else :
        # 안이라면 키만큼 값을 더하여 해당 문자를 암호화 (문자열이 암호키보다 길 수 있으므로 %을 사용)
        ascNum = char + int(key[index % len(key)])
        # 더한 값이 사용할 아스키 문자의 범위를 벗어난다면 범위 처음으로 되돌림
        if ascNum > asciiMax :
            ascNum -= (asciiMax - asciiMin)
        # 문자로 변환하고 출력할 내용에 추가
        messEncr = messEncr + chr(ascNum)

# 결과 출력하기
print("암호화한 메세지 :" , messEncr)