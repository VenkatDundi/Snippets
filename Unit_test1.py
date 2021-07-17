import unittest
from math import factorial as fct                  

''' Sample Unit test checks for two functions with various test cases and outcomes '''

def fact(n):
    f = 1

    if isinstance(n,int):                           # Sample unit test scenario to test few cases for Factorial
        for i in range(1,n+1):
            f *= i
        return f
    else:
        raise ValueError("Can't calculate factorial of a string")

def palindrome(s):                                  # Sample unit test scenario to test few cases for Palindrome

    s = reversed(list(s))
    return ''.join(s)
    

class SampleTest(unittest.TestCase):

    def test_fact1(self):                                        # Testing usual scenario
        n = 8
        factorial = fact(n)
        self.assertEqual(factorial, fct(n), "Should be {}".format(fct(n)))

    def test_fact2(self):                                       # Testing error scenario
        n = 'K'
        factorial = fact(n)
        self.assertEqual(factorial, fct(n), "Should be {}".format(fct(n)))

    def test_fact3(self):
        n = 'abc'                                               # Testing raise exception scenario
        #self.assertRaises(ValueError, fact, n)
        
        with self.assertRaises(ValueError):
            fact(n)

    def test_palindrome1(self):                                 # test cases should start with 'test'
        s = input("\nEnter the String : ")
        self.assertEqual(s[::-1], palindrome(s), "Should be {}".format(s[::-1]))

    def test_palindrome2(self):
        s = input("\nEnter the String : ")
        self.assertEqual(s[::-2], palindrome(s), "Should be {}".format(s[::-1]))

if __name__ == '__main__':
    unittest.main()