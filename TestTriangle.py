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
        
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')
    
    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isoceles','4,4,5 should be Isoceles')
    
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,1,4),'NotATriangle','1,1,4 is not a triangle')    
    
    def testIfValidIntegers(self): 
         self.assertEqual(classifyTriangle(3.4,4.5,6.7),'InvalidInput','3.4,4.5,6.7 are not integers')
    
    def testValidInputA(self): 
        self.assertEqual(classifyTriangle(0,-2,-1),'InvalidInput','0,-2,-1 should be invalid input')
        
    def testValidInputB(self): 
        self.assertEqual(classifyTriangle('-sv',-3,4.0),'InvalidInput','-sv,-3,4.0 should be invalid sides')
        
    def testTriangleSides(self): 
        self.assertEqual(classifyTriangle(300,499,500),'InvalidInput','300,499,500 should be invalid sides')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


