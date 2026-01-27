"""
geometry מודול
==============
חישובי שטחים גיאומטריים
"""

from constants import PI


def circle_area(radius):
    """מחזיר את שטח העיגול"""
    return PI * radius ** 2


def rectangle_area(width, height):
    """מחזיר את שטח המלבן"""
    return width * height


def triangle_area(base, height):
    """מחזיר את שטח המשולש"""
    return (base * height) / 2
