`session python hands on by` `**Darshan Ingle**`

**Reverse the order of words in the sentence**
"""""""
- convert the string to list of words
- list.reverse()
""""""
string = ""I Love My India""
lis = string.split("" "")
reverse_str = lis[::-1]
str_ = "" "".join(reverse_str)
print(str_)"

**Write a program that receives a tring and shifts all the vowels in it to the begining. Output the resultant string. The order of vowels wrt each other as well as the order of other characters wrt each other should stay the same.**

Input: You love Python
Output: ouoeoY lv Pythn"

"""
1. Make two empty strings
2. iterate over sentence
3. check if letter in sentece is vowel or not 
4. append the vowels to list 1
5. append the remaining to list 2
6. join both the list
"""
``py
sentence = "You love Python!"
L1 = []
L2 = []
for v in sentence:
    if v in "aeiouAEIOU":
        L1.append(v)
    else:
        L2.append(v)

L3 = ''.join(L1+L2)
print(L3)
``

**Two strings are anagrams of each other if you can rearrange the characters of one string to make other string. Given two strings, can you find if they are anagrams of each other?**

Input: thing
       night
Output: True

Input: rescue
       secure
Output: True
``py
def is_anagram(a,b):
    if sorted(a) ==sorted(b):
        return True
    else:
        return False
is_anagram('thing', 'night')
``

**4. WAP that computes the value of n+nn+nnn+nnnn+...nn...n n times with a given number as the value of n.**

Input: 3
You have to find: 3+33+333
Output: 369

Input: 2
You have to find: 2+22
Output: 24

Input: 10
You have to find: 10+1010+101010+...+10101010101010101010
Output: I dont know...whatever it be

``py
num = int(input())
summ = 0

for i in range(0, num):
    summ += int( str( num ) + i * str(num))
    
print(summ)
``

**5. Take input from the user in the format and print the output in the desired format as well.**

Input: {'Mobile':['Redmi','Samsung','Realme], 'Laptop':['Dell','HP'], 'TV':['Videocon','Sony']}

Output:['Mobile_Redmi','Mobile_Samsung','Mobile_Realme','Laptop_Dell', 'Laptop_HP','TV_Videocon','TV_Sony']

``py
import ast
inp_str = input()
input_dict = ast.literal_eval(inp_str)

final_list = []
for key in input_dict.keys():
    for word in input_dict[key]:
        final_list.append(str(key)+'_'+str(word))
        
print(final_list)

``