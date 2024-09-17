import random

num = random.randint(0, 10)
while True:
    guess = input("Guess a number between 0 and 10: ")

    if int(guess) == num:
        print(guess + ' as the correct answer!')
    elif int(guess) < num:
        print("Too low try again")
    elif int(guess) > num:
        print("Too high try again")
    else:
        print("Error. Try again later")

