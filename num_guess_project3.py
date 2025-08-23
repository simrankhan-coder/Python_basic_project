import random
number=random.randint(1,100)
attempt=0
max_attempts=7

print(" Guess the Number(1 to 100)")
while attempt<max_attempts:
    try:
        guess=int((input(f"Attempt{attempt+1}:Enter your Guess:")))
        attempt+=1
        if(guess==number):
            print("Correct!You guesses it..")
            break
        elif guess<number:
            print("Too Low value!")
        else:
            print("Too High value!")
    except ValueError:
        print("Please enter a valid number.")
    if attempt==max_attempts and guess!=number:
        print(f"Out of attempts!The number was {number}.")