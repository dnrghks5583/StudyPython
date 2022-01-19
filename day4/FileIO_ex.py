# File IO
# File 출력

# f = open('newfile.txt', 'w')
# f.close()

# f = open('C:\\Sources\\sample\\test.txt', 'w')
# f = open('C:/Sources/sample/test.txt', 'w')  same
# f.close()
# print('파일이 생성되었습니다.') 

f = open('newfile.txt', 'r', encoding = 'utf-8')

# for line in f :
#     print(line, end = '')
    
while True :
    
    line = f.readline()
    
    if not line :
        break
    print(line)

f.close()