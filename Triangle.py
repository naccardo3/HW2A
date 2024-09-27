# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a<=0 or b<=0 or c<=0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    
    if a == b == c:
        return 'Equilateral'
    
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2):
        return 'Right'
    
    if a == b or b == c or a == c:
        return 'Isoceles'
    return 'Scalene'
