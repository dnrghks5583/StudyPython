string = 'Hello'
n = int(input('n : '))
idx = 0

while idx + n <= len(string) :
    print(string[idx : idx + n])
    idx += 1
