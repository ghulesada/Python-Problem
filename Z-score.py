import numpy as np

size = int(input())
input_list = input().split(" ")
threshold = float(input())

float_list = []

for i in input_list:
    float_list.append(float(i))

# print(float_list)
salary = []

for i in range(size-1):
    salary.append(float_list[i])

# print(salary)

salary = np.array(salary)
# print(salary)

mean = np.mean(salary)
std = np.std(salary)

outlier = []
salary = list(salary)
for i in salary:
    z = (i-mean)/std
    if z > threshold:
        outlier.append(i)

# print(outlier)

index_outlier = []
for i in outlier:
    # result = np. where(arr == 15)
    temp = salary.index(i)
    index_outlier.append(temp + 1)

for i in index_outlier:
    print(i, end=" ")
