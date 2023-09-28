class Cat:
    def __init__(self, age=1):
        self.age = age
    
    def say_smth(self):
        print("meow")
    
    def ask_for_food(self):
        self.say_smth()
    
class Tiger(Cat):
    def say_smth(self):
        print("Rrrr")
    
    def ask_for_food(self):
        print("(not asking, just hunting...)")

tiger = Tiger(5)
tiger.say_smth()
tiger.ask_for_food()
