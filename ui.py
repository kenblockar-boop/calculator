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


def statistics_menu():
    print("\n--- תפריט סטטיסטיקה ---")
    print("1. ממוצע")
    print("2. מקסימום")
    print("3. מינימום")
    print("4. חציון")
    print("0. חזרה לתפריט הראשי")

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
    print("סטטיסטיקה 8.")
    print("הצג קבועים 9.")
    print("--- היסטוריה ---")
    print("הצג היסטוריה 10.")
    print("נקה היסטוריה 11.")
    print("יציאה 0.")
    return input(" :בחר פעולה")


