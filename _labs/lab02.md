---
title: # Lab 02: 

description: Conditionals, Reporters, & Abstraction
due: Monday June 30th, 2359 hrs
gradescope_assignment_id: 
submission_files:
---

# Lab 2:  Conditionals, Reporters, & Abstraction

## Instructions: 
This worksheet serves as a guide and set of instructions to complete lab 2. All material was sourced from the CS10 version of The Beauty and Joy of Computing course.

- You **must** use the [starter file, found here](https://snap.berkeley.edu/snap/snap.html#open:https://cs10.org/bjc-r/prog/conditionals/lab3-starter-code-v2.xml) to get credit for the lab.
- Additionally, here is the [workbook](https://cs10.org/bjc-r/llab/html/topic.html?topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment) that you can read through for further context and additional (non-required) material.
- All material was sourced from the CS10 version of The Beauty and Joy of Computing course.

## Submitting: 

You will need to fill in the blocks under "Lab 2: Conditionals, Reporters, & Abstraction" and submit this to Gradescope. 
- To receive full credit, you will need to complete the required blocks, and the required blocks must pass all tests from the autograder in Gradescope. 
- For instructions on how to submit to labs to Gradescope, please see [this page](https://docs.google.com/document/d/1XAcZc9ypX07-bt0gK6uQ4P-06SrjPRsgiOjERIOlvYU/edit?usp=sharing).

Please note, you must use the [starter file](https://snap.berkeley.edu/snap/snap.html#open:https://cs10.org/bjc-r/prog/conditionals/lab3-starter-code-v2.xml), and you must NOT edit the name of any of the required blocks. Failing to do either for these will result in the autograder failing.

## Objectives:
So far, you've practiced writing scripts that carry out short sequences of commands. These scripts will run every single one of their blocks, no matter how. In this lab you will explore a new level of complexity with the idea of conditionals. By the end of the lab, you will:
- Implement conditional statements into your code
- Practice writing and reading functions with booleans and boolean operators
- Understand the use of reporter functions and their outcomes

## Required Blocks: 
- [Block 1: traffic signal (color)](#block-1-traffic-signal-color)
- [Block 2: letter grade (number)](#block-2-letter-grade-number)
- [Block 3: is (num1) between (num2) and (num3)](#block-3-is-num1-between-num2-and-num3)
- [Block 4: sum of two smallest (num1) and (num2) and (num3)](#block-4-sum-of-two-smallest-num1-and-num2-and-num3)

## Important Topics mentioned in the Workbook: 
For better understanding of the lab we highly recommend going through these workbook pages! Topics that are important but not required for this lab will be indicated with an asterisk**. These topics are best reviewed in order and as you complete the lab. 
- [Introduction: why do we need conditionals?](https://cs10.org/bjc-r/cur/programming/conditionals/conditionals-intro.html?1&1&1&2&2&2&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
- [If and If-else](https://cs10.org/bjc-r/cur/programming/conditionals/if-and-if-else.html?1&1&1&2&2&2&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
- [More Complex Boolean Expressions](https://cs10.org/bjc-r/cur/programming/conditionals/complex-booleans.html?1&1&1&1&2&2&2&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)**
- [Predicates](https://cs10.org/bjc-r/cur/programming/conditionals/predicates.html?1&1&1&1&2&2&2&2&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
- [The Max block](https://cs10.org/bjc-r/cur/programming/functions/review-max-block.html?1&1&1&1&2&2&2&2&3&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)

## [Block 1: Traffic signal (color)](https://cs10.org/bjc-r/cur/programming/functions/reporters.html?1&1&1&2&2&2&3&3&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
Objective:
- Create a **reporter** block that when inputted a traffic light color it makes the sprite report the appropriate action (see below)  

Inputs: 
- color = any text
    - This variable takes in any text input.
    - Any text can be typed, but for the autograder we will be testing the three traffic light colors: Red, Green, Yellow 

Output: 
- Reports: Text 
- The following inputs and outputs need to be case sensitive to pass the autograder 
    - Input: Green --> Output: Go
    - Input: Red --> Output: Stop
    - Input: Yellow --> Output: Yield

Examples:
- ![example of traffic signal reporter 'Yellow' with output 'Yield'](asssets/images/lab_images/lab3_b1_1.png)
- ![example of traffic signal reporter 'Red' with output 'Stop'](asssets/images/lab_images/lab3_b1_2.png)
- ![example of failed traffic signal reporter 'Cheese' with output 'did not report'](asssets/images/lab_images/lab3_b1_3.png)

## [Block 2: letter grade (number)](https://cs10.org/bjc-r/cur/programming/functions/reporters.html?1&1&1&2&2&2&3&3&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
Objective:
- Create a reporter block that when inputted percentage, makes the sprite say the associated letter grade. For example, letter grade (74) should say "C."
- Standardized Letter Grade 
    - A: 90-100, B: 80-89.99, C 70-79.99, D: 60-69.99, F < 60 
    - Note that the autograder is sensitive to decimals and should work for all non negative numbers. Ex. 89.99123123

Inputs: 
- number = any number
    - This variable takes in any number. However we can assume that the user will input a non negative, whole number 100 or less. 



Output: 
- Reports: Text 
- The following outputs need to be case sensitive to pass the autograder. No spaces, no quotes ""
    - **A**: 90-100, **B**: 80-89.99, **C**: 70-89.99, **D**: 60-69.99, **F**: < 60

Examples:
- ![example of letter grade reporter '89.999' with output 'B'](asssets/images/lab_images/lab3_b2_1.png)
- ![example of letter grade reporter '70' with output 'C'](asssets/images/lab_images/lab3_b2_2.png)
- ![example of letter grade reporter '2' with output 'F'](asssets/images/lab_images/lab3_b2_3.png)

## [Block 3: is (num1) between (num2) and (num3)](https://cs10.org/bjc-r/cur/programming/functions/predicates/predicates-make-a-between-block.html?1&1&1&2&2&2&3&3&3&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment)
Objective:
- Create a predicate block that determines if a number is between two other numbers. The block should return true if the first number is between the two numbers or if it is equal to either of the numbers.
- Note: num1, num2, num3 can be the same numbers 
- Num2 and num3 can be non numerical order, that is num3 can be less than num2 

Inputs: 
- num1, num2, num3 = any number
    - This variable takes in any and all numbers

Output:
- Reports a boolean (True or False) 

Examples:
- ![example of is '3' between '1' and '5' and reports 'True'](asssets/images/lab_images/lab3_b3_1.png)
- ![example of is '9' between '1' and '5' and reports 'False'](asssets/images/lab_images/lab3_b3_2.png)
- ![example of is '88' between '36' and '-5' and reports 'False'](asssets/images/lab_images/lab3_b3_3.png)
- ![example of is '4' between '4' and '4' and reports 'True'](asssets/images/lab_images/lab3_b3_4.png)

## [Block 4: sum of two smallest (num1) and (num2) and (num3)]
Objective:
- Edit a reporter block named "sum of two smallest" that takes three numbers as inputs, and reports the sum of the two smallest
- If two of the greatest numbers are the same the block should report the smallest and any of the two
- If three numbers are the same, the block should report the sum of two of the numbers

Inputs: 
- num1, num2, num3 = any number
    - This variable takes in any and all numbers

Output:
- Reports: Num (the sum of the smallest two numbers) 

Examples:
- ![example of sum of two smallest '2' and '5' and '5' and reports '7'](asssets/images/lab_images/lab3_b4_1.png)
- ![example of sum of two smallest '9' and '9' and '9' and reports '18'](asssets/images/lab_images/lab3_b4_2.png)
- ![example of sum of two smallest '1' and '12' and '2' and reports '3'](asssets/images/lab_images/lab3_b4_1.png)

> Hint: Look at the [max block](https://cs10.org/bjc-r/cur/programming/functions/review-max-block.html?1&1&1&2&2&2&3&3&3&4&4&topic=berkeley_bjc%2Fintro_pair%2F2-conditionals-testing-su21.topic&course=cs10_fa21.html&novideo&noreading&noassignment). How does it work? 

**You can always check the validity of your solutions by using the local autograder. Remember to submit on Gradescope and complete the conceptual portion!** 
