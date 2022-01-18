# 기본 for 문

# arr = list(range(1, 100))

# for i in arr :
#     print(f'{i:0.1f}')

# tuple
arr2 = ('me', 'my', 'friend', 'jane')

# for i in arr2 :
#     print(f'{i:>10}')

# 합계 계산
# numbers = list(range(1, 21, 2))
# sum = 0
# for i in numbers :
#     sum += i
# print(f'{numbers[-1]}까지의 총 합은 {sum}입니다.')

# 홀짝 구분
# numbers = list(range(1, 21))

# for i in numbers :
#     if i % 2 == 0 : # even
#         print(f'{i}는 짝수')
#     else : # odd
#         print(f'{i}는 홀수')

# 13이상이면 탈출
# numbers = list(range(1, 21))

# for i in numbers :
#     if i == 15 :
#         continue  # break
    
#     if i % 2 == 1 :
#         print(f'{i}는 홀수')

# 구구단
# for i in range(1, 10) :
#     print(f'{i}단 시작')
#     for j in range(1, 10) :
#         print(f'{i} x {j} = {i * j:2d}', end = '  ')
#     print('')

# inline for
a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)