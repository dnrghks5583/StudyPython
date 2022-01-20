# oracle 연동
# pip install cx_oracle

import cx_Oracle as ora

# data source name (dsn)
# makedsn('host명/IP 주소', port number, service_name)
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
# connect(user, password, dsn, encoding)
conn = ora.connect(user = 'scott', password = 'tiger', encoding = 'utf-8', dsn = dsn)

cur = conn.cursor()

try :
    # for row in cur.execute('SELECT * FROM emp') :   # ; 사용x
    #    print(row)
    cur.execute('SELECT COUNT(*) FROM emp')
    result = cur.fetchone() # 값 하나 가져올 때
    print(result)

except ora.DatabaseError as e:
    print(f'DB query문이 잘못되었습니다. {e}')

finally :
    cur.close()     # cursor 부터 닫고
    conn.close()    # 접속 종료