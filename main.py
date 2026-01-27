# מחשבון פשוט
# גרסה 3.1 – מבנה תקין + תפריט סטטיסטיקה

from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulo, factorial
from ui import get_number, show_menu, statistics_menu
from stats import average, find_max, find_min, median
from history import add_to_history, show_history, clear_history
from constants import show_constants

print("╔════════════════════════════╗")
print("║    !ברוכים הבאים למחשבון    ║")
print("║           גרסה 4.0         ║")
print("╚════════════════════════════╝")



while True:
    choice = show_menu()

    if choice == "0":
        print("!להתראות")
        break

    # פעולות בסיסיות
    elif choice == "1":
        num1 = get_number("הכנס מספר ראשון:")
        num2 = get_number("הכנס מספר שני:")
        result = add(num1, num2)
        print(f"תוצאה: {result}")
        add_to_history(f"{num1} + {num2}", result)

    elif choice == "2":
        num1 = get_number("הכנס מספר ראשון:")
        num2 = get_number("הכנס מספר שני:")
        result = subtract(num1, num2)
        print(f"תוצאה: {result}")
        add_to_history(f"{num1} - {num2}", result)

    elif choice == "3":
        num1 = get_number("הכנס מספר ראשון:")
        num2 = get_number("הכנס מספר שני:")
        result = multiply(num1, num2)
        print(f"תוצאה: {result}")
        add_to_history(f"{num1} * {num2}", result)

    elif choice == "4":
        num1 = get_number("הכנס מספר ראשון:")
        num2 = get_number("הכנס מספר שני:")
        result = divide(num1, num2)
        print(f"תוצאה: {result}")
        add_to_history(f"{num1} / {num2}", result)

    # פעולות מתקדמות
    elif choice == "5":
        num1 = get_number("הכנס מספר:")
        num2 = get_number("הכנס חזקה:")
        result = power(num1, num2)
        print(f"תוצאה: {result}")
        add_to_history(f"{num1} ** {num2}", result)

    elif choice == "6":
        num = get_number("הכנס מספר:")
        result = square_root(num)
        print(f"תוצאה: {result}")
        add_to_history(f"√{num}", result)

    elif choice == "7":
        num = get_number("הכנס מספר:")
        result = factorial(num)
        print(f"תוצאה: {result}")
        add_to_history(f"{num}!", result)

    # תפריט סטטיסטיקה
    elif choice == "8":
        lst_num = []
        while True:
            numbers = input("הכנס רשימת מספרים:")
            if numbers == "0":
                break
            lst_num.append(float(numbers))

        while True:
            statistics_menu()
            stat_choice = input("בחר אפשרות: ")
            if stat_choice == "0":
                break

            if stat_choice == "1":
                result = average(lst_num)
                print(f"ממוצע: {result}")
                add_to_history(f"average({numbers})", result)

            elif stat_choice == "2":
                result = find_max(lst_num)
                print(f"מקסימום: {result}")
                add_to_history(f"max({numbers})", result)

            elif stat_choice == "3":
                result = find_min(lst_num)
                print(f"מינימום: {result}")
                add_to_history(f"min({numbers})", result)

            elif stat_choice == "4":
                result = median(lst_num)
                print(f"חציון: {result}")
                add_to_history(f"median({numbers})", result)

            else:
                print("בחירה לא חוקית בתפריט סטטיסטיקה")

    elif choice == "9":
        show_constants()
        
    # היסטוריה
    elif choice == "10":
        show_history()

    elif choice == "11":
        clear_history()

    else:
        print("!בחירה לא חוקית")
