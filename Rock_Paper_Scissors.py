#Rock Paper Scissors Game With Validation

import random
com = random.choice(("R","P","S"))

user = ""
while user not in ["R","P","S"]:
    user = input("R for Rock, P for Paper, S for Scissors: ").upper()

lis = [["R","S"],["P","R"],["S","P"]]

def winner():
    if user == com:
        print("\tEQUAL, No winner")
    # elif user == "R" and com == "S" or user == "P" and com == "R" or user == "S" and com == "P":
    #     print("User winnnnnnnn!!")
    elif [user,com] in lis:
        print("\tYou win!!")
    else:
        print("\tYou Lost")
    
print(f"\nComputer choosed {com}, User choosed {user}")
winner()