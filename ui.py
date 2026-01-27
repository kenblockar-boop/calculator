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
    """מציג את התפריט"""
    print("\n--- תפריט סטטיסטיקה ---")
    print("1. ממוצע")
    print("2. מקסימום")
    print("3. מינימום")
    print("4. חציון")
    print("0. חזרה לתפריט הראשי")


def geometry_menu():
    """מציג את התפריט"""
    print("\n--- תפריט גאומטריה ---")
    print("1. שטח עיגול")
    print("2. שטח מלבן")
    print("3. שטח משולש")
    print("0. חזרה לתפריט הראשי")

def percentages_menu():
    """מציג את התפריט"""
    print("\n--- תפריט אחוזים ---")
    print("1. כמה זה X אחוז מ־Y")
    print("2. אחוז שינוי בין שני ערכים")
    print("3. הוספת אחוז לערך")
    print("4. הורדת אחוז מערך")
    print("5. כמה אחוז X מתוך Y")
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
    print("גאומטריה 10.")
    print("אחוזים 11.")
    print("--- היסטוריה ---")
    print("הצג היסטוריה 12.")
    print("נקה היסטוריה 13.")
    print("יציאה 0.")
    return input(" :בחר פעולה")



