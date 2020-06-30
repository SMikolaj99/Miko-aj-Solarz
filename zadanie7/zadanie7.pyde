from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'

class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    def gimmePaw(self):
        image(loadImage("cat.png"), random(10, width-40), random(10, height-20))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass

class Kot(Pet):
     def __init__(self, name):
        self.name = name
     def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
  
def setup():
    background(50,150,100)
    size(600,600)
    textSize(20)
    gandalf = Kot('Gandalf')
    golden = Cat('Golden')
    global list_of_pets
    list_of_pets = [golden, gandalf] 
    print(isinstance(gandalf, Pet))
    print(golden+gandalf)
   
def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Cat): 
            pet.gimmePaw()
