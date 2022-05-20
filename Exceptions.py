# You'll have to use the following strings:
# 1) "Enter the numerator: "
# 2) "Enter the denominator: "
# 3) "The numerator is not a number."
# 4) "The denominator is not a number."
# 5) "You cannot divide by 0."
# 6) "This division cannot be performed."
# 7) "The result of this division is _."
# 8) "Goodbye!"
# char1 = "denominator"
# char2 = "numerator"
# char3=""
try:
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")
    try:
        numerator = float(numerator)

    except ValueError:
        print("The numerator is not a number.")

    try:
        denominator = float(denominator)
    except ValueError:
        print("This division cannot be performed.")

    try:
        division = numerator / denominator
        print(f"The result of this is division is: {division}")

    except ZeroDivisionError:
        print("You cannot divide by 0.")
except Exception:
    print("This division cannot be performed.")
finally:
    print("Goodbye!")