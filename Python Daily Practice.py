# Question 1:

# lis = []    # empty list

# # for block: providing required range
# for n in range(2000, 3201):

#     # if block and conditions
#     if (n % 7 == 0) and (n % 5 != 0):
#         lis.append(str(n))  # conv to str

# # Printing comma-separated sequence
# print(','.join(lis))

# ----------------------------------------------------------------
# Question 2:

# # Method 1: reverse iteration


# n = int(input("Enter a number: "))


# def factorial(num):
#     if num < 0:
#         return "No Factorial for negative number"

#     if num == 0:
#         return 1

#     result = 1  # initializing var

#     # reverse iteration
#     for i in range(num, 0, -1):
#         result = result * i
#     return result


# print("Factorial =", factorial(n))
# print()

# # Method 2: Recursive Function


# def factorial(num):
#     if num < 0:
#         return "No Factorial for negative number"

#     if num == 0:
#         return 1

#     # recurring
#     return num * factorial(num - 1)


# n = int(input("Enter a number: "))    # take input
# print("Factorial =", factorial(n))
# print()

# # Method 3: While Loop


# def factorial(num):
#     if num < 0:
#         return "No Factorial for negative number"

#     fact = 1
#     while (num > 0):
#         fact = fact * num
#         num = num - 1
#     return fact


# n = int(input("Enter a number: "))
# print("Factorial =", factorial(n))

# ----------------------------------------------------------------

# Question 3

# # take input and convert it to int
# num = int(input("Enter a number: "))

# # initializing a dictionary
# result = dict()

# # using for loop to fill the dictionary
# for i in range(1, num+1):
#     result[i] = i*i

# # printing the result
# print(result)

# ----------------------------------------------------------------

# Question 4

# # Take input with comma-separated sequence
# numbers = input()

# # create list
# lis = numbers.split(',')

# # create tuple
# tupl = tuple(lis)

# # print results
# print(lis)
# print(tupl)

# ----------------------------------------------------------------

# Question 5

class InputOutputString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


str_object = InputOutputString()
str_object.getString()
str_object.printString()

# Need explanation on it
