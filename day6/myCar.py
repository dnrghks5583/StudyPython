from vehicle import car

if __name__ == '__main__' :

    myCar = car('부2022', 'red')
    
    print(myCar)
    
    ## __brand : private
    print(myCar.getBrand())
    myCar.__brand = '기아'     
    print(myCar.getBrand())
    myCar.setBrand('기아')    
    print(myCar.getBrand())

    myCar.straight()
    myCar.back()
    myCar.left()
    myCar.right()
    myCar.stop()
