import random

numbers = [10, 20, 30, 40, 50, 60]
chosen_number = random.choice(numbers)
guess = int(input("Harsh, guess the number: "))
print("Numbers list is:", numbers)

if guess > chosen_number:
    print("Too high! Try again.")
elif guess < chosen_number:
    print("Too low! Try again.")
else:
    print("Correct! Well done Harsh")

print("Chosen number was:", chosen_number)