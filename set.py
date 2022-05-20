chars = set()

while True:
    character = input("Enter a character: ")

    if character in chars or len(character) > 1:
        print(f"Number of unique characters entered: {len(chars)}")
        break

    chars.add(character)