num = float(input("Enter a number: "))

if 10 <= num <= 20:
    num2 = float(input("Enter another number: "))
    sum = num + num2
    print(f"The sum of the two numbers is:{sum}")
    if sum >= 100:
        print("Wow that's a huge number bro!")
