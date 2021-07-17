import unittest
from student import Student

class Test_Student(unittest.TestCase):

    def setUp(self):                                                            # common input values for all test cases 
        self.a = Student('Kevin', 'George', 15, 82)
        self.b = Student('Rose', 'Bradley', 15, 85)

    def tearDown(self):                                                         # To remove any property once test case executed
        pass

    def test_name(self):
        
        self.assertEqual(self.a.email, 'Kevin.George@gmail.com')                # changed first name and check correspnding email
        self.a.fname = 'Louis'
        self.assertEqual(self.a.email, 'Louis.George@gmail.com')

    def test_score(self):

        self.assertEqual(self.a.marks(), (82 * 1.02))                          # changed score and tested against updated score
        self.b.score = 80
        self.assertTrue(self.b.marks() == self.b.score * self.b.marks_incr)

    def test_details(self):

        self.assertEqual(self.b.email, 'Rose.Bradley@gmail.com')                
        self.b.lname = 'Mckarthy'                                              # changed lname and tested corresponding email
        self.assertTrue(self.b.email == 'Rose.Bradley@gmail.com')


if __name__ == '__main__':
    unittest.main()


