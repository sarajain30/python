import random

score = 0

while True:
    word = input("type rock, paper, scissors or quit: ")

    if word == "rock":
        choice = 1
    elif word == "paper":
        choice = 2
    elif word == "scissors":
        choice = 3
    elif word == "quit":
        print(f"you scored {score} points ")
        break
    else:
        print("sorry that does not work you have to type rock, paper, scissors or quit ")
        continue

    computer = random.randint(1,3)

    if computer == 1:
        print("I picked rock ")
    elif computer == 2:
        print("I picked paper ")
    elif computer == 3:
        print("I picked scissors ")
    
    
    if computer == choice:
        print("it's a tie ")
    elif computer == 1 and choice == 2:
        score = score + 1
        print("you win! ")
    elif computer == 2 and choice == 3:
        score = score + 1
        print("you win! ")
    elif computer == 3 and choice == 1:
        score = score + 1
        print("you win! ")
    else:
        score = score - 1
        print("you lose ")

        






