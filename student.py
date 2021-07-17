class Student:

# Sample student class with attributes

    marks_incr = 1.02

    def __init__(self, fname, lname, age, score):                   
        self.fname = fname
        self.lname = lname
        self.age = age
        self.score = score
    
    @property                                                               # @property - Helps in achieving getter & setter menthods
    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)
    
    @property
    def details(self):
        return "{} {}, aged {}".format(self.fname, self.lname, self.age)

    def marks(self):
        return self.score * self.marks_incr