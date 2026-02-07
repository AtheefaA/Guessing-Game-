import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)  

# Initialize guess variable
guess = None

# Play the guessing game
while guess != number:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You guessed it! The number was", number)