my_string = input("Enter a word or sentence, please. ")
reversed_string = ''
'''
#strings are immutable
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i], end = ' ')
'''

for i in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[i]

print(reversed_string)
