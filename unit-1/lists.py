#declare an empty list
classmates = []

#add items to list
classmates.append('Sue')
classmates.append('Shad')
classmates.append('Mayank')
classmates.append('Gus')
classmates.append('Chin')
classmates.append('Eva')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Julian')
classmates.append('Aaron')

'''
print(classmates)

#access an item at a specific position
#print(classmates[2]) #third element

#get the size of the list
#print(len(classmates))

#remove an item from end of list
classmates.pop()

print(classmates)

#insert at specific position
classmates.insert(0, 'Dan')
print(classmates)

#removing an item from the list
classmates.remove('Gus')
print(classmates)

#edit an item in the list
classmates[1] = 'Sue Work'
print(classmates)
'''

#iterate over a list
'''
for classmate in classmates:
    if(classmate == 'Gus'):
        print("Great, Gus is in the class!")
'''
'''
#edit elements while iterating
for index, classmate in enumerate(classmates):
    #classmates[index] = classmate.upper()
    classmates[index] = classmates[index].upper()

print(classmates) 
'''

#Create a list of all the Marvel movies from Iron Man to End Game

#Go through the list, and create a second list with all the titles that have 'The' in their names

marvel_movies = ['Iron Man', 
    'The Incredible Hulk',
    'Iron Man II',
    'Thor',
    'Captain America: The First Avenger',
    'The Avenegers', 
    'Iron Man III', 
    'Thor: The Dark World', 
    'Captain America: The Winter Soldier', 
    'Guardians of the Galaxy',
    'Avengers: Age of Ultron',
    'Ant-Man',
    'Captain America: Civil War',
    'Doctor Strange',
    'Guardians Of The Galaxy Vol. 2',
    'Spiderman: Homecoming',
    'Thor: Ragnarok',
    'Black Panther',
    'Avengers: Infinity War',
    'Ant-Man and the Wasp',
    'Captain Marvel',
    'Avengers: Endgame'  
    ]

movies_with_the = []

for index, movie in enumerate(marvel_movies):
    if "the " in movie.lower():
        movies_with_the.append(movie)

print(movies_with_the)
print(len(movies_with_the))
