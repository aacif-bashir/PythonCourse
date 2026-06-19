import utils.transport
import utils.session
import random 

computer = random.choice([-1, 0, 1])
computerDict = {-1: "snake", 0: "water", 1: "gun"}

you = input("Enter the choice (s/w/g): ")
yourDict = {"s": "snake", "w": "water", "g": "gun"}

yourChoice = yourDict[you]
computerChoice = computerDict[computer]

print(f"Computer choice is {computerChoice} and your choice is {yourChoice}")

if computerChoice == yourChoice:
    print("Draw")

elif computerChoice == "snake" and yourChoice == "water":
    print("You lose")

elif computerChoice == "water" and yourChoice == "gun":
    print("You lose")

elif computerChoice == "gun" and yourChoice == "snake":
    print("You lose")

else:
    print("You win")