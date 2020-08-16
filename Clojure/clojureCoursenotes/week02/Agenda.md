## Week Two Agenda

### 1. Homework review

- review at least 2 applications that someone else wrote
  - Leiningan is written in clojure
    - have a folder for every command line api/command/function
    - well tested- testing appears to be built in to clojure
    - looks a lot like OO code that uses dependency injection.  Always coding to an interface
  - Advent of Code- answers to smallish problems
    - code golf seems to be a common pastime
  - Temperature conversion Gui
    - Clojure can interact with Swing library
    - doto function: does things to a particular gui component
  - Planets and properties to determine if planets are habitable
    - hashmap syntax
  - Sorting Algorithms
    - Sorting algorithms are hair-ripping-inducing
- come with at least 1 running example of something you wrote (can be tiny)

###  2. Coding Challenges for Today*

Do these in any order.  Work with someone (we'll learn better that way).  Share your solutions as you solve them.  

Make sure you have cloned a copy of the coursenotes repo.   We'll each make our own branch and merge the best solution for each challenge into the course notes 

1. Write a function that takes a list of integers as input and returns a list containing the negative of all the integers.
   - input [ 1,2,3] -> output[-1,-2,-3]
2. Write a function that takes an integer (target) and a list of integers and returns true if the target is in the list, false otherwise
3. Write a function that takes a list of integers and returns a new list containing only the positive numbers from the original list.
   - variation: return only the odd numbers
4. Write a function that takes a list of integers and returns a different list with all the duplicates removed.
5. Write a function that takes two lists of integers as input, merges them into a single sorted list, retaining duplicates.
   - variation: remove duplicates
6. Write a function that returns the last element of a list.
7. Write a function that takes a list and an integer (k) and returns the kth element of the list
8. Write a function that returns the reverse of a list
9. Write a function that returns true if a list is a palindrome
10. Write a function that flattens a nested list structure
    - ie (some function '(a (b (d e) f)))  would return a b d e f
    - hint: use (list) and (conj) functions

### 3. Homework

- Bring some project ideas for next week's class 
  - i.e. what will you be doing for that last 30%
  - Teaching Learning conference:  Collaborative Learning.
- Make sure you've done at least 50% of the programming exercises
- Make Some IDE choices
  - Intellij
  - VS-Code
  - 



*challenges inspired by: http://www.ic.unicamp.br/~meidanis/courses/mc336/2006s2/funcional/L-99_Ninety-Nine_Lisp_Problems.html