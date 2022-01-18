# 무한 루프
val = 0

while True :

    print(''' 작업할 번호를 입력하세요. 
    1. 회원 입력
    2. 회원 거색
    3. 회원 수정
    4. 회원 삭제
    5. 종료
    숫자 입력 : ''', end = '')
    
    val = int(input())

    if val == 1 :
        print('회원 정보 화면으로 전환')
    elif val == 2 :
        print('회원 검색 화면으로 전환')
    elif val == 3:
        print('회원 수정 화면으로 전환')
    elif val == 4 :
        print('회원 삭제 화면으로 전환')
    elif val == 5 :
        break
    else :
        print('잘못된 입력입니다.')
        print('1~5 사이의 수를 입력하세요')
        continue
    
print('회원 정보 프로그램 종료')