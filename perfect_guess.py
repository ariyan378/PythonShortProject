import random
n = random.randint(1,100)

a= -1
guesses = 0 
while (a != n):
    guesses +=1
    a = int (input("Guess a number : "))
    if(a>n):
        print("Lower the number please :) ")
    else:
        print("Higher number please :)") 


print(f"You have guessed the number corrrectly in {guesses} attempt")