class Person :

    name = '무명' # no name
    age = 0
    height = 0
    gender = ''
    feetSize = 200
    bloodType = ''

    def introduce(self) :
        greeting = f'''안녕하세요 저는 {self.name}입니다. {self.gender}구요. {self.age}살입니다.'''
        print(greeting)

    def eat(self, food) :
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def work(self, drink) :
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다.')

    def __init__(self, name, age, height, gender, feetSize, bloodType) -> None:    # constructor

        self.name = name
        self.age = age
        print('person이 생성되었습니다.')

        self.height = height
        self.gender = gender
        self.feetSize = feetSize
        self.bloodType = bloodType 

if __name__ == '__main__' :
    
    kuh = Person('uk', 26, 168, '남자', 255, 'AB')

    kuh.eat('본죽')
    kuh.work('핫식스')
    kuh.introduce()
