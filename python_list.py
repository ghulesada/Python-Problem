"""
Notion 
https://www.notion.so/Python-Lists-7f011e696f76412180697f4a027bbcf1

hashnode draft
https://hashnode.com/draft/63372aa2fa20fa4bc8e561a4
"""

"""
# What is a list?
List is a datastructure in python
List is ordered - the order at which you store the elements will stay the same untill you chage it
List is changable/mutable - the elements in list can be changed or replaced
List allows duplicates - a single elements can be added many times to the same list
List allows you to store different data types all together

# How to make a list?
Place items inside Square Brackets
"""
# =================================================================================================================================# # Creating list
# lis = [1, True, "Hello World!", 5.022, (5, 6), {"A": 'a', "B": 'b'}]

# print("This is our list:", lis)      # printing list
# print("Type of lis is:", type(lis))  # checking type

# -------------------------------------------------------------------------------------------------------------------------
# # OUTPUT
# """
# This is our list: [1, True, 'Hello World!', 5.022, (5, 6), {'A': 'a', 'B': 'b'}]
# Type of lis is: <class 'list'>
# """
# # =================================================================================================================================
# # Accessing Items from list
# lst = ["First element", "Second element", "Third element", "Fourth element"]

# # Access First element
# print(lst[0])
# print(lst[-4])  # negative indexing
# print()

# # Access second element
# print(lst[1])
# print(lst[-3])  # negative indexing
# print()

# # Access Third element
# print(lst[2])
# print(lst[-2])  # negative indexing
# print()

# # Access fourth element
# print(lst[3])
# print(lst[-1])  # negative indexing
# print()

# # -----------------------------------------------------------------------------------------------------
# # OUTPUT
# """
# First element
# First element

# Second element
# Second element

# Third element
# Third element

# Fourth element
# Fourth element
# """

# =================================================================================================================================
# Get index by providing value
# index()
# """The index() method returns the position at the first occurrence of the specified value."""
# shopping_list.index("Adapter for iPhone")


# import string
# fruits = ["apple", "orange", "pomegranate"]
# # index -->  0         1          2
# print(fruits.index("pomegranate"))
# ----------------------------------------------------------------

# # OUTPUT
# """
# 2
# """
# -#-#-#-#-#-#-#-#-
# No match
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(numbers.index(0))
# ----------------------------------------------------------------

# # OUTPUT
# """
# ValueError: 0 is not in list
# """

# -#-#-#-#-#-#-#-#-
# # try except
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# try:
#     print(numbers.index(0))
# except ValueError:
#     print("item does not exist")
# # ----------------------------------------------------------------

# # OUTPUT
# """
# item does not exist
# """

# -#-#-#-#-#-#-#-#-
# With optional parameters
# Loading the lowercase alphabet to a list
#
# >>>>>>>>>>>>>>>>>
# =================================================================================================================================

# # Add elements to the list
# # append()
# """The append() method adds an item to the end of the list."""

# # Example 1: Adding Element to a List
# # List of things I want to buy
# shopping_list = ["iPhone 14", "Fridge", "Television"]

# # oh!!!, I forgot APPLE dont provide "Adapter" for charging, so I will addeng it in the list
# shopping_list.append("Adapter for iPhone")

# # Lets see the complete list
# print(shopping_list)

# # Example 2: Adding List to a List

# # animals list
# animals = ['cow', 'buffalo']

# # list of wild animals
# wild_animals = ['tiger', 'fox']

# # appending wild_animals list to animals
# animals.append(wild_animals)

# print('Updated animals list: ', animals)


# # extend()
# """The extend() method adds the specified list elements (or any iterable) to the end of the current list."""
# # I want to add fruits to my shopping_list
# shopping_list.extend(fruits)

# # insert()
# """The insert() method inserts the specified value at the specified position."""
# shopping_list.insert(-1, "T-Shirt")


# # Delete elements form the list
# # clear()
# """Remove all elements from the list:"""
# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.clear()
# print(fruits)

# # pop()
# """The pop() method removes the element at the specified position."""
# removed_element = fruits.pop(0)

# # remove()
# """The remove() method removes the first occurrence of the element with the specified value."""
# shopping_list.remove("Television")

# # Update elements form the list

# # Sorting list
# # sort()
# """The sort() method sorts the items of a list in ascending or descending order."""
# even_numbers = [44, 66, 24, 2, 8, 6, 10]
# even_numbers.sort()
# even_numbers.sort(reverse=True)
# list_of_tuples = [(1, 1), (1, 2), (1, 3),
#                   (2, 1), (2, 2), (2, 3),
#                   (3, 1), (3, 2), (3, 3)]
# # sort by 1st value in tuple
# list_of_tuples.sort(key=lambda x: x[0])
# print(list_of_tuples)
# # sort by 2nd value in tuple
# list_of_tuples.sort(key=lambda x: x[1]
# print(list_of_tuples)

# # Find length of list
# # print(len(lis))

# # Find Largest Number in the list

# # Find Smalles Number in the list

# # Clear List
# # clearing the list
# list.clear()

# # clearing the list
# del list[:]

# # Check if the element Exist in the list

# # Reversing the list
# # reverse()
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(numbers.reverse)

# # Cloning or Copying the list
# # copy()
# """The copy() method returns a copy of the specified list."""
# shopping_list_copy=shopping_list.copy()
# print(shopping_list_copy)


# # Count Occurance of element in list
# # count()
# """The count() method returns the number of elements with the specified value.

# """
# points=[1, 4, 2, 5, 7, 8, 5, 3, 1, 5]

# count_5=points.count(5)

# # Find Sum and Average of list
