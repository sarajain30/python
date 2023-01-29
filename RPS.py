import random

computer = random.randint(1,3)

choice = int(input("type 1 for rock, 2 for paper or 3 for scissors :"))

if computer == 1:
    print("I picked rock ")
elif computer == 2:
    print("I picked paper ")
elif computer == 3:
    print("I picked scissors ")


if computer == choice:
    print("it's a tie ")
elif computer == 1 and choice == 2:
    print("you win! ")
elif computer == 2 and choice == 3:
    print("you win! ")
elif computer == 3 and choice == 1:
    print("you win! ")
else:
    print("you lose ")

    






