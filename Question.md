Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

Problem Unserstanding:
condition --> divisible by 7, not multiple of 5
rage --> 2000, 3201
output --> comma-separated sequence

Step to Solve:
1. make a empty list "lis" for storing values satisfying condition
2. use for loop and provide required range
3. use if block for logical and for conditioning
4. while appending convert the numbers to string
5. joing the strings in the list with comma and print

Question 2: Level 1

Write a program which can compute the factorial of a given numbers.

The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Concept of Factorial
- Factorial of 5 = 1 x 2 x 3 x 4 x 5 = 120
- Factorial of 0 = 1
- Factorial of 1 = 1
- Factorial of 2 = 1 x 2 = 2

Steps to Solve
1. Take the input and convert it to int data type
2. Check if the value is negative then factorial does not exist
3. Check if the value is equal to zero, if true then return 1
4. use for loop to perform reverse iteration, to multiply values in decreasing order
5. return the result
6. call the function to test the output

```python
# Method 1: reverse iteration


n = int(input("Enter a number: "))


def factorial(num):
    if num < 0:
        return "No Factorial for negative number"

    if num == 0:
        return 1

    result = 1  # initializing var

    # reverse iteration
    for i in range(num, 0, -1):
        result = result * i
    return result


print("Factorial =", factorial(n))
print()

# Method 2: Recursive Function


def factorial(num):
    if num < 0:
        return "No Factorial for negative number"

    if num == 0:
        return 1

    # recurring
    return num * factorial(num - 1)


n = int(input("Enter a number: "))    # take input
print("Factorial =", factorial(n))
print()

# Method 3: While Loop


def factorial(num):
    if num < 0:
        return "No Factorial for negative number"

    fact = 1
    while (num > 0):
        fact = fact * num
        num = num - 1
    return fact


n = int(input("Enter a number: "))
print("Factorial =", factorial(n))

# Output1:
"""
Enter a number: 4
Factorial = 24

Enter a number: 4
Factorial = 24

Enter a number: 4
Factorial = 24
"""

# Output2:
"""
Enter a number: -1
Factorial = No Factorial for negative number

Enter a number: -1
Factorial = No Factorial for negative number

Enter a number: -1
Factorial = No Factorial for negative number
"""

# Output3:
"""
Enter a number: 0
Factorial = 1

Enter a number: 0
Factorial = 1

Enter a number: 0
Factorial = 1
"""
```

Question 3: Level 1
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

Problem Understandings:
store key as i and value as i*i in a dictionary for a given integer (range)

Steps to solve: 
1. take input form the user and convert it to integer
2. then initialize a dictionary "result"
3. now use for loop to fill the dictionary with 'i' as key and i*i as value
4. print the dictionary

Solution:
```python
# take input and convert it to int
num = int(input("Enter a number: "))

# initializing a dictionary
result = dict()

# using for loop to fill the dictionary
for i in range(1, num+1):
    result[i] = i*i

# printing the result
print(result)
#---------------------------------------
# Output
"""
Enter a number: 8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
```

Question 4: Level 1
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

Problem:
take a list of numbers and create a list and tuple of numbers

Step to solve:
1. take the input
2. split the number on comma
3. create list and tuple of numbers
4. print the result

```python
# Take input with comma-separated sequence
numbers = input()

# create list
lis = numbers.split(',')

#create tuple
tupl = tuple(lis)

# print results
print(lis)
print(tupl)

#----------------------------------------------
# Output
"""
Enter number (comma-separated) 1,2,3,4
['1', '2', '3', '4']
('1', '2', '3', '4')
"""

```

Question 5: Level 1

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Problem
class with methods getString and printString
include simple test function

Steps to solve:
1. define class

