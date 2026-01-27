"""בדיקות למחשבון"""

from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulo, factorial
from ui import get_number, show_menu
from stats import average, find_max, find_min, median


# בדיקות פעולות בסיסיות
assert add(3, 2) == 5, "בדיקת חיבור נכשלה"
assert subtract(10, 4) == 6, "בדיקת חיסור נכשלה"
assert multiply(4, 3) == 12, "בדיקת כפל נכשלה"
assert divide(20, 4) == 5, "בדיקת חילוק נכשלה"

# בדיקות פעולות מתקדמות
assert power(2, 3) == 8, "בדיקת חזקה נכשלה"
assert square_root(16) == 4, "בדיקת שורש נכשלה"

# בדיקות פעולת מודולו
assert modulo(10, 3) == 1, "בדיקת מודולו נכשלה"
assert modulo(20, 5) == 0, "בדיקת מודולו נכשלה"

# בדיקות פעולת פקטוריאל
assert factorial(0) == 1, "בדיקת פקטוריאל נכשלה"
assert factorial(5) == 120, "בדיקת פקטוריאל נכשלה"

# בדיקות פונקציות סטטיסטיות – ממוצע
assert average([1, 2, 3, 4, 5]) == 3, "בדיקת ממוצע נכשלה"
assert average([10, 20]) == 15, "בדיקת ממוצע נכשלה"

# בדיקות פונקציות סטטיסטיות – מקסימום
assert find_max([1, 7, 3, 9, 2]) == 9, "בדיקת מקסימום נכשלה"

# בדיקות פונקציות סטטיסטיות – מינימום
assert find_min([1, 7, 3, 9, 2]) == 1, "בדיקת מינימום נכשלה"

# בדיקות פונקציות סטטיסטיות – חציון
assert median([1, 3, 5]) == 3, "בדיקת חציון נכשלה"
assert median([1, 2, 3, 4]) == 2.5, "בדיקת חציון נכשלה"


print("✅ כל הבדיקות עברו בהצלחה!")
