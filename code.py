import random
program=random.randint(0,2)
print("Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("0 For Rock and 1 For paper and 2 For scissor")
user=int(input("Enter a number: "))
if(program==user):
    print("Draws")
elif (program==0 and user==2) or (program==1 and user==0) or (program==2 and user==1):
    print("Loses")
else:
    print("Wins")
