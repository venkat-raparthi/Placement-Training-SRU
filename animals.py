class Animals:
    def __init__(self,name,species,sound):
        self.name=name
        self.species=species
        self.sound=sound
    def make_sound(self):
        print(f"The {self.species} named {self.name} sounds '{self.sound}' ")
class Lion(Animals):
    def __init__(self,name):
        super().__init__(name, "Lion","roar")
    def get_info(self):
        print("lions are the kings of the jungle")
class Elephant(Animals):
    def __init__(self,name):
        super().__init__(name, "Elephant","Trumpet")
    def get_info(self):
        print("Elephants are the largest land animals")
class Snake(Animals):
    def __init__(self,name):
        super().__init__(name, "Snake","Hiss")
    def get_info(self):
        print("Snakes can be found on every continent except antartica")

leo = Lion("Leo")
ellie = Elephant("Ellie")
slyther = Snake("Slyther")

leo.make_sound()
leo.get_info()
print()

ellie.make_sound()
ellie.get_info()
print()

slyther.make_sound()
slyther.get_info()
print()
