import random

class Animal:
    def __init__(self, name):
        self.name = name 
    
    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Dog(Animal):
    def __init__(self,name):
        # Animal(Dog,self).__init__(name)
        super(Dog,self).__init__(name)
        self.breed = random.choice(['Shih Tzu','Beagle','Mutt'])
    
    def fetch(self, thing):
        print(f"{self.name} goes after the {self.thing}")

d = Dog('chiwawa')
print(d.name)

#Multiple Inheritance

# Python does a depth search first when evaluating a method

class A:
    def dothis(self):
        print('A class')

class B(A):
    pass 

class C:
    def dothis(self):
        print('C class')

class D(B, C):
    pass

print(D.mro())
# call order: D=>B=>A=>C
d_inst = D()
d_inst.dothis()
#  When D() is called python looks in the D class is there is the dothis method
# then at the first method D inhertis from which is B and then it look for
# the method in B and when it doesnt find it, it looks in A and then executes the method
# Therefore when it comes to python inheritance, it does a depth search and not a breadth search
