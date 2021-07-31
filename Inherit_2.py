class Base1(object):
    def __init__(self):
        self._str1 = "Geek1"
        print("Base1")
        print(self._str1)
  
class Base2(object):
    def __init__(self):
        self._str1 = "Geek2"        
        print("Base2")
        print(self._str1)
  
class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("derived")
    
    def printStrs(self):
        print(self._str1, self._str1)

d = Derived()
d.printStrs()