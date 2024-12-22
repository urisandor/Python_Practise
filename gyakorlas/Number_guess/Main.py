import random


random = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))
    if guess == random:
        break
    elif guess < random:
        print("The number is greater")
    elif guess > random:
        print("The number is lesser")

print(f"The number is {random}!!")
print("You Won!!")

