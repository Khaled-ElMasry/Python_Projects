#it's a word a game >> There's an already written story and you've to fill the gaps with any words.
# for practising string concatenation in different ways.
import random

Profession = input("profession: ")
Name = input("Name: ")
Age = int(input("Age: "))
Study = input("Study Field: ")


story1 = "My Name is {}, IM Studying {}, \
I will work as a {}, My Age is {}".format(Name,Study,Profession,Age)

story2 = f"""
{Name}'s father was a great {Profession}, 
He studied {Study},
And worked as {Profession},
He died at the age of {Age} 
"""

story3 = f"{Name} was one of the greatest {Profession}s, \
He studied {Study}, \
His first invention was at the age of {Age}"

# printing as C LANGUAGE using symbols like %d %s
story4 = "His Name is %s, His Age is %d, His profession is %s, and last he studies %s" % (Name,Age,Profession,Study)

#random.choice function take 2 arguments >> first must be a list or tuple or ... 
print(random.choice((story1,story2,story3,story4)))

