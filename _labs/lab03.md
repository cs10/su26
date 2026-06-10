---
title: # Lab 03: Lists + Loops

description: Lists + Loops
due: Tuesday July 1st, 2359 hrs
gradescope_assignment_id: 
submission_files:
---

# Lab 3:  Lists + Loops

## Instructions: 

This worksheet serves as a guide and set of instructions to complete lab 3. All material was sourced from the CS10 version of The Beauty and Joy of Computing course.

- You **must** use the [starter file, found here](https://snap.berkeley.edu/snap/snap.html#present:Username=jedi_force&ProjectName=Lab%3a%20Lists%20%2b%20Loops&editMode&noRun) to get credit for the lab.
- **This lab has NO workbook.** All instructions are within this page and starter file

## Submitting: 

You will need to fill in the blocks under "Lab 3: Lists + Loops" and submit this to Gradescope. 
- To receive full credit, you will need to complete the required blocks, and the required blocks must pass all tests from the autograder in Gradescope. 
- For instructions on how to submit to labs to Gradescope, please see [this page](https://docs.google.com/document/d/1XAcZc9ypX07-bt0gK6uQ4P-06SrjPRsgiOjERIOlvYU/edit?usp=sharing).

Please note, you must use the [starter file](https://snap.berkeley.edu/snap/snap.html#present:Username=jedi_force&ProjectName=Lab%3a%20Lists%20%2b%20Loops&editMode&noRun), and you must NOT edit the name of any of the required blocks. Failing to do either for these will result in the autograder failing.

## Objectives:

Previously in the lab, we have worked with iteration (loops) when creating polygons. In lecture, we saw how we can use iteration with variables and with lists. By the end of the lab, you will be comfortable implementing and understanding:
- Iterative functions
- Fucntions using the list data type
- The ordered characteristic of lists
- The differences between the various loops
- When to use certain loops
- How to filter and keep items from a list
- How to use variables with lists

## Required Blocks: 

***Please note, all functions must be completed iteratively. HOFs and Recursion are banned. You will need 10/10 points from the autograder to recieve credit for the coding portion of the lab.***
- Block 1: add all numbers from num1: _ to num2: _
- Block 2: report only even numbers from list: _
- Block 3: add start num: _ until > than stop num: _ and is odd
    - "for each" and "for i" blocks are also banned **for this function only**.
- Block 4:  is num: _ prime?
- Block 5: report only prime numbers from list: _

## Block 1: add all numbers from num1: _ to num2: _

Objective:
- Add all the numbers together in the range from num1 to num2. The starting number will be num1, and you will continuously add numbers until you reach num2 (the final number to add).  

Inputs: 
- num1: Number
- num2: Number

Output: 
- Reports: Number 

Examples:
- add all numbers from num1: "1" to num2: "5" will add 1 + 2 + 3 + 4 + 5. This will return 15.
- add all numbers from num1: "3" to num2: "7" will add 3 + 4 + 5 + 6 + 7. This will return 25.
- add all numbers from num1: "-4" to num2: "2" will add -4 + -3 + -2 + -1 + 0 + 1 + 2. This will return -7.
- add all numbers from num1: "2" to num2: "2" will not add but start and end at 2. This will return 2.


## Block 2: report only even numbers from list: _

Objective:
- Report a new list that only contains numbers that are even (i.e. divisible by 2). You should be returning a new list that only keeps the even numbers.
- You may use the “mod" block. Mod stands for modulus. Given two numbers, a (the dividend) and b (the divisor), the modulus operation a mod b returns the remainder when a is divided by b. For example, 4 mod 2 is 0 since 4 is divisible by 2. 4 mod 3 is 1. [See this Wikipedia article](https://en.wikipedia.org/wiki/Modulo) for more information on modulus.

Inputs: 
- input: List

Output: 
- Reports: List 

Examples:
- report only even numbers from list "[1, 2, 3, 4, 5]". This will return the list with [2, 4].
- report only even numbers from list "[2, 4, 6, 8]". This will return the list with [2, 4, 6, 8].
- report only even numbers from list "[-2, -4, -6, -8]". This will return the list with [-2, -4, -6, -8].
- report only even numbers from list "[1, 3, 5, 7]". This will return an empty list (a list containing no items) [].

## Block 3: add start num: _ until > than stop num: _ and is odd

Objective:
- Add numbers continuously starting at a start number until the added numbers are greater than the stop number AND the added numbers are odd. Both of these conditions need to be true until the loop terminates.
- Each time the loop is iterated through, the output number will be added to by a number incrementing by 1 starting at the start num.  
- ***For this function, you will need the "repeat until" block. You are NOT allowed to use the "for i" loop OR the "for each item" loop.***

Inputs: 
- start: Number
- stop: Number

Output:
- Reports: Number

Restrictions:
- Cannot use "for each item" or "for i" blocks. Must use "repeat until".

Examples:
- add start num: "1" until > than stop num: "2" and is odd. The following numbers will be added: 1 + 2. This will return 3.
- add start num: "1" until > than stop num: "7" and is odd. The following numbers will be added: 1 + 2 + 3 + 4 + 5. This will return 15.
- add start num: "3" until > than stop num: "6" and is odd. The following numbers will be added: 3 + 4. This will return 7.

## Block 4: is num: _ prime?

Objective:
- Evaluates the number and returns true if the number is prime, and return false if the number is NOT prime. To do this, you will need to check if all the numbers smaller than the given number and greater than 1 are divisible by the given number.
- Note, a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- 0 and 1 are neither prime nor composite, so the domain will be greater than 1.

Inputs: 
- num: Number
  - num will always be greater than 1.

Output:
- Reports: Boolean 

Examples:
- is num: "17" prime?. This will return True.
- is num: "10" prime?. This will return False.
- is num: "2” prime?. This will return True.

## Block 5: report only prime numbers from list: _

Objective:
- Report a new list that only contains prime numbers. This function should filter out any non-prime numbers from the input list.
  - The order of the items should still be preserved - just filtered.

Notes:
- You can and should use the "is num: _ prime?" block you just made!
- **There is a typo in one of the test cases: Ex: report only prime number from list: "[2, 4, 6, 8]"; This will return an empty list.**
  - **This list should return [2]**

Inputs:
- Input: List

Outputs:
- Output: List

Examples:
- report only prime numbers from list: "[2, 3, 4, 5]": This will return [2, 3, 5].
- report only prime number from list: "[11, 7, 6, 8]": This will return [11, 7].
- report only prime number from list: "[4, 6, 8, 10]": This will return an empty list.

## **(Optional) Extremely Challenging:** Block 6: report the duplicates in list: _

Objective:
- Write a function that takes a list of integers and returns a list of all the integers that appear more than once in the input list. The returned list should not contain any duplicates. If there are no duplicates, then the function should report any empty list.
  - The order of the items should still be preserved - just filtered.

Notes:
- This block is optional and not required for the lab!
- There is a built-in function in Snap! called "uniques". You are NOT allowed to use this function.

Inputs:
- Input: List

Outputs:
- Output: List

Examples:
- report the duplicates in list: "[1, 2, 1, 3, 2, 3]". This will return: [1, 2, 3].
- report the duplicates in list: "[4, 4, 3, 10, 33, 4]". This will return: [4].
- report the duplicates in list: "[7, 2, 3, 2, 7]". This will return: [7, 2].
- report the duplicates in list: "[1, 4, 6, 3]". This will return an empty list.




**You can always check the validity of your solutions by using the local autograder. Remember to submit on Gradescope and complete the conceptual portion!** 
