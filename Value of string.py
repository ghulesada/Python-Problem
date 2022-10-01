import string
values_lower = dict()
values_upper = dict()

for i, letter in enumerate(string.ascii_lowercase):
    values_lower[letter] = i + 1

for i, letter in enumerate(string.ascii_uppercase):
    values_upper[letter] = i + 27

values = {**values_lower, **values_upper}


def asciiconver(values, istring):
    total = 0
    print(list(istring))
    for i in list(istring):
        print(" value of", i, "is -->", values[i])
        total = total + values[i]
    return print("The total value is", total)


asciiconver(values, 'abcdEf')
