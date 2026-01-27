"""
stats מודול
===========
.פונקציות סטטיסטיות בסיסיות
"""


def average(numbers):
    """מחשב ממוצע של רשימת מספרים"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """מוצא את המספר הגדול ביותר"""
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers):
    """מוצא את המספר הקטן ביותר"""
    if not numbers:
        return None
    return min(numbers)


def median(numbers):
    """מוצא את החציון"""
    lst = list(numbers)
    l = len(lst)
    if l % 2 == 1:
        return lst[l // 2]
    return (lst[l // 2 - 1] + lst[l // 2]) / 2


