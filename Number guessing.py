import random
secret_num=random.randint(1,100)
while True:
    guess=int(input("Guess a number between 1 to 100:"))
    if guess==secret_num:
        print("Congartulations!You guessed it Right")
        break
    elif guess<secret_num:
        print("Too Low!Try Again")
    else:
        print("Too High!try Again")
    