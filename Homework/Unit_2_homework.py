#list intersection
'''
fruits = ["apple", "orange", "grapes", "mango"] 
second_fruits = ["mango", "pear", "grapes", "apple", "pineapple"]
new_list = []

for fruit in fruits:
    for fruit2 in second_fruits:
        #compare lists to look for similarities between the two lists
        if fruit == fruit2:
            #create new list with matching
            new_list.append(fruit)
            
print(new_list)
'''

#function accepts two lists and returns the intersection
def list_intersection(first_list, second_list):
    #create an empty list
    intersection = []
    #check each item in the first list
    for item in first_list:
        if item in second_list:
            intersection.append(item)
    
    return intersection 

def item_count(list_a, search_key):
    counter = 0
    for item in list_a:
        if item == search_key:
            counter += 1
    
    return counter 


print(item_count([1,2,4,3,4], 4))

'''
print(list_intersection([1,2,3,4], [1,2,3])) 
'''
