"""
percentages מודול
=================
פונקציות לחישוב אחוזים
"""


def percent_of(number, percent):
    """מחזיר כמה זה X אחוז מ־Y"""
    return (number * percent) / 100


def percentage_change(old_value, new_value):
    """מחזיר את אחוז השינוי בין שני ערכים"""
    if old_value == 0:
        raise ValueError("לא ניתן לחשב אחוז שינוי כאשר הערך המקורי הוא 0")
    return ((new_value - old_value) / old_value) * 100


def add_percentage(number, percent):
    """מוסיף אחוז לערך"""
    return number + percent_of(number, percent)


def subtract_percentage(number, percent):
    """מוריד אחוז מערך"""
    return number - percent_of(number, percent)


def what_percent(part, whole):
    """מחזיר כמה אחוז X הוא מתוך Y"""
    if whole == 0:
        raise ValueError("הערך הכולל לא יכול להיות 0")
    return (part / whole) * 100
