"""
ui מודול
========
.מכיל פונקציות לממשק המשתמש
"""

def get_number(prompt):
    """מקבל מספרים מהמשתמש"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("שגיאה! נא להזין מספר")


def show_menu():
    """מציג את התפריט"""
    print("\n=== תפריט ===")
    print("חיבור 1.")
    print("חיסור 2.")
    print("כפל 3.")
    print("חילוק 4.")
    print("חזקה 5.")
    print("שורש 6.")
    print("עצרת 7.")
    print("ממוצע 8.")
    print("מקסימום 9.")
    print("מינימום 10.")
    print("חציון 11.")
    print("--- היסטוריה ---")
    print("הצג היסטוריה 12.")
    print("נקה היסטוריה 13.")
    print("יציאה 0.")
    return input(" :בחר פעולה")

