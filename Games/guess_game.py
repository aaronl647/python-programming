#ask user to guess your secret number

#loop as long as users unput is not equal to secret number

#print message if it is equal, then end loop

#if guess is greater or less than 2, print almost there
#if guess is greater or less than secret by 2, print too far 

def wrong():
    return "Not correct"
    
def almost():
    return "Almost there!"

def far():
    return "Too far!"

secret = 7
guess = int(input("Guess my secret number: "))

while guess != secret:
    print(wrong())
    if guess +- 2:
        print(almost())
    elif guess +- 3:
        print(far())
    guess = int(input("Guess my secret number: "))

print("You got it!")