
Problem Set 2
===============

Written by: Computer Science Dapartment, The Pingry School

Solved By: YOUR NAME HERE

## Submission

This problem set will be submitted by pushing to github. Begin by accepting this assignment which will create your own repository. After cloning your repository to your local system, you can start solving the problems. The file structure is already sketched out for you.

## Grading

| Grade Category               | Points Earned |
| ---------------------------- | ------------- |
| Automated Tests              | 15 pts        |
| README and .gitignore        | 2 pts         |
| Progressive Commits          | 1 pt          |
| Coding Style and Readability | 2 pts         |

Do NOT use any built-in or standard library functions except len(), type(), print(), and range() unless it is specified that you may.

| Grade Penalty                         | Points Deducted |
| ------------------------------------- | --------------- |
| Using prohibited functions or modules | 1 pt each       |
| Asking for user input in the runner   | 1 pt            |

The Problems
------------
### Insertion Sort

Design a function called `insertion_sort` that takes a list as a parameter, sorts it in-place, and returns it. It should use the Insertion Sort algorithm to accomplish this.

https://www.youtube.com/watch?v=DFG-XuyPYUQ

### Variable Length Integers

 Design a function called `add_variable` that takes two lists and returns a list.
 The returned list should contain the result of adding the two parameters
 together. You may assume, as a precondition, that each parameter array
 contains only ints between 0-9.

For example:
   [3, 2, 4, 6, 4] + [1, 3, 5, 5, 9] = [4, 6, 0, 2, 3]

Motivation for this problem:
Python is convenient for many reasons, but one thing it does is automatically handle variable size for you. That is, no matter how big a value gets, python will grow the variable to be able to handle it. This is different from other languages such as Java and C, which limit variables to a certain number of bytes (usually 32, but not always).

How does Python escape this? Well, its data structures are capable of growing like how lists grow. For this function, you will mimic this behavior by representing a number as a list. So instead of x = 598, we would say x = [5, 9, 8].

Remember that the lists may not necessarily be the same size.

### Spam Filter

Create a function called `spam_filter` that takes in a list of strings, called
 messages, and a list of prohibited words called badWords. It then removes from the list any message that contains a word in the badWords list. There’s a catch though. When evaluating, your function should ignore any character that is not a letter.


For example, if the word “dirty” is contained the list of bad words, then a string in messages containing “d^^***irt###%y” should be removed. You may want to create “helper” functions to complete this. A function that takes in a string and simply removes all non-letter characters might be helpful.

Return the updated list of valid messages in their original form (not with special characters removed).

### Merging two lists 

 Make a function called `merge_lists` that takes two sorted lists as parameters.
 The function should return a new sorted list which is the result of merging
 these lists together.

NOTE: Using the built-in sorted(), list.sort() or your own sorting algorithm is NOT allowed. Why? Because sorting is an O(n2) algorithm, and this can be done in O(n) if you don't use a sorting algo.

list1 = [2, 13, 19]
list2 = [3, 6, 9, 22]

returned list
[2, 3, 6, 9, 13, 19, 22]

Hint: You may need 3 indices - 1 for each list - to keep track of where you are. POSTCONDITION: Neither parameter list should be changed.

### Fibonacci Sequence

Create a function named `is_fib`. The `is_fib` function takes in a list of int values and returns whether or not they are a Fibonacci Sequence starting at 0.

You can read more about Fibonacci numbers here: http://en.wikipedia.org/wiki/Fibonacci_number

Remember, a list containing just 0 would still be a correct sequence.

### Word Frequency Analysis

 Create a function named `word_freq` that takes a file name (a string). `word_freq` returns a dictionary that contains the number of
 occurrences of every word in the file. For example:

the -> 12
a -> 11
dog -> 6
python -> 2
aardwolf -> 1

### Ten Greatest in a Dictionary

Create a function named `ten_greatest` that will take in a dictionary of words
and frequencies (like the one you just created) and return a list that contains the ten keys with the highest values (ie. the ten most common words).

### Building a Dictionary

 Write a function called `validate_5k` that takes a list of tuples as an
 argument. Each tuple contains a runner's last name, and 5k time (in minutes
 and seconds) as strings. For example, the argument could be:

 [(“Smith”, “18.58”),
  (“Williams”, “20.45”),
  (“Pingry”, “21.13”),
  (“Jones”, “19.09”),
  ("Orndorff", "17.91")]

 The function builds and returns a dictionary where the keys are runner names,
 and the values are times. Your function should validate both the name (must be
 at least two characters) and the time (neither minutes nor seconds should be
 over 60). If either of these criteria fail, the item should be ignored.
 You may assume that the time portion only contains digits and a single '.'.

### XOR of Lists

Create a function called `xor` that takes two lists and returns a list that is
the XORing of the two parameter lists together. How does XOR apply to lists?
If we XOR 2 lists together, the resulting list should contain only objects
that appear in one of the lists, but not both of the lists.

Example: [1,2,5,7,9] XOR [1,2,4,8.9] -> [4,5,7,8]
