import unittest

def fun(x,y):

    return x*y

class myTest(unittest.TestCase):

        def test(self):
            
            self.assertEqual(fun(4,5),20)

if __name__=='__main__':
    
    unittest.main()
