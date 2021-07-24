class A():
    def __init__(self, a):
        self.a = a
    
    def __add__(self, o):
        return self.a + o.a

    def __gt__(self, o):
        if self.a > o.a:
            return "{} is greater than {}".format(self.a, o.a) 
        elif self.a < o.a:
            return "{} is greater than {}".format(o.a, self.a)
        else:
            return "{} is equal to {}".format(self.a, o.a)


ob1 = A(0)
ob2 = A(0)

print(ob1 + ob2)

print(ob1 > ob2)