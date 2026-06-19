class Student:
    def __init__(self,name,age,rollno):
        self.name=name 
        self.__age=age
        self.__rollno=rollno
    def study(self):
        print('reading')
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')
alekhya=Student('alekhya',21,'L12')
print(alekhya.name)
print(alekhya.__age)
print(alekhya.__rollno)
alekhya.study()
alekhya.eat()
alekhya.sleep()