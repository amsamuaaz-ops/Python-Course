from abc import ABC, abstractmethod

class Animal(ABC):
    def ph(self):
       pass

class human(Animal):
    def move(self):
        print("I can walk and run")

class snake(Animal):
    def move(self):
        print("I crawl")

class dog(Animal):
    def move(self):
        print("I Bark")

class lion(Animal):
    def move(self):
        print("i can roar")

obj = human()
obj.move()

obj1 = snake()
obj1.move()

obj2 = dog()
obj2.move()

obj3 = lion()
obj3.move()