class Person(object):
    
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def display(self):
        return "{} {}, aged {}".format(self.fname,self.lname,self.age)
    
class Student(Person):

    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.year = year
    
p1 = Person('Micheal', 'Raj', 23)

print(p1.display())

s1 = Student('George', 'Kenny', 25, 1997)

print(s1.display())