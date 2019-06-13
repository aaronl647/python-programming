def say_hi():
     print("my favourite greeting")

my_question = input("Do you want to know my favourite greeting? Enter 'yes' to see greeting ")

if my_question.lower() == "yes":
    say_hi()
else:
    print("Invalid input, please try again")
