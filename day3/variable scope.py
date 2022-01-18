# 변수 lifescope

def vartest(a) :
    a = a + 1
    return a

a = vartest(10)
print(a)