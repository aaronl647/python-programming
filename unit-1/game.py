#ask user to guess your secret number

#loop as long as users unput is not equal to secret number

#print message if it is equal, then end loop

#if guess is greater or less than 2, print almost there
#if guess is greater or less than secret by 2, print too far 

secret = 7
guess = int(input("Guess my secret number: "))

while guess != secret:
    print("Not correct")
    guess = int(input("Guess my secret number: "))
print("You got it!")