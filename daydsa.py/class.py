class Alekhya:
    def __init__(self, name,storage,speed):
        self.name=name
        self.storage=storage 
        self.speed=speed
    def display_features(self):
        print("name:",self.name )
        print("storage:",self.storage)
        print("speed:", self.speed)
    def boring(self):
        print("does something interesting")
    def hungry(self):
        print("eats healthy food")
    def morning(self):
        print("gets ready and goes to collage")
    def collage_time(self):
        print("building skills")
    
r1=Alekhya("Alex","100GB","1000M/S")
r1.display_features()
r1.boring()
r1.hungry()
r1.morning()
r1.collage_time()


        


