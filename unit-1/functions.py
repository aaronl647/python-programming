#function with a single argument
'''
def print_msg(message):
    print(message)

print_msg("python rocks!!!")
'''

#function that returns a result
'''
def square(value):
    result = value * value
    return result

answer = square(10)
print(answer)
'''

#functions with multiple arguments
'''
def greetings(name, job, hobby):
    print(f'Hello {name} your job is {job} and you like {hobby}')

greetings('Aaron', 'student', 'swimming')
'''
'''
def reverse_list(my_list):
    new_list = []
    #iterate over list in reverse order
    for list in range(len(my_list) - 1, -1, -1):
        #add each element to a list
        new_list.append(my_list[list])
        #return the reversed list
    return new_list

my_list = [1, 2, 3, 4, 5]
fruits = ["Apples","Oranges","Kiwi", "Banana"]
result = reverse_list(my_list)

print(result)
print(reverse_list(fruits))
'''

'''
def reverse_string(my_string):
    reversed_string = ''
    for i in range(len(my_string) - 1, -1, -1):
         reversed_string += my_string[i]
    return reversed_string

def is_palindrome(word):
    #check if word is the same forwards as backwards
    word_reversed = reverse_string(word)
    if word_reversed == word:
        return True
    return False
    #return True if it is, False otherwise


print(is_palindrome(input("Enter a word. ")))
'''


