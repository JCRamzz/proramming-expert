strings = []
numbers = []

for i in range(5):
    strings.append(input("Enter a string: "))

for j in range(3):
    num = int(input("Enter a number: "))
    if 0 <= num <= 4:
        numbers.append(num)

for each in numbers:
    print(strings[each], end="")

