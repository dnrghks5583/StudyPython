# Cursor에 접근하는 함수 작성

import cx_Oracle as ora

def myConnection() :

    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    con = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return con 

def getAllData(con) :   # con object

    cur = con.cursor()  # create cursor
    query = 'SELECT * FROM emp'
    for row in cur.execute(query) :
        print(row)      # 모든 data를 한 줄씩 출력
    cur.close()

def getNameAndJobData(con) :

    cur = con.cursor()
    query = 'SELECT ename, job FROM emp'    # emp table ename, job
    cur.execute(query)    

    while True :

        row = cur.fetchone()       # row(record) 읽기
        if row is None :
            break
        print(row)
    cur.close()

def getDeptName(con, tup) :

    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2'
    cur = con.cursor()
    # cur.execute(query, param)

    for row in cur.execute(query, tup) :
        print(row)

    # row = cur.fetchone()
    # print(row)
    cur.close()

def joinTable (con) :

    query =  '''SELECT e.ename
                     , e.job
                     , d.deptno
                     , d.loc
                     , d.dname
                  FROM emp e, dept d
                 WHERE e.deptno = d.deptno'''   # inner join
    cur = con.cursor()
    
    for row in cur.execute(query) :
        print(row)
    cur.close()

if __name__ == '__main__' :

    print('Python Start') 
    scottCon = myConnection()

    # print('emp table')
    # getAllData(scottCon)

    # print('emp 2 Columns')
    # getNameAndJobData(scottCon)

    print('Dept Name')
    # num = int(input('검색할 부서 입력 : '))
    # loc = input('검색할 지역 입력 : ')
    # tup = [num, loc.upper()]
    # getDeptName(scottCon, tup)
    tup = (30, 'CHICAGO')
    getDeptName(scottCon, tup)

    print('Join Table')
    joinTable(scottCon)

    scottCon.close()
    print('Python end')