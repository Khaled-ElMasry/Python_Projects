#Hangman
#A Radnom word is choosen, as W___ , user have to guess the missing chars, and he had 7 valid trials.
import random
words = ["absence","abuse","account","accident","beneath","bend","benefit","biology","bitter","candidate","campaign","camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient","supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle","global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat","yellowish","zone"]

word = random.choice(words).upper()





#Copy the random word to a list of chars, and reveal the first char only.
#instead of writig the 5 line code .. i write into 1 line:
# for i,char in enumerate(word):
#     if i == 0:
#         print(char,end="")
#     else:
#        print("_",end="")
GuessWord = list(f"{word[0]}{'_'*(len(word)-1)}")


#replace the first char with *, keep the rest of the word.
word = f"*{word[1:]}"
# or
# word = word.replace(word[0],"*")


def win():
    #here i join the list back to a string and captalize it
    GuessWord = "".join(GuessWord).capitalize()

    #here i made my touch and used center function >> to center the word between ~ 
    #total count will be 12 >> so if the word has 5 chars , it will be printed as >> 12-5=7 >> 4~ word 3~ >> ~~~~word~~~ 
    x = GuessWord.center(12,'~')
    print(f"\nBravo, The Word is {x}\n")



lives = 7
#keep repeating until the lives end.
# for i in range(lives):
while True:
    if '_' in GuessWord == 0:
        win()
        break

    print("".join(GuessWord).capitalize())

#ask user to guess a char, if he enters multiple chars as input, he will get error msg.
    User_Guess = input("\nGuess The Character: ").upper()
    while len(User_Guess) != 1:
        User_Guess = input("\nonly 1 char allowed, Enter Again: ").upper()
  

#find the index of the guessed char .. if not exist will get -1
    loc = word.find(User_Guess)

#if the char exist in the word, it will replace _ in GuessWord with the char
    if loc > 0:
        GuessWord[loc] = User_Guess

# i wanted to replace the gussed char in the orignal word with * >> but i could't assign it in this way >>word[loc] = "*"<<, because assigment works only with list not string
# so i used replace function which take (old,new,how many chars in the sentence will be replaced)  
        word = word.replace(User_Guess,"*",1)
    else:
        lives -=1
    #  def loss():
        if "".join(GuessWord).count('_') > 0 and lives == 0:
            print("\nYou Lost.")
            break
        print("Wrong Guess, Try again")




