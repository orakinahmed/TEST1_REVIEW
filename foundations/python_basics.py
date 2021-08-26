# DATA STRUCTURES

# 1. Dictionaries -> A key value pair set of data
# Typically describe one thing. Ex. Student Info (name, age, height, ethnicity)
# Symbol {}

# Creating
studentInfo = {'name': 'Rakin', 'age': 25, 'height': 160, 'ethnicity': 'asian'}

# Accessing Data by its key
student = studentInfo['name'] 

# Looping through each key
for item in studentInfo:
    print(studentInfo[item])

# ------------------------------------------------------------------------------

# 2. List -> A list of data
# Can be a list of different or the same thing. Ex. Apple, Bananna, Grape
# Symbol []

# Creating
fruits = ['apple', 'banana', 'grape']

# Accessing Data by its index
fruit = fruits[0]

# Loop through each index
for i in range(0, len(fruits)):
    print(fruits[i])


# ------------------------------------------------------------------------------

# Condtions
myName = 'Faraz'

if myName == 'Bob':
    print('That my name! WOW!')
else: 
    print('Thats not my name!')


# Nested Data Structure Loop

movieData = [
    {'name':'Jurassic Park', 'release_year':1991, 'parental_rating':'R', 'audience_score':5},
    {'name':'Avatar', 'release_year':2007, 'parental_rating':'R', 'audience_score':5},
    {'name':'Avengers', 'release_year':2005, 'parental_rating':'PG-13', 'audience_score':4},
    {'name':'Predator', 'release_year':1982, 'parental_rating':'R', 'audience_score':5},
    {'name':'Barbie Movie', 'release_year':2019, 'parental_rating':'PG', 'audience_score':2},
    {'name':'Terminator', 'release_year':1985, 'parental_rating':'R', 'audience_score':1},
    {'name':'Goofy Movie', 'release_year':2001, 'parental_rating':'G', 'audience_score':4},
    {'name':'Paul Gilbert: Mall Cop', 'release_year': 2015, 'parental_rating':'PG-13', 'audience_score':5}
]


# Function to Display Each Release Year & Check if its older than 1990

def findOldMovies():
    for i in range(0, len(movieData)):
        currentMovie = movieData[i]

        if currentMovie['release_year'] < 1990:
            print(currentMovie['name'])

# Call Function by its name
findOldMovies()