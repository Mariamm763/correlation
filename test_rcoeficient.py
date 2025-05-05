import unittest
from rcoefficient import rcoefficient

class Testrcoeficient(unittest.TestCase):

    def test_rcoeficient_positive(self):
        a = [1,2,3]
        b = [2,4,6]
        self.assertAlmostEqual(rcoefficient(a,b),1.0)
    
    def test_rcoeficient_negativecorrelation(self):
        a = [1, 2, 3]
        b = [6, 4, 2]
        self.assertAlmostEqual(rcoefficient(a, b), -1.0)
    
    def test_rcoeficient_correlation(self):
        a = [1, 2, 3]
        b = [7, 7, 7]
        with self.assertRaises(ZeroDivisionError):
            rcoefficient(a, b)

if __name__ == "__main__":
    unittest.main()
