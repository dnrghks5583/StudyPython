# using table : divtbl, membertbl

import cx_Oracle as ora

def myConnection() :

    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    return ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8') 

def getAllDataFromDivtbl(conn) :

    query = 'SELECT * FROM divtbl'
    cur = conn.cursor()

    for row in cur.execute(query) :
        print(row)
    cur.close()

def insertDataIntoDivtbl(conn, tup) :

    query = '''INSERT INTO divtbl (division, names)
               Values (:1, :2)'''
    cur = conn.cursor()
    cur.execute(query, tup)
    cur.close()

    conn.commit() # COMMIT
    # conn.rollback # ROLLBACK

def getDataFromMembertbl(conn) :    # 일부 데이터 가져오기

    query = '''SELECT names
                    , levels
                    , addr
                    , mobile
                    , email
                 FROM membertbl
                WHERE addr LIKE \'서울%\'
                  AND UPPER(email) LIKE \'%@NAVER.COM\'
                ORDER BY idx DESC'''

    cur = conn.cursor()
    for row in cur.execute(query) :
        print(row)
    cur.close()

def setNewMemberIntoMembertbl(conn, tup) :

    query = '''SELECT ROWNUM, idx
                 FROM (
                      SELECT idx FROM membertbl
                      ORDER BY idx DESC  
                      ) 
                WHERE ROWNUM = 1'''
    cur = conn.cursor()
    cur.execute(query)

    idx = cur.fetchone()
    if idx is None :    # fatchone exception
        idx = 0
    else :
        idx = (idx[1] + 1, )
    new_tup = idx + tup

    query = '''INSERT INTO membertbl (idx, names, levels, userid, password)
               VALUES (:1, :2, :3, :4, :5)'''
    cur.execute(query, new_tup)
    conn.commit()
    cur.close()

def setChangeMemeberFromMembertbl(conn, tup) :

    query = '''UPDATE membertbl
                  SET addr = :1
                    , mobile = :2
                    , email = :3
                WHERE idx = :4'''
    cur = conn.cursor()
    cur.execute(query, tup)
    cur.close()
    conn.commit()

def deleteDivision(conn, division) :
    
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur = conn.cursor()
    cur.execute(query, (division, )) # one element tuple
    cur.close()
    conn.commit()

if __name__ == '__main__' :

    print('책 대여점 프로그램 시작\n')
    scott_con = myConnection()

    # 1. divtbl에서 데이터 조회
    # print('책 장르 정보 조회')
    # getAllDataFromDivtbl(scott_con)
    
    # 2. divtbl에 새로운 데이터 입력
    # print('책 장르 정보 입력')
    # division = input('구분 코드 입력 : ')
    # names    = input('장르명 입력 : ')
    # insertDataIntoDivtbl(scott_con, (division, names))
    # print('정보 입력 성공')

    # 3. membertbl에서 데이터 조회
    # getDataFromMembertbl(scott_con)

    # 4. membertbl에 새로운 데이터 입력
    # print('신규 회원 입력')
    # names = input('회원 이름 입력 : ')
    # levels = input('레벨 입력(A~D) : ')
    # userID = input('ID 입력(최대 20자) : ')
    # password = input('비밀 번호 입력(최대 20자) : ')
    # tup = (names, levels, userID, password)

    # setNewMemberIntoMembertbl(scott_con, tup)
    # print('신규 회원 저장 성공')

    # 5. membertbl 새 데이터를 수정
    # print('회원 정보 수정')
    # idx = input('변경 회원 번호 입력 : ')
    # addr = input('주소 입력 : ')
    # mobile = input('휴대폰 번호 입력(-포함) : ')
    # email = input('이메일 입력 : ')

    # tup = (addr, mobile, email, idx)
    # setChangeMemeberFromMembertbl(scott_con, tup)
    # print('회원 정보 수정 완료')

    # 6. divtbl에서 임의 데이터 삭제
    print('책 장르정보 삭제')
    division = input('삭제할 장르 코드 입력 : ')
    deleteDivision(scott_con, division)
    print('삭제 성공')

    scott_con.close()
    print()