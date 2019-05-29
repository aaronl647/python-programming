def say_hi():
     return "my favourite greeting"

my_question = input("Do you want to know my favourite greeting? ")

if my_question == "yes":
    print(say_hi())
elif my_question == "no":
    print("okay..")
else:
    print("Invalid input, please try again.")
