# 부산 버스 노선별 이용건수
import csv

file_name = '부산버스정보.csv'
f = open(file_name, mode = 'r', encoding = 'utf-8')

reader = csv.reader(f, delimiter = ',')
next(reader) # 첫 번째 줄 삭제
for line in reader :
    print(line)

f.close()