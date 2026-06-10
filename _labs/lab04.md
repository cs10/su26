---
title: # Lab 04: Lists + HOFs

description: Lists + HOFs
due: Wednesday July 2nd, 2359 hrs
gradescope_assignment_id: 
submission_files:
---

# Lab 4:  Lists + HOFs

## Instructions: 

This worksheet serves as a guide and set of instructions to complete lab 3. All material was sourced from the CS10 version of The Beauty and Joy of Computing course.

- You **must** use the [starter file, found here](https://snap.berkeley.edu/snap/snap.html#open:https://cs10.org/bjc-r/prog/hofs/lab4-starter-code.xml) to get credit for the lab.
- Additionally, [here is the workbook](https://cs10.org/bjc-r/topic/topic.html?topic=berkeley_bjc/lists/lists-I.topic&course=&novideo&noreading&noassignment) that you can read through for further context and additional (non-required) material.

## Submitting: 

You will need to fill in the blocks under "Lab 4: Lists + HOFs" and submit this to Gradescope. 
- To receive full credit, you will need to complete the required blocks, and the required blocks must pass all tests from the autograder in Gradescope. 
- For instructions on how to submit to labs to Gradescope, please see [this page](https://docs.google.com/document/d/1XAcZc9ypX07-bt0gK6uQ4P-06SrjPRsgiOjERIOlvYU/edit?usp=sharing).

Please note, you must use the [starter file](https://snap.berkeley.edu/snap/snap.html#open:https://cs10.org/bjc-r/prog/hofs/lab4-starter-code.xml), and you must NOT edit the name of any of the required blocks. Failing to do either for these will result in the autograder failing.

Please use the “run autograder” block for testing. Do not use the other predicate blocks found in the autograder block sections.

## Objectives:

Previously, you've explored lists, a collection of elements that can be accessed by their position. By the end of the lab, you will:
- Understand and implement lists into your code
- Practice using high order functions in your code
- Understand the use and importance of high order functions

## Required Blocks: 

- Block 1: acronym of list (wordlist)
- Block 2: acronym keep only capitals (input)
- Block 3:  exaggerate (input)
- Block 4:  expand (input)

## **Important Topics in Workbook**

For better understanding of the lab we highly recommend going through these workbook pages! Topics that are important but not required for this lab will be indicated with an asterisk**. These topics are best reviewed in order and as you complete the lab. 
- [What good are lists?](https://cs10.org/bjc-r/cur/programming/lists/hof/what-good-are-lists.html?topic=berkeley_bjc%2Flists%2Flists-I.topic&course&novideo&noreading&noassignment)
- [Transforming each item of a list](https://cs10.org/bjc-r/cur/programming/lists/hof/transforming-each-item-of-a-list.html?topic=berkeley_bjc%2Flists%2Flists-I.topic&course&novideo&noreading&noassignment)
- [Choosing some items from a list](https://cs10.org/bjc-r/cur/programming/lists/hof/choosing-some-items-from-a-list.html?topic=berkeley_bjc%2Flists%2Flists-I.topic&course&novideo&noreading&noassignment)
- [Combining all the items of a list](https://cs10.org/bjc-r/cur/programming/lists/hof/combining-all-the-items-of-a-list.html?topic=berkeley_bjc%2Flists%2Flists-I.topic&course&novideo&noreading&noassignment)
- [Composing higher order functions to solve more complicated problems](https://cs10.org/bjc-r/cur/programming/lists/hof/composing-higher-order-functions-to-solve-more-complicated-problems.html?topic=berkeley_bjc%2Flists%2Flists-I.topic&course&novideo&noreading&noassignment)

## Block 1: acronym of list (wordlist)

Objective:
- Create a reporter block that reports the first letter of each string, all joined together.

Notes:
- You should not use map or combine when creating your block
- You must use hyperblocks! Use of HOFs and iterative blocks will fail the tests!
- Try the join block

Inputs: 
- wordlist: List

Output: 
- Reports: Text 

Examples:
- acronym of list (University, of, California, Berkeley) will report "UoCB"
- acronym of list (North, East, South, West) will report "NEWS"

## Block 2: acronym keep only capitals (input)

Objective:
- Create a reporter block that reports the first letter of each string with a capital letter in the front, all joined together.

Inputs: 
- input: Text
  - usually a sentence or phrase

Output: 
- Reports: Text 

Examples:
- acronym keep only capitals (University of California Berkeley is the best) will report "UCB"
- acronym keep only capitals (As Soon As Possible) will report "ASAP"

## Block 3: exaggerate (input)

Objective:
- Write a reporter exaggerate that takes a sentence as input and reports an exaggerated version.
- It should replace "good" with "great," "bad" with "terrible," and "like" with "love”  
- It should replace every number with twice the number.
- 
Inputs: 
- input: Text
  - usually a sentence or phrase

Output:
- Reports: Text

Examples:
- exaggerate(I like eating 12 dumplings because they are good) will report "I love eating 24 dumplings because they are great".
- exaggerate(Marius is bad at chemistry but good at computer science) will report "Marius is terrible at chemistry but great at computer science".
- exaggerate(There are 30 chairs in lab) will report "There are 60 chairs in lab"

## Block 4: expand (input)

Objective:
- Write an expand reporter that takes a sentence as input, and reports a sentence that's the same except that each number in the input is replaced by that many copies of the following word

Notes:
- If the last word is a number, add the number unmodified. 

Inputs: 
- input: Text
  - usually a sentence or phrase

Output:
- Reports: Text 

Examples:
- expand(I love 3 you) will report "I love you you you".
- expand(I am taking CS 10) will report "I am taking CS 10".
- expand(3 computers and 1 television) will report "computers computers computers and television".


**You can always check the validity of your solutions by using the local autograder. Remember to submit on Gradescope and complete the conceptual portion!** 
