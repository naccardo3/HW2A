# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be a isoceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4, 4, 2), 'Isoceles', '4,4,2 should be a isoceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be a scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10, 8, 7), 'Scalene', '10,8,7 should be a scalene')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 is not triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be invalid')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1,1,1 should be invalid')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

