import abc 

class GetSetParent:
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, value):
        self.value = 0
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_value(self, value):
        if not isinstance(value, int):
            value = 0
        return super().set_value(value)
    
    def showdoc(self):
        print(f"GetSetInt object {id(self)}, only accepts integer values")

class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.valuelist = [value]
    
    def get_value(self):
        return self.valuelist[-1]
    
    def get_values(self):
        return self.valuelist
    
    def set_value(self, value):
        self.valuelist.append(value)
    
    def showdoc(self):
        print(f"GetSetList object, len {len(self.valuelist)} stores  a history of values set")

gsl = GetSetList(5)
gsl.set_value(10)
gsl.set_value(20)
print(gsl.get_value())
print(gsl.get_values())
gsl.showdoc()