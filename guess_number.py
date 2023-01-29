import random

number = random.randint(1, 100)

guess = 0
points = 10
print("you start with 10 points")

while guess != number and points > 0:
    guess = int(input("guess a number between one and hunndred :"))

    if guess > number:
        points = points-1
        print("my number is lower")
        print("you lost one point")
    if guess < number:
        points = points-1
        print("my number is higher")
        print("you lost one point")
    else:
        print(f"you scored {points} points")
        print("you won!!!")

    if points == 0:
        print("you lose😥 you have 0 points")
        print(f"my number was {number}")