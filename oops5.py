from abc import ABC, abstractmethod

class absclass(ABC):
    def print(self,x):
        print("Passed In value",x)

    @abstractmethod
    def task(self):
        print("I am the abstract method from absclass ")

class test_class(absclass):
    def task(self):
        print("HI i am abstract method")

test_obj = test_class()
test_obj.task()
test_obj.print(100)