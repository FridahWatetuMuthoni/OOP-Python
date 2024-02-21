#class creation
class Animal:
    def __init__(self, number):
        self.number = number 
    def increase(self):
        self.number += 1
        return self.number

#creating a class instance and calling its methods
#each method has a different memory address
dog = Animal(10)
print(dog.increase())

#checking the type of the dog instance
print(type(dog))

#Encapsulation
class MyInteger:
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.value = val
    
    def get_val(self):
        return self.value
    
    def increment_value(self):
        self.value = self.value + 1

# __init__ constructor
# init method is called automatically when an object instance is created

class MyNum:
    def __init__(self,value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value
    
    def increment(self):
        self.value = self.value + 1
        return self.value

# class attributes
"""
Attributes look up order: When looking up an attribute, the attribute is first
searched in the instance before looking for it in the class.
Instances have access to the class data which is the same accross all the instances
"""

class YourClass:
    classy = 10
    
    def __init__(self):
        self.insty = 0
    
    def self_value(self, value):
        self.insty = value
    
    def get_value(self):
        return self.insty
        
dd = YourClass()
print(dd.classy)
print(dd.get_value())


#counts the number of objects created from the class
class InstanceCounter:
    count = 0
    
    def __init__(self, value):
        self.value = self.filter_int(value)
        InstanceCounter.count += 1
        
    @staticmethod
    def filter_int(value):
        if not isinstance(value, int):
            return 0
        else:
            return value
    
    @classmethod
    def get_count(cls):
        return cls.count
        
    def set_value(self, value):
        self.value = value 
    
    def get_value(self):
        return self.value
     

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in [a, b, c]:
    print(f"Value of object: {obj.get_value()}")
    print(f"Count: {obj.get_count()}")

#polymorphism

string = 'hello'
print(string.__len__())
print(string.__contains__('lo'))
print(string.__add__(' world'))