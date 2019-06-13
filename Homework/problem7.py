
#list of cereals
breakfast = ["Wheaties", "Froot Loops", "Cinnamon Toast Crunch", "Frosted Flakes", "Cap n' Crunch"]

#defining functions 
def cereal_time():
    return " are yummy!"

def cereal_time_2():
    return " is yummy!"

for food in breakfast:
    #checks for the letter s at the end of every item in the list 
    #[-1] makes the code check the last letter first
    if food[-1] == "s":
        #prints out "are yummy" if a 's'is found
        print(food + cereal_time())
        #prints "is yummy" if there is no s found
    else: 
        print(food + cereal_time_2())
