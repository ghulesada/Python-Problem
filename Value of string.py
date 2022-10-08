import string

# creating dictionaries for Uppercase and Lowercase
values_lower = dict()
values_upper = dict()
# Lower case
for i, letter in enumerate(string.ascii_lowercase):
    values_lower[letter] = i + 1
# Upper case
for i, letter in enumerate(string.ascii_uppercase):
    values_upper[letter] = i + 27
# Merging dictionaries
values = {**values_lower, **values_upper}

# Funtion for calculation


def asciiconver(values, istring):
    total = 0
    print(list(istring))
    for i in list(istring):
        print(" value of", i, "is -->", values[i])
        total = total + values[i]
    return print("The total value is", total)


asciiconver(values, 'abcdEf')
