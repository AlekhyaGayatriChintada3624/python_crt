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
Calling..."""
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def make_call(self):
        print("calling...")
    def show_details(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("price:",self.price)
m1=Mobile('Samsung','S24',80000)
m1.make_call()
m1.show_details()