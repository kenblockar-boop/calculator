"""
history מודול
=============
.שומר היסטוריה של חישובים
"""

# רשימה לשמירת ההיסטוריה
calculation_history = []

def add_to_history(expression, result):
    """מוסיף חישוב להיסטוריה"""
    entry = f"{expression} = {result}"
    calculation_history.append(entry)

def show_history():
    """מציג את כל ההיסטוריה"""
    if not calculation_history:
        print("אין היסטוריה עדיין")
        return
    print("\n=== היסטוריה ===")
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. {entry}")

def clear_history():
    """מנקה את ההיסטוריה"""
    calculation_history.clear()
    print("ההיסטוריה נמחקה")
