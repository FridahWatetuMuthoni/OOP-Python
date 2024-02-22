# Object Oriented Programming

## Instance Methods and Attributes

Classes basically provide the blueprint to create objects.
Each object has the same methods but its state is different in each instance

## Encapsulation

Encapsulation basically refers to the safe storage of data(as
attributes) in an instance.
Data should only be accessed with the getter function or instance methods
Data should be validated as correct depending on the class requirements.
Data should be safe from changes by external processes

## **init** constructor

The **init** is a special method that allows us to initialize attributes
the moment the instance is created.

## polymophism

Polymophism is when several classes have the same method in them.
One example of polymophism is the len() function which can be used by
several objects: strings, lists, dicts, tuples etc.

```python

string = 'hello'

#This is the same as
print(string.__len__())
#this
print(len(string))

```

## abstract base classes

An abstract class is a kind of 'model' for other classes to be defined.
it is not designed to construct instances, but can be subclassed by regular classes.
Abstract classes can define an interface, or methods that must be implemented by its subclasses.
If a class does not implement all required methods it will raise TypeError at runtime.
To make a class Abstract Base Class (ABC), you need to import `abc` module and use `@abstractmethod` decorator above any abstract methods.
The python abc module enables the creation of abstract base classes.

## Inheritance

When working in a child class we can choose to implement parent class methods
in different ways.

1. inherit: simply use the parents class defined method
2. Override/Overload: provide childs own version of the method
3. Extend: do work in addition to that in parent's method
4. provide: implement abstract method that parent requires
