#ask user to guess your secret number

#loop as long as users unput is not equal to secret number

#print message if it is equal, then end loop

secret = 7
guess = int(input("Guess my secret number: "))

while guess != secret:
    print("Not correct")
    guess = int(input("Guess my secret number: "))
print("You got it!")