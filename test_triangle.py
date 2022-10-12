# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangle(unittest.TestCase):
    """This code implements the unit test functionality
       define multiple sets of tests as functions with names that begin
    """
    def test_right_triangle_a(self):
        "This tests the Right triangle functionality"
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def test_right_triangle_b(self):
        "This tests the Right triangle functionality"
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def test_equilateral_triangle(self):
        "This tests the equilateral triangle functionality"
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def test_scalene_triangle(self):
        "This tests the scalene triangle functionality"
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')
    def test_isoceles_triangle(self):
        "This tests the isoceles triangle functionality"
        self.assertEqual(classify_triangle(4,4,5),'Isoceles','4,4,5 should be Isoceles')
    def test_not_a_triangle(self):
        "This tests if a valid triangle "
        self.assertEqual(classify_triangle(1,1,4),'NotATriangle','1,1,4 is not a triangle')
    def test_valid_integers(self):
        "This tests if given invalid inputs"
        self.assertEqual(classify_triangle(3.4,4.5,6.7),'InvalidInput','are not integers')
    def test_valid_input_a(self):
        "This tests if given invalid inputs"
        self.assertEqual(classify_triangle(0,-2,-1),'InvalidInput','should be invalid input')
    def test_valid_input_b(self):
        "This tests if given invalid inputsy"
        self.assertEqual(classify_triangle('-sv',-3,4.0),'InvalidInput','should be invalid sides')
    def test_triangle_sides(self):
        "This tests the max size of a triangle"
        self.assertEqual(classify_triangle(300,499,500),'InvalidInput','should be invalid sides')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    