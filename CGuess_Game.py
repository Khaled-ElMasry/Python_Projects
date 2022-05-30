#User Think of a Number ,Computer will Guess it and Provide Feedback.
import random
print("<<<Think of a Number>>>")

def Guess():
    Low,High = map(int, input("Enter The Lowest and Highest Number To Guess Between: ").split())
    Feedback=""
    while Feedback != 'C':
        Guessed_Num = random.randint(Low,High)

        Feedback = input(f""" is {Guessed_Num} is The Right answer ??
        Too High (H), Too Low (L), Correct (C): """).upper()

        if Feedback == 'H':
            High = Guessed_Num - 1
        elif Feedback == 'L':
            Low = Guessed_Num + 1

    print(f"Done ,{Guessed_Num} is The Right answer")

while True: 
    try:
        Guess()
    except ValueError:
        print("Enter Corrct Values")
        continue

# Try the Guess function:
# if there's an error excute except:   
    # it will print something
    # continue and the start the try again
# in this way >> i made a while loop on exception part

