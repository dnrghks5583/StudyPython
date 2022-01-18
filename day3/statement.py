# if 구문 - 흐름 제어
# name = '욱환'
# name = ['명건', '태경', '기영', '욱환']
name = ('명건', '태경', '기영', '욱환', '다원')

# if name == '욱환' or name == '명건' :

if '명건' in name :
    print('의사를 만나러 갑니다.')
    print('의사선생님께 인사합니다.')
elif name =='다원' :
    print('주사실로 갑니다.')
else :
    print('호출할때까지 대기합니다.')
