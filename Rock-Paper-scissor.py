import random
choices=["rock","paper","scissor"]
user=input("enter rock,paper or scissor:")
computer=random.choice(choices)
print("your choose:",user)
print("computer chose:",computer)
if user==computer:
    print("it is a tie!")
elif (user=='rock' and computer=='scissor') or (user=='paper' and computer=='rock') or(user=='scissor'and computer=='paper'):
    print("You win!")
else:
    print("Computer wins!")

