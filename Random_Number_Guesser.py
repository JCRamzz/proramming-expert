import random
while True:
    start = input("Enter the start of the range: ")
    if not start.isdigit():
        print("Please enter a valid number.")
        continue
    break

while True:
    end = input("Enter the end of the range: ")
    if not end.isdigit():
        print("Please enter a valid number.")
        continue
    if int(end) < int(start):
        print("Please enter a valid number.")
        continue
    break

wrongCount = 0
correctNum = random.randint(int(start), int(end))

while True:
    guess = input("Guess a number: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    wrongCount += 1

    if int(guess) == correctNum:
        suffix = ''
        if wrongCount > 1:
            suffix = 's'
        print(f"You guessed the number in {wrongCount} attempt{suffix}.")
        break


