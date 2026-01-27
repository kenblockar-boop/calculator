"""
advanced מודול
==============
.מכיל פעולות חשבון מתקדמות: חזקה, שורש, מודולו
"""

def power(base, exponent):
    """העלאה בחזקה"""
    return base ** exponent


def square_root(n):
    """שורש ריבועי"""
    if n < 0:
        return "שגיאה! אין שורש למספר שלילי"
    return n ** 0.5


def modulo(a, b):
    """שארית מחילוק"""
    return a % b

def factorial(n):
    """מחשב עצרת של מספר"""
    if n < 0:
        return "!שגיאה: אין עצרת למספר שלילי"
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result

