# -*- coding: utf-8 -*-
"""
A module for classifying types of triangles based on side lengths.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on the lengths of its three sides.

    Parameters:
    side_a (int): Length of the first side of the triangle.
    side_b (int): Length of the second side of the triangle.
    side_c (int): Length of the third side of the triangle.

    Returns:
    str: Type of triangle - 'Equilateral', 'Isosceles', 'Scalene', 'Right', 
         'NotATriangle', or 'InvalidInput'.
    """
    result = 'Scalene'  # Default result if no other condition is met

    # Validate input types and value ranges
    if not all(isinstance(side, int) for side in (side_a, side_b, side_c)):
        result = 'InvalidInput'
    elif any(side <= 0 or side > 200 for side in (side_a, side_b, side_c)):
        result = 'InvalidInput'
    # Check if the inputs form a valid triangle
    elif (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        result = 'NotATriangle'
    # Classify triangle type
    elif side_a == side_b == side_c:
        result = 'Equilateral'
    elif (side_a ** 2 + side_b ** 2 == side_c ** 2) or \
         (side_a ** 2 + side_c ** 2 == side_b ** 2) or \
         (side_c ** 2 + side_b ** 2 == side_a ** 2):
        result = 'Right'
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        result = 'Isosceles'
    return result
