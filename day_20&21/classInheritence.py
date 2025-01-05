
'''we can inherit some features from
one class to another class so that we dont
have to code the entire class again'''

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


'''we are creating a class called 
fish and we know that it will inherit some
characteristics as an animal, so just add the 
animal in fish class'''

class Fish(Animal):
    def __init__(self):
        super().__init__() #this line is for animal class

    def breathe(self): #to edit the breath of animal for fish use
        super().breathe()
        print("doing this under water.")
        
    def swim(self):
        print("moving in water.")



nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
