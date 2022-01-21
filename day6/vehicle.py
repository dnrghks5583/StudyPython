class car :

    car_number = '22나 4444'
    __brand = '현대'
    color = '흰색'
    fuel = '가솔린'
    year = '2010'

    def __init__(self, car_number, color) -> None :
        self.car_number = car_number
        self.color = color

    def __str__ (self) -> str :
        return f'제 차는 {self.year}년에 만들어진 {self.fuel} 차량입니다.'
    
    def getBrand(self) :
        return self.__brand

    def setBrand(self, brand) :
        self.__brand = brand

    def straight(self) :
        print(f'{self.color}차가 직진')

    def back(self) :
        print('후진')

    def left(self) :
        print('좌회전')

    def right(self) :
        print('우회전')
    
    def stop(self) :
        print('정지')