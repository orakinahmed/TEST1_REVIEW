// DATA STRUCTURES

// 1. Dictionaries -> A key value pair set of data
// Typically describe one thing. Ex. Student Info (name, age, height, ethnicity)
// Symbol {}

// Creating
var studentInfo = {'name': 'Rakin', 'age': 25, 'height': 160, 'ethnicity': 'asian'};

// Accessing Data by its key
var student = studentInfo['name'];

// Looping through each key
for (item in studentInfo) {
    console.log(studentInfo[item]);
}
// ------------------------------------------------------------------------------

// 2. List -> A list of data
// Can be a list of different or the same thing. Ex. Apple, Bananna, Grape
// Symbol []

// Creating
var fruits = ['apple', 'banana', 'grape'];

// Accessing Data by its index
var fruit = fruits[0];

// Loop through each index
for (var i=0; i < fruits.length; i++) {
    console.log(fruits[i]);
}


// ------------------------------------------------------------------------------

// Condtions
var myName = 'Faraz';

if (myName === 'Bob'){
    console.log('That my name! WOW!');
} else {
    console.log('Thats not my name!');
}


// Nested Data Structure Loop

var movieData = [
    {'name':'Jurassic Park', 'release_year':1991, 'parental_rating':'R', 'audience_score':5},
    {'name':'Avatar', 'release_year':2007, 'parental_rating':'R', 'audience_score':5},
    {'name':'Avengers', 'release_year':2005, 'parental_rating':'PG-13', 'audience_score':4},
    {'name':'Predator', 'release_year':1982, 'parental_rating':'R', 'audience_score':5},
    {'name':'Barbie Movie', 'release_year':2019, 'parental_rating':'PG', 'audience_score':2},
    {'name':'Terminator', 'release_year':1985, 'parental_rating':'R', 'audience_score':1},
    {'name':'Goofy Movie', 'release_year':2001, 'parental_rating':'G', 'audience_score':4},
    {'name':'Paul Gilbert: Mall Cop', 'release_year': 2015, 'parental_rating':'PG-13', 'audience_score':5}
];


// Function to Display Each Release Year & Check if its older than 1990

function findOldMovies() {
    for (var i=0; i < movieData.length; i ++) {
        currentMovie = movieData[i]

        if (currentMovie['release_year'] < 1990) {
            console.log(currentMovie['name']);
        }
    }
}

// Call Function by its name
findOldMovies()