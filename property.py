class Alphabet:
    def __init__(self,value):
        self._value=value
    def getValue(self):
        print("Getting value")
        return self._value 
        
    def Setvalue(self,value):
        print("Setting value to "+value)
        self._value=value 
    def delvalue(self):
        print("Deleting value")
        del self._value 
    value=property(getValue,Setvalue,delvalue)
x=Alphabet("python")
print(x.value)
x.value="code"
del x.value
