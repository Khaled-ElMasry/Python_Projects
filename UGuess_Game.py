#User Guess The Number
import random
Num = 0
x= int(input("Enter Last Number for Range: "))
#Pick a Random Num between 1 and x .. x is included.
XGussed = random.randint(1,x)

def guess():
    global Num
    while Num != XGussed:
        Num = int(input("Enter Gussed Number: "))
        if XGussed > Num:
            print("Too Low, Try Agin")
        elif XGussed < Num:
            print("Too High, Try Agin")
    print(f"Congratulation, {Num} is The Right Answer")

guess()

#In The FUNCTION i used "global" beacuse without it i will get a " referenced before assignment" Error >> which mean i have the same Variable twice one local and one global .. python is confused which one to work on .. so i have to tell him to work on the global.
#"global" must be at the top of the function .. otherwise i will get a "global declaration" Error.