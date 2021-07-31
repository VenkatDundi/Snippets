class A():
    def m(self):
        print("Class A")

class B():
    def m(self):
        print("Class B")

class C(B, A):
    print("class C")

obj1 = C()

obj1.m()

print(C.mro())                 # Method Resolution Order based on convention of "OBJECT" super class
