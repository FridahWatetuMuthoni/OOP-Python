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
