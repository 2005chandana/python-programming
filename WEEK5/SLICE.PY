1)SYNTAX

my_list = [1, 5, 10, 15, 20]
print(my_list)

2)CONSTRUCTOR

print([True, False, False, "1"])
my_list = list(["Lists", "are", "useful!"])
print(my_list)

3)COMPREHENSION

my_list = [num for num in range (1,6)]
print(my_list)

4)INDEX SINGLE ELEMENTS
Reassigning a list#
my_list = [num for num in range (1,6)]
print(my_list)

element = my_list[2]
print(element)

INDEXING PORTIONS LIST

my_list = [num for num in range (1,6)]
my_list[start:end]

my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]
my_new_list = [2,5]

print(my_new_list)

NEGATIVE INDEXING

my_list = [num for num in range (1,6)]

last_element = my_list[-1]in
print(last_element)

OUT OF RANGE INDEX VALUES

my_list = [num for num in range (1,6)]

try:Reassigning a list#
    element = my_list[10]in
except IndexError:
    print("Index is out of range!")

THE APPEND() METHOD

my_list = [12, 19, 26, 23]
my_list.append(30)
print(my_list)

THE EXTEND() METHOD

python_datatypes = ["lists"]
python_datatypes.extend(["tuples", "sets"])
print(python_datatypes)

MODIFYING LISTS

blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
blue_shades[2] = 'sapphire'

print(blue_shades)

MODIFYING MULTIPLE ELEMENTS

blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:2] = ['denim', 'aqua']

print(blue_shades)

DIFFERENT NUMBER OF ELEMENTS THAN THE SPECIFIED RANGE

print(blue_shades)blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:1] = ['deninim', 'aqua']
print(blue_shades)
blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
blue_shades[0:4] = ['denim', 'aqua']
print(blue_shades)

REASSIGNING A LIST_

blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']

blue_shades = ['cobalt', 'azure', 'ice blue']
print(blue_shades)

DELETING A SMALL ELEMENT

space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

del space_movies[2]
print(space_movies)

DELETING MULTIPLE ELEMENTS

space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

del space_movies[1:3]
print(space_movies)

REMOVING BY VALUE

space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
print(space_movies)

space_movies.remove('Gravity')
print(space_movies)

CLEARING THE ENTIRE LIST

space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
space_movies.clear()
print(space_movies)

THE POP() METHOD

space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

removed_movie = space_movies.pop(2)
print("The removed movie is = " + removed_movie)
print(space_movies)

LIST SLICING
SYNTAX

my_list = [1, 5, 10, 15, 20, 25, 30]
print(my_list[0:2])
my_list = [1, 5, 10, 15, 20, 25, 30]

my_list[0:2] = 50, 55
print(my_list)

THE STEP PARAMETER

my_list = [1, 5, 10, 15, 20, 25, 30]

print(my_list[1:5:2])

SLICING FROM THE BEGGINING

my_list = [1, 5, 10, 15, 20, 25, 30]

print(my_list[1:5:2])



