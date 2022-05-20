string = input("Enter a word: ")

x = {}

for key in string:
    x[key] = x.get(key, 0) + 1
for key, value in x.items():
    print(f"{key}: {value}")
