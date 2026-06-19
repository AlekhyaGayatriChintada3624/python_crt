##class Student:
##    def __init__(self,name,branch,collage):
##        self.__name=name
##        self.__branch=branch
##        self.__collage=collage
##    def hungry(self):
##        print ("eat food")
##    def get_properties(self):
##        return self.__name
##        return self.__branch
##        return self.__collage
##        
##    def exams(self):
##        print ("go to study hours")
##    def night(self):
##        print ("need to sleep 8 hours")
##    def morning(self):
##        print ("go to collage")
##    def brake_time(self):
##        print ("relax and enjoy")
##student1=Student("alekhya","ECE","MLEW")
##print(student1.get_properties())
##student1.hungry()
##student1.exams()

"""nside the editor, complete the following steps:
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dog's name followed by " says Woof!"
Create an object d1 of the Dog class with name "Buddy" and age 3
Call the bark method on d1
📋 Copy Text"""
##class kukka:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def bark(self):
##        print(self.name,"says Woof!")
##
##
##dog=kukka("buddy","3")
##dog.bark()


"""Inside the editor, complete the following steps:
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1"""

##class car:
##    def __init__(self,brand):
##        self.brand=brand
##    def show(self):
##        print(self.brand)
##
##
##car1=car("lamborgini")
##car1.show()


"""Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade"""

##class Student:
##    def __init__(self,name,grade):
##        self.name=name
##        self.grade=grade
##s1=Student("anna","A")
##print(s1.grade)
##s1.grade="B"
##print(s1.grade)
##

##class Rectangle:
##    def __init__(self,width,height):
##        self.width=width
##        self.height=height
##
##    def area(self):
##        return self.width*self.height
##
##r1=Rectangle(5,3)
##print(r1.area())

##
##class Animal:
##    def __init__(self,name):
##        self.name=name
##    def speak(self):
##        print(self.name)
##
##class Dog(Animal):
##    pass
##
##d1=Dog("Rex")
##d1.speak()
##

"""Level 1: Basic OOP Practice Questions

Question 1: Mobile Phone Class

Create a class called Mobile.

Attributes:

brand

model

price


Methods:

make_call()

show_details()


Expected Output

Brand: Samsung
Model: S24
Price: 80000
Calling...


---"""

##class Mobile:
##    def __init__(self,brand,model,price):
##        self.brand=brand
##        self.model=model
##        self.price=price
##    def make_call(self):
##        print("Calling...")
##    def show_details(self):
##        print("brand :", self.brand)
##        print("model:", self.model)
##        print("price:" ,self.price)
##
##m1=Mobile("samsung","s24",80000)
##m1.show_details()
##m1.make_call()
##        


"""Question 2: Student Class

Create a class called Student.

Attributes:

name

roll_no

branch


Method:

display()


Create 3 student objects and display details."""

##class Student:
##    def __init__(self,name,rollno,branch):
##        self.name=name
##        self.rollno=rollno
##        self.branch=branch
##    def display_details(self):
##        print("name:",self.name)
##        print("rollno:",self.rollno)
##        print("branch:",self.branch)
##
##s1=Student("Alekhya","L4","ECE")
##s2=Student("Anju",404,"CSE")
##s3=Student("gayatri",81,"IT")
##
##s1.display_details()
##s2.display_details()
##s3.display_details()


"""---

Question 3: Car Class

Create a class called Car.

Attributes:

brand

color


Method:

start_engine()


Output:

Toyota car started"""

##class Car:
##    def __init__(self,brand,colour):
##        self.brand=brand
##        self.colour=colour
##    def start_engine(self):
##        print(self.brand,"car started""")
##c1=Car("BMW","White")
##c1.start_engine()

"""Question 4: Bank Account

Create a class called BankAccount.

Attributes:

account_holder

balance


Methods:

deposit()

withdraw()

check_balance()



---"""
"""
class BankAccount:
    
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def diposit(self):
        dip_amount=int(input("enter ur dip amount:"))
        amount=dip_amount+self.balance
        print(self.account_holder,"ammount dipositate",amount)
    def withdraw(self):
        draw_amount=int(input("enter ur draw amount:"))
        amount=self.balance-draw_amount
        print(self.account_holder,"ammount debited", draw_amount)
    def checkbalance(self):
        print(self.account_holder,"balance amount:",self.balance)
a1=BankAccount("Alekhya",10000000000)
a2=BankAccount("ajibun",1000000)
a3=BankAccount("arjun",2000000)

a1.diposit()
a1.withdraw()
a1.checkbalance()"""

##a2.diposit()
##a2.withdraw()
##a2.checkbalance()
##
##a3.diposit()
##a3.withdraw()
##a3.checkbalance()
##

    

"""Level 2: Constructor Practice

Question 5: Watch Class

Using your Casio Watch example.

Attributes:

brand
current_time
battery_percentage

Methods:

show_time()
light_on()
beep()


---"""
"""
from datetime import date, datetime
class Watch:
    def __init__(self,brand,current_time,battery_percentage):
        self.brand=brand
        self.current_time=current_time
        self.batter_percentage=battery_percentage

    def show_time(self):
        print(datetime.now())
    def light_on(self):
        print("light is on")
    def beep():
        print("beep! beep!")

w1=Watch("casio",datetime.now(),80)
w1.show_time()
w1.light_on()
w1.beep()
print(w1.current_time)"""


"""ums = list(map(int, input("Enter numbers: ").strip("[]").split(",")))
t = int(input("Enter target: "))

class Solution:
    def __init__(self, nums, t):
        self.nums = nums
        self.t = t

    def twosum(self):
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.t:
                    print(i, j)

 Outside the class
obj = Solution(nums, t)
obj.twosum()
       
c=0
for i in range(100,117):
    for j in range(8,19):
        c+=1
        print(c,i,j)"""
"""def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
 
##print(fun(22))"""
##def factorial_function(n):
##    if n < 0:
##        return None
##    if n < 2:
##        return 1
##    return n * factorial_function(n - 1)
## 
## 
##print(factorial_function(-1))
##print(factorial_function(0))
##print(factorial_function(2))
##print(factorial_function(5))
def fib(n):
"""    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))
##
##        
"""
def h():
    for i in range(3):
        pass
print(h())
##numbers = list(map(int, input("Enter the list of numbers: ").split(",")))
##def Add(numbers):
##    sum=0
##    if len(numbers) == 0:
##        print("zero numbers are present in list",numbers)
##        return 0
##    
##    for i in numbers:
##        sum += i
##        return sum
##    
##print(Add(numbers))

