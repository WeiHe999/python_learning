#!/usr/bin/env python
# coding: utf-8

# # Python Basic Exercise for Beginners

# In[98]:


# DFS search
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []

def dfs(graph,node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

dfs(graph1,'A')
print(visited)

parents = {}
for k, s in enumerate(visited):
    for x in visited[:k][::-1]:
        if s in graph1[x]:
            parents[s] = x
            break
print(parents)

# print the links
for k, s in enumerate(visited):
    if k>0:
        print('{}==>{}'.format(parents[s], s))


# ## Question 1: Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum

# In[3]:


num1 = int(input("Your first number: "))
num2 = int(input("Your second number: "))
product = num1 * num2
addition = num1 + num2
if product < 1000:
    print(product)
else:
    print(addition)


# ## Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

# In[5]:


def add(num1, num2):
    return(num1 + num2)
for x in range(0, 10):
    if x == 0:
        continue
    else:
        print(add(x, x-1))


# ## Question 3: Accept string from a user and display only those characters which are present at an even index number.

# In[16]:


word = input("Your word: ")
list1 = list(word)
list2 = []
for k, x in enumerate(list1):
    if k % 2 == 0:
        list2.append(x)
    else:
        continue
str1 = ''.join(list2)
print(str1)


# ## Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

# In[32]:


string = input("Enter a word or sentence: ")
n = int(input("Enter a number: "))
list1 = list(string)
list2 = []
for k,x in enumerate(list1):
    if k <= n - 1:
        continue
    else:
        list2.append(x)
str1 = ''.join(list2)
print(str1)


# ## Question 5: Given a list of numbers, return True if first and last number of a list is same

# In[38]:


import random
def check_first_and_last(list1):
    if list1[0] == list1[-1]:
        print(True)
    else:
        print(False)
list1 = [1, 2, 1]
check_first_and_last(list1)


# ## Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

# In[41]:


def put_mult_of_5(list1):
    set1 = set(list1)
    list2 = list(set1)
    list3 = []
    for x in list1:
        if x % 5 == 0:
            list3.append(x)
        else:
            continue
    return(list3)
list1 = [12, 13452, 15625, 1000]
put_mult_of_5(list1)


# ## Question 7: Return the total count of string “Emma” appears in the given string

# In[48]:


Emmas = 0
Emma = input("Enter 1 or 2 sentences including the word Emma: ")
listEmma = list(Emma)
for k,x in enumerate(listEmma):
    list1 = listEmma[k:k + 4]
    str1 = ''.join(list1)
    if str1 == 'Emma':
        Emmas = Emmas + 1
    else:
        continue
print(Emmas)


# ## Question 8: Print the following pattern

# In[53]:


number = int(input("How long do you want your pattern to be? "))
for x in range(number + 1):
    list1 = [str(x)] * x
    str1 = ' '.join(list1)
    print(str1)


# ## Question 9: Reverse a given number and return true if it is the same as the original number

# In[60]:


str1 = input("Enter a number: ")
str2 = str1[::-1]
number1 = int(str1)
number2 = int(str2)
if number2 == number1:
    print(True)
else:
    print(False)


# ## Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

# In[65]:


list1 = []
list2 = []
list3 = []
for x in range(0,10):
    n = random.randint(1,20)
    list1.append(n)
for x in range(0,10):
    m = random.randint(1,20)
    list2.append(m)
for x in list1:
    if x % 2 == 1:
        list3.append(x)
    else:
        continue
for y in list2:
    if y % 2 == 0:
        list3.append(y)
print(list3)


# # Python Data Structure Exercise for Beginners

# ## Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

# In[68]:


list1 = []
list2 = []
list3 = []
for x in range(0,10):
    n = random.randint(1,20)
    list1.append(n)
for y in range(0,10):
    m = random.randint(1,20)
    list2.append(m)
for k,a in enumerate(list1):
    if k % 2 == 0:
        list3.append(a)
for c,b in enumerate(list2):
    if c % 2 == 1:
        list3.append(b)
print(list3)


# ## Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

# In[80]:


List = [54, 44, 27, 79, 91, 41]
print("The list:", List)
element = List[4]
print("I removed", element1, "from index 4 and I added", element1)
print("back to index 2. I also added", element1, "to the end of the list.")
List.remove(element)
List.insert(2, element)
List.append(element)
print(List)


# ## Exercise Question 3: Given a list slice it into a 3 equal chunks and reverse each list

# In[92]:


list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list:", list1)
x = len(list1)
if x % 3 == 0:
    y = int(x/3)
    chunk1 = []
    for n in range(y):
        chunk1.append(list1[n])
    chunk1 = chunk1[::-1]
    chunk2 = []
    for n in range(y):
        chunk2.append(list1[3 + n])
    chunk2 = chunk2[::-1]
    chunk3 = []
    for n in range(y):
        chunk3.append(list1[6 + n])
    chunk3 = chunk3[::-1]
else:
    print("Not a multiple of 3.")
print(chunk1)
print(chunk2)
print(chunk3)


# ## Exercise Question 4: Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

# In[99]:


dict_1 = {'a1': 1, 'b': 2}
list(dict_1.keys())


# In[100]:


list(dict_1.values())


# In[101]:


for k, v in dict_1.items():
    print(k, v)


# In[102]:


list_2 = [(k, v) for k, v in dict_1.items()]
print(list_2)


# In[104]:


if 'g1' in dict_1:
    print('it is in the dict')
else:
    print('It is not in the dict')


# In[105]:


list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list:", list1)
dict1 = {}
for x in list1:
    if x in dict1:
        dict1[x] = dict1[x] + 1
    else:
        dict1[x] = 1
print(dict1)


# ## Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair

# In[108]:


list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
print("First List:", list1)
print("Second List:", list2)
list3 = []
for k in range(len(list1)):
    tuple1 = (list1[k], list2[k])
    list3.append(tuple1)
set1 = set(list3)
print(set1)


# ## Exercise Question 6: Given a following two sets find the intersection and remove those elements from the first set

# In[110]:


list_a = [1,2, 3, 5]
list_b = [2, 4, 3]
set_inter = set(list_a).intersection(set(list_b))
print(set_inter)
list_inter = list(set_inter)
print(list_inter)


# In[114]:


list1 = [65, 42, 78, 83, 23, 57, 29]
list2 = [67, 73, 43, 48, 83, 57, 29]
set1 = set(list1)
set2 = set(list2)
print("First set:", set1)
print("Second set:", set2)
setinter = set1.intersection(set2)
print("Intersection set:", setinter)
for x in setinter:
    list1.remove(x)
set3 = set(list1)
print("First set after removing common elements:", set3)


# ## Exercise Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set

# In[120]:


list1 = [27, 43, 34]
list2 = [34, 93, 22, 27, 43, 53, 48]
set1 = set(list1)
set2 = set(list2)
print("First set:", set1)
print("Second set:", set2)
print("First set is subset of second set - True")
print("Second set is subset of First set -  False")
print("First set is Super set of second set -  False")
print("Second set is Super set of First set -  True")
if set1.issubset(set2) == True:
    for x in set1:
        set2.remove(x)
print(set2)


# ## Bubblesort!

# In[135]:


get_ipython().run_cell_magic('time', '', 'def bubblesort(list1):\n    for x in range(len(list1) - 1):\n        for k in range(len(list1) - 1):\n            if list1[k] > list1[k + 1]:\n                a = list1[k]\n                list1[k] = list1[k + 1]\n                list1[k + 1] = a\n    return(list1)\nlist1 = []\nfor i in range(0, 100):\n    c = random.randint(1, 50)\n    list1.append(c)\nprint(list1)\nlist2 = bubblesort(list1)\nprint(list2)')


# ## Selectionsort!

# In[136]:


get_ipython().run_cell_magic('time', '', 'def selectionsort(list1):\n    list2 = []\n    for x in range(len(list1) - 1):\n        a = min(list1)\n        list2.append(a)\n        list1.remove(a)\n    list2.append(list1[0])\n    return(list2)\nlist1 = []\nfor i in range(0, 100):\n    b = random.randint(1, 50)\n    list1.append(b)\nprint(list1)\nlist2 = selectionsort(list1)\nprint(list2)')


# ## Insertionsort!

# In[234]:


def insert_element(list1, a):
    list2 = []
    for k, s in enumerate(list1):
        if a > s:
            list2.append(s)
        else:
            list2.append(a)
            list2 = list2 + list1[k:]
            break
    return(list2)

def insertionsort(list1):
    list2 = []
    for s in list1:
        insert_element(s, list2)
    return(list2)


# In[235]:


get_ipython().run_cell_magic('time', '', 'list1 = []\nfor i in range(0, 100):\n    a = random.randint(1, 50)\n    list1.append(a)\nprint(list1)\nlist2 = selectionsort(list1)\nprint(list2)')


# ## Exercise Question 8: Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list

# In[ ]:


dict_a={'a': 1, 'b':2}
list_v = list(dict_a.values())
list_k = list(dict_a.keys())


# In[154]:


list1 = [47, 64, 69, 37, 76, 83, 95, 97]
list2 = []
dict1 = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}
listv = list(dict1.values())
for x in list1:
    if x in listv:
        list2.append(x)
    else:
        continue
print("After removing unwanted elements:", list2)


# ## Exercise Question 9: Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates

# In[162]:


speed = {'Jan':47, 'Feb':52, 'March':47, 'April':44, 'May':52, 'June':53, 'July':54, 'Aug':44, 'Sept':54}
list1 = []
listv = list(speed.values())
set1 = set(listv)
list2 = list(set1)
print("Result:", list2)


# ## Exercise Question 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number

# In[167]:


list1 = [87, 45, 41, 65, 94, 41, 99, 94]
print("List:", list1)
set1 = set(list1)
list2 = list(set1)
list2 = sorted(list2)
print("After removing duplicates:", list2)
tuple1 = tuple(list2)
print("Tuple:", tuple1)
num1 = min(list2)
num2 = max(list2)
print("Min:", num1)
print("Max:", num2)


# # Lists

# ## Exercise Question 1: Given a Python list you should be able to display Python list in the following order

# In[174]:


list1 = [100, 200, 300, 400, 500]
list2 = list1[::-1]
print(list2)


# ## Exercise Question 2: Concatenate two lists index-wise

# In[178]:


list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [a + b for a, b in zip(list1, list2)]
print(list3)


# ## Exercise Question 3: Given a Python list. Turn every item of a list into its square

# In[208]:


def square(list1, list2):
    for n in list1:
        a = n**2
        list2.append(a)
    return(list2)
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
square(list1, list2)


# ## Exercise Question 4: Concatenate two lists in the following order

# In[213]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)


# ## Exercise Question 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

# In[214]:


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)


# ## Exercise Question 6: Remove empty strings from the list of strings

# In[216]:


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("List:", list1)
list2 = list(filter(None, list1))
print("After removing:", list2)


# ## Exercise Question 7: Add item 7000 after 6000 in the following Python List

# In[217]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


# ## Factorials

# In[218]:


def fact(n):
    if n >= 1:
        return(n * fact(n - 1))
    else:
        return(1)


# In[227]:


fact(10)


# ## Fibonacci

# In[222]:


def fib(n):
    if n >= 3:
        return(fib(n - 1) + fib(n - 2))
    else:
        return(1)


# In[232]:


fib(10)


# ## Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

# In[236]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
list1[2][1][2].extend(sublist)
print(list1)


# ## Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# In[237]:


list1 = [5, 10, 15, 20, 25, 50, 20]
i = list1.index(20)
list1[i] = 200
print(list1)


# ## Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list

# In[240]:


list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
for x in list1:
        if x == 20:
            continue
        else:
            list2.append(x)
print(list2)


# ## A typical car can hold 4 passengers and 1 driver, overall allowing 5 people to travel around. Given n number of people, return how many cars are needed to seat everyone comfortably.

# In[245]:


n = int(input("Number of people: "))
if n % 5 == 0:
    print(int(n / 5))
else:
    print("Number of cars:", int(n / 5) + 1)


# ## Create a function that takes a string and returns the number (count) of vowels contained within it.

# In[250]:


def count_vowels(str1):
    str1 = str1.lower()
    vowelcount = 0
    list_v = list("aeiou")
    for s in list(str1):
        if s in list_v:
            vowelcount = vowelcount + 1
    return(vowelcount)
n = input("Enter a word: ")
print("Number of vowels:", count_vowels(n))


# ## Create a function that takes a string (will be a persons first and last name) and returns a string with the first and last name swapped.

# In[251]:


firstname = input("Your first name: ")
lastname = input("Your last name: ")
print("Your name:", firstname, lastname)
print("Your name swapped:", lastname, firstname)


# ## Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

# In[272]:


def asciicode(str1):
    if str1.islower() == True:
        str_lower = str1
        str_upper = str1.upper()
    else:
        str_lower = str1.lower()
        str_upper = str1
    print("Ascii Value(lowercase):", ord(str_lower))
    print("Ascii Value(uppercase):", ord(str_upper))
str3 = input("Enter a character: ")
asciicode(str3)


# ## Create a function that takes a string and returns a string in which each character is repeated once.

# In[281]:


def doublechar(str1):
    list1 = list(str1)
    list2 = []
    for x in list1:
        list2.append(x)
        list2.append(x)
    str1 = ''.join(list2)
    return(str1)
str2 = input("Enter something that can contain letters, numbers, and symbols: ")
print("Output:", doublechar(str2))


# ## Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

# In[290]:


def reverse(str1):
    if str1.lower() == 'true':
        return(False)
    elif str1.lower() == 'false':
        return(True)
    else:
        return("boolean expected")
str2 = input("Type True or False(can type something else): ")
reverse(str2)


# ## Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

# In[295]:


def XO(str1):
    list1 = list(str1)
    xcount = 0
    ocount = 0
    for x in list1:
        if x == 'x':
            xcount = xcount + 1
        elif x == 'o':
            ocount = ocount + 1
        else:
            continue
    if xcount == 0 and ocount == 0:
        return(True)
    elif xcount == ocount:
        return(True)
    elif xcount > ocount or ocount > xcount:
        return(False)
    else:
        return(True)
str2 = input("Enter a string with x and o's: ")
XO(str2)


# ## Binarysearch!

# In[301]:


list1 = [2,4,5,78,9,12,14,17,19,22,25,27,28,33,37]
n = 29
def linearsearch(list1, n):
    for i in range(len(list1)):
        if list1[i] == n:
            return(True)
    return(False)
def binarysearchiterative(list1, n):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = (low + high) // 2
        if n == list1[mid]:
            return(True)
        elif n < list1[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return(False)
def binarysearchrecursive(list1, n, low, high):
    if low > high:
        return(False)
    else:
        mid = (low + high) // 2
        if n == list1[mid]:
            return(True)
        elif n < list1[mid]:
            return(binarysearchrecursive(list1, n, low, mid - 1))
        else:
            return(binarysearchrecursive(list1, n, mid + 1, high))
print(binarysearchiterative(list1, n))
print(binarysearchrecursive(list1, n, 0, len(list1) - 1))


# ## Jumpsearch!

# In[361]:


import math

def Jumpsearch(list1, n):
    length = len(list1)
    num_blocks = 5
    block_size = math.ceil((len(list1)/num_blocks))
    # create a list of blocks
    list_lists = []
    for k in range(num_blocks):
        block = list1[k*block_size: (k+1)*block_size]
        list_lists.append(block)
    print(list_lists)
    # search for each block
    for block in list_lists:
        if block[-1]<n:
            continue
        elif block[-1]==n:
            return(True)
        else:
            break
    # search in the block
    for s in block:
        if s==n:
            return(True)
        elif s>n:
            return(False)
        else:
            continue
    return(False)    


# In[362]:


list1 = [1,2,3,4,4,5,6,7,7,8,9,10,13,17,19,26,26,29]
n = 30
Jumpsearch(list1, 14)


# ## Write a function that finds the sum of the first n natural numbers. Make your function recursive.

# In[381]:


def sum_numbers(n):
    if n > 1:
        total = n + sum_numbers(n - 1)
        return(total)
    else:
        return(1)
    return(total)
sum_numbers(5)


# ## Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.

# In[9]:


def listofmultiples(x, y):
    list1 = []
    for i in range(y):
        list1.append(x * (i + 1))
    return(list1)
listofmultiples(5, 7)


# ## The iterated square root of a number is the number of times the square root function must be applied to bring the number strictly under 2. Given an integer, return its iterated square root. Return "invalid" if it is negative.

# In[16]:


import math
def i_sqrt(n):
    if n < 0:
        return "Invalid!"
    else:
        n = int(math.sqrt(n))
    return n
i_sqrt(7)


# ## In each input list, some numbers repeat. Write a function that returns the rest of the numbers

# In[7]:


def returnunique(list1):
    list2 = []
    for x in list1:
        count = list1.count(x)
        if count == 1:
            list2.append(x)
        else:
            continue
    return(list2)
list1 = [1,1,2,3,4,4,6,7,7,6,8,8]
returnunique(list1)


# ## Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.

# In[13]:


def stupid_addition(x, y):
    if type(x) == type(y):
        if type(x) == int:
            return int(str(x) + str(y))
        return int(x) + int(y)
stupid_addition('1', '2')


# ## Mergesort!

# In[19]:


def Mergesort_split(a):
    list2 = []
    for x in range(len(list1)):
        sublist1 = [a[x]]
        list2.append(sublist1)
    return list2
a = [1,2,3,2,1,5]
Mergesort_split(a)


# In[22]:


def Merge2lists(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    c = c + a[i:] + b[j:]
    return(c)


# In[ ]:





# In[33]:


def Mergelists(listoflists):
    while True:
        list1 = []
        for i in range(0, len(listoflists), 2):
            a = listoflists[i]
            if i + 1 < len(listoflists):
                b = listoflists[i + 1]
                c = Merge2lists(a, b)
                list1.append(c)
            else:
                list1.append(a)
        if len(list1) == 1:
            break
        else:
            listoflists = list1
    return(list1[0])
listoflists = [[1], [2], [3], [2], [1], [5]]
Mergelists(listoflists)

def Mergesort(list1):
    list2 = Mergesort_split(list1)
    list3 = Mergelists(list2)
    return list3
list1 = [6,5,4,3,2,1]
Mergesort(list1)
# ## Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone. See the resources tab for the formula.

# In[36]:


def cone_volume(h, r):
    return round((1/3)*math.pi*(r**2)*h,2)
cone_volume(3, 2)


# ## Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

# In[38]:


def find_even(n):
    return [x for x in range(2,n + 1,2)]
find_even(8)


# ## Given a word, return False the word contains duplicate letters. Return True otherwise.

# In[58]:


def no_duplicates(str1):
    list2 = []
    list1 = list(str1)
    for x in list1:
        if x not in list2:
            list2.append(x)
        else:
            return False
    return True
no_duplicates('no')


# ## Write a function that finds the sum of the first n natural numbers. Make your function recursive.
# 
# 

# In[62]:


def sum_numbers(n):
    if n > 1:
        total = n + sum_numbers(n - 1)
        return(total)
    else:
        return(1)
sum_numbers(5)


# ## Create a function, that will for a given a, b, c, do the following: Add a to itself b times. Check if the result is divisible by c.

# In[64]:


def abcmath(a, b, c):
    total = a * (2 ** b)
    if total % c == 0:
        return True
    else:
        return False
abcmath(1, 2, 4)


# ## Create a function that takes a list and finds the integer which appears an odd number of times.
# 
# 

# In[67]:


def find_odd(list1):
    for x in list1:
        if x % 2 == 0:
            continue
        else:
            return x
find_odd([2,4,6,8,9])


# ## Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
# 
# 

# In[72]:


def timeformilkandcookies(y, m, d):
    if m == 12 and d == 24:
        return True
    return False
timeformilkandcookies(2014, 11, 24)


# ## Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.
# 
# 

# In[74]:


def next_in_line(list1, n):
    if list1 == []:
        return "No list has been selected!"
    else:
        list1.remove(list1[0])
        list1.append(n)
        return list1
next_in_line([1,2,3,4], 5)


# ## Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
# 
# 

# In[81]:


def index_of_caps(str1):
    list2 = []
    list1 = list(str1)
    for k, x in enumerate(list1):
        if x.isupper() == True:
            list2.append(k)
        else:
            continue
    return list2
index_of_caps("UnicOrn")


# ## Create a function that takes a string and returns a new string with all vowels removed.
# 
# 

# In[86]:


def remove_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list1 = list(str1)
    for x in list1:
        if x in vowels:
            list1.remove(x)
    str2 = ''.join(list1)
    return str2
remove_vowels("Happy Thanksgiving!")


# ## Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
# 
# 

# In[95]:


def issymmetrical(n):
    str1 = str(n)
    str2 = str1[::-1]
    if str2 == str1:
        return True
    else:
        return False
issymmetrical(7227)


# ## Create a function that takes a string and returns a string with its letters in alphabetical order.
# 
# 

# In[96]:


def alphabet_soup(str1):
    s = sorted(str1)
    str1 = ''.join(s)
    return str1
alphabet_soup('edabit')


# ## Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).
# 
# 

# In[118]:


def nth_element(list1, n):
    if n <= len(list1):
        return sorted(list1)[n-1]
    else:
        return None
nth_element([1,2,3,4], 1)


# ## Create a function that takes a list and returns a new list containing only prime numbers.
# 
# 

# In[122]:


def primecheck(n):
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                return False
                break
        else:
            return True
    else:
        return False


# In[123]:


def filter_primes(list1):
    for x in list1:
        if primecheck(x) == True:
            continue
        else:
            list1.remove(x)
    return(list1)
filter_primes([2,3,4])


# ## You are given three inputs: a string, one letter, and a second letter. Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

# In[126]:


def first_before_second(str1, str2, str3):
    list1 = str(list(str1))
    for x in list1:
        if x == str2:
            return True
        elif x == str3:
            return False
        else:
            continue
first_before_second("knaves knew about waterfalls", "k", "w")


# ## Create a function that reverses letters in a string but keeps digits in their current order.
# 
# 

# In[134]:


def reverse(str1):
    str2 = str1[::-1]
    return str2
reverse('abc')


# ## Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
# 
# 

# In[137]:


def add_str_nums(str1, str2):
    return str(int(str1) + int(str2))
add_str_nums('4', '5')


# ## Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
# 
# 

# In[147]:


def remove_letters(list1, str1):
    list3 = []
    list2 = list(str1)
    list4 = []
    for x in list1:
        if x in list2:
            if x in list4:
                list3.append(x)
            else:
                list4.append(x)  
        else:
            list3.append(x)
    return(list3)
remove_letters(['h', 'e', 'l', 'o', 'l'], 'hel')


# ## Create a function that evaluates an equation.
# 
# 

# In[148]:


def eq(str1):
    return eval(str1)
eq('1 + 2')


# ## A number has a breakpoint if it can be split in a way where the digits on the left side and the digits on the right side sum to the same number. For instance, the number 35190 can be sliced between the digits 351 and 90, since 3 + 5 + 1 = 9 and 9 + 0 = 9. On the other hand, the number 555 does not have a breakpoint (you must split between digits). Create a function that returns True if a number has a breakpoint, and False otherwise.

# In[14]:


def break_point(n):
    str1 = str(n)
    list1 = list(str1)
    b = 0
    e = len(list1) - 1
    m = (b + e) // 2
    sublist1 = list(list1[0 : m + 1])
    sublist2 = list(list1[m + 1 : e + 1])
    count1 = 0
    count2 = 0
    for x in sublist1:
        count1 = count1 + int(x)
    for y in sublist2:
        count2 = count2 + int(y)
    if count1 == count2:
        return True
    else:x
        sublist1 = list(list1[0 : m])
        sublist2 = list(list1[m : e + 1])
        count1 = 0
        count2 = 0
        for x in sublist1:
            count1 = count1 + int(x)
        for y in sublist2:
            count2 = count2 + int(y)
        if count1 == count2:
            return True
        else:
            return False
break_point(12321)


# ## Write a function that returns the longest common ending between two strings.
# 
# 

# In[15]:


def longest_common_ending(str1, str2):
    while not str1.endswith(str2):
        str2 = str2[1:]
    return str2
longest_common_ending('punctuation', 'hibernation')


# ## Create a function that takes in two words as input and returns a list of three elements, in the following order: Shared letters between two words. Letters unique to word 1. Letters unique to word 2. Each element should have unique letters, and have each letter be alphabetically sorted.

# In[180]:


def letters(str1, str2):
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list1 = list(str1)
    list2 = list(str2)
    for x in list1:
        if x in list2:
            list3.append(x)
        else:
            list4.append(x)
    for x in list2:
        if x not in list1:
            list5.append(x)
    str3 = ''.join(list3)
    str4 = ''.join(list4)
    str5 = ''.join(list5)
    list6.append(str3)
    list6.append(str4)
    list6.append(str5)
    return(list6)
letters('hello', 'hi')


# ## Find out if a right-angled triangle can be made given some facts about the shape. Given varying information about a shape, create a function that returns True if the shape could be a right-angle triangle and False if not. You will be given a list of numbers and a string stating whether the numbers are angles or sides. The information may indicate more than one possible shape, but we just need to know if these details could be found in a right-angled triangle.

# In[19]:


def isrightangle(list1, str1):
        if len(list1) == 3 and str1 == 'side':
            if list1[0] ** 2 + list1[1] ** 2 == list1[2] ** 2 or list1[1] ** 2 + list1[0] ** 2 == list1[2] ** 2 or list1[2] ** 2 + list1[1] ** 2 == list1[0] ** 2 or list1[0] ** 2 + list1[2] ** 2 == list1[1] ** 2:
                return True
            else:
                return False
        elif len(list1) == 2 and str1 == 'angle':
            return True
        else:
            return False
isrightangle([3,4,6], 'side')


# ## Write a function that sort each string in a list by the letter in alphabetic ascending order (a-z).
# 
# 

# In[26]:


def sort_by_letter(list1):
    return sorted(list1, key=lambda x: sorted(x)[-1])
sort_by_letter(['123c', '234a', '245z'])


# ## Create a function that subtracts one positive integer from another, without using -.
# 
# 

# In[28]:


def mysub(a, b):
    c = a + (-b)
    return(c)
mysub(1, 2)


# ## "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back. Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

# In[33]:


def lovesme(n):
    list1 = (['Loves me', 'Loves me not']*n)[:n]
    list1[-1] = list1[-1].upper()
    return ', '.join(list1)
lovesme(2)


# ## In this challenge, it's time to ban some impenitent digit! Your job is to delete the digits of a given number that, within their name written in English, contain a given vowel. Given an integer n, and a string ban being the vowel to search, implement a function that returns: If the given vowel is not present in the name of any of the digits of n, the same n. If n has at least a digit that contains the given vowel in its name, the new integer obtained after the elimination of banned digits (as a natural number without leading zeros). If all digits of n are banned, a string "Banned Number".

# In[47]:


def digitalvowelban(n, str1):
    dict1 = {'e': '0135789', 'i': '5689', 'o': '0124', 'u': '4'}
    new = ''.join(x for x in str(n) if x not in dict1.get(str1, ''))
    return 'Banned Number' if not new else int(new)
digitalvowelban(143, 'o')


# ## Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed. Given a censored string and a string of the censored vowels, return the original uncensored string.

# In[49]:


def uncensor(str1, str2):
    str1 = str1.replace('*', '{}')
    return str1.format(*v)
uncensor('H*ll*', 'eo')


# ## Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

# In[ ]:


def next_prime(n):
    while [x for x in range(2, n) if n % x == 0]:
        n += 1
    return n


# ## Write a function that returns True if two lists, when combined, form a consecutive sequence.
# 
# 

# In[52]:


def consecutive_combo(list1, list2):
    list3 = list1 + list2
    return max(list3) - min(list3) == len(list3) - 1
consecutive_combo([7, 4, 5, 1], [2, 3, 6])


# ## Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
# 
# 

# In[68]:


def isinorder(str1):
    list1 = list(str1)
    if list1 == sorted(list1):
        return True
    return False
isinorder('abc')


# ## Creates a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.

# In[70]:


def roundnumber(x, y):
    a = y * (x // y)
    b = y * ((x // y) + 1)
    dist1 = b - x
    dist2 = x - a
    if dist1 > dist2:
        return a
    else:
        return b
roundnumber(46, 7)


# ## A set is a collection of unique items. A set can be formed from a list from removing all duplicate items. Create a function that sorts a list and removes all duplicate items from it.

# In[3]:


def setify(list1):
    return list(set(list1))
setify([1,2,3,3,3,3,2])


# ## Create a function that returns the mean of all digits.
# 
# 

# In[6]:


def mean(n):
    total = 0
    list1 = [int(x) for x in str(n)]
    for x in list1:
        total = total + x
    return int(total / len(list1))
mean(42)


# ## With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples)

# In[7]:


list1 = [1, 2, 3, 4, 5, 6]
first = list1[0]
middle = list1[1 : -1]
last = list1[-1]
last


# ## Make a function that encrypts a given input with these steps: Input: "apple" Step 1: Reverse the input: "elppa" Step 2: Replace all vowels using the following chart: Step 3: Add "aca" to the end of the word: "1lpp0aca" Output: "1lpp0aca"
# 

# In[10]:


def encrypt(word):
    return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'
encrypt('a')


# ## lPaeesh le pemu mnxit ehess rtnisg! Oh, sorry, that was supposed to say: Please help me unmix these strings! Somehow my strings have all become mixed up; every pair of characters has been swapped. Help me undo this so I can understand my strings again.

# In[ ]:


def unmix(str1):
    if len(str1) < 2:
        return str1
    return str1[1] + str1[0] + unmix(str1[2:])


# ## Create a function that filters out factorials from a list. A factorial is a number that can be represented in the following manner: Recursively, this can be represented as:

# In[13]:


def isfactorial(x, current_factor = 1):
    if x == 1:
        return True
    elif x % current_factor == 0:
        return isfactorial(x/current_factor, current_factor + 1)
    else:
        return False
def filterfactorials(list1):
    return [x for x in list1 if isfactorial(x)]
filterfactorials([1,2,6])


# ## Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list. List order is:

# In[20]:


def count_datatypes(*arguments):
    list1 = [type(x) for x in arguments]
    return [list1.count(x) for x in (int, str, bool, list, tuple, dict)]
count_datatypes(1, 45, "Hi", False)


# ## Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.

# In[21]:


def convert_to_hex(str1):
    return ' '.join(hex(ord(x))[2:] for x in str1)
convert_to_hex('Big Boi')


# ## Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list. In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.

# In[25]:


def flip_list(list1):
    return [n[0] if isinstance(n, list) else [n] for n in list1]
flip_list([[1],[2],[3],[4]])


# ## Given two integers a and b, return how many times a can be halved while still being greater than b.
# 
# 

# In[35]:


def halvecount(x, y):
    count = 0
    while x > y:
        x = x / 2
        count = count + 1
    return count
halvecount(4, 2)


# ## Imagine a school that kids attend for 6 years. In each year, there are five groups started, marked with the letters a, b, c, d, e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and for the last year, the groups are 6a, 6b, 6c, 6d, 6e. Write a function that returns the groups in the school by year (as a string), separated with a comma and a space in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".

# In[48]:


def printallgroups():
    str1 = ''
    list1=list('abcde')
    for x in range(1, 7):
        for s in list1:
            str2 = '{}{}'.format(x, s)
            str1 = str1 + str2 + ', '
    return str1[:-2]
printallgroups()


# ## Create a function that finds how many prime numbers there are, up to the given integer.

# In[5]:


def primenumbers(n):
    return sum(1 for x in range(2, n) if all(x % y for y in range(2, x)))
primenumbers(100)


# ## Additional spaces have been added to a sentence. Return the correct sentence by removing them. All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.
# 
# 

# In[6]:


def correctspacing(s):
    return ' '.join(s.split())
correctspacing('Hello                    world')


# ## Given the month and year as numbers, return whether that month contains a Friday 13th.
# 
# 

# In[11]:


from datetime import date
def hasfriday13(m, y):
    return date(y, m, 13).strftime("%A")=='Friday'
hasfriday13(5, 2005)


# ## Write a function that takes a list of elements and returns only the integers.
# 
# 

# ## A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain: Create a function that determines whether or not a list is a factor chain.

# In[16]:


def factorchain(list1):
    if len(list1) <= 0:
        return False
    elif len(list1) == 1:
        return True
    for x in range(len(list1) - 1):
        if list1[x + 1] % list1[x] == 0:
            return True
        else:
            return False
factorchain([1,2,4,8])


# ## Create a function that takes a string and returns the number (count) of vowels contained within it.
# 
# 

# In[17]:


def countvowels(str1):
    return sum(x in "aeiou" for x in str1)
countvowels('hello')


# ## Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
# 
# 

# In[19]:


def nameshuffle(str1):
    x = str1.split(' ')
    return x[-1] + " " + x[0]
nameshuffle('Donald Trump')


# ## You are given three inputs: a string, one letter, and a second letter. Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

# In[23]:


def firstbeforesecond(str1, first, second, f = 0, s = 0):
    for char in str1:
        if char == first:
            f = 1
        elif char == second:
            s = 1
        if char == second and f == 0:
            return False
        elif char == first and s == 1:
            return False
    return True
firstbeforesecond("a rabbit jumps joyfully", "a", "j")


# ## Write a function that takes a positive integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration. In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots. Return the number of dots that exist in the whole pentagon on the Nth iteration.

# In[21]:


def pentagonal(n):
    if n == 1:
        return 1
    return pentagonal(n - 1) + 5 * (n - 1)
pentagonal(5)


# ## A block sequence in three dimensions. We can write a formula for this one: Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.
# 
# 

# In[24]:


def blocks(step):
    if step <= 0:
        return 0
    if step == 1:
        return 5
    return (5 + step) + blocks(step - 1)
blocks(5)


# ## Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
# 
# 

# In[26]:


def rearrangeddifference(n):
    d = ''.join(sorted(str(n)))
    return int(d[::-1]) - int(d)
rearrangeddifference(9765432)


# ## Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
# 
# 

# In[27]:


def filterlist(list1):
    return [x for x in list1 if type(x) is not str]
filterlist([1,2,3,'hello'])


# ## A snail fell into a bucket and wanted to crawl out. Assuming we already know the snail can climb 5cm per minute, the snail can crawl for 30 minutes continuously and then need to rest for 10 minutes. When it is resting it will slide down 30cm. How many minutes will it take for a snail to crawl out at different depths? Create a function that takes a number of the bucket depth (the unit is cm) as an argument and returns the minutes.

# In[29]:


import math
def crawl(d):
    if d == 150:
        return 30
    e = 40 * (d // 120)
    b = math.ceil((d % 120) / 5)
    return b + e
crawl(500)


# ## Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
# 
# 

# In[33]:


def censorstring(str1, list1, c):
    for w in list1:
        str1 = str1.replace(w, c * len(w))
    return str1
censorstring("Today is a Wednesday!", ["Today", "a"], "-")


# ## Create a function that returns the number of characters shared between two words.
# 
# 

# In[36]:


def sharedletters(str1, str2):
    x = 0
    for y in set(str1):
        if y in str2:
            x += 1
    return x
sharedletters('wussup', 'whatsup')


# ## Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
# 
# 

# In[39]:


def addindexes(list1):
    list2 = []
    for k, x in enumerate(list1):
        list2.append(k + x)
    return list2
addindexes([0,0,0,0,0])


# ## Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
# 
# 

# In[40]:


def noduplicateletters(phrase):
    x = phrase.split()
    for y in x:
        for z in set(y):
            if y.count(z) > 1:
                return False
    return True
noduplicateletters("Fortune favours the bold.")


# ## Create a function that takes in n, a, b and returns the number of values raised to the nth power that lie in the range [a, b], inclusive.
# 
# 

# ## A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.
# 
# 

# In[42]:


def almostpalindrome(str1): 
    count = 0
    palindrome = str1[::-1]
    for x in range(len(str1)):
        if str1[x] != palindrome[x]:
            count += 1
    return (count == 2)
almostpalindrome('abccia')


# ## Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
# 
# 

# In[44]:


def isinorder(str1):
    value = ord(str1[0])
    for x in range(1, len(str1)):
        if value > ord(str1[x]):
            return False
        else:
            value = ord(str1[x])
    return True
isinorder('edabit')


# ## In this challenge, you have to establish if a given number is undulating. A number n is undulating when the following conditions are all true: n has at least three digits. n has exactly two different digits. the two digits of n are alternating without repeating groups. If we think of the first digit of an undulating number as an "A", and the second digit as a "B", we notice a sequence of the form "ABA" that can repeat infinite times and ends either with an "A" or with a "B", but without clusters of "AA" or "BB" in it. Given a positive integer n, implement a function that returns True if n is an Undulating number, or False if it's not.

# In[45]:


def isundulating(x):
    if x < 100:
        return False
    t1 = set(list(str(x)))
    if len(t1) != 2:
        return False
    t2 = list(map(int, str(x)))
    list1 = []
    list2 = []
    for y in range(len(t2)):
        if y % 2 == 0:
            list1.append(t2[y])
        else:
            list2.append(t2[y])
    if sum(list1) / len(list1) == t2[0] and sum(list2) / len(list2) == t2[1]:
        return True
    return False
isundulating(121)


# ## Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# 
# 

# In[46]:


def majorityvote(list1):
    for x in set(list1):
        if list1.count(x) > len(list1) / 2:
            return x
    return None
majorityvote(['A', 'B', 'B', 'A', 'A'])


# ## Python got drunk and the built-in functions str() and int() are acting odd: You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.
# 
# 

# In[49]:


def inttostr(n):
    return str(n)
inttostr(5)
def strtoint(n):
    return int(n)
strtoint('6')


# In[50]:


inttostr(5)


# ## Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
# 
# 

# In[51]:


def convert(h, m):
    return (3600 * h) + (60 * m)
convert(1, 3)


# ## Create a function that takes a list and returns the sum of all numbers in the list.
# 
# 

# In[53]:


def getsumofelements(list1):
    return sum(list1)
getsumofelements([1,2,3,4])


# ## Create a function that takes a list and returns the difference between the biggest and smallest numbers.
# 
# 

# In[54]:


def differencemaxmin(list1):
    return max(list1) - min(list1)
differencemaxmin([1,2,3,4,5,6])


# ## Class

# In[62]:


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def get_name(self):
        return self.name


# In[63]:


p1 = Person("Wei", "23")
p2 = Person("Yingying", "40")


# In[64]:


print(p1.get_name())
print(p2.get_name())


# ## Stack

# In[74]:


a=['a']
a==[]


# In[94]:


class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
        return self.items
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)


# In[95]:


s = Stack()
print(s.is_empty())
s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.peek())
s.pop()
s.pop()
print(s.peek())
print(s.size())


# ## Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. The function will take three arguments: a as the coefficient of x^2 b as the coefficient of x c as the constant term
# 

# In[103]:


def quadraticequation(a, b, c):
    return (-b + ((b ** 2) - 4 * a * c) ** (1 / 2)) / (2 * a)
quadraticequation(1,0,0)


# ## Given a letter, created a function which returns the nearest vowel to the letter. If two vowels are equidistant to the given letter, return the earlier vowel.
# 
# 

# In[116]:


def nearest_vowel(str1):
    closestvowel = [abs(ord(str1) - ord('a')), 'a']
    for vowel in 'eiou':
        distance = abs(ord(str1) - ord(vowel))
        if distance < closestvowel[0]:
            closestvowel[0] = distance
            closestvowel[1] = vowel
    return closestvowel[1]
nearest_vowel('c')


# ## Creates a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.
# 
# 

# In[118]:


def round_number(n, m):
    x, o = m + 0, n + 0
    while x % m and o % m:
        x -= 1
        o += 1
    return o if not o % m else x
round_number(33, 25)


# In[119]:


def does_rhyme(str1, str2):
    vowels = set(list('aeiou'))
    a = str1.lower().split()[-1]
    b = str2.lower().split()[-1]
    return set(a) & vowels == set(b) & vowels
does_rhyme("Sam I am!", "Green eggs and ham.")


# ## Write three functions: boolean_and boolean_or boolean_xor These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.

# In[123]:


def boolean_and(list1):
    for i in range(1,len(list1)):
        if list1[i-1] and list1[i]:
            list1[i] = True
        else:
            list1[i] = False
    return list1[-1]
def boolean_or(list1):
    for i in range(1,len(list1)):
        if list1[i-1] or list1[i]:
            list1[i] = True
        else:
            list1[i] = False
    return list1[-1]
def boolean_xor(list1):
    for i in range(1,len(list1)):
        if list1[i-1] != list1[i]:
            list1[i] = True
        else:
            list1[i] = False
    return list1[-1]
boolean_and([True, True, False, True])


# In[124]:


boolean_or([True, True, False, False])


# In[125]:


boolean_xor([True, True, False, False])


# ## Create a function that creates a box based on dimension n.
# 
# 

# In[126]:


def makebox(n):
    if n == 1:
        return ['#']
    else:
        top = ['#' * n]
        bottom = ['#' * n]
        middle = ['#' + ' ' * (n-2) + '#'] * (n-2)
        return top + middle + bottom
makebox(5)


# ## Write a function that returns True if a given name can generate an array of words.
# 
# 

# In[127]:


def anagram(name, words):
    name_letters = [letter.lower() for letter in name if letter != ' ']
    words_letters = ''.join(words)
    return sorted(name_letters) == sorted(words_letters)
anagram("Justin Bieber", ["injures", "ebb", "it"])


# ## A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column). Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

# In[167]:


def tallestskyscraper(list1):
    return sum(1 for x in list1 if sum(x) > 0)
tallestskyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
])


# ## Create a function that takes a string and returns the first character that repeats.If there is no repeat of a character , then return "-1".
# 
# 

# In[206]:


def firstrepeat(str1):
    list1 = list(str1)
    list2 = list(set(list1))
    list3 = []
    if list2 == list1:
        return -1
    else:
        for x in list1:
            if x not in list3:
                list3.append(x)
            else:
                return x
firstrepeat('legolas')


# ## Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. Watch out for strings!
# 
# 

# In[210]:


def countmissingnums(list1):
    listn = sorted([int(x) for x in list1 if x.isdecimal()])
    n = [x for x in range(listn[0], listn[-1]+1) if x not in listn]
    return len(n)
countmissingnums(["1", "3", "5", "7", "9"])


# ## Given any number, we can create a new number by adding the sums of squares of digits of that number. For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers: Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy. Not all numbers are happy. If we started with 11, the sequence would be: This sequence will never reach 1, and so the number 11 is called unhappy. Given a positive whole number, you have to determine whether that number is happy or unhappy.
# 
# 
# 
# 
# 

# In[212]:


def happy(n):
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False
        n = sum(int(x) ** 2 for x in str(n))
happy(203)


# ## Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
# 
# 

# In[213]:


def pairs(list1):
    list2 = []
    while len(list1) > 0:
        if len(list1) == 1:
            list2.append([list1.pop()] * 2)
        else:
            list2.append([list1.pop(0),list1.pop()])
    return list2
pairs([1, 2, 3, 4, 5, 6, 7])


# ## Create a function that returns true if a given inequality expression is correct and false otherwise.
# 
# 

# In[215]:


def correctsigns(str1):
    list1 = [int(y) if y.isdigit() else y for y in str1.split()]
    for x in range(0, len(list1)-2, 2):
        if list1[x + 1] == '>':
            if list1[x] <= list1[x + 2]:
                return False
        elif list1[x + 1] == '<':
            if list1[x] >= list1[x + 2]:
                return False
    return True
correctsigns("3 < 7 < 11")


# ## Starting with either 3 or 5 and given these operations: add 5 multiply by 3 You should say if it is possible to reach the target number n.

# In[216]:


def only5and3(n):
    while n > 3:
        for x in range(2, 10):
            if n == (3 ** x):
                return True
        n -= 5
        if n == 3 or n == 5:
            return True
    return False
only5and3(14)


# ## Create a function that takes a list and returns the number of ALL elements within it (including those within the sub-level list(s)).
# 
# 

# In[217]:


# i hate red bean
# chiken
# are awesome
def deepcount(list1):
    count = 0
    for x in list1:
        if isinstance(x, list):
            count += 1
            count += deepcount(x)
        else:
            count +=1
    return count
deepcount([1, 2, 3])


# ## Write a function that sorts only the odd numbers in a list in ascending order, keeping the even numbers in their current place. For example, if our input list is: [5, 2, 6, 6, 1, 4, 9, 3]:

# In[230]:


def oddsort(list1):
    oddsnumbers = sorted([n for n in list1 if n % 2], reverse = True)
    for x, n in enumerate(list1):
        list1[x] = oddsnumbers.pop() if n % 2 else n
    return list1
oddsort([7, 5, 2, 3, 1])


# ## Write a function that takes a string as an argument and returns the left most digit in the string.
# 
# 

# In[229]:


def leftdigit(str1):
    for x in str1:
        if x.isdigit():
            return int(x)
leftdigit("TrAdE2W1n95!")


# ## Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.
# 
# 

# In[238]:


def posnegsort(list1):
    list2 = sorted([x for x in list1 if x > 0])
    for k, y in enumerate(list1):
        if y < 0:
            list2.insert(k, y)
    return list2
posnegsort([6, 3, -2, 5, -8, 2, -2])


# ## Bubblesort 2

# In[327]:


def bubble_sort(list1):
    n = len(list1)
    # outer-loop: (n-1) steps
    for k in range(n-1):
        print('****outer-loop: {}'.format(k))
        # inner loop: from index 1 to index n-1-k
        for m in range(1, n-k):
            print('inner-loop: {}'.format(m))
            # compare with the previous element and swap if less than it
            if list1[m]<list1[m-1]:
                tmp = list1[m-1]
                list1[m-1] = list1[m]
                list1[m] = tmp 
    return list1

bubble_sort([5,3,2,1])            


# ## assignment

# In[360]:


def randompyramid():
    a = 0
    for x in range(11, 0, -1):
        a += 1
        for j in range(1, x + 1):
            print(a, end = ' ')
        print('\r')
randompyramid()


# ## assignment

# In[385]:


list1 = [2, 5, 1, 4, 7]
if len(list1) == 1:
    print('Make the list longer.')
for x in range(0, len(list1) - 1):
    for m in range(1, len(list1) - x):
        print(list1[m], end = ' ')
        if list1[m] < list1[m - 1]:
            a = list1[m]
            list1[m] = list1[m - 1]
            list1[m - 1] = a
    print('\r')
print(list1)


# ## A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order. Some examples of alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop. Create a function that takes in a sentence as input and returns True if there is at least one alphabetically sorted word inside that has a minimum length of 3.

# In[432]:


def alphabeticallysorted(str1):
    s = ''.join(x for x in str1.lower() if x.isalpha() or x == ' ')
    for w in s.split():
        if ''.join(sorted(w)) == w and len(w) > 2:
            return True
    return False
alphabeticallysorted('Paula has a French accent.')


# ## Write a function that takes a list of elements and returns only the integers.
# 
# 

# In[435]:


def returnonlyinteger(list1):
    return [x for x in list1 if type(x) == int]
returnonlyinteger([9, 2, "space", "car", "lion", 16])


# ## What do the numbers 4, 6, 8, 9 and 0 have in common? They all have holes in them! Notice how the number 8 contains not one, but two holes. Given a list of numbers, sort the list in accordance to how many holes occur in the number. It should be sorted in ascending order.

# In[437]:


def holeysort(list1):
    list2 = []
    d = {'4':1,'6':1,'8':2,'0':1,'9':1}
    list1 = list1 = [str(x) for x in list1]
    for a in list1:
        n = 0
        for b in a:
            if b in d:
                n += d[b]
            else:
                n += 0
        list2.append((a, n))
    a = lambda x : x[1]
    return [int(a[0]) for a in sorted(list2, key = a, reverse = False)]
holeysort([100, 888, 1660, 11])


# ## Create a function that returns all pairs of numbers in a list that sum to a target. Sort the pairs in ascending order with respect to the smaller number, then order each pair in this order: [smaller, larger].

# In[440]:


def allpairs(list1, n):
    list2 = []
    for x in range(len(list1)):
        for y in range(x + 1, len(list1)):
            if list1[x] + list1[y] == n: list2.append(sorted([list1[x],list1[y]]))
    return sorted(list2)
allpairs([2,3,4,5], 7)


# ## Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be found in biglst, and in the same order. Examples: [4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1]. [5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1]. [5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered sublist of [3, 2, 1, 2, 3]. Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.

# In[441]:


def isordsub(list1, list2):
    for x in list1:
        if x in list2:
            list2 = list2[list2.index(x) + 1:]
        else:
            return False
    return True
isordsub([4, 3, 2], [5, 4, 3, 2, 1])


# ## Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

# In[443]:


def advancedsort(list1):
    list2 = [[n] * list1.count(n) for n in list1]
    list3 = []
    for x in list2:
        if x not in list3:
            list3.append(x)
    return list3
advancedsort([2, 1, 2, 1])


# ## Create a function that takes a string consisting of lowercase letters, uppercase letters and numbers and returns the string sorted in the same way as the examples below.

# In[445]:


def sortkey(char):
    a = 2 * ord(char.lower())
    if char.isupper():
        a = a + 1
    if char.isdigit():
        a = a + 200
    return a


# In[446]:


def sorting(str1):
    return ''.join(sorted(list(str1), key = sortkey))
sorting('eA2a1E')


# ## Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.

# In[451]:


def missingnum(list1):
    list2 = [1,2,3,4,5,6,7,8,9,10]
    for x in list2:
        if x in list1:
            continue
        else:
            return x
missingnum([1,2,3,4,5,6,7,8,9])


# ## A numbers factor length is simply its total number of factors.  For instance: Create a function that sorts a list by factor length in descending order. If multiple numbers have the same factor length, sort these numbers in descending order, with the largest first. In the example below, since 13 and 7 both have only 2 factors, we put 13 ahead of 7.

# In[452]:


def factors(n):
    return len([x for x in range(1, n + 1) if n % x == 0])


# In[453]:


def factorsort(list1):
    list2 = sorted([[factors(a), a] for a in list1])[::-1]
    return [x[1] for x in list2]
factorsort([1, 2, 31, 4])


# ## Write a function that returns the next largest number that can be created from the same digits as the input.

# In[458]:


def nextnumber(n):
    list1 = [int(x) for x in str(n)]
    for y in range(len(list1) - 1, 0, -1):
        if list1[y - 1] < list1[y]:
            digit = list1[y - 1]
            while digit not in list1[y:]:
                digit += 1
            near = list1[y:].index(digit) + y
            list1[y - 1], list1[near] = list1[near], list1[y - 1]
            list1[y:] = sorted(list1[y:])
            return int(''.join(str(a) for a in list1))
    return n
nextnumber(19)


# ## Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

# In[473]:


def indexofcaps(str1):
    return [str1.index(x) for x in str1 if x.isupper()]
indexofcaps('eDaBiT')


# ## Write a function that repeats the shorter string until it is equal to the length of the longer string.
# 
# 

# In[477]:


def lengthen(str1, str2):
    short, long = sorted([str1, str2], key = len)
    output = short * (int(len(long) / len(short)) + 1)
    return output[:len(long)]
lengthen('abcdefg', 'ab')


# ## Create a function that takes in a number as a string n and returns the number without trailing and leading zeros. Trailing Zeros are the zeros after a decimal point which don't affect the value (e.g. the last three zeros in 3.4000 and 3.04000). Leading Zeros are the zeros before a whole number which don't affect the value (e.g. the first three zeros in 000234 and 000230).

# In[480]:


def removeleadingtrailing(n):
    str1 = str(float(n))
    if str1.endswith('.0'):
        return str1[:-2]
removeleadingtrailing('230.000')


# ## Create a function that tweaks letters by one forward (+1) or backwards (-1) according to a list.

# In[486]:


def tweakletters(str1, list1):
    list2= 'abcdefghijklmnopqrstuvwxyz'
    str2 = ''
    for x in range(len(str1)):
        str2 = str2 + list2[(list2.index(str1[x]) + list1[x]) % 26]
    return str2
tweakletters("apple", [0, 1, -1, 0, -1])


# ## Binarysearch 2

# In[493]:


def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list1[mid]
        if guess == n:
            return mid
        elif guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return None
binary_search([1,2,3,4,5,6,7,8,9,10,100],2)


# ## What do the digits 0, 4, 6, 8, and 9 have in common? Well, they are whole numbers... and they are also hole numbers (not actually a thing until now). Hole numbers are numbers with holes in their shapes (8 is special in that it contains two holes).  14 is a hole number with one hole. 88 is a hole number with four holes. Your task is to create a function with argument N that returns the sum of the holes for the integers n in the range of range 0 < n <= N. To illustrate, sum_of_holes(14) returns 7, because there are 7 holes in 4, 6, 8, 9, 10 and 14.

# In[495]:


def sumofholes(n):
    dict1 = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
    holes = 0
    for x in range(4, n + 1):
        holes += sum(dict1.get(a, 0) for a in str(x))
    return holes
sumofholes(4)


# ## Create a function that can convert from normal notation to tally-mark notation and vice versa. In tally-mark notation, a number can be decomposed as the sum of 5s + remainder. The function will look like this: switch_notation([current scores], desired notation)

# In[505]:


def switchnotation(list1, str1):
    if str1 == 'tally':
        return [int(('5' * (x // 5) + str(x % 5)).rstrip('0')) for x in list1]
    return [sum(int(a) for a in str(b)) for b in list1]
switchnotation([51], 'normal')


# ## Selectionsort 2

# In[535]:


def minnumber(list1):
    minnum = list1[0]
    minnum_index = 0
    for k, x in enumerate(list1):
        if x < minnum:
            minnum = x
            minnum_index = k
    return minnum_index


# In[537]:


def selection_sort(list1):
    list2 = []
    for x in range(len(list1)):
        index = minnumber(list1)
        list2.append(list1[index])
        list1.pop(index)
    return list2
selection_sort([2,4,1,5,3])


# ## Recursion

# In[548]:


def countdownwith5_loop(n):
    if n % 5 != 0:
        while n % 5 != 0:
            n = n - 1
    for x in range(int(n / 5 + 1)):
        print(n, end=', ')
        n = n - 5
countdownwith5_loop(101)


# In[547]:


def countdownwith5_recur(n):
    if n % 5 != 0:
        while n % 5 != 0:
            n = n - 1
    if n >= 0:
        print(n, end=', ')
        countdownwith5_recur(n - 5)
    else:
        return
countdownwith5_recur(101)


# ## An anagram is a word, x, formed by rearranging the letters that make up another word, y, and using up all the letters in y at the same frequency. For example, "dear" is an anagram of "read" and "plead" is an anagram of "paled". The Hamming distance between two strings is the number of positions at which they differ. Hamming distances can only be calculated for strings of equal length. They only have the third position (index 2) in common, giving them a Hamming distance of 5. As anagrams are of identical length, the Hamming distance between them can be calculated. These strings differ at the first and last positions, giving them a Hamming distance of 2. "Plead" and "paled" have a Hamming distance of 3. Create a function that takes two strings, and returns: True if they are anagrams of each other and their Hamming distance is equal to their length (i.e. no letters in the same positions). False if they aren't anagrams, or Their Hamming distance if they are anagrams with >=1 letter at the same index.

# In[550]:


def maxham(str1, str2):
    if len(str1) != len(str2):
        return False
    elif set(str1) != set(str2):
        return False
    else:
        counter = 0
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                counter = counter + 1
        if counter == len(str1):
            return True
        else:
            return counter
maxham("dear", "read")


# ## Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

# In[553]:


def cardhide(str1):
    lastfournums = str1[-4:]
    str2 = ""
    for n in range(0, len(str1) - 4):
        str2 += "*"
    return str2 + lastfournums
cardhide('1234123456785678')


# ## Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another phrase txt2.

# In[552]:


def canbuild(str1, str2):
    for x in list(str1):
        if x != ' ' and str1.count(x) > str2.count(x):
            return False
    return True
canbuild("got 2 go", "gogogo 2 today")


# ## The weight of a word can be calculated by summing the Unicode code point for each character in the word, excluding any punctuation: Write a function that takes a sentence as a string, returning True if all word weights increase for each word in the sentence, and False if any word weight decreases or remains the same.

# In[554]:


def wordWeight(n):
    weight = 0
    for a in n:
        if a.isalpha():
            weight = weight + ord(a)
    return weight


# In[556]:


def increasingwordweights(s):
    sentencelist = s.split()
    pweight = wordWeight(sentencelist[0])
    for x in range(1, len(sentencelist)):
            weight = wordWeight(sentencelist[x])
            if pweight >= weight:
                return False
            pweight = weight
    return True
increasingwordweights("Why not try?")


# ## Write a function that swaps the first pair (1st and 2nd characters) with the second pair (3rd and 4th characters) for every quadruplet substring.

# In[562]:


def swaptwo(str1):
    if len(str1) < 4:
        return str1
    return str1[2 : 4] + str1[:2] + ''.join(swaptwo(str1[4:]))
swaptwo('ABCDEFGH')


# ## Create a left rotation and a right rotation function that returns all the left rotations and right rotations of a string.

# In[566]:


def leftrotations(str1):
    rotated = [str1]
    for x in range(1, len(str1)):
        rotated.append(rotated[-1][1:] + rotated[-1][0])
    return rotated
def rightrotations(str1):
    rotated = [str1]
    for x in range(1, len(str1)):
        rotated.append(rotated[-1][-1] + rotated[-1][:-1])
    return rotated
leftrotations("abc")


# In[565]:


rightrotations("abc")


# ## Create a function that reverses letters in a string but keeps digits in their current order.
# 
# 

# In[571]:


def reverse(str1):
    list1 = list(str1)
    listindex = []
    listvalue = []
    list2 = []
    for k, x in enumerate(list1):
        if x.isnumeric():
            listindex.append(k)
            listvalue.append(x)
        elif x.isalpha():
            list2.append(x)
    list2 = list2[::-1]
    for a, b in zip(listindex,listvalue):
        list2.insert(a, b)
    return "".join(list2)
reverse("ab89c")


# ## A word-chain is an array of words, where the next word is formed by changing exactly one letter from the previous word. We do not add or subtract letters from words, only change them. Create a function that returns True if an array is a word-chain and False otherwise.

# In[572]:


def iswordchain(list1):
    for k, x in zip(list1, list1[1:]):
        if sum(a != b for a, b in zip(k, x)) != 1:
            return False
    return True
iswordchain(["meal", "seal", "seat", "beat", "beet"])


# ## Implement a function count_substring that counts the number of substrings that begin with character "A" and ends with character "X". For example, given the input string "CAXAAYXZA", there are four substrings that begin with "A" and ends with "X", namely: "AX", "AXAAYX", "AAYX", and "AYX".

# In[574]:


def countsubstring(str1):
    count = 0
    for x in range(len(str1) - 1):
        if str1[x] == 'A':
            count += str1[x + 1:].count('X')
    return count
countsubstring("CAXAAYXZA")


# ## Create a function that takes in two words as input and returns a list of three elements, in the following order: Shared letters between two words. Letters unique to word 1. Letters unique to word 2. Each element should have unique letters, and have each letter be alphabetically sorted.

# In[579]:


def letters(str1, str2):
    a = set(str1)
    b = set(str2)
    return [''.join(sorted(x)) for x in (a & b, a - b, b - a)]
letters("sharp", "soap")


# ## D&Q loop

# In[4]:


def farmloop(h, w):
    large = max(h, w)
    small = min(h, w)
    while large % small != 0:
        a = large - ((large // small) * small)
        large = max(a, small)
        small = min(a, small)
    return(small)
farmloop(1680, 640)


# ## D&C recur

# In[18]:


def farmrecur(h, w):
    large = max(h, w)
    small = min(h, w)
    if large % small == 0:
        return(small)
    else:
        a = large - ((large // small) * small)
        large = max(a, small)
        small = min(a, small)
        return farmrecur(large, small)
farmrecur(1680, 640)


# In[39]:


def sumfunction(list1):
    total = 0
    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + sumfunction(list1[1:])
sumfunction([1,2,3,4])


# In[41]:


def maxnumber(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return max(list1[0], maxnumber(list1[1:]))
maxnumber([1,2,3,4])


# ## Write a function that sorts a list of integers by their digit length in descending order, then settles ties by sorting numbers with the same digit length in ascending order.
# 
# 

# In[43]:


def digitsort(list1):
    list1.sort(reverse = True)
    list2 = []
    dict1 = {list1[x] : len(str(list1[x])) for x in range(0,len(list1))}       
    dict2 = {n : sorted([a for a in dict1.keys() if dict1[a] == n]) for n in set(dict1.values())}
    for b in sorted(dict2.keys(), reverse = True):
        list2 += dict2[b]
    return list2
digitsort([77, 23, 5, 7, 101])


# In[52]:


def isitempty(list1):
    return list1 == []


# In[55]:


def length(list1):
    if islistempty(list1) == True:
        return 0
    else:
        return 1 + length(list1[1:])
length([1,4,5])


# ## A number n is called uban if its name (in English) does not contain the letter "u". In particular, it cannot contain the terms "four", "hundred", and "thousand", so the uban number following 99 is 1,000,000.
# 
# 

# In[58]:


def uban(n):
    list1 = list(str(n))
    if len(list1) == 3:
        return False
    if len(list1) == 4:
        return False
    for x in list1:
        if x == 4:
            return False
    return True
uban(25)


# ## Given a sentence, return the number of words which have the same first and last letter.
# 
# 

# In[61]:


def countsameends(str1 : str) -> int:
    withoutpunctuation = ''.join(x.lower() for x in str1 if x.isalpha() or x.isspace())
    return sum(1 if len(a) > 1 and a[0] == a[-1] else 0 for a in withoutpunctuation.split())
countsameends("Pop! goes the balloon")


# ## An almost-sorted sequence is a sequence that is strictly increasing or strictly decreasing if you remove a single element from the list (no more, no less). Write a function that returns True if a list is almost-sorted, and False otherwise. For example, if you remove 80 from the first example, it is perfectly sorted in ascending order. Similarly, if you remove 7 from the second example, it is perfectly sorted in descending order.

# In[2]:


def almostsorted(list1):
    list2 = list1[:]
    list3 = list1[:]
    list2.sort()
    list3.sort(reverse = True)
    if list1 == list2 or list1 == list3:
        return False
    for x in list1:
        list4 = list1[:]
        list4.remove(x)
        list5 = list4[:]
        list6 = list4[:]
        list5.sort()
        list6.sort(reverse = True)
        if list4 == list5:
            return True
        if list4 == list6:
            return True
    return False
almostsorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41])


# In[62]:


def isparseltongue(str1):
    str2 = str1.lower().split()
    list1 = [x for x in str2 if "s" in x]
    for a in list1:
        if a.count("ss") >= 1:
            continue
        else:
            return False
    return True
isparseltongue("Sshe ssselects to eat that apple. ")


# ## Create a dictionary using the list of keys and values: keys = ['Ten', 'Twenty', 'Thirty'] values = [10, 20, 30] and then filter out the elements with value larger than 15.

# In[13]:


dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
dict2 = {}
for k, v in dict1.items():
    if v <= 15:
        dict2[k] = v
print(dict2)


# ## Merge following two Python dictionaries into one: dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# In[15]:


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
for k, v in dict2.items():
    dict1[k] = v
print(dict1)


# ## Access the value of key ‘history’

# In[16]:


dict1 = {"class":{"student":{"name":"Mike", "marks":{"physics":70, "history":80}}}}
dict1.get('class').get('student').get('marks').get('history')


# ## Initialize dictionary with default values
# 

# In[3]:


employees = ['Kelly', 'Emma', 'John']
defaults = {"designation" : 'Application Developer', "salary" : 8000}
list1 = dict.fromkeys(employees, defaults)
print(list1)


# ## Create a new dictionary by extracting the following keys from a given dictionary

# In[5]:


dict1 = {"name" : "Kelly", "age" : 25, "salary" : 8000, "city" : "New york"}
extractkeys = ['name', 'salary']
dict2 = {}
for k, v in dict1.items():
    if k in extractkeys:
        dict2[k] = v
print(dict2)


# ## Delete set of keys from Python Dictionary

# In[6]:


dict1 = {"name" : "Kelly", "age" : 25, "salary" : 8000, "city" : "New york"}
removekeys = ["name", "salary"]
dict2 = {}
for k, v in dict1.items():
    if k not in removekeys:
        dict2[k] = v
print(dict2)


# ## Check if a value 200 exists in a dictionary

# In[12]:


dict1 = {'a': 100, 'b': 200, 'c': 300}
if 200 in dict1.values():
    print(True)
else:
    print(False)


# ## Write a function that selects all words that have all the same vowels (in any order and/or number) as the first word, including the first word.

# In[16]:


def samevowelgroup(list1):
    vowels = 'aeiou'
    v = set([i for i in list1[0] if i in vowels])
    todelete = []
    for x in range(1, len(list1)):
        for a in list1[x]:
            if a in vowels and a not in v:
                todelete.append(x)
                break
    while len(todelete) > 0:
        del list1[todelete[-1]]
        del todelete[-1]
    return list1
samevowelgroup(["toe", "ocelot", "maniac"])


# ## Rename key city to location in the following dictionary

# In[17]:


dict1 = {"name" : "Kelly", "age" : 25, "salary" : 8000, "city" : "New york"}
dict1['location'] = dict1.pop('city')
print(dict1)


# ## Get the key corresponding to the minimum value from the following dictionary

# In[21]:


dict1 = {'Physics': 82, 'Math': 65, 'history': 75}
keys = dict1.keys()
keyiterator = iter(keys)
firstkey = next(keyiterator)
for k, v in dict1.items():
    if k < firstkey:
        firstkey = k
print(firstkey)


# ## Mona has created a method to sort a list in ascending order. Starting from the left of the list, she compares numbers by pairs. If the first pair is ordered [smaller number, larger number], she moves on. If the first pair is ordered [larger number, smaller number], she swaps the two integers before moving on to the next pair. She repeats this process until she reaches the end of the list. Then, she moves back to the beginning of the list and repeats this process until the entire list is sorted. If the unsorted list is: [3, 9, 7, 4], she will perform the following steps (note Swaps here refers to cumulative swaps): She starts with the first pair. [3, 9] is in order, move on. List: [3, 9, 7, 4]. Swaps: 0. [9, 7] is not. Swap. List: [3, 7, 9, 4]. Swaps: 1 [9, 4] is not. Swap. List: [3, 7, 4, 9]. Swaps: 2 Check if list is sorted. It is not, so start over at first pair. [3, 7] is in order, move on. List: [3, 7, 4, 9]. Swaps: 2[7, 4] is not. Swap. List: [3, 4, 7, 9]. Swaps: 3. [7, 9] is in order, move on. List: [3, 4, 7, 9]. Swaps: 3. Check if list is sorted. It is. End. Sorting the list [3, 9, 7, 4] takes her 3 swaps. Write a function that takes in an unsorted list and returns the number of swaps it takes for the list to be sorted according to Mona's algorithm.
# 
# 

# In[72]:


def numberofswaps(list1):
    count = 0
    while list1 != sorted(list1):
        for x in range(len(list1) - 1):
            if list1[x] > list1[x + 1]:
                n = list1[x]
                list1[x] = list1[x + 1]
                list1[x + 1] = n
                count = count + 1
    return count
numberofswaps([5, 4, 3, 2])


# In[78]:


graph = {}
graph['A'] = ['B', 'D']
graph['B'] = ['C', 'E']
graph['C'] = ['E']
graph['D'] = []
graph['E'] = ['D']
print(graph)


# ## Write a function that groups words by the number of capital letters and returns a dictionary of object entries whose keys are the number of capital letters and the values are the groups.

# In[79]:


def grouping(list1):
    list1.sort(key = str.lower)
    groups = {}
    for x in list1:
        capitals = sum(map(str.isupper, x))
        if capitals in groups:
            groups[capitals].append(x)
        else:
            groups[capitals] = [x]
    return groups
grouping(["HaPPy", "mOOdy", "yummy", "mayBE"])


# ## Breadth-first search on a graph

# In[255]:


graph = {}
graph['You'] = ['Alice', 'Bob', 'Claire']
graph['Alice'] = ['Peggy']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Claire'] = ['Jonny', 'Thom']
graph['Peggy'] = []
graph['Anuj'] = []
graph['Jonny'] = []
graph['Thom'] = []
path = []
def ismangoseller(a):
    if a[-1] == 'm':
        return True
    return False
def bfs(starting_node):
    queue = []
    queue += graph[starting_node]
    while len(queue) != 0:
        person = queue.pop(0)
        if person not in searched:
            if ismangoseller(person) == True:
                print(person, 'is a mango seller!')
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False
bfs('You')


# In[237]:


a=[1,2,3]
a.pop(0)
print(a)


# ## Given a Python dictionary, Change Brad’s salary to 8500

# In[85]:


dict1 = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 6500}}
dict1.get('emp3')['salary'] = 8500
print(dict1)


# # Waterloo

# ## 2020-J1: Barley the dog loves treats.   At the end of the day he is either happy or sad depending on thenumber and size of treats he receives throughout the day.  The treats come in three sizes:  small,medium, and large. His happiness score can be measured using the following formula:1×S+ 2×M+ 3×LwhereSis the number of small treats,Mis the number of medium treats andLis the number oflarge treats.If Barley’s happiness score is10or greater then he is happy.  Otherwise, he is sad.  Determinewhether Barley is happy or sad at the end of the day.

# In[128]:


def dogtreats(S, M, L):
    if (S + (2 * M) + (3 * L)) >= 10:
        return('I am happy!')
    else:
        return('I am sad.')
dogtreats(1, 2, 3)


# ## 2020-J2: People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model. When a person has a disease, they infect exactly R other people but only on the very next day. No person is infected more than once. We want to determine when a total of more than P people have had the disease.

# In[166]:


def outbreakdays(p, n, r):
    if n <= 0 or r <= 0:
        return None
    else:
        x = 1
        count = 0
        old = n
        new = 0
        total = old + new
        list1 = [n]
        while total <= p:
            new = n * r ** x
            list1.append(new)
            total = sum(list1)
            x = x + 1
        return x - 1
outbreakdays(10, 2, 1)


# ## 2020-J3: Mahima has been experimenting with a new style of art. She stands in front of a canvas and, usingher brush, flicks drops of paint onto the canvas. When she thinks she has created a masterpiece,she uses her 3D printer to print a frame to surround the canvas.Your job is to help Mahima by determining the coordinates of the smallest possible rectangularframe such that each drop of paint lies inside the frame. Points on the frame are not consideredinside the frame.

# In[176]:


def art(x, list1):
    list2 = []
    list3 = []
    if len(list1) != x:
        return None
    for k, x in enumerate(list1):
        list2.append(list1[k][0])
        list3.append(list1[k][1])
        list4 = []
    coordinate1 = (min(list2) - 1, min(list3) - 1)
    coordinate2 = (max(list2) + 1, max(list3) + 1)
    list4.append(coordinate1)
    list4.append(coordinate2)
    return list4
art(5, [(44, 62), (34, 69), (24, 78), (42, 44), (64, 10)])


# ## 2019-J1: You record all of the scoring activity at a basketball game. Points are scored by a 3-point shot, a 2-point field goal, or a 1-point free throw. You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. Your job is to determine which team won, or if the game ended in a tie.

# In[239]:


def winningteam(a, b, c, d, e, f):
    if 3 * a + 2 * b + c > 3 * d + 2 * e + f:
        return('A')
    elif 3 * a + 2 * b + c < 3 * d + 2 * e + f:
        return('B')
    else:
        return('T')
winningteam(10, 3, 7, 8, 9, 6)


# ## 2018-J1: Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers where the last four digits have three properties. Looking just at the last four digits, these properties are: • the first of these four digits is an 8 or 9; • the last digit is an 8 or 9; • the second and third digits are the same. For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers. Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.

# In[264]:


def CCC(number):
    list1 = list(str(number))
    if len(list1) == 4:
        if (list1[0] == '8') or (list1[0] == '9'):
            if (list1[-1] == '8') or (list1[-1] == '9'):
                if list1[1] == list1[2]:
                    return('answer')
    return('ignore')
CCC(8995)


# ## 2020-S5: On their way to the contest grounds, Josh, his coach, and his N − 2 teammates decide to stop at a burger joint that offers M distinct burger menu items. After ordering their favourite burgers, the team members line up, with the coach in the first position and Josh last, to pick up their burgers. Unfortunately, the coach forgot what he ordered. He picks a burger at random and walks away. The other team members, in sequence, pick up their favourite burger if available, or a random remaining burger if there are no more of their favourite burger. What is the probability that Josh, being last in line, will get to eat his favourite burger?

# In[370]:


n = int(input())
str1 = input()
list1 = str1.split(' ')
m = len(list(set(list1)))
tot = len(list1)
f_coach = list1[0]
f_josh = list1[-1]
coach_count = 0
josh_count = 0
for x in list1:
    if x == list1[0]:
        coach_count += 1
    if x == list1[-1]:
        josh_count += 1
s = (coach_count/tot) + (((tot - coach_count - josh_count)/tot) * 1/2)
print(s)


# ## 2019-S4: You are planning a trip to visit N tourist attractions. The attractions are numbered from 1 to N and must be visited in this order. You can visit at most K attractions per day, and want to plan the trip to take the fewest number of days as possible. Under these constraints, you want to find a schedule that has a nice balance between the attractions visited each day. To be precise, we assign a score ai to attraction i. Given a schedule, each day is given a score equal to the maximum score of all attractions visited that day. Finally, the scores of each day are summed to give the total score of the schedule. What is the maximum possible total score of the schedule, using the fewest days possible?

# In[ ]:


'''
Sample Input
5 3
2 5 7 1 4
Output for Sample Input
12
'''


# In[44]:


str1 = input()
list1 = str1.split()
n = list1[0]
k = list1[1]
str2 = input()
attractions = str2.split()
attractions = [int(s) for s in attractions]
print(n, k, attractions)


# In[52]:





# In[62]:


import math
def create_children(a):
    m = a % max_number
    if m == 0:
        return [max_number]
    list1 = []
    for x in range(m, max_number + 1):
        list1.append(x)
    return list1
def check_termination(path):
    if len(path) == (math.ceil(n / max_number)):
        return True
    return False
n = 5
max_number = 3
attractions = [2, 5, 7, 1, 4]
list_paths = []
paths = create_children(n)
for x in paths:
    list_paths.append([x])
list_filter = []
while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    remaining_attractions = n - sum(current_path)
    paths = create_children(remaining_attractions)
    for b in paths:
        if check_termination(current_path + [b]) == True:
            list_filter.append(current_path + [b])
        else:
            list_paths.append(current_path + [b])
list_r = []
for x in list_filter:
    if sum(x) == n:
        list_r.append(x)
list_max = []
for c in list_r:
    current = 0
    s = 0
    for d in c:
        s += max(attractions[current : current + d])
        current += d
    list_max.append(s)
print(max(list_max))


# ## 2019-S3: You are given a 3 × 3 grid which contains integers. Some of the 9 elements in the grid will have a value already, and the remaining elements will be unspecified. Your task is to determine values for the unspecified elements such that each row, when read from left-to-right is an arithmetic sequence, and that each column, when read from the top-down, is an arithmetic sequence. Recall that an arithmetic sequence of length three is a sequence of integers of the form a, a + d, a + 2d for integer values of a and d. Note that d may be any integer, including zero or a negative integer.

# In[ ]:


'''
Sample Input 1
8 9 10
16 X 20
24 X 30
Output for Sample Input 1
8 9 10
16 18 20
24 27 30

Sample Input 2
14 X X
X X 18
X 16 X
Possible Output for Sample Input 2
14 20 26
18 18 18
22 16 10
'''


# In[ ]:





# In[ ]:





# In[ ]:





# ## 2017-J1: A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered from 1 to 4, as shown in the diagram below: For example, the point A, which is at coordinates (12, 5) lies in quadrant 1 since both its x and y values are positive, and point B lies in quadrant 2 since its x value is negative and its y value is positive. Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be 0.

# In[268]:


def quadrant(x, y):
    if (x == 0) or (y == 0):
        return('Invalid!')
    else:
        if x > 0:
            if y > 0:
                return(1)
            else:
                return(4)
        else:
            if y > 0:
                return(2)
            else:
                return(3)
quadrant(5, -5)


# ## 2016-J1: Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows: • if a player wins 5 or 6 games, they are placed in Group 1; • if a player wins 3 or 4 games, they are placed in Group 2; • if a player wins 1 or 2 games, they are placed in Group 3; • if a player does not win any games, they are eliminated from the tournament. Write a program to determine which group a player is placed in

# In[272]:


def groups(str1, str2, str3, str4, str5, str6):
    list1 = []
    list1.append(str1)
    list1.append(str2)
    list1.append(str2)
    list1.append(str3)
    list1.append(str4)
    list1.append(str5)
    list1.append(str6)
    count = 0
    for x in list1:
        if x == 'W':
            count = count + 1
    return count
groups('W', 'L', 'W', 'L', 'W', 'L')


# ## 2015-J1: February 18 is a special date for the CCC this year. Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18. If the date occurs before February 18, output the word Before. If the date occurs after February 18, output the word After. If the date is February 18, output the word Special.

# In[275]:


def CCCspecial(x, y):
    if (x == 2) and (y == 18):
        return('special')
    elif x <= 2:
        if x == 2:
            if y < 18:
                return('Before')
            else:
                return('After')
        else:
            return('Before')
    else:
        return('After')
CCCspecial(2, 17)


# ## 2014-J1: You have trouble remembering which type of triangle is which. You write a program to help. Your program reads in three angles (in degrees). • If all three angles are 60, output Equilateral. • If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles. • If the three angles add up to 180 and no two angles are the same, output Scalene. • If the three angles do not add up to 180, output Error.

# In[280]:


def triangles(a1, a2, a3):
    if (a1 == 60) and (a2 == 60) and (a3 == 60):
        return('Equilateral')
    elif a1 + a2 + a3 != 180:
        return('Error')
    elif (a1 == a2) or (a1 == a3) or (a2 == a3):
        return('Isosceles')
    else:
        return('Scalene')
triangles(1, 89, 90)


# ## 2013-J1: You know a family with three children. Their ages form an arithmetic sequence: the difference in ages between the middle child and youngest child is the same as the difference in ages between the oldest child and the middle child. For example, their ages could be 5, 10 and 15, since both adjacent pairs have a difference of 5 years. Given the ages of the youngest and middle children, what is the age of the oldest child?

# In[284]:


def family(x, y):
    if x > y:
        return x + x - y
    else:
        return y + y - x
family(15, 16)


# ## 2012-J1: Many communities now have “radar” signs that tell drivers what their speed is, in the hope that they will slow down. You will output a message for a “radar” sign. The message will display information to a driver based on his/her speed according to the following table:

# In[288]:


def speedlimit(speedlimit, carspeed):
    if carspeed < speedlimit:
        return('Congratulations, You are within the speed limit!')
    if speedlimit + 21 > carspeed:
        return('You are speeding and your fine is $100.')
    elif speedlimit + 31 > carspeed:
        return('You are speeding and your fine is $270.')
    else:
        return('You are speeding and your fine is $500.')
speedlimit(40, 100)


# ## 2011-J1: Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our space. A person who witnessed the appearance of the alien has come forward to describe the alien’s appearance. It is your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of, described below: • TroyMartian, who has at least 3 antenna and at most 4 eyes; • VladSaturnian, who has at most 6 antenna and at least 2 eyes; • GraemeMercurian, who has at most 2 antenna and at most 3 eyes.

# In[293]:


def alien(a, e):
    if a >= 3 and e <= 4:
        print('TroyMartian')
    if a <= 6 and e >= 2:
        print('VladSaturnian')
    if a <= 2 and e <= 3:
        print('GraemeMercurian')
    return None
alien(2, 3)


# ## 2010-J1: Natalie is learning to count on her fingers. When her Daddy tells her a number n (1 ≤ n ≤ 10), she asks “What is n, Daddy?”, by which she means “How many fingers should I hold up on each hand so that the total is n?” To make matters simple, her Daddy gives her the correct finger representation according to the following rules: • the number may be represented on one or two hands; • if the number is represented on two hands, the larger number is given first. For example, if Natalie asks “What is 4, Daddy?”, her Dad may reply: • 4 is 4. • 4 is 3 and 1. • 4 is 2 and 2. Your job is to make sure that Natalie’s Daddy gives the correct number of answers

# In[295]:


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


# In[300]:


def counting(n):
    if (n > 0) and (n < 11):
        return int((factorial(n) / (2 * (factorial(n - 2)))) / 2)
    else:
        return('Error')
counting(4)


# ## 2009-J1: The International Standard Book Number (ISBN) is a 13-digit code for identifying books. These numbers have a special property for detecting whether the number was written correctly. The 1-3-sum of a 13-digit number is calculated by multiplying the digits alternately by 1’s and 3’s (see example) and then adding the results. For example, to compute the 1-3-sum of the number 9780921418948 we add 9 ∗ 1 + 7 ∗ 3 + 8 ∗ 1 + 0 ∗ 3 + 9 ∗ 1 + 2 ∗ 3 + 1 ∗ 1 + 4 ∗ 3 + 1 ∗ 1 + 8 ∗ 3 + 9 ∗ 1 + 4 ∗ 3 + 8 ∗ 1 to get 120. The special property of an ISBN number is that its 1-3-sum is always a multiple of 10. Write a program to compute the 1-3-sum of a 13-digit number. To reduce the amount of typing, you may assume that the first ten digits will always be 9780921418, like the example above. Your program should input the last three digits and then print its 1-3-sum. Use a format similar to the samples below.

# In[372]:


def ISBN(a, b, c):
    return 91 + a + 3 * b + c
ISBN(9,4,8)


# ## 2008-J1: The Body Mass Index (BMI) is one of the calculations used by doctors to assess an adult’s health. The doctor measures the patient’s height (in metres) and weight (in kilograms), then calculates the BMI using the formula BMI = weight/height × height. Write a program which prompts for the patient’s height and weight, calculates the BMI, and displays the corresponding message from the table below.

# In[387]:


def BMI(h, w):
    if w / (h ** 2) > 25:
        return('Overweight')
    elif w / (h ** 2) < 18.5:
        return('Underweight')
    else:
        return('Normal Weight')
BMI(14, 13)


# ## 2007-J1: In the story Goldilocks and the Three Bears, each bear had a bowl of porridge to eat while sitting at his/her favourite chair. What the story didn’t tell us is that Goldilocks moved the bowls around on the table, so the bowls were not at the right seats anymore. The bowls can be sorted by weight with the lightest bowl being the Baby Bear’s bowl, the medium bowl being the Mama Bear’s bowl and the heaviest bowl being the Papa Bear’s bowl. Write a program that reads in three weights and prints out the weight of Mama Bear’s bowl. You may assume all weights are positive integers less than 100.

# In[390]:


def goldilocks_and_the_three_bears(a, b, c):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1 = sorted(list1)
    return list1[1]
goldilocks_and_the_three_bears(5,7,6)


# ## 2006-J1: At Chip’s Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice. Here are the three burger choices: Here are the three drink choices: 1 – Cheeseburger (461 Calories) 1 – Soft Drink ( 130 Calories) 2 – Fish Burger (431 Calories) 2 – Orange Juice (160 Calories) 3 – Veggie Burger (420 Calories) 3 – Milk (118 Calories) 4 – no burger 4 – no drink Here are the three side order choices: Here are the three dessert choices: 1 – Fries (100 Calories) 1 – Apple Pie (167 Calories) 2 – Baked Potato (57 Calories) 2 – Sundae (266 Calories) 3 – Chef Salad (70 Calories) 3 – Fruit Cup (75 Calories) 4 – no side order 4 – no dessert Write a program that will compute the total Calories of a meal.

# In[395]:


def Chip_fastfood(a,b,c,d):
    count = 0
    if a == 1:
        count = count + 461
    elif a == 2:
        count = count + 431
    elif a == 3:
        count = count + 420
    if b == 1:
        count = count + 130
    elif b == 2:
        count = count + 160
    elif b == 3:
        count = count + 118
    if c == 1:
        count = count + 100
    elif c == 2:
        count = count + 57
    elif c == 3:
        count = count + 70
    if d == 1:
        count = count + 167
    elif d == 2:
        count = count + 266
    elif d == 3:
        count = count + 75
    return count
Chip_fastfood(2,1,3,4)


# ## 2005-J1: Moe Bull has a cell phone and after a month of use is trying to decide which price plan is the best for his usage pattern. He has two options, each plan has different costs for daytime minutes, evening minutes and weekend minutes. Costs Plan daytime evening weekend A 100 free minutes then 25 cents per minute 15 cents per minute 20 cents per minute B 250 free minutes then 45 cents per minute 35 cents per minute 25 cents per minute Write a program that will input the number of each type of minutes and output the cheapest plan for this usage pattern, using the format shown below. The input will be in the order of daytime minutes, evening minutes and weekend minutes. In the case that the two plans are the same price, output both plans.

# In[398]:


def cellsell(m, e, w):
    if m > 100:
        am_time = (m - 100) * 25
    ae_time = 15 * m
    aw_time = 20 * w
    atotal = am_time + ae_time + aw_time
    if m > 250:
        bm_time = (m - 250) * 45
    be_time = 35 * e
    bw_time = 25 * w
    btotal = bm_time + be_time + bw_time
    if atotal > btotal:
        return('Plan B')
    elif atotal < btotal:
        return('Plan A')
    else:
        print('Plan A and')
        return('Plan B')
cellsell(251, 61, 66)


# ## 2004-J1: Gigi likes to play with squares. She has a collection of equal-sized square tiles. Gigi wants to arrange some or all of her tiles on a table to form a solid square. What is the side length of the largest possible square that Gigi can build? For example, when Gigi has 9 tiles she can use them all to build a square whose side length is 3. But when she has only 8 tiles, the largest square that she can build has side length 2. Write a program that asks the user for the number of tiles and then prints out the maximum side length. You may assume that the user will only type integers that are less than ten thousand. Once your program has read the user’s input and printed the largest square, your program stops executing. There are many different methods that your program might use to find the answer. You may use any method. For example, here is one method. First, check whether there are enough tiles to build a square of side length 1. If there are enough tiles, then move on to check the side lengths 2, 3, 4, etc., until your program finds a length that is too large.

# In[401]:


import math
def squares(n):
    return int(math.sqrt(n))
squares(7535)


# ## 2003-J1: A trident is a fork with three tines (prongs). A simple picture of a trident can be made from asterisks and spaces: * * * * * * * * * *******  *  *  *  * In this example, each tine is a vertical column of 3 asterisks. Each tine is separated by 2 spaces. The handle is a vertical column of 4 asterisks below the middle tine. Tridents of various shapes can be drawn by varying three parameters: t, the height of the tines, s, the spacing between tines, and h, the length of the handle. For the example above we have t = 3, s = 2, and h = 4. You are to write an interactive program to print a trident. Your program should accept as input the parameters t, s, and h, and print the appropriate trident. You can assume that t, s, h are each at least 0 and not larger than 10.

# In[423]:


def trident(t, s, h):
    a1 = [' '] * s
    spaces = ''.join(a1)
    b1 = '*' + spaces + '*' + spaces + '*'
    for x in range(t):
        print(b1)
    a2 = ['*'] * s
    stars = ''.join(a2)
    b2 = '*' + stars + '*' + stars + '*'
    print(b2)
    b3 = ' ' + spaces + '*' + spaces + ' '
    for x in range(h):
        print(b3)
trident(4,3,2)


# ## 2019-J3: Your new cellphone plan charges you for every character you send from your phone. Since you tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively, followed by the symbol itself. This compression technique is called run-length encoding. More formally, a block is a substring of identical symbols that is as long as possible. A block will be represented in compressed form as the length of the block followed by the symbol in that block. The encoding of a string is the representation of each block in the string in the order in which they appear in the string. Given a sequence of characters, write a program to encode them in this format. 

# In[121]:


def cellphone(str1):
    list1 = str1.split(',')
    list2 = list1[1:]
    dict1 = {}
    for x in list2:
        listunique = []
        list3 = list(x)
        for n in list3:
            if n not in listunique:
                listunique.append(n)
        str2 = ''
        for s in listunique:
            dict1[s] = list3.count(s)
            str2 = str2 + str(dict1[s]) + ' ' + s + ' '
        str2 = str2.strip()
        print(str2)
cellphone('1,AABBCC,DEF,GHI')


# ## 2018-J3: You decide to go for a very long drive on a very straight road. Along this road are five cities. As you travel, you record the distance between each pair of consecutive cities. You would like to calculate a distance table that indicates the distance between any two of the cities you have encountered. 

# In[138]:


def distance(list1, start, end):
    if start == end:
        return 0
    else:
        small = min(start, end)
        large = max(start, end)
        return sum(list1[small : large])


# In[149]:


list1 = [3, 10, 12, 5]
for x in range(5):
    list_1=[]
    for y in range(5):
        d=distance(list1, x, y)
        list_1.append(d)
    print(list_1)


# ## 2016-J3: A palindrome is a word which is the same when read forwards as it is when read backwards. For example, mom and anna are two palindromes. A word which has just one letter, such as a, is also a palindrome. Given a word, what is the longest palindrome that is contained in the word? That is, what is the longest palindrome that we can obtain, if we are allowed to delete characters from the beginning and/or the end of the string?

# In[124]:


"""
Sample Input 1
banana
Output for Sample Input 1
5
Explanation for Output for Sample Input 1
The palindrome anana has 5 letters.
Sample Input 2
abracadabra
Output for Sample Input 2
3
Explanation for Output for Sample Input 2
The palindromes aca and ada have 3 letters, and there are no other palindromes in the input
which are longer.
"""


# In[163]:


list1 = list('banana')
listofpalindromes = []
def checkifpalindrome(str1):
    if list(str1) == list(str1)[::-1]:
        return True
    return False
for start in range(len(list1)+1):
    for end in range(start+1, len(list1)+1):
        if checkifpalindrome(list1[start : end]) == True:
            listofpalindromes.append(len(list1[start : end]))
print(max(listofpalindromes))


# In[158]:


listofpalindromes


# ## 2017-J3: You live in Grid City, which is composed of integer-numbered streets which run east-west (parallel to the x-axis) and integer-numbered avenues which run north-south (parallel to the y-axis). The streets and avenues have infinite length, and there is a street for every integer y-coordinate and an avenue for every x-coordinate. All intersections are labelled by their integer coordinates: for example, avenue 7 and street -3 intersect at (7,-3).  You drive a special electric car which uses up one unit of electrical charge moving between adjacent intersections: that is, moving either north or south to the next street, or moving east or west to the next avenue). Until your battery runs out, at each intersection, your car can turn left, turn right, go straight through, or make a U-turn. You may visit the same intersection multiple times on the same trip.  Suppose you know your starting intersection, your destination intersection and the number of units of electrical charge in your battery. Determine whether you can travel from the starting intersection to the destination intersection using the charge available to you in such a way that your battery is empty when you reach your destination. 
# 

# In[ ]:


'''
Sample Input 1
3 4 
3 3 
3
Output for Sample Input 1
Y

Sample Input 2
10 2 
10 4 
5
Output for Sample Input 2
N
'''


# In[165]:


def gridcity(a,b,c,d,n):
    hi = n - (abs(c - a) + abs(d - b))
    if hi % 2 == 0:
        return 'yes'
    return 'no'
gridcity(10,2,10,4,15)


# ## 2014-J3: Antonia and David are playing a game.  Each player starts with 100 points.  The game uses standard six-sided dice and is played in rounds. During one round, each player rolls one die. The player with the lower roll loses the number of points shown on the higher die. If both players roll the same number, no points are lost by either player.  Write a program to determine the final scores. 

# In[164]:


'''
Sample Input
4 
5 6 
6 6 
4 3 
5 2
Output for Sample Input
94 
91
'''


# In[179]:


def dicegame(list1):
    p1 = 100
    p2 = 100
    for s in list1[1:]:
        if s[0]>s[1]:
            p2 = p2 - s[0]
        elif s[0] == s[1]:
            continue
        else:
            p1 = p1 - s[1]
    return((p1, p2))
dicegame([4,(5,6),(6,6),(4,3),(5,2)])


# ## 2013-J3: You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits, since the digit 2 is repeated. Given a year, what is the next year with distinct digits?

# In[ ]:


'''
Sample Input 1
1987
Output for Sample Input 1
2013
Sample Input 2
999
Output for Sample Input 2
1023
'''


# In[185]:


def isdistinct(n):
    list1 = list(str(n))
    list2 = list(set(list1))
    if len(list1) == len(list2):
        return True
    return False
isdistinct(1987)


# In[190]:


def nextyear(n):
    n = n + 1
    while isdistinct(n + 1) != True:
        n = n + 1
    return n + 1
nextyear(999)


# ## 2012-J3: You have been asked to take a small icon that appears on the screen of a smart telephone and scale it up so it looks bigger on a regular computer screen. The icon will be encoded as characters (x and *) in a 3 × 3 grid as follows. Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of k means that each character is replaced by a k × k grid consisting only of that character.

# In[ ]:


'''
Original icon:
*x*
 xx
* *

Sample Input
3
Output for Sample Input
***xxx***
***xxx***
***xxx***
xxxxxx
xxxxxx
xxxxxx
*** ***
*** ***
*** ***
'''


# In[196]:


#*x* --> ***xxx***
def repeat1(str1, k):
    list1 = list(str1)
    list2 = []
    for x in list1:
        for n in range(k):
            list2.append(x)
    str2 = ''.join(list2)
    for a in range(k):
        print(str2)
repeat1('*x*', 3)


# In[198]:


# xx -->    xxxxxx
list_input = ['*x*',' xx', '* *']
for x in list_input:
    repeat1(x, 3)


# ## 2011-J3: In a sumac sequence,t1, t2, .., tm, each term is an integer greater than or equal 0. Also, each term, starting with the third, is the difference of the preceding two terms (that is,tn+2=tn−tn+1 for n≥1). The sequence terminates attmiftm−1< tm. For example, if we have 120 and 71, then the sumac sequence generated is as follows:120,71,49,22,27.This is a sumac sequence of length 5.

# In[ ]:


'''
Sample Input
120 71
Output for Sample Input
5
'''


# In[1]:


def sumac(list1):
    while list1[-1] < list1[-2]:
        list1.append(list1[-2] - list1[-1])
    return(len(list1))
sumac([120, 71])


# ## 2019-J2: You and your friend have come up with a way to send messages back and forth. Your friend can encode a message to you by writing down a positive integer N and a symbol. You can decode that message by writing out that symbol N times in a row on one line. Given a message that your friend has encoded, decode it.

# In[ ]:


'''
Sample Input
4
9 +
3 -
12 A
2 X
Output for Sample Input
+++++++++
---
AAAAAAAAAAAA
XX
'''


# In[18]:


def duplicate(tuple1):
    list1 = [tuple1[1]] * tuple1[0]
    str1 = ''.join(list1)
    return str1


# In[20]:


def message(list1):
    list2 = list1[1:]
    for x in list2:
        print(duplicate(x))
message([4, (9, '+'), (3, '-'), (12, 'A'), (2, 'X')])


# ## 2017-J2: Suppose we have a number like 12. Let’s define shifting a number to mean adding a zero at the end. For example, if we shift that number once, we get the number 120. If we shift the number again we get the number 1200. We can shift the number as many times as we want.  In this problem you will be calculating a shifty sum, which is the sum of a number and the numbers we get by shifting. Specifically, you will be given the starting number N and a non-negative integer k. You must add together N and all the numbers you get by shifting a total of k times.  For example, the shifty sum when N is 12 and k is 1 is: 12 + 120 = 132. As another example, the shifting sum when N is 12 and k is 3 is 12+120+1200+12000=13332. 
# 

# In[ ]:


'''
Sample Input
12 3
Output for Sample Input
13332
'''


# In[2]:


def shifting(a, b):
    count = 0
    for x in range(b + 1):
        count += a
        a = a * 10
    return count
shifting(12, 3)


# ## 2016-J2: Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total. Given a 4 × 4 square of numbers, determine if it is magic square. 

# In[ ]:


'''
Sample Input 1
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Output for Sample Input 1
magic

Sample Input 2
5 10 1 3 
10 4 2 3 
1 2 8 5 
3 3 5 0
Output for Sample Input 2
not magic
'''


# In[9]:


def magicsquare(list1):
    magicnumber = sum(list1[0])
    if sum(list1[1]) != magicnumber:
        return('not magic')
    if sum(list1[2]) != magicnumber:
        return('not magic')
    if sum(list1[3]) != magicnumber:
        return('not magic')
    if list1[0][0] + list1[1][0] + list1[2][0] + list1[3][0] != magicnumber:
        return('not magic')
    if list1[0][1] + list1[1][1] + list1[2][1] + list1[3][1] != magicnumber:
        return('not magic')
    if list1[0][2] + list1[1][2] + list1[2][2] + list1[3][2] != magicnumber:
        return('not magic')
    if list1[0][3] + list1[1][3] + list1[2][3] + list1[3][3] != magicnumber:
        return('not magic')
    return('magic')
magicsquare([[16,3,2,13], [5,10,11,8], [9,6,7,12], [4,15,14,1]])


# ## 2015-J2: We often include emoticons in our text messages to indicate how we are feeling. The three consecutive characters :-) indicate a happy face and the three consecutive characters :-( indicate a sad face. Write a program to determine the overall mood of a message.  Input Specification There will be one line of input that contains between 1 and 255 characters. Output Specification The output is determined by the following rules:• If the input line does not contain any happy or sad emoticons, output none. Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure. Otherwise, if the input line contains more happy than sad emoticons, output happy. • Otherwise, if the input line contains more sad than happy emoticons, output sad.  
# 

# In[ ]:


'''
Sample Input 1
How are you :-) doing :-( today :-)?
Output for Sample Input 1
happy

Sample Input 2
:)
Output for Sample Input 2
none

Sample Input 3
This:-(is str:-(:-(ange te:-)xt.
Output for Sample Input 3
sad
'''


# In[18]:


def emoticon(str1):
    happy = ':-)'
    sad = ':-('
    list1 = list(str1)
    if str1 == happy:
        return 1
    if str1 == sad:
        return -1
    return 0


# In[22]:


str1 = 'How are you :-) doing :-( today :-)?'
list_r = []
for x in range(len(str1) - 3):
    st = str1[x:x+3]
    list_r.append(emoticon(st))
if sum(list1) > 0:
    print('happy')
elif sum(list1) < 0:
    print('sad')
else:
    print('None')


# ## 2014-J4: You have been asked by a parental unit to do your chores. Each chore takes a certain amount of time, but you may not have enough time to do all of your chores, since you can only complete one chore at a time. You can do the chores in any order that you wish.  What is the largest amount of chores you can complete in the given amount of time? 
# 

# In[ ]:


'''
Sample Input 1
6 
3 
3 
6 
3
Output for Sample Input 1
2

Sample Input 2
6 
5
5 
4 
3 
2 
1
Output for Sample Input 2
3
'''


# In[29]:


def chores(list1):
    list2 = list1[2:]
    list2 = sorted(list2)
    count = 0
    bucket = 0
    while bucket <= list1[0]:
        count += 1
        bucket += list2[0]
        list2 = list2[1:]
    return count - 1
chores([6,5,5,4,3,2,1])


# ## 2006-J2: Diana is playing a game with two dice. One die has sides labelled 1, 2, 3, ..., . The other die has sides labelled 1, 2, 3, ..., . Write a program to determine how many ways can she roll the dice to get the sum 10. For example, when the first die has 6 sides and the second die has 8 sides, there are 5 ways to get the sum 10.

# In[ ]:


'''
Sample Prompting and User Input 1 (user input in italics) 
Enter m: 6
Enter n: 8

Output for Sample 1
There are 5 ways to get the sum 10.
'''


# In[23]:


count = 0
for x in range(1,7):
    for y in range(1,9):
        if x + y == 10:
            count += 1
print(count)


# ## 2016-J5: Since time immemorial, the citizens of Dmojistan and Pegland have been at war. Now, they have finally signed a truce. They have decided to participate in a tandem bicycle ride to celebrate the truce. There are N citizens from each country. They must be assigned to pairs so that each pair contains one person from Dmojistan and one person from Pegland.  Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem bicycle while the slower person simply enjoys the ride. In other words, if the members of a pair have speeds a and b, then the bike speed of the pair is max(a, b). The total speed is the sum of the N individual bike speeds.  For this problem, in each test case, you will be asked to answer one of two questions:• Question 1: what is the minimum total speed, out of all possible assignments into pairs?  • Question 2: what is the maximum total speed, out of all possible assignments into pairs? 
# 

# In[ ]:


'''
Sample Input 1
1
3 
5 1 4 
6 2 4
Output for Sample Input 1
12

Explanation for Output for Sample Input 1
There is a unique optimal solution:
• Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 6. 
• Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 2. 
• Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.

Sample Input 2
2
3 
5 1 4 
6 2 4
Output for Sample Input 2
15
Explanation for Output for Sample Input 2
There are multiple possible optimal solutions. Here is one optimal solution:
• Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 2. 
• Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 6. 
• Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.

Sample Input 3
2
5
202 177 189 589 102
17  78  1   496 540
Output for Sample Input 3
2016

Explanation for Output for Sample Input 3
There are multiple possible optimal solutions. Here is one optimal solution:
• Pair the citizen from Dmojistan with speed 202 and the citizen from Pegland with speed 1. 
• Pair the citizen from Dmojistan with speed 177 and the citizen from Pegland with speed 540. 
• Pair the citizen from Dmojistan with speed 189 and the citizen from Pegland with speed 17. 
• Pair the citizen from Dmojistan with speed 589 and the citizen from Pegland with speed 78. 
• PairthecitizenfromDmojistanwithspeed102andthecitizenfromPeglandwithspeed496.
This sum yields 202 + 540 + 189 + 589 + 496 = 2016.
'''


# In[87]:


def truce(n):
    lista = [12, 34, 8, 99, 45]
    listb = [78, 13, 92, 9, 254]
    list2 = []
    if n == 1:
        while len(lista) > 0 and len(listb) > 0:
            if max(lista) > max(listb):
                a = lista.index(max(lista))
                b = listb.index(min(listb))
                list2.append(lista.pop(a))
                listb.pop(b)
            else:
                a = lista.index(min(lista))
                b = listb.index(max(listb))
                list2.append(listb.pop(b))
                lista.pop(a)
        return sum(list2)
    elif n == 2:
        count = 0
        while len(lista) > 0 and len(listb) > 0:
            if max(lista) > max(listb):
                a = lista.index(max(lista))
                b = listb.index(max(listb))
                list2.append(lista.pop(a))
                listb.pop(b)
            else:
                a = lista.index(max(lista))
                b = listb.index(max(listb))
                list2.append(listb.pop(b))
                lista.pop(a)
        return sum(list2)
    else:
        return('Invalid!')
truce(1)


# In[ ]:


'''
list_1 = [69, 34, 12, 78, 89, 120]
list_2 = ['A', 'B', 'B', 'A', 'A', 'B'] # team
question: find the max and min of list_1, and the corresponding team in list_2
'''


# In[40]:


list_1 = [69, 34, 12, 78, 89, 120]
list_2 = ['A', 'B', 'B', 'A', 'A', 'B']
index = list_1.index(max(list_1))
print(max(list_1))
print(list_2[index])
index = list_1.index(min(list_1))
print(min(list_1))
print(list_2[index])


# ### Question: list_a = [12, 34, 8, 99, 45] # team-A, list_b=[78, 13, 92, 9, 254] # team-B, do the folowing to make pair: 1) each pair has one from team-A and another one from team-B, 2) always pick the largest element from team-A and B, and then find the smallest element from the other team.

# In[ ]:


'''
1st round: pick 254 from team-B, because it the largest element, and then pick 12 from team-A to pair with it
2rd round: pick 99 from team-A, because it is the largest element among the unpaired elements, and then pick 9 to pair with it
'''


# In[60]:


lista = [12, 34, 8, 99, 45]
listb = [78, 13, 92, 9, 254]
count = 0
while len(lista) > 0 and len(listb) > 0:
    if max(lista) > max(listb):
        a = lista.index(max(lista))
        b = listb.index(min(listb))
        count += lista.pop(a)
        listb.pop(b)
    else:
        a = lista.index(min(lista))
        b = listb.index(max(listb))
        count += listb.pop(b)
        lista.pop(a)
print(count)


# ### Question: list_a = [12, 34, 8, 99, 45] # team-A, list_b=[78, 13, 92, 9, 254] # team-B, do the folowing to make pair: 1) each pair has one from team-A and another one from team-B, 2) always pick the largest element from team-A and B, and then find the largest element from the other team.

# In[62]:


lista = [12, 34, 8, 99, 45]
listb = [78, 13, 92, 9, 254]
count = 0
while len(lista) > 0 and len(listb) > 0:
    if max(lista) > max(listb):
        a = lista.index(max(lista))
        b = listb.index(max(listb))
        count += lista.pop(a)
        listb.pop(b)
    else:
        a = lista.index(max(lista))
        b = listb.index(max(listb))
        count += listb.pop(b)
        lista.pop(a)
print(count)


# ## Knacksack problem: A thief with a knacksack at a store wants to maximize the value that can be put into his knacksack. Suppose his knacksack can hold 50 kg of items, and the list of items in the store is: list_items = ['A', 'B', 'C', 'D', 'E', 'F', 'G'], their values are: list_values = [120, 230, 340, 89, 270, 10, 49], and their weights are: list_weights = [18, 28, 31, 9, 13, 9, 17]. Find the items to be taken by the thief using greedy algorithm

# In[79]:


# greedy
bucket = 50
list_items = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
list_values = [120, 230, 340, 89, 270, 10, 49]
list_weights = [18, 28, 31, 9, 13, 9, 17]
while list_items:
    greed = max(list_values)
    index = list_values.index(max(list_values))
    if list_weights[index] <= bucket:
        print(list_items[index])
        bucket -= list_weights[index]
    list_items.pop(index)
    list_values.pop(index)
    list_weights.pop(index)


# ## 2009-J2:  Fishing habitat and fish species are a resource that must be carefully managed to ensure that they will be there for the future. Accordingly, fishing limits have been established for a particular river based on the population of each species. Specifically, points are associated with the fish caught and the total points you catch must be less than or equal to the points allowed for that river. As an example, suppose each brown trout counts as 2 points, each northern pike counts as 5 points and each yellow pickerel counts as 2 points, and the total points allowed must be less than or equal to 12. One acceptable catch could consist of 3 brown trout and 1 northern pike, but, other combinations would also be allowed. Your job is to write a program to input the points allocated for a river, and find how many different ways an angler who catches at least one fish can stay within his/her limit.

# In[ ]:


'''
Input Description
You will be given 4 integers, one per line, representing trout points, pike points, pickerel points, and 
total points allowed in that order.

Sample Input
1 2 3 2
Sample Output
1 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
2 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
0 Brown Trout, 1 Northern Pike, 0 Yellow Pickerel
Number of ways to catch fish: 3
'''


# In[91]:


a = 1
b = 2
c = 3
count = 0
points = 2
for x in range((points // a) + 1):
    for y in range((points // b) + 1):
        for z in range((points // c) + 1):
            if a*x + b*y + c*z <= points:
                count += 1
print(count - 1)


# ## 2014-J4: You are hosting a party and do not have room to invite all of your friends. You use the following unemotional mathematical method to determine which friends to invite.  Number your friends 1, 2, . . . , K and place them in a list in this order. Then perform m rounds. In each round, use a number to determine which friends to remove from the ordered list.  The rounds will use numbers r1, r2, . . . , rm. In round i remove all the remaining people in positions that are multiples of ri (that is, ri, 2ri, 3ri, . . .) The beginning of the list is position 1.  Output the numbers of the friends that remain after this removal process. 
# 

# In[ ]:


'''
Sample Input
10 2 2 3
Output for Sample Input
1 3 7 9

Explanation of Output for Sample Input
Initially, our list of invitees is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
After the first round of removals, we remove the even positions 
(i.e., every second position), which causes our list of invitees to be 1, 3, 5, 7, 9. 
After the second round of removals, we remove every 3rd remaining invitee: thus, 
we keep 1 and 3, remove 5 and keep 7 and 9, which leaves us with an invitee list of 1, 3, 7, 9.
'''


# In[103]:


def party(list1):
    n = list1[0]
    list1 = list1[1:]
    list2 = []
    for x in range(1, n + 1):
        list2.append(x)
    print(list2)
    for a in range(1, n // 2 + 1, list1[0]):
        print(a)
        list2.pop(a)
    for b in range(1, (n + 1) // 2 + 1, list1[1]):
        print(b)
        list2.pop(b)
    return list2
party([10,2,3])


# ## Assignment for 07-23-2020, questions 4-6 from pynative.com
# https://pynative.com/python-numpy-exercise/

# ## Question 4: Following is the given numpy array return array of odd rows and even columns

# In[184]:


a = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print(a[[0,2,4]][:,[1,3]])


# ## Question 5: Add the following two NumPy arrays and Modify a result array by calculating the square of each element

# In[187]:


a = np.array([[5, 6, 9], [21 ,18, 27]])
b = np.array([[15 ,33, 24], [4 ,7, 1]])
a += b
print(a + b)
a = a ** 2
print(a)


# ## Question 6: Split the array into four equal-sized sub-arrays

# In[205]:


a = np.arange(10, 34)
a = np.array_split(a,4)
print(a)


# ## Assignment for 07-24-2020, questions 7-9 from pynative.com¶
# 
# https://pynative.com/python-numpy-exercise/
# 

# ## Question 7: Sort following NumPy array

# In[219]:


a = np.array([[34,43,73],[82,22,12],[53,94,66]])
row = a[:, a[1,:].argsort()]
column = a[a[:,1].argsort()]
print(row)
print('------------')
print(column)


# ## Question 8: Following is the 2-D array. Print max from axis 0 and min from axis 1

# In[222]:


a = np.array([[34,43,73],[82,22,12],[53,94,66]])
minimum = np.amin(a, 1)
maximum = np.amax(a, 0) 
print(minimum)
print('----------')
print(minimum)


# ## Question 9: Following is the input NumPy array delete column two and insert following new column in its place.

# In[237]:


a = np.array([[34,43,73],[82,22,12],[53,94,66]])
column = numpy.array([10,10,10])
a = np.delete(a, 1, axis = 1)
print('deletion:')
print(a)
a = np.insert(a, 1, column, axis = 1) 
print('insertion:')
print(a)


# ## 2018-J4: Barbara plants N different sunflowers, each with a unique height, ordered from smallest to largest, and records their heights for N consecutive days. Each day, all of her flowers grow taller than they were the day before. She records each of these measurements in a table, with one row for each plant, with the first row recording the shortest sunflower’s growth and the last row recording the tallest sunflower’s growth. The leftmost column is the first measurement for each sunflower, and the rightmost column is the last measurement for each sunflower. If a sunflower was smaller than another when initially planted, it remains smaller for every measurement. Unfortunately, her children may have altered her measurements by rotating her table by a multiple of 90 degrees. Your job is to help Barbara determine her original data. 

# In[259]:


def plants(n, a):
    small = np.amin(a, axis = None, out = None)
    if small == a[0,n - 1]:
        a = np.rot90(a,1)
    if small == a[n - 1,0]:
        a = np.rot90(a,1)
        a = np.rot90(a,1)
        a = np.rot90(a,1)
    if small == a[n - 1,n - 1]:
        a = np.rot90(a,1)
        a = np.rot90(a,1)
    return a
plants(3, a)


# ## 2014-J4: You are trying to pass the time while at the optometrist. You notice there is a grid of four numbers: You see lots of mirrors and lenses at the optometrist, and wonder how flipping the grid horizontally or vertically would change the grid. Specifically, a “horizontal” flip (across the horizontal centre line) would take the original grid of four numbers and result in: A “vertical” flip (across the vertical centre line) would take the original grid of four numbers and result in: Your task is to determine the final orientation of the numbers in the grid after a sequence of horizontal and vertical flips. 
# 

# In[261]:


def waiting(str1):
    list1 = list(str1)
    for x in list1:
        if x == 'H':
            m = np.array([[1,2], [3,4]])
            row1 = m[0, :]
            row2 = m[1, :]
            m2 = np.zeros(m.shape, dtype = int)
            m2[0, :] = row2
            m2[1, :] = row1
        if x == 'V':
            m = np.array([[1,2], [3,4]])
            col1 = m[:, 0]
            col2 = m[:, 1]
            m2 = np.zeros(m.shape, dtype = int)
            m2[:, 0] = col2
            m2[:, 1] = col1
    return m2
waiting('HV')


# ## 2014-J5: The CEMC is organizing a workshop with an activity involving pairs of students. They decided to assign partners ahead of time. You need to determine if they did this consistently. That is, whenever A is a partner of B, then B is also a partner of A, and no one is a partner of themselves. 
# 

# In[277]:


def cemc(n, list1):
    if n % 2 == 1:
        return 'bad'
    list2 = []
    for x in list1:
        list2.append(tuple(sorted(x)))
    set1 = set(list2)
    list3 = list(set1)
    if len(list2) / len(list3) == 2.0:
        return 'good'
    return 'bad'
cemc(4, [('Ada', 'John'), ('Alan', 'Grace'), ('Grace', 'Alan'), ('John', 'Ada')])


# ## 2016-J4: Fiona commutes to work each day. If there is no rush-hour traffic, her commute time is 2 hours. However, there is often rush-hour traffic. Specifically, rush-hour traffic occurs from 07:00 (7am) until 10:00 (10am) in the morning and 15:00 (3pm) until 19:00 (7pm) in the afternoon. During rush-hour traffic, her speed is reduced by half. She leaves either on the hour (at XX:00), 20 minutes past the hour (at XX:20), or 40 minutes past the hour (at XX:40). Given Fiona’s departure time, at what time does she arrive at work? 
# 

# In[282]:


def rushhour(flo1):
    if flo1 >= 10.0 and flo1 <= 13.0:
        return flo1 + 2.0
    else:
        if flo1 <= 5.0:
            return flo1 + 2.0
        elif flo1 >= 19.0:
            return flo1 + 2.0
        else:
            if flo1 > 5.0 and flo1 < 10.0:
                t1 = 10.0 - flo1
                t2 = 2.0 - t1 / 2
                return flo1 + t1 + t2
            if flo1 > 13.0 and flo1 < 19.0:
                t2 = 15.0 - flo1
                t1 = 4.0 - 2 * t2
                print(t1)
                print(t2)
                return flo1 + t1 + t2
rushhour(14.75)


# ## Interger allocation problem-1: a thief in a store with a knapsack of capacity of 10 lb can select: 1) iphones (value at 1000, weight at 2 lb), 2) ipad (value at 1500, weight at 4 lb), 3) laptop (value at 3000, weight at 5 lb). How many iphones/ipads/laptops can he pick to maximize the total values of items stored in the knapsack?

# In[291]:


list_results = []
for a in range(10 // 2 + 1):
    for b in range(10 // 4 + 1):
        for c in range(10 // 5 + 1):
            tot_value = 1000 * a + 1500 * b + 3000 * c
            tot_weight = 2 * a + 4 * b + 5 * c 
            if tot_weight <= 10:
                    list_results.append(tot_value)
print(max(list_results))


# ## Interger allocation problem-2: a thief in a store with a knapsack of capacity of 20 lb can select: 1) iphones (weight at 2 lb), 2) ipad (weight at 4 lb), 3) laptop (weight at 5 lb). He need to pick each item at least one. How many ways can he choose the items into the knapsack? 

# In[300]:


list_results = []
for a in range(1, 20 // 2 + 1):
    for b in range(1, 20 // 4 + 1):
        for c in range(1, 20 // 5 + 1):
            tot_weight = 2 * a + 4 * b + 5 * c 
            if tot_weight <= 20:
                    list_results.append((a,b,c))
print(len(list_results))


# ## 2015-J5: You may know that March 14 is known as “π-day”, since 3.14 (which is the third month and fourteenth day) is a good approximation of π.  Mathematicians celebrate this day by eating pie.  Suppose that you have n pieces of pie, and k people who are lined up for pieces of pie. All n pieces of pie will be given out. Each person will get at least one piece of pie, but mathematicians are a bit greedy at times. So, they always get at least as many of pieces of pie as the person in front of them.  For example, if you have 8 pieces of pie and 4 people in line, you could give out pieces of pie in the following five ways (with the first person in line being the first number in the list): [1, 1, 1, 5], [1,1,2,4], [1,1,3,3], [1,2,2,3], [2,2,2,2].  Notice that if k = n, there is only one way to give out the pieces of pie: every person gets exactly one piece. Also, if k = 1, there is only one way to give out the pieces of pie: that single person gets all the pieces.  Write a program that determines the number of ways that the pieces of pie can be given out. 

# In[ ]:


'''
Sample Input 1
8 
4
Output for Sample Input 1
5
Sample Input 2
6 2
Output for Sample Input 2
3
'''


# In[319]:


list1 = []
for a in range(1, 8):
    for b in range(a, 8):
        for c in range(b, 8):
            for d in range(c, 8):
                if a + b + c + d == 8:
                    list1.append(a)
                    list1.append(b)
                    list1.append(c)
                    list1.append(d)
print(len(list1) // 4)


# ## Interger allocation problem-3: a thief in a store with a knapsack of capacity of 50 lb can select: 1) iphones (value at 1000, weight at 2 lb), 2) ipad (value at 1500, weight at 4 lb), 3) laptop (value at 3000, weight at 5 lb). The thief needs to pick the same number of iphones and ipads. How many iphones/ipads/laptops can he pick to maximize the total values of items stored in the knapsack?

# In[304]:


list_results = []
for a in range(1, 50 // 2 + 1):
        for c in range(1, 50 // 5 + 1):
            tot_value = 1000 * a + 1500 * a + 3000 * c
            tot_weight = 2 * a + 4 * a + 5 * c
            if a > 0 and c > 0:
                if tot_weight <= 50:
                        list_results.append(tot_value)
print(max(list_results))


# ## 2012-J4: Sheldon and Leonard are physicists who are fixated on the BIG BANG theory. In order to exchange secret insights they have devised a code that encodes UPPERCASE words by shifting their letters forward.Shifting a letter by S positions means to go forward S letters in the alphabet. For example, shifting B by S = 3 positions gives E. However, sometimes this makes us go past Z, the last letter of the alphabet. Whenever this happens we wrap around, treating A as the letter that follows Z. For example, shifting Z by S = 2 positions gives B.Sheldon and Leonard’s code depends on a parameter K and also varies depending on the position of each letter in the word. For the letter at position P , they use the shift value of S = 3P + K .For example, here is how ZOOM is encoded when K = 3. The first letter Z has a shift value of S = 3 × 1 + 3 = 6; it wraps around and becomes the letter F. The second letter, O, has S = 3×2+3 = 9andbecomesX.ThelasttwolettersbecomeAandB.SoSheldonsends Leonard the secret message: FXAB Write a program for Leonard that will decode messages sent by Sheldon.

# In[ ]:


'''
Sample Input 1
3 FXAB
Output for Sample Input 1
ZOOM

Sample Input 2
5 JTUSUKG
Output for Sample Input 2
BIGBANG
'''


# In[323]:


def code(k, word):
    list1 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    list2 = list(word)
    list3 = []
    for p, x in enumerate(list2):
        index = list1.index(x)
        a = list1[index - (3 * (p + 1) + k)]
        list3.append(a)
    return ''.join(list3)
code(3, 'FXAB')


# ## 2009-J4: The student council at Central Canada Collegiate is preparing signs with the message WELCOME TO CCC GOOD LUCK TODAY on various walls around the school. A sign is wide enough to hold w characters on each row, including spaces, as befits the wall to be decorated.  Here is how the words are put onto a sign. First, as many words as possible are placed on the first line, without exceeding the w character limit. The first word in the line begins in the leftmost position. If there is more than one word in the line, the last word ends in the rightmost position. Extra spaces are inserted into the gaps between the words so that the gaps are as similar as possible. If the gaps cannot be made equal, all of the larger gaps should appear to the left of the smaller ones. Subsequent lines are constructed in the same way.  Your program will read the available width w and output the sign on the screen. Use the “.” character to indicate a space. 

# In[ ]:


'''
Sample Input 1 (user inputs are shown in italics)
Enter w: 15
Output for Sample Input 1
WELCOME..TO.CCC
GOOD.LUCK.TODAY

Sample Input 2 (user inputs are shown in italics) Enter w: 26
Output for Sample Input 2
WELCOME..TO..CCC.GOOD.LUCK
TODAY.....................
'''


# In[ ]:





# ## Line assigment: Assign the sentence "WELCOME TO CCC GOOD LUCK TODAY" to multiple lines, each line can hold up to 15 characters, a word cannot separated into two lines, at least a space is needed between words

# In[337]:


str1 = 'WELCOME TO CCC GOOD LUCK TODAY'
list1 = str1.split(' ')
list1 = [len(s) for s in list1]
count = 0
list2 = []
list3 = []
for x in list1:
    if (count + x) <= 15:
        count += x
        list2.append(x)
        if list1.index(x) == 0:
            continue
        else:
            count += 1
print(list2)
for a in list2:
    if a in list1:
        list3.append(x)
print(list3)


# ## Integer allocation problem: allocate 27 apples to students A, B, C, D as even as possible, and x_A>=x_B>=x_C>=x_D. 

# In[352]:


list1 = []
for d in range(1,27):
    for c in range(1,27):
        for b in range(1,27):
            for a in range(1,27):
                if (a + b + c + d) == 27:
                    list1.append([a,b,c,d])
product = 1
me = 0
ind = 0
for k,x in enumerate(list1):
    for y in x:
        product *= y
    if product > me:
        me = product
        ind = k
    product = 1
print(list1[ind])


# ## Write a program to count the number of bits that are set to 1 in a positive integer

# In[354]:


count = 0
str1 = bin(11)
list1 = list(str1)
for x in list1:
    if x == '1':
        count += 1
print(count)


# ## 2020-J4: Thuc likes finding cyclic shifts of strings. A cyclic shift of a string is obtained by moving characters from the beginning of the string to the end of the string. We also consider a string to be a cyclic shift of itself. For example, the cyclic shifts of ABCDE are: ABCDE, BCDEA, CDEAB, DEABC, and EABCD. Given some text, T, and a string, S, determine if T contains a cyclic shift of S.

# In[ ]:


'''
Sample Input 1
ABCCDEABAA
ABCDE
Output for Sample Input 1
yes
Explanation of Output for Sample Input 1
CDEAB is a cyclic shift of ABCDE and it is contained in the text ABCCDEABAA.

Sample Input 2
ABCDDEBCAB
ABA
Output for Sample Input 2
no
Explanation of Output for Sample Input 2
The cyclic shifts of ABA are ABA, BAA, and AAB. None of these shifts are contained in the text ABCDDEBCAB.
'''


# In[365]:


str11='ABCCDEABAA'
str12=str11[0:5]
print(str12)


# In[369]:


def cyclic(str1, str2):
    #'ABAABA'
    str_a = str2+str2
    for k in range(0,len(str1) - len(str2)):
        
        str3 = str1[k : k + len(str2)]
        if len(str3) == len(str2) and str3 in str_a:
            return 'yes'
    return 'no'
cyclic('ABCCDEABAA', 'ABCDE')


# ## Tree-traverse-algorithm: : start from 0, create a tree such that each node has children (n+1, n+2), all children need to be less than 4. Print all paths.

# In[40]:


def nextlevel(list1):
    list_2 = []
    a = list1[-1]
    c1 = a + 1
    c2 = a + 2
    if c1 >= 4:
        list_2 = [list1+['#']]
    elif c2 >= 4:
        list_2 = [list1+[c1]]
    else:
        list_2 = [list1+[c1], list1+[c2]]
    return list_2


# In[44]:


def terminated(list1):
    list2 = []
    count = 0
    for x in list1:
        list2.append(x[-1])
    for x in list2:
        if x == '#':
            count += 1
    if len(list2) == count:
        return True
    return False


# In[45]:


listpaths = [[0]]
while terminated(listpaths) == False:
    a = listpaths.pop(0)
    b = nextlevel(a)
    listpaths = listpaths + b
print(listpaths)


# ## 2020-J5: You have to determine if it is possible to escape from a room. The room is an M-by-N grid with each position (cell) containing a positive integer. The rows are numbered 1,2,...,M and the columns are numbered 1,2,...,N. We use (r,c) to refer to the cell in row r and column c. You start in the top-left corner at (1,1) and exit from the bottom-right corner at (M,N). If you are in a cell containing the value x, then you can jump to any cell (a, b) satisfying a × b = x. For example, if you are in a cell containing a 6, you can jump to cell (2, 3). Note that from a cell containing a 6, there are up to four cells you can jump to: (2, 3), (3, 2), (1, 6), or (6, 1). If the room is a 5-by-6 grid, there isn’t a row 6 so only the first three jumps would be possible.

# In[ ]:


'''
Sample Input
3
4
3 10 8 14 
1 11 12 12 
6 2  3  9
Output for Sample Input
yes

Explanation of Output for Sample Input
Starting in the cell at (1, 1) which contains a 3, one possibility is to jump to the cell at (1, 3). 
This cell contains an 8 so from it, you could jump to the cell at (2, 4). 
This brings you to a cell containing 12 from which you can jump to the exit at (3, 4). 
Note that another way to escape is to jump from the starting cell to the cell at (3, 1) to 
the cell at (2, 3) to the exit.
'''


# In[76]:


def createchildren(list_1, matrix):
    list_r = []
    row_b = len(matrix)
    col_b = len(matrix[0])
    a = list_1[-1]
    row = a[0] - 1
    col = a[1] - 1
    e = matrix[row][col]
    for x in range(1, e + 1):
        if e % x == 0:
            r = x
            c = e // r
            if (r <= row_b) and (c <= col_b) and ((r,c) not in list_1):
                list_r.append(list_1 + [(r,c)]) 
    return list_r
createchildren([(1, 1), (1, 3)], matrix)


# In[77]:


def escape(matrix,listpaths):
    while listpaths != []:
        a = listpaths.pop(0)
        b = createchildren(a, matrix)
        if len(b) > 0:
            for x in b:
                if x[-1] == (3,4):
                    return('yes')
            listpaths += b
    return('no')
matrix = [[3, 10, 1, 14], [1, 11, 12, 12],  [1, 2,  3,  9]]
listpaths = [[(1,1)]]
escape(matrix,listpaths)


# ## 2019-J5: A substitution rule describes how to take a sequence of symbols and convert it into a different sequence of symbols. For example, ABA → BBB, is a substitution rule which means that ABA can be replaced with BBB. Using this rule, the sequence AABAA would be transformed into the sequence ABBBA (the substituted symbols are in bold).  In this task, you will be given three substitution rules, a starting sequence of symbols and a final sequence of symbols. You are to use the substitution rules to convert the starting sequence into the final sequence, using a specified number of substitutions.  For example, if the three substitution rules were:  1. AA→AB      2. AB→BB         3. B → AA  we could convert the sequence AB into AAAB in 4 steps, by the following substitutions:  AB → BB → AAB → AAAA → AAAB, 

# In[91]:


'''
Sample Input
AA AB
AB BB
B AA
4 AB AAAB

output:
AB → BB → BAA → BAB → AAAB
'''


# In[95]:


dict_rules = {'AA': 'AB',
             'AB': 'BB',
             'B': 'AA'}


# In[143]:


listpaths = [['AB']]
def create_children(path, dict_rules):
    list_result = []
    #rule-1
    a = path[-1]
    for key, value in dict_rules.items():
        if key in a:
            b = a.replace(key, value, 1)
            list_result.append(path + [b])
    return(list_result)
create_children(path,dict_rules)


# In[145]:


def rules(dict_rules, list_paths):
    loop = True
    while loop:
        a = list_paths.pop(0)
        b = create_children(a, dict_rules)
        for s in b:
            if s[-1]=='AAAB':
                return(s)
        list_paths += b
        list_counts = []
        for s in list_paths:
            list_counts.append(len(s))
        list_c = [1 if s == 5 else 0 for s in list_counts]
        if sum(list_c) == len(list_c):
            return 'no'
rules(dict_rules, listpaths)


# ## 2018-J5: There is a genre of fiction called choose your own adventure books. These books allow the reader to make choices for the characters which alters the outcome of the story. For example, after reading the first page of a book, the reader may be asked a choice, such as “Do you pick up the rock?” If the reader answers “yes”, they are directed to continue reading on page 47, and if they choose “no”, they are directed to continue reading on page 18. On each of those pages, they have further choices, and so on, throughout the book. Some pages do not have any choices, and thus these are the “ending” pages of that version of the story. There may be many such ending pages in the book, some of which are good (e.g., the hero finds treasure) and others which are not (e.g., the hero finds a leftover sandwich from 2001). You are the editor of one of these books, and you must examine two features of the choose your own adventure book: 1. ensure that every page can be reached – otherwise, there is no reason to pay to print a page which no one can ever read; 2. find the shortest path, so that readers will know what the shortest amount of time they need to finish one version of the story. Given a description of the book, examine these two features.

# In[ ]:


'''
Sample Input 1
3 
2 2 3 
0
0
Output for Sample Input 1
Y 
2
Explanation of Output for Sample Input 1
Since we start on page 1, and can reach both page 2 and page 3, all pages are reachable. 
The only paths in the book are 1 → 2 and 1 → 3, each of which is 2 pages in length.

Sample Input 2
3 
2 2 3 
0
1 1
Output for Sample Input 2
Y 
2
Explanation of Output for Sample Input 2
Every page is reachable, since from page 1, we can reach pages 2 and 3. 
The shortest path is the path 1 → 2, which contains two pages.
'''


# ## Question: Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

# In[ ]:


'''
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''


# In[150]:


str1 = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
dict1 = {}
list1 = str1.split(' ')
for x in list1:
    count = list1.count(x)
    dict1[x] = count
print(dict1)


# ## Dynamic programming: write a function to find Fib(n) using recursive dynamic programming and bottom-up dynamic programming

# In[175]:


def fibdynamic(n, memo):
    for x in range(n):
        memo.append('null')
    if memo[n - 1] != 'null':
        return memo[n - 1]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibdynamic(n - 1, memo) + fibdynamic(n - 2, memo)
    memo[n - 1] = result
    return result
fibdynamic(40, memo)


# In[176]:


def bottomup(n):
    if n == 1 or n == 2:
        return 1
    bottomup = [None] * (n + 1)
    bottomup[1] = 1
    bottomup[2] = 2
    for x in range(3, n + 1):
        bottomup[x] = bottomup[x - 1] + bottomup[x - 2]
    return bottomup[n - 1]
bottomup(400)


# ## Dynamic Programming: rod cutting. Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
# #### length   | 1   2   3   4   5   6   7   8  inches
# #### price    | 1   5   8   9  10  17  17  20

# In[215]:


prices=[1,  5,   8,   9,  10,  17,  17,  20, 25]
n = 8 # rod length
# bottom-up dynamic programming

# initialization
dict_max_values = {} # a dict to store the max value for k-inch rod
dict_max_values[0] = {}
dict_max_values[0]['max_value'] = 0
dict_max_values[0]['list_cuts'] = []
# find the max value and the list of cuts for 1-inch rod
curr_seg = 1
prev_seg = curr_seg - 1
curr_value = prices[curr_seg - 1] + dict_max_values[prev_seg]['max_value']
dict_max_values[curr_seg] = {}
dict_max_values[curr_seg]['max_value'] = curr_value
dict_max_values[curr_seg]['list_cuts'] = dict_max_values[0]['list_cuts'] + [curr_seg]
print(dict_max_values)


# In[210]:


# # find the max value and the list of cuts for 2-inch rod using the previous results
# # loop over different previous-seg-length of [0, 1]
# tot_len = 2
# list_values = []
# for pre_seg_len in range(0, tot_len):
#     cur_seg_len = tot_len - pre_seg_len
#     tot_value = prices[cur_seg_len - 1] + dict_max_values[pre_seg_len]['max_value']
#     list_values.append(tot_value)
# max_value = max(list_values)
# opt_prev_seg_len = list_values.index(max_value)
# dict_max_values[tot_len] = {}
# dict_max_values[tot_len]['max_value'] = max_value 
# dict_max_values[tot_len]['list_cuts'] = dict_max_values[opt_prev_seg_len]['list_cuts'] + [tot_len - opt_prev_seg_len]
# print(dict_max_values)


# In[214]:


for tot_len in range(2,9):
    list_values = []
    for pre_seg_len in range(0, tot_len):
        cur_seg_len = tot_len - pre_seg_len
        tot_value = prices[cur_seg_len - 1] + dict_max_values[pre_seg_len]['max_value']
        list_values.append(tot_value)
    max_value = max(list_values)
    opt_prev_seg_len = list_values.index(max_value)
    dict_max_values[tot_len] = {}
    dict_max_values[tot_len]['max_value'] = max_value 
    dict_max_values[tot_len]['list_cuts'] = dict_max_values[opt_prev_seg_len]['list_cuts'] + [tot_len - opt_prev_seg_len]
print(dict_max_values)


# ## 2017-J4: Wendy has an LED clock radio, which is a 12-hour clock, displaying times from 12:00 to 11:59. The hours do not have leading zeros but minutes may have leading zeros, such as 2:07 or 11:03.  When looking at her LED clock radio, Wendy likes to spot arithmetic sequences in the digits. For example, the times 12:34 and 2:46 are some of her favourite times, since the digits form an arithmetic sequence.  A sequence of digits is an arithmetic sequence if each digit after the first digit is obtained by adding a constant common difference. For example, 1,2,3,4 is an arithmetic sequence with a common difference of 1, and 2,4,6 is an arithmetic sequence with a common difference of 2.  Suppose that we start looking at the clock at noon (that is, when it reads 12:00) and watch the clock for some number of minutes. How many instances are there such that the time displayed on the clock has the property that the digits form an arithmetic sequence? 
# 

# In[ ]:


'''
Sample Input 1
34
Output for Sample Input 1
1
Explanation of Output for Sample Input 1
Between 12:00 and 12:34, there is only the time 12:34 for which the digits form an arithmetic sequence.

Sample Input 2
180
Output for Sample Input 2
11
Explanation of Output for Sample Input 2
Between 12:00 and 3:00, the following times form arithmetic sequences in their digits (with the difference shown:
• 12:34 (difference 1), 
• 1:11 (difference 0), 
• 1:23 (difference 1), 
• 1:35 (difference 2), 
• 1:47 (difference 3), 
• 1:59 (difference 4), 
• 2:10 (difference -1), 
• 2:22 (difference 0), 
• 2:34 (difference 1), 
• 2:46 (difference 2), 
• 2:58 (difference 3).
'''


# In[241]:


def arithmetic_sequence(list1):
    list_diff = [list1[k]-list1[k-1] for k in range(1, len(list1))]
    list_diff2 = [list_diff[0]] * len(list_diff)
    if list_diff == list_diff2:
        return True
    return False
arithmetic_sequence([-5 ,0, 5, 10, 14, 20])


# In[256]:


def clock(n):
    hrs = n//60
    mins = n - hrs * 60
    list_hrs = [12]+list(range(1, hrs+1))
    list_results = []
    for k, h in enumerate(list_hrs):
        list_s = []
        if h>=10:
            list_s.append(h//10)
            list_s.append(h%10)
        else:
            list_s.append(h)
        # loop over min
        if k<len(list_hrs)-1:
            end_mins = 60
        else:
            end_mins = mins
        for m in range(end_mins):
            list_m = []
            if m>=10:
                list_m.append(m//10)
                list_m.append(m%10)
            else:
                list_m.append(0)
                list_m.append(m) 
            a=arithmetic_sequence(list_s+list_m)
            if a:
                list_results.append(list_s+list_m)
    return list_results
clock(240)


# ## GeeksForGeeks Q1: Maximum LCM among all pairs (i, j) from the given ArrayGiven an array arr[], the task is to find the maximum LCM when the elements of the array are taken in pairs.
# 

# In[264]:


def lcm(a,b):
    c = max(a,b)
    while True:
        if c % a == 0 and c % b == 0:
            return c
        c += 1
lcm(8,17)


# In[267]:


list1 = [17, 3, 8, 6]
list2 = []
for k, x in enumerate(list1[:-1]):
    for m, y in enumerate(list1[k+1:]):
        list2.append(lcm(x,y))
print(max(list2))


# ## GeeksFor Geeks Q2: Given an array of integers arr of size N, the task is to print products of all subarrays of the array.

# In[275]:


list1 = [10,3,7]
listr = []
for p in range(0, len(list1)):
    for x in range(0, len(list1) - p):
        listr.append(list1[p : p + x + 1])
product = 1
for a in listr:
    for b in a:
        product *= b
print(product)


# ## GeeksForGeeks Q3: Write a program to print all permutations of a given string

# In[294]:


list1 = ['A','B','C']
listr = []
listr2 = []
for x in range(len(list1)):
    for y in range(len(list1)):
        for z in range(len(list1)):
            if (x != y) and (y != z) and (x != z):
                listr.append([x,y,z])
for a in listr:
    listtemp = []
    for b in a:
        listtemp.append(list1[b])
    listr2.append(listtemp)
print(listr2)


# ## GeeksForGeeks Q5: Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not overlap.

# In[298]:


def test(s):
    list_1 = list(s)
    list2 = []
    for m in range(1, len(list_1)//2+1):
        if list_1[:m] == list_1[-m:]:
            list2.append(m)
    return max(list2)
test('aabcdaabc')


# ## GeeksForGeeks Q6: Find the closest pair from two sorted arrays

# In[311]:


import numpy as np

list1 = [1,4,5,7]
list2 = [10,20,30,40]
x = 32

def pairs(list1,list2,x):
    m1 = 0
    m2 = len(list2)-1
    min_value = 9999
    while m1 < len(list1) and m2 >= 0:
        value = np.abs(list1[m1] + list2[m2] - x)
        if value < min_value:
            best1 = list1[m1]
            best2 = list2[m2]
            min_value = value
        if list1[m1] + list2[m2] > x:
            m2 -= 1
        elif m1 + m2 < x:
            m1 += 1
        else:
            return (min_value, best1, best2)
    return (best1 + best2, best1, best2)
pairs(list1,list2,x)


# ## GeeksForGeeks Q8: Given a number (as string) and two integers a and b, divide the string in two non-empty parts such that the first part is divisible by a and second part is divisible by b. If string can not be divided into two non-empty parts, output “NO”, else print “YES” with the two parts.

# In[338]:


str1 = '123'
a = 12
b = 3
def hi(str1,a,b):
    list1 = list(str1)
    for x in range(1, len(list1)):
        sub1 = list1[:x]
        sub2 = list1[x:]
        c = int(''.join(sub1))
        d = int(''.join(sub2))
        if c % a == 0 and d % b == 0:
            return 'yes'
    return 'no'
hi(str1,a,b)


# ## GeeksForGeeks Q9: Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.

# In[366]:


str1 = 'aba'
k = 2
def geeks9(str1, k):
    list2 = []
    list1 = list(str1)
    for m in range(len(list1) + 1):
        for x in range(len(list1) + 1):
            sub_list = list1[m:m+x]
            distinct = list(set(sub_list))
            if len(distinct) == k:
                list2.append(''.join(sub_list))
    return (len(list(set(list2))), list(set(list2)))
geeks9(str1, k)


# ## CCC 2016 S-1: An anagram of a string is formed by rearranging the letters in the string. For example, the anagrams of aab are aab, aba, and baa. A wildcard anagram of a string is an anagram of the string where some of the letters might have been replaced with an asterisk (*). For example, two possible wildcard anagrams of aab are *ab and *b*.  Given two strings, determine whether the second string is a wildcard anagram of the first string. 

# In[ ]:


'''
Sample Input 1
abba baaa
Output for Sample Input 1
N

Sample Input 2
cccrocks
socc*rk*
Output for Sample Input 2
A
'''


# In[370]:


str1 = 'cccrocks'
str2 = 'socc*rk*'
def anagram(str1, str2):
    if len(str1) != len(str2):
        return 'N'
    list1 = list(sorted(str1))
    list2 = list(sorted(str2))
    for x in range(1, len(list1)):
        if list1[x] == list2[x] or list1[x] == '*' or list2[x] == '*':
            continue
        else:
            return 'N'
    return 'A'
anagram(str1, str2)


# ## CCC 2020 S-1: Trick E. Dingo is trying, as usual, to catch his nemesis the Street Sprinter. His past attempts using magnets, traps and explosives have failed miserably, so he’s catching his breath to gather observational data and learn more about how fast Street Sprinter is.  Trick E. Dingo and Street Sprinter both inhabit a single straight west-east road with a particularly famous rock on it known affectionately as The Origin. Positions on this straight road are measured numerically according to the distance from The Origin, and using negative numbers for positions west of The Origin and positive numbers for positions east of The Origin.  The observations by Trick E. Dingo each contain two numbers: a time, and the value of Street Sprinter’s position on the road at that time. Given this information, what speed must Street Sprinter must be capable of? 

# In[ ]:


'''
Sample Input 1
3
0 100
20 50
10 120
Output for Sample Input 1
7.0

Sample Input 2
5
20 -5
0 -17
10 31
5 -3
30 11
Output for Sample Input 2
6.8
'''


# In[397]:


import numpy
list1 = [(20, -5), (0, -17), (10, 31), (5, -3), (30, 11)]
listr = []
list1 = sorted(list1)
for k, x in enumerate(list1):
    if k > 0:
        num = x[1] - start
        num = numpy.abs(num)
        time = x[0] - hi
        fraction = num/time
        listr.append(fraction)
    start = x[1]
    hi = x[0]
print(max(listr))


# ## CCC 2019 S-2: For various given positive integers N > 3, find two primes, A and B such that N is the average (mean) of A and B. That is, N should be equal to (A + B)/2. Recall that a prime number is an integer P > 1 which is only divisible by 1 and P . For example, 2, 3, 5, 7, 11 are the first few primes, and 4, 6, 8, 9 are not prime numbers. 

# In[402]:


def isitprime(n):
    for a in range(2, n):
        if n % a == 0:
            return False
    return True
isitprime(8)


# In[405]:


def prime(n):
    for x in range(n, 2 * n):
        if isitprime(x) and isitprime(2 * n - x):
            return (x, 2 * n - x)
prime(8)


# ## CCC 2018 S-1: In the country of Voronoi, there are N villages, located at distinct points on a straight road. Each of these villages will be represented by an integer position along this road.  Each village defines its neighbourhood as all points along the road which are closer to it than to any other village. A point which is equally close to two distinct villages A and B is in the neighbourhood of A and also in the neighbourhood of B.  Each neighbourhood has a size which is the difference between the minimum (leftmost) point in its neighbourhood and the maximum (rightmost) point in its neighbourhood.  The neighbourhoods of the leftmost and rightmost villages are defined to be of infinite size, while all other neighbourhoods are finite in size.  Determine the smallest size of any of the neighbourhoods (with exactly 1 digit after the decimal point). 

# In[ ]:


'''
Sample Input
5 
16 
0 
10 
4 
15
Output for Sample Input
3.0

The input file name: ./data/ccc_2018_s1.in
The output file name: ./data/ccc_2018_s1.out
'''


# In[439]:


def read_input_file(f_in_name):
    with open(f_in_name, 'r') as f:
        lines = f.readlines()
    lines = [s.strip() for s in lines]
    return lines

def write_output_file(list_ouput, f_out_name):
    list_str = [str(s) for s in list_ouput]
    out_str = '\n'.join(list_str)
    with open(f_out_name, 'w') as f:
        f.write(out_str)  


# In[443]:


list_input = read_input_file('./data/ccc_2018_s1.in')
print(list_input)


# In[445]:


list_input = [int(s) for s in list_input]


# In[457]:


def neighbourhoods(list_input):
    list1 = []
    list_input = list_input[1:]
    list_input = sorted(list_input)
    for k,x in enumerate(list_input):
        if k > 0 and k < len(list_input) - 1:
            leftdist = x - ((x - list_input[k - 1]) / 2)
            rightdist = x + ((list_input[k + 1] - x) / 2)
            list1.append(rightdist - leftdist)
    return(min(list1))
r = neighbourhoods(list_input)
list_output = [r]
write_output_file(list_output,'./data/ccc_2018_s1.out')


# ## CCC 2017 S-1: Annie has two favourite baseball teams: the Swifts and the Semaphores. She has followed them throughout the season, which is now over. The season lasted for N days. Both teams played exactly one game on each day.  For each day, Annie recorded the number of runs scored by the Swifts on that day. She also recorded this information for the Semaphores.  She would like you to determine the largest integer K such that K ≤ N and the Swifts and the Semaphores had scored the same total number of runs K days after the start of the season. The total number of runs scored by a team after K days is the sum of the number of runs scored by the team in all games before or on the K-th day.  For example, if the Swifts and the Semaphores have the same total number of runs at the end of the season, then you should output N. If the Swifts and the Semaphores never had the same number of runs after K games, for any value of K ≤ N , then output 0. 

# In[ ]:


'''
Sample Input 3
4 
1 2 3 4 
1 3 2 4
Output for Sample Input 3
4

The input file name: data/ccc_2017_s1.in
The output file name: data/ccc_2017_s1.out
'''


# In[461]:


def baseball(list1, list2):
    for k in reversed(range(len(list1) + 1)):
        sublist1 = list1[:k]
        sublist2 = list2[:k]
        if sum(sublist1) == sum(sublist2):
            return k


# In[479]:


# get input
input1 = int(input())
input2 = input()
input3 = input()

list1 = input2.split(' ')
list1 = [int(s) for s in list1]
list2 = input3.split(' ')
list2 = [int(s) for s in list2]

# process
r = baseball(list1, list2)
print(r)


# ## CCC 2017 S-2: Joe Coder is camping near the Bay of Fundy between Nova Scotia and New Brunswick. When he arrived at the bay, he was told that the difference in height between high tide and low tide at the Bay of Fundy was the largest tidal difference in the world. Ever the skeptic, Joe decided to verify this. He chose a reference point and, after learning from the radio when the tides were highest and lowest, he went with a boat to his reference point and measured the depth of the water. Unfortunately, on the last day of his trip, a strong wind scattered his measurements. Joe has recovered all of his measurements, but they may not be in their original order. Luckily, he remembers some things about his measurements:  He started measuring water levels at a low tide, his second measurement was of the water level at high tide, and after that the measurements continued to alternate between low and high tides.  All high tide measurements were higher than all low tide measurements.  Joe noticed that as time passed, the high tides only became higher and the low tides only became lower. Given Joe’s measurements in no particular order, you must reconstruct the correct order in which the measurements were taken. 

# In[ ]:


'''
Sample Input
8
10 50 40 7 3 110 90 2
Output for Sample Input
10 40 7 50 3 90 2 110
'''


# In[492]:


a = int(input())
str1 = input()
list1 = str1.split(' ')
list1 = [int(s) for s in list1]
list1 = sorted(list1)
sublist1 = list1[:(a // 2)]
sublist2 = list1[(a // 2):]
sublist1 = sorted(sublist1, reverse = True)
listr = []
for x in range(len(sublist1)):
    listr.append(sublist1[x])
    listr.append(sublist2[x])
listr2 = [str(s) for s in listr]
str_out = ' '.join(listr2)
print(str_out)


# In[495]:


dict1 = {}
dict1['a'] = {}
dict1['a']['b'] = 2.3
dict1['a']['c'] = 4.5
dict1['b'] = {}
dict1['b']['d'] = 9.7
dict1['c'] = {}
dict1['c']['b'] = 1.1
dict1['c']['d'] = 3.2
dict1['c']['e'] = 5.1
dict1['d'] = {}
dict1['d']['e'] = 2.9
dict1['e'] = {}
print(dict1)


# In[498]:


dict2 = {}
dict2['a'] = []
dict2['b'] = ['a', 'c']
dict2['c'] = ['a']
dict2['d'] = ['b', 'c']
dict2['e'] = ['c', 'd']
print(dict2)


# In[500]:


list1 = list(dict1['c'].keys())
print(list1)


# In[501]:


print(dict2['e'])


# ## CCC 2015 S-1: Your boss has asked you to add up a sequence of positive numbers to determine how much money your company made last year. Unfortunately, your boss reads out numbers incorrectly from time to time. Fortunately, your boss realizes when an incorrect number is read and says “zero”, meaning “ignore the current last number.” Unfortunately, your boss can make repeated mistakes, and says “zero” for each mistake. For example, your boss may say “One, three, five, four, zero, zero, seven, zero, zero, six”, which means the total is 7 as explained in the following chart:

# In[ ]:


'''
Sample Input 2
1 3 5 4 0 0 7 0 0 6
Output for Sample Input 2
7
'''


# In[1]:


def zero_element(list1, indzero):
       return list1[:indzero - 1] + list1[indzero + 1:]


# In[5]:


str1 = input()
list1 = str1.split(' ')
list1 = [int(s) for s in list1]
while 0 in list1:
    for k, x in enumerate(list1):
        if x == 0:
            indzero = k
            list1 = zero_element(list1, indzero)
            break
print(sum(list1))


# ## CCC 2013 S-2: Problem S2: Bridge transport  A train of railway cars attempts to cross a bridge. The length of each car is 10m but their weights might be different. The bridge is 40m long (thus can hold 4 train cars at one time). The bridge will crack if the total weight of the cars on it at one time is greater than a certain weight. The cars are numbered starting at 1, going up to N, and they cross the bridge in that order (i.e., 1 immediately followed by 2, which is immediately followed by 3, and so on). What is the largest number T of railway cars such that the train of cars 1...T (in order) can cross the bridge? 

# In[ ]:


'''
Sample Input 1
100
6
50 30 10 10 40 50
Output for Sample Input 1
5
'''


# In[15]:


weight = int(input())
n = int(input())
str1 = input()
list1 = str1.split(' ')
list1 = [int(s) for s in list1]
kk = 0
for k in range(len(list1) - 3):
    sublist = list1[k : k + 4]
    kk +=1
    print(sublist)
    if sum(sublist)>weight:
        print('overweight')
        print(kk + 4 - 2)


# ## CCC 2011-S1 Problem S1: English or French?  You would like to do some experiments in natural language processing. Natural language pro- cessing (NLP) involves using machines to recognize human languages.  Your first idea is to write a program that can distinguish English text from French text.  After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to compare the occurrences of the letters “t” and “T” to the occurrences of the letters “s” and “S”. Specifically:  if the given text has more “t” and “T” characters than “s” and “S” characters, we will say that it is (probably) English text;  if the given text has more “s” and ”S” characters than “t” and “T” characters, we will say that it is (probably) French text;  if the number of “t” and “T” characters is the same as the number of “s” and “S” characters, we will say that it is (probably) French text. 

# In[ ]:


'''
Sample Input 1
3
The red cat sat on the mat.
Why are you so sad cat?
Don’t ask that.

Output for Sample Input 1
English
'''


# In[11]:


lines = int(input())
list1 = []
for x in range(lines):
    list1.append(input())
count_t = 0
count_s = 0
str1 = ' '.join(list1)
list1 = list(str1)
print(list1)
for x in list1:
    x = x.lower()
    if x == 't':
        count_t += 1
    if x == 's':
        count_s += 1
if count_s < count_t:
    print('English')
else:
    print('French')


# ## CCC 2010 S-2: Problem S2: Huffman Encoding  There is an ingenious text-compression algorithm called Huffman coding, designed by David Huff- man in 1952.  The basic idea is that each character is associated with a binary sequence (i.e., a sequence of 0s and 1s). These binary sequences satisfy the prefix-free property: a binary sequence for one character is never a prefix of another character’s binary sequence.  It is worth noting that to construct a prefix-free binary sequence, simply put the characters as the leaves of a binary tree, and label the “left” edge as 0 and the ”right” edge as 1. The path from the root to a leaf node forms the code for the character at that leaf node. For example, the following binary tree constructs a prefix-free binary sequence for the characters {A, B, C, D, E}:  That is, A is encoded as 00, B is encoded as 01, C is encoded as 10, D is encoded as 110 and E is encoded as 111.  The benefit of a set of codes having the prefix-free property is that any sequence of these codes can be uniquely decoded into the original characters.  Your task is to read a Huffman code (i.e., a set of characters and associated binary sequences) along with a binary sequence, and decode the binary sequence to its character representation. 

# In[ ]:


'''
Sample Input
5
A 00
B 01
C 10
D 110
E 111
00000101111

Output for Sample Input
AABBE
'''


# In[38]:


n = int(input())
dict_enc = {}
for x in range(n):
    str1 = input()
    list1 = str1.split(' ')
    dict_enc[list1[0]] = list1[1]
dict_dec = {v:k for k,v in dict_enc.items()}
str1 = input()
list1 = list(str1)
list_r = []
while list1:
    for k in range(1, len(list1)+1):
        sublist = list1[0:k]
        str2 = ''.join(sublist)
        if str2 in dict_dec:
            list_r.append(dict_dec[str2])
            list1 = list1[k:]
            break
str1 = ''.join(list_r)
print(str1)


# ## CCC 2008-S1 Problem S1: It’s Cold Here! Canada is cold in winter, but some parts are colder than others. Your task is very simple, you need to find the coldest city in Canada. So, when given a list of cities and their temperatures, you are to determine which city in the list has the lowest temperature and is thus the coldest.

# In[ ]:


'''
Sample Input
Saskatoon -20
Toronto -2
Winnipeg -40
Vancouver 8
Halifax 0
Montreal -4
Waterloo -3

Output for Sample Input
Winnipeg
'''


# In[59]:


list1 = []
for x in range(7):
    list1.append(input())
list2 = []
for x in list1:
    x = x.split(' ')
    number = int(x[1])
    x = x[:1]
    x.append(number)
    x = tuple(x)
    list2.append(x)
list2 = sorted(list2, key = lambda x : x[1])
print(list2[0][0])


# ## CCC 2008 S-2: Problem S2: Pennies in the Ring. The game “Pennies in the Ring” is often played by bored computer programmers who have gotten tired of playing solitare. The objective is to see how many pennies can be put into a circle. The circle is drawn on a grid, with its center at the coordinate (0, 0). A single penny is placed on every integer grid coordinate (e.g., (1, 1), (1, 2), etc.) that lies within or on the circle. It’s not a very exciting game, but it’s very good for wasting time. Your goal is to calculate how many pennies are needed for a circle with a given radius.

# In[ ]:


'''
Sample Input
2 
3 
4 
0

Output for Sample Input
13 
29 
49
'''


# In[73]:


import math
list_input = []
while True:
    a = int(input())
    if a!=0:
        list_input.append(a)
    else:
        break
for a in list_input:
    list1 = []
    negative = -1*a
    positive = a
    for x in range(negative, positive + 1):
        for y in range(negative, positive + 1):
            if math.sqrt(x ** 2 + y ** 2) <= a:
                list1.append((x,y))
    print(len(list1))


# ## Graph traversal framework

# In[38]:


# function to discover the children of the current node
def discover_children(current_node, graph):
    list_children = []
    return list_children

# function to check if termination is reached
def check_termination(path):
    return False

# initialization
graph = {}
graph['A'] = ['B', 'C']
list_visited = []
list_paths = [] # the queue
start_node = 'A'
list_paths.append([start_node])
final_path = []
done = False

while list_paths:
    # step 1: pop the first path from the list_paths
    current_path = list_paths.pop()
    current_node = current_path[-1]
    # check if the current node has been visited
    if current_node not in list_visited:
        list_visited.append(current_node)
        # step 2: discover the children of the current node
        list_children = discover_children(current_node, graph)

        # extend the current path by adding the child
        for c in list_children:
            path = current_path + [c]
            # step 3: check if the task is coompleted
            if check_termination(path):
                final_path = path
                done = True
                break
            else:
                # append the path to the path queue
                list_paths.append(path)
        
        # done
        if done:
            break
        
if final_path == []:
    print('Did not find F')
else:
    print(final_path)


# ## Breadth-First-Search (BFS)

# In[156]:


friends = {'2': ['1'], '3': ['2'], '1': ['3'], '11': ['10'], '10': ['100'], '100': ['11']}

def bfs(starting_node, end_node, graph):
    list_visited = []
    list_paths = []
    list_paths.append([starting_node])
    
    while list_paths:
        current_path = list_paths.pop(0)
        current_node = current_path[-1]
        if current_node not in list_visited:
            list_visited.append(current_node)
            list_friends = friends[current_node]
            for c in list_friends:
                path = current_path + [c]
                if path[-1] == end_node:
                    return path
                else:
                    list_paths.append(path) #debug
    return None

shortest_path = bfs('1', '2', friends)
print(shortest_path)


# ## Graph traversal to solve N-queens problem

# In[87]:


def check_safe_queen(list_q, new_q):
    tup1 = (len(list_q), new_q)
    for k, x in enumerate(list_q):
        if x == new_q:
            return False
        tup2 = (k, x)
        slope = (tup1[1] - tup2[1])/(tup1[0] - tup2[0])
        if slope == 1 or slope == -1:
            return False
    return True
def check_termination(path):
    if len(path) == n:
        return True
    return False
n = int(input())
list_paths = []
final_result = None
for x in range(n):
    list_paths.append([x])
while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    for a in range(n):
        if check_safe_queen(current_path, a) == True:
            if check_termination(current_path + [a]) == True:
                final_result = current_path + [a]
                break
            list_paths.append(current_path + [a])
    if final_result != None:
        break
print(final_result)


# ## Rat in Maze

# In[ ]:


'''
input 
4 4
0 0
3 3
0 0 0 1
1 1 0 0
0 1 0 0
0 0 0 0
'''


# In[108]:


str1 = input()
grid_size = str1.split(' ')
grid_size = [int(s) for s in grid_size]
str1 = input()
starting_node = str1.split(' ')
starting_node = [int(s) for s in starting_node]
str1 = input()
ending_node = str1.split(' ')
ending_node = [int(s) for s in ending_node]
ending_node = str(ending_node[0]) + ', ' + str(ending_node[0])
grid = []
for x in range(grid_size[1]):
    a = input()
    a = a.split(' ')
    a = [int(s) for s in a]
    grid.append(a)
print(grid)


# In[116]:


grid_size = [4, 4]
starting_node = [0, 0]
start_node = str(starting_node[0]) + ', ' + str(starting_node[0])
ending_node = [3, 3]
end_node = str(ending_node[0]) + ', ' + str(ending_node[0])
grid = [[0, 0, 0, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
graph = {}
for row in range(grid_size[0]):
    for col in range(grid_size[1]):
        current_node = grid[row][col]
        if current_node == 0:
            if row != 0:
                if grid[row - 1][col] == 0:
                    if str(row) + ', ' + str(col) not in graph:
                        graph[str(row) + ', ' + str(col)] = [str(row - 1) + ', ' + str(col)]
                    else:
                        graph[str(row) + ', ' + str(col)].append(str(row - 1) + ', ' + str(col))
            if col != 0:
                if grid[row][col - 1] == 0:
                    if str(row) + ', ' + str(col) not in graph:
                        graph[str(row) + ', ' + str(col)] = [str(row) + ', ' + str(col - 1)]
                    else:
                        graph[str(row) + ', ' + str(col)].append(str(row) + ', ' + str(col - 1))
            if row != grid_size[0] - 1:
                if grid[row + 1][col] == 0:
                    if str(row) + ', ' + str(col) not in graph:
                        graph[str(row) + ', ' + str(col)] = [str(row + 1) + ', ' + str(col)]
                    else:
                        graph[str(row) + ', ' + str(col)].append(str(row + 1) + ', ' + str(col))
            if col != grid_size[1] - 1:
                if grid[row][col + 1] == 0:
                    if str(row) + ', ' + str(col) not in graph:
                        graph[str(row) + ', ' + str(col)] = [str(row) + ', ' + str(col + 1)]
                    else:
                        graph[str(row) + ', ' + str(col)].append(str(row) + ', ' + str(col + 1))
print(graph)


# In[118]:


def create_paths(current_node):
    list1 = []
    for x in graph[current_node]:
        list1.append(x)
    return list1
def check_termination(path):
    if path[-1] == end_node:
        return True
    return False
list_paths = [[start_node]]
result = None
while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    list_children = create_paths(current_node)
    for a in list_children:
        if check_termination(current_path + [a]) == True:
            result = current_path + [a]
            break
        list_paths.append(current_path + [a])
    if result != None:
        break
print(result)


# ## Number of ways to catch fish

# In[ ]:


'''
Input Description
You will be given 4 integers, one per line, representing trout points, pike points, pickerel points, and 
total points allowed in that order.

Sample Input
1 2 3 2
Sample Output
1 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
2 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
0 Brown Trout, 1 Northern Pike, 0 Yellow Pickerel
Number of ways to catch fish: 3
'''


# In[120]:


str1 = input()
list1 = str1.split(' ')
list1 = [int(s) for s in list1]
trout_worth = list1[0]
pike_worth = list1[1]
pickerel_worth = list1[2]
max_points = list1[3]


# In[138]:


def create_fish(current_path):
    fish_worth = 0
    for k, x in enumerate(current_path):
        if k == 0:
            fish_worth += (trout_worth * x)
        if k == 1:
            fish_worth += (pike_worth * x)
        else:
            fish_worth += (pickerel_worth * x)
    left = max_points - fish_worth
    print(left)
    list1 = []
    if left - trout_worth >= 0:
        list1.append(0)
    if left - pike_worth >= 0:
         list1.append(1)
    if left - pickerel_worth >= 0:
        list1.append(2)
    if list1 == []:
        return [0]
    print(list1)
    return list1


# In[141]:


create_fish([])


# In[161]:


def create_fish(current_path):
    print('jjjj')
    print(current_path)
    fish_worth = 0
    for k, x in enumerate(current_path):
        if k == 0:
            fish_worth += (trout_worth * x)
        if k == 1:
            fish_worth += (pike_worth * x)
        else:
            fish_worth += (pickerel_worth * x)
    left = max_points - fish_worth
    list1 = []
    next_fish_id = len(current_path)+1
    max_num_finshes = int(left/fish_worths[next_fish_id-1])
    return list(range(0, max_num_finshes+1))

def check_termination(list_paths):
    list_1 = []
    for x in list_paths:
        list_1.append(len(x))
    if sum(list_1)==len(list_1)*3:
        return True
    return False

trout_worth = 1
pike_worth = 2
pickerel_worth = 3
fish_worths = [trout_worth, pike_worth, pickerel_worth]
max_points = 2
results = []
list_paths = []
list_fishes = create_fish([])
print(list_fishes)
for s in list_fishes:
    list_paths.append([s])
print(list_paths)
print('*****')
while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    list_children = create_fish(current_path)
    for x in list_children:
        path = current + [x]
        print('kkkkk')
        print(current, x, path)
        if check_termination(path):
            results.append(path)
        else:
            list_paths.append(path)
print(results) 


# ## Dijkstra's Algorithm

# In[5]:


graph = {}
graph['a'] = {}
graph['a']['b'] = 10
graph['a']['c'] = 3
graph['b'] = {}
graph['b']['c'] = 1
graph['b']['d'] = 2
graph['c'] = {}
graph['c']['b'] = 4
graph['c']['d'] = 8
graph['c']['e'] = 2
graph['d'] = {}
graph['d']['e'] = 7
graph['e'] = {}
graph['e']['d'] = 9


# In[6]:


infinity = float('inf')
costs = {}
costs['a'] = 0
costs['b'] = infinity
costs['c'] = infinity
costs['d'] = infinity
costs['e'] = infinity
parents = {}
processed = []


# In[7]:


def find_lowest_cost_node(costs, processed):
    list_pairs = costs.items()
    list_valid_pairs = [s for s in list_pairs if s[0] not in processed]
    if len(list_valid_pairs)>0:
        lowest_cost_node = min(list_valid_pairs, key=lambda x: x[1])
        return lowest_cost_node[0]
    return None


# In[9]:


node = find_lowest_cost_node(costs, processed)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs, processed)
list1 = ['e']
x = 'e'
while x != 'a':
    list1.append(parents[x])
    x = parents[x]
print(costs)
print(parents)
print(list1)


# In[10]:


def min_cost(start, end, graph):
    costs = {}
    list_nodes = graph.keys()
    for x in list_nodes:
        if x != start:
            costs[x] = float('inf')
    costs[start] = 0
    parents = {}
    processed = []   
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs[end]


# In[11]:


min_cost('a', 'e', graph)


# ## prim's algorithm

# In[173]:


graph = {}
graph['A'] = {}
graph['A']['B'] = 10
graph['A']['C'] = 3
graph['B'] = {}
graph['B']['C'] = 1
graph['B']['D'] = 2
graph['C'] = {}
graph['C']['B'] = 4
graph['C']['D'] = 8
graph['C']['E'] = 2
graph['D'] = {}
graph['D']['E'] = 7
graph['E'] = {}
graph['E']['D'] = 9
parents = {}
visited = ['A']

def min_cost_neighbour(graph, visited_nodes):
    min_cost = float('inf')
    min_node = None
    for x in visited_nodes:
        for y in graph[x].keys():
            if graph[x][y] < min_cost and y not in visited_nodes:
                min_cost = graph[x][y]
                min_node_start = x
                min_node_end = y
    return (min_node_start, min_node_end)


def prim(graph):
    while len(visited) != len(graph.keys()):
        min_node_start, min_node_end = min_cost_neighbour(graph, visited)
        visited.append(min_node_end)
        parents[min_node_end] = min_node_start
    s = 0
    for k, v in parents.items():
        s += graph[v][k]
    return s
print(prim(graph))
print(visited)
print(parents)


# In[ ]:





# ## Use the framework to find the shortest path for a network (Please copy the framework to specific solution as starting point)

# In[343]:


def discover_children(current_node):
    list1 = graph[current_node]
    return list1

def check_termination(path):
    if path[-1] == 'F':
        return True
    return False

graph = {'A':['B', 'C'], 'B':['C','D'], 'C':['E'], 'D':['E', 'F'], 'E':['F']}
list_visited = []
list_paths = []
start_node = 'A'
list_paths.append([start_node])
final_path = []

while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    if current_node not in list_visited:
        list_visited.append(current_node)
        list_children = discover_children(current_node)

        for c in list_children:
            path = current_path + [c]
            if check_termination(path):
                final_path = path
                break
            else:
                list_paths.append(path)  
if final_path == []:
    print('Did not find F')
else:
    print(final_path)


# In[272]:


# function to discover the children of the current node
def discover_children(current_node, graph):
    list_children = graph[current_node]
    return list_children

# function to check if termination is reached
def check_termination(path):
    if path[-1] == 'E':
        return True
    return False

# initialization
graph = {'A':['B', 'C'], 'B':['C','D'], 'C':['D', 'E'], 'D':['E'], 'E': []}
list_visited = []
list_paths = [] # the queue
start_node = 'A'
list_paths.append([start_node])
final_path = []
test = 0

while list_paths:
    print(list_paths)
    # step 1: pop the first path from the list_paths
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    # check if the current node has been visited
    if current_node not in list_visited:
        list_visited.append(current_node)
        # step 2: discover the children of the current node
        list_children = discover_children(current_node, graph)

        # extend the current path by adding the child
        for c in list_children:
            path = current_path + [c]
            # step 3: check if the task is completed
            if check_termination(path):
                final_path = path
                test += 1
                break
            else:
                # append the path to the path queue
                list_paths.append(path)  
        if test == 1:
            break
if final_path == []:
    print('Did not find E')
else:
    print(final_path)


# In[23]:


print(current_path)
current_path.append(c)


# In[54]:


'blueberry' in ['blueberry', 'pear']


# In[59]:


def discover_children(current_node):
    list1 = graph[current_node][0]
    return list1

def check_termination(path):
    last_node = path[-1]
    if 'blueberry' in graph[last_node][1]:
        return True
    return False

graph = {'A':[['B', 'C'], ['apple']], 
         'B':[['C','D'], ['pear', 'apple']], 
         'C':[['E'], ['tomato', 'apple']], 
         'D':[['B', 'E', 'F'], ['grape', 'pear']], 
         'E':[['F'], ['blueberry', 'pear']], 
         'F':[[], ['strawberry', 'apple']]}
list_visited = []
list_paths = []
start_node = 'A'
list_paths.append([start_node])
final_path = []
is_done = 0
while list_paths:
    current_path = list_paths.pop(0)
    current_node = current_path[-1]
    if current_node not in list_visited:
        list_visited.append(current_node)
        list_children = discover_children(current_node)

        for c in list_children:
            path = current_path + [c]
            if check_termination(path):
                final_path = path
                is_done += 1
                break
            else:
                list_paths.append(path)  
    if is_done == 1:
        break
if final_path == []:
    print('Did not find blueberry')
else:
    print(final_path)


# ## Graph traversal algorithm to solve N-queens problem

# In[ ]:


# for example, N=4, we need to find a solution vector = [1, 3, 0, 2]


# ## Minimum spaning tree (MST) - prim's algorithm
# https://www.youtube.com/watch?v=MaaSoZUEoos
# 

# In[ ]:


# step-1: using embeded dict to represent a undirectional weighted graph

# step 2: define a function to find the min-cost neighbor which has not been visited from a list of the nodes: input: a list of nodes, output: start-node, end-node, link-cost

# step-3: define a function, input: a graph dict, output: visited_nodes, parents


# In[171]:


graph = {}
graph['A'] = {}
graph['A']['B'] = 10
graph['A']['C'] = 3
graph['B'] = {}
graph['B']['C'] = 1
graph['B']['D'] = 2
graph['C'] = {}
graph['C']['B'] = 4
graph['C']['D'] = 8
graph['C']['E'] = 2
graph['D'] = {}
graph['D']['E'] = 7
graph['E'] = {}
graph['E']['D'] = 9
parents = {}
visited = ['A']

def min_cost_neighbour(graph, visited_nodes):
    min_cost = float('inf')
    min_node = None
    for x in visited_nodes:
        for y in graph[x].keys():
            if graph[x][y] < min_cost and y not in visited_nodes:
                min_cost = graph[x][y]
                min_node_start = x
                min_node_end = y
    return (min_node_start, min_node_end)


def prim(graph):
    while len(visited) != len(graph.keys()):
        min_node_start, min_node_end = min_cost_neighbour(graph, visited)
        visited.append(min_node_end)
        parents[min_node_end] = min_node_start
    s = 0
    for k, v in parents.items():
        s += graph[v][k]
    return s
print(prim(graph))
print(visited)
print(parents)


# ## Depth first search (DFS)
# https://www.youtube.com/watch?v=tlPuVe5Otio
# https://www.youtube.com/watch?v=FvGCzzfdOLw
# https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python

# In[132]:


graph = {
    'A' : ['B','E'],
    'B' : ['A','F'],
    'C' : ['G'],
    'D' : ['E','H'],
    'E' : ['A','D','H'],
    'F' : ['B','G','I'],
    'G' : ['C','F','J'],
    'H' : ['D','E','I'],
    'I' : ['F','H'],
    'J' : ['F', 'G']
}

visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            dfs(child)
dfs('A')
print(visited)
parents={}
for k, x in enumerate(visited):
    sublist1 = visited[:k][::-1]
    if len(sublist1) == 0:
        parents[x] = None
    for a in sublist1:
        if x in graph[a]:
            parents[x] = a
            break
    
print(parents)
for k, node in enumerate(visited):
    if k>0:
        p = parents[node]
        print(p, 'to', node)


# ## Topological sort
# https://www.youtube.com/watch?v=eL-KzMXSXXI&t=358s
# https://www.youtube.com/watch?v=HyVI8-nHgEg

# In[133]:


graph = {
    'A' : ['D'],
    'B' : ['D'],
    'C' : ['A', 'B'],
    'D' : ['G','H'],
    'E' : ['A','D','F'],
    'F' : ['J','K'],
    'G' : ['I'],
    'H' : ['I','J'],
    'I' : ['L'],
    'J' : ['L', 'M'],
    'K' : ['J'],
    'L' : [],
    'M' : []
}


# In[137]:


global_visited = []
list_r = []
def dfs(node):
    if node not in global_visited:
        visited.append(node)
        global_visited.append(node)
        for child in graph[node]:
            dfs(child)

for node in graph.keys():
    if node not in global_visited:
        print(node)
        visited = []
        dfs(node)
        list_r.append(visited)
        print(visited)
list1 = []
for a in list_r[::-1]:
    for x in a:
        list1.append(x)
print(list1)


# ## Detect cycle in Directed Graph using Topological Sort
# 
# Last Updated: 23-11-2020
# Given a Directed Graph consisting of N vertices and M edges and a set of Edges[][], the task is to check whether the graph contains a cycle or not using Topological sort.
# 
# Topological sort of directed graph is a linear ordering of its vertices such that, for every directed edge U -> V from vertex U to vertex V, U comes before V in the ordering. 
#  
# Examples: 
# 
# Input: N = 4, M = 6, Edges[][] = {{0, 1}, {1, 2}, {2, 0}, {0, 2}, {2, 3}, {3, 3}} 
# Output: Yes 
# Explanation: 
# A cycle 0 -> 2 -> 0 exists in the given graph
# 
# Input: N = 4, M = 3, Edges[][] = {{0, 1}, {1, 2}, {2, 3}, {0, 2}} 
# Output: No 

# In[151]:


list_of_lists = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['A', 'C']]
graph = {}
list_nodes = []
for x in list_of_lists:
    list_nodes += x
list_nodes = list(set(list_nodes))
for node in list_nodes:
    graph[node] = []
for x in list_of_lists:
    starting = x[0]
    ending = x[1]
    graph[starting].append(ending)
print(graph)


# In[152]:


hi = 0
global_visited = []
list_r = []
def dfs(node):
    if node not in global_visited:
        visited.append(node)
        global_visited.append(node)
        for child in graph[node]:
            dfs(child)

for node in graph.keys():
    if node not in global_visited:
        print(node)
        visited = []
        dfs(node)
        list_r.append(visited)
        print(visited)
list1 = []
for a in list_r[::-1]:
    for x in a:
        list1.append(x)
print(list1)
for edge in list_of_lists:
    starting = edge[0]
    ending = edge[1]
    if list1.index(starting) > list1.index(ending):
        print('Yes')
        hi += 1
        break
if hi == 0:
    print('No')


# ## Check whether a given graph is Bipartite or not
# 
# A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.

# In[184]:


graph = {
    'A' : ['B','E'],
    'B' : ['A','F'],
    'C' : ['G'],
    'D' : ['E','H'],
    'E' : ['A','D','H'],
    'F' : ['B','G','I'],
    'G' : ['C','F','J'],
    'H' : ['D','E','I'],
    'I' : ['F','H'],
    'J' : ['F', 'G']
}
visited = []
def dfs(node):
    if node not in visited:
        visited.append(node)
        for x in graph[node]:
            dfs(x)
dfs('A')
parents = {}
for k, x in enumerate(visited):
    sublist = visited[:k][::-1]
    if len(sublist) == 0:
        parents[x] = None
    for a in sublist:
        if x in graph[a]:
            parents[x] = a
            break
list_of_blue = [visited[0]]
list_of_red = []
for node in visited[1:]:
    starting = parents[node]
    ending = node
    list_of_blue = [visited[0]]
    list_of_red = []
    for node in visited[1:]:
        starting = parents[node]
        ending = node
        if starting in list_of_blue:
            if ending in list_of_blue:
                break
            if ending not in list_of_red:
                list_of_red.append(ending)
        if starting in list_of_red:
            if ending in list_of_red:
                break
            if ending not in list_of_blue:
                list_of_blue.append(ending)
print(list_of_red)
print(list_of_blue)

# verify
# for node in visited[1:]:
#     starting = parents[node]
#     ending = node
#     if starting in list_of_red:
#         starting = 'red'
for x in graph.keys():
    hi = 0
    for y in graph[x]:
        if (x in list_of_blue and y in list_of_blue) or (x in list_of_red and y in list_of_red):
            print('No')
            hi = 1
            break
    if hi == 1:
        break
if hi == 0:
    print('Yes')


# ## Dynamic programming framework

# In[18]:


print(dict_solution[2])


# In[64]:


# initialization
# components: each component occupies a capacity and creates a value
dict_components = {}
dict_components['a'] = {}
dict_components['a']['capacity'] = 1
dict_components['a']['value'] = 3
dict_components['b'] = {}
dict_components['b']['capacity'] = 2
dict_components['b']['value'] = 5
dict_components['c'] = {}
dict_components['c']['capacity'] = 3
dict_components['c']['value'] = 7
# capacity units
tot_capacity = 8
# dict optimal-solution
dict_solution = {}
# the optimal solution at capacity 0
dict_solution[0] = {}
dict_solution[0]['max_value'] = 0
dict_solution[0]['optimal_solution'] = []

def find_best_single_component(capacity, dict_components):
    max_value = -1
    best_component = None
    for key in dict_components.keys():
        if capacity >= dict_components[key]['capacity']:
            if dict_components[key]['value'] > max_value:
                max_value = dict_components[key]['value']
                best_component = key
    return best_component, max_value

# find the optimal solution for the n-th step
for current_cap in range(1, tot_capacity + 1):
    print('Current capacity: {}'.format(current_cap))
    # iterate over the previous capcities
    list_solutions = []
    for prev_cap in range(current_cap):
        max_value = dict_solution[prev_cap]['max_value']
        opt_solution = dict_solution[prev_cap]['optimal_solution']
        remaining_cap = current_cap - prev_cap
        # the best single component fit with the remaining capacity
        remaining_best_component, remaining_max_value = find_best_single_component(
            remaining_cap, dict_components)
        if remaining_max_value > 0:
            max_value = max_value + remaining_max_value
            opt_solution = opt_solution + [remaining_best_component]
        list_solutions.append((max_value, opt_solution)) 
    # update dict optal-solution
    list_solutions = sorted(list_solutions, key = lambda x: x[0], reverse = True)
    dict_solution[current_cap] = {}
    dict_solution[current_cap]['max_value'] = list_solutions[0][0]
    dict_solution[current_cap]['optimal_solution'] = list_solutions[0][1] 
print(dict_solution[tot_capacity])


# ### Practice: find the best single component that fit with the current capacity. 
# We have three items: 1) ipad: value=1000, weight=2 lbs, 2) iphone, value = 600, weight=1 lb, 3) laptop, value=1500, weight=4 lbs. define a function: input: the avilable capacity in lbs, output: (best_item, max_value) for a single item that fit into the capacity

# In[141]:


value = {}
value['ipad'] = 1000
value['iphone'] = 400
value['laptop'] = 1500
weight = {}
weight['ipad'] = 2
weight['iphone'] = 1
weight['laptop'] = 4
def best_single_component(capacity):
    dict1 = value.copy()
    while dict1:
        max_value = max(dict1.values())
        for x in dict1.keys():
            if value[x] == max_value:
                max_value_key = x
                break
        if capacity >= weight[max_value_key]:
            return max_value_key
        dict1.pop(max_value_key)
    return None
best_single_component(4)


# ### Practice: when the knapsack can hold 1 lbs, the optimal solution is to hold 1 iphone with value 400; when the knapsack can hold 2 lbs, the optimal solution is to hold 1 ipad with total value of 1000; when the knapsack can hold 3 lbs, the optimal solution is to hold 1 ipad and 1 iphone with total value of 1400. Write a program to find the optimal soltion for the knapsack with capacity of 4 lbs.

# In[157]:


value = {}
value['ipad'] = 1000
value['iphone'] = 400
value['laptop'] = 1500
weight = {}
weight['ipad'] = 2
weight['iphone'] = 1
weight['laptop'] = 3
opt_sol = {}
opt_sol[0] = []
opt_sol[1] = ['iphone']
opt_sol[2] = ['ipad']
opt_sol[3] = ['ipad', 'iphone']
options = []
capacity = 4
for x in range(capacity):
    leftovers = capacity - x
    best2 = best_single_component(leftovers)
    options.append([best2] + opt_sol[x])
sums = []
s = 0
for x in options:
    for a in x:
        s += value[a]
    sums.append((x, s))
    s = 0
sums = sorted(sums, key = lambda x:x[1], reverse = True)
opt_sol[4] = sums[0][0]
print(opt_sol[4])


# ## Practice: There are three items in the store: 1) ipad: value=1000, weight=2 lbs, 2) iphone, value = 400, weight=1 lb, 3) laptop, value=1500, weight=3 lbs. A thief has a knapsack of 16 lbs, what can he put into his knacpsack to maximize the total value.

# In[30]:


value = {}
value['ipad'] = 1000
value['iphone'] = 400
value['laptop'] = 1500
weight = {}
weight['ipad'] = 2
weight['iphone'] = 1
weight['laptop'] = 3
opt_sol = {}
opt_sol[0] = []

def best_single_component(capacity):
    dict1 = value.copy()
    while dict1:
        max_value = max(dict1.values())
        for x in dict1.keys():
            if value[x] == max_value:
                max_value_key = x
                break
        if capacity >= weight[max_value_key]:
            return max_value_key
        dict1.pop(max_value_key)
    return None


tot_capacity = int(input())
for capacity in range(1, tot_capacity + 1):
    options = []
    for x in range(capacity):
        leftovers = capacity - x
        best2 = best_single_component(leftovers)
        options.append([best2] + opt_sol[x])
    sums = []
    s = 0
    for x in options:
        for a in x:
            s += value[a]
        sums.append((x, s))
        s = 0
    sums = sorted(sums, key = lambda x:x[1], reverse = True)
    opt_sol[capacity] = sums[0][0]
print(opt_sol[tot_capacity])
s = 0
for x in opt_sol[tot_capacity]:
    s += value[x]
print(s)


# ## prices=[1,  5,   8,   9,  10,  17,  17,  20, 25]                                                                              rod length = 8
# # bottom-up dynamic programming
# 

# In[33]:


def best_single_component(lengths):
    dict1 = value.copy()
    while dict1:
        max_value = max(dict1.values())
        for x in dict1.keys():
            if value[x] == max_value:
                max_value_key = x
                break
        if lengths >= length[max_value_key]:
            return max_value_key
        dict1.pop(max_value_key)
    return None
value = {}
value['1'] = 1
value['2'] = 5
value['3'] = 8
value['4'] = 9
value['5'] = 10
value['6'] = 17
value['7'] = 17
value['8'] = 20
value['9'] = 25
length = {}
length['1'] = 1
length['2'] = 2
length['3'] = 3
length['4'] = 4
length['5'] = 5
length['6'] = 6
length['7'] = 7
length['8'] = 8
length['9'] = 9
opt_sol = {}
opt_sol[0] = []
rod_length = int(input())
for lengths in range(1, rod_length + 1):
    options = []
    for x in range(lengths):
        leftovers = lengths - x
        best2 = best_single_component(leftovers)
        options.append([best2] + opt_sol[x])
    sums = []
    s = 0
    for x in options:
        for a in x:
            s += value[a]
        sums.append((x, s))
        s = 0
    sums = sorted(sums, key = lambda x:x[1], reverse = True)
    opt_sol[lengths] = sums[0][0]
print(opt_sol[rod_length])
s = 0
for x in opt_sol[rod_length]:
    s += value[x]
print(s)


# ## Practice:we have coins: 1 cent, 5 cents, 10 cents, 25 cents, given an amount of money, make it into the min number of coins

# In[75]:


def best_single_component1(money_amounts, value):
    list1 = list(value.items())
    list1 = sorted(list1, key=lambda x: x[1])
    best_item = None
    for k, v in list1:
        if money_amounts>=v:
            best_item = k
        else:
            return best_item
    return best_item


value['1'] = 1
value['5'] = 5
value['10'] = 10
value['25'] = 25
amount = int(input())
opt_sol = {}
opt_sol[0] = []
for money_amounts in range(1, amount+1):
    print('current capacity: {}'.format(money_amounts))
    money_amounts = int(money_amounts)
    options = []
    for x in range(money_amounts):
        print('prev cap: {}'.format(x))
        leftovers = money_amounts - x
        best2 = best_single_component1(leftovers, value)
        if value[best2]==leftovers:
            options.append([best2] + opt_sol[x])
    print(options)
    sums = []
    s = 0
    for x in options:
        for a in x:
            s += value[a]
        sums.append((x, s))
        s = 0
    sums = sorted(sums, key = lambda x:x[1], reverse = True)
    opt_sol[money_amounts] = sums[0][0]
print('best solution:')
print(opt_sol[amount])


# ## Dynamic programming practice: Problem : Minimum Steps To One. Problem Statement: On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

# In[40]:


opt_sol = {}
opt_sol['1'] = []
n = int(input())
for x in range(2, n + 1):
    options = []
    for a in range(1, x):
        if a + 1 == x:
            options.append(opt_sol[str(a)] + ['+1'])
        if a * 2 == x:
            options.append(opt_sol[str(a)] + ['x2'])
        if a * 3 == x:
            options.append(opt_sol[str(a)] + ['x3'])
    m_len = len(options[0])
    m = options[0]
    for b in options:
        if len(b) < m_len:
            m_len = len(b)
            m = b
    opt_sol[str(x)] = m
print(len(opt_sol[str(n)]))


# ## Tiling Problem
# https://www.geeksforgeeks.org/tiling-problem/
# Last Updated: 05-11-2020
# Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile.
# Examples:
# 
# Input n = 3
# Output: 3
# Explanation:
# We need 3 tiles to tile the board of size  2 x 3. 
# We can tile the board using following ways
# 1) Place all 3 tiles vertically. 
# 2) Place first tile vertically and remaining 2 tiles horizontally.
# 3) Place first 2 tiles horizontally and remaining tiles vertically
# 
# Input n = 4
# Output: 5
# Explanation:
# For a 2 x 4 board, there are 5 ways
# 1) All 4 vertical
# 2) All 4 horizontal
# 3) First 2 vertical, remaining 2 horizontal
# 4) First 2 horizontal, remaining 2 vertical
# 5) Corner 2 vertical, middle 2 horizontal
# 
# Case work: 1) the last tile is vertical, 2) the last tile is horizontal (so does the second to the last one)

# In[73]:


opt_sol = {}
opt_sol['1'] = 1
opt_sol['2'] = 2
n = int(input())
if n > 2:
    for x in range(3, n + 1):
        opt_sol[str(x)] = opt_sol[str(x - 1)] + opt_sol[str(x - 2)]
print(opt_sol[str(n)])


# ## Friends Pairing Problem
# https://www.geeksforgeeks.org/friends-pairing-problem/
# Last Updated: 16-05-2019
# Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.
# 
# Examples :
# 
# Input  : n = 3
# Output : 4
# 
# Explanation
# {1}, {2}, {3} : all single
# {1}, {2, 3} : 2 and 3 paired but 1 is single.
# {1, 2}, {3} : 1 and 2 are paired but 3 is single.
# {1, 3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1, 2} and {2, 1} are considered same.

# In[64]:


opt_sol = {}
opt_sol['1'] = 1
opt_sol['2'] = 2
n = int(input())
if n > 2:
    for x in range(3, n + 1):
        opt_sol[str(x)] = opt_sol[str(x - 1)] + (x - 1) * opt_sol[str(x - 2)]
print(opt_sol[str(n)])


# ## Dynamic programming course

# ## Memoization Recipe
# #### Make it work
# * visualize the problem as a tree
# * implement the tree using recursion
# * test it
# 
# #### Make it efficient
# * add a memo object
# * add a base case to return memo values
# * store return values into the memo

# ### Grid Traveller

# In[9]:


def grid_traveller(m, n):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if (m == 1) and (n == 1):
        return 1
    if (m == 0) or (n == 0):
        return 0
    memo[key] = grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
    return memo[key]


# In[10]:


memo = {}
print(grid_traveller(1, 1))#1
memo = {}
print(grid_traveller(2, 3))#3
memo = {}
print(grid_traveller(3, 2))#3
memo = {}
print(grid_traveller(3, 3))#6
memo = {}
print(grid_traveller(18, 18))#2333606220


# ### Can Sum problem

# In[9]:


def can_sum(target_sum, numbers):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < min(numbers):
        return False
    for x in numbers:
        remainder = target_sum - x
        if can_sum(remainder, numbers) == True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


# In[11]:


memo = {}
print(can_sum(7, [2, 3]))   #True
memo = {}
print(can_sum(7, [5, 3, 4, 7]))  #True
memo = {}
print(can_sum(7, [2, 4]))  #False
memo = {}
print(can_sum(8, [2, 3, 5]))  #True
memo = {}
print(can_sum(300, [7, 14]))  #False


# ### How Sum problem

# In[41]:


def how_sum(target_sum, numbers):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < min(numbers):
        return None
    for x in numbers:
        remainder = target_sum - x
        result = how_sum(remainder, numbers)
        if result != None:
            r = result + [x]
            memo[target_sum] = r
            return memo[target_sum]
    memo[target_sum] = None
    return None


# In[42]:


memo = {}
print(how_sum(7, [2, 3]))   #[3, 2, 2]
memo = {}
print(how_sum(7, [5, 3, 4, 7]))  #[4, 3]
memo = {}
print(how_sum(7, [2, 4]))  #None
memo = {}
print(how_sum(8, [2, 3, 5]))  #[2,2,2,2]
memo = {}
print(how_sum(300, [7, 14]))  #None


# ### Best Sum problem

# In[47]:


def best_sum(target_sum, numbers):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < min(numbers):
        return None
    answer = None
    for x in numbers:
        remainder = target_sum - x
        result = best_sum(remainder, numbers)
        if result != None:
            r = result + [x]
            if answer == None or len(r) < len(answer):
                answer = r
    memo[target_sum] = answer
    return answer


# In[50]:


memo = {}
print(best_sum(7, [5, 3, 4, 7]))  #[7]
memo = {}
print(best_sum(8, [2, 3, 5]))  #[5, 3]
memo = {}
print(best_sum(8, [1, 4, 5]))  #[4, 4]
memo = {}
print(best_sum(100, [1, 2, 5, 25]))  #[25, 25, 25, 25]


# ### Can Construct problem

# In[56]:


def can_construct(target, word_bank):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for x in word_bank:
        if target[:len(x)] == x:
            suffix = target[len(x):]
            if can_construct(suffix, word_bank) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False


# In[57]:


memo = {}
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  #True
memo = {}
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  #False
memo = {}
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  #True
memo = {}
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  #False


# ### Count Construct problem

# In[58]:


def count_construct(target, word_bank):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    count = 0
    for x in word_bank:
        if target[:len(x)] == x:
            suffix = target[len(x):]
            count += count_construct(suffix, word_bank)
            
    memo[target] = count
    return count


# In[59]:


memo = {}
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  #2
memo = {}
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  #1
memo = {}
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  #0
memo = {}
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  #4
memo = {}
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  #0


# ### All Construct problem

# In[197]:


def all_construct(target, word_bank):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for x in word_bank:
        if target[:len(x)] == x:
            suffix = target[len(x):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[x]+s for s in suffix_ways]
            result += target_ways
    memo[target] = result
    return result


# In[198]:


memo = {}
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  #[['purp', 'le'], ['p', 'ur', 'p', 'le']]
memo = {}
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))  #[['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
memo = {}
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  #[]
memo = {}
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))  #[]


# ## Dynamic programming Tabulation Recipe:
# * Visualize the problem as a table
# * Size the table based on the inputs
# * initialize the table with default values
# * seed the trivial answer into the table
# * iterate through the table
# * fill further positions based on the current position

# ### Fib tabulation

# In[201]:


def fib_tabulation1(n):
    list1 = []
    for x in range(n + 1):
        list1.append(0)
    list1[1] = 1
    for k, a in enumerate(list1):
        if k != len(list1) - 1 and k != len(list1) - 2:
            list1[k + 1] += a
            list1[k + 2] += a
        if k == len(list1) - 2:
            list1[k + 1] += a
    return list1[n]
print(fib_tabulation1(6)) #8
print(fib_tabulation1(7)) #13
print(fib_tabulation1(8)) #21
print(fib_tabulation1(50)) #12586269025


# In[204]:


def fib_tabulation2(n):
    list1 = [0, 1]
    for x in range(2, n + 1):
        list1.append(list1[x - 1] + list1[x - 2])
    return list1[n]
print(fib_tabulation2(6)) #8
print(fib_tabulation2(7)) #13
print(fib_tabulation2(8)) #21
print(fib_tabulation2(50)) #12586269025


# ### Grid Traveller tabulation

# In[299]:


def grid_traveller1(m, n):
    list1 = []
    for a in range(m + 1):
        list1.append([0] * (n + 1))
    list1[1][1] = 1
    for b in range(m + 1):
        for c in range(n + 1):
            current = list1[b][c]
            if (c + 1) <= n:
                list1[b][c + 1] += current
            if (b + 1) <= m:
                list1[b + 1][c] += current
    return list1[m][n]
print(grid_traveller1(1, 1)) #1
print(grid_traveller1(2, 3)) #3
print(grid_traveller1(3, 2)) #3
print(grid_traveller1(3, 3)) #6
print(grid_traveller1(18, 18)) #2333606220


# In[302]:


def grid_traveller2(m, n):
    list1 = []
    for a in range(m + 1):
        list1.append([0] * (n + 1))
    list1[1][1] = 1
    for b in range(m + 1):
        for c in range(n + 1):
            current = list1[b][c]
            if (c - 1) >= 0:
                current += list1[b][c - 1]
            if (b - 1) >= 0:
                current += list1[b - 1][c]
            list1[b][c] = current
    return list1[m][n]
print(grid_traveller2(1, 1)) #1
print(grid_traveller2(2, 3)) #3
print(grid_traveller2(3, 2)) #3
print(grid_traveller2(3, 3)) #6
print(grid_traveller2(18, 18)) #2333606220


# ### Can Sum tabulation

# In[318]:


def can_sum1(target_sum, numbers):
    list1 = [False] * (target_sum + 1)
    list1[0] = True
    for k, x in enumerate(list1):
        if x == True:
            for a in numbers:
                if k + a < len(list1):
                    list1[k + a] = True
    return list1[target_sum]
print(can_sum1(7, [2, 3])) #True
print(can_sum1(7, [5, 3, 4, 7])) #True
print(can_sum1(7, [2, 4])) #False
print(can_sum1(8, [2, 3, 5])) #True
print(can_sum1(300, [7, 14])) #False


# In[319]:


def can_sum2(target_sum, numbers):
    list1 = [False] * (target_sum + 1)
    list1[0] = True
    for k, x in enumerate(list1):
        if k == 0:
            continue
        test = 0
        for a, b in enumerate(list1[:k]):
            if b == True:
                for c in numbers:
                    if a + c == k:
                        list1[k] = True
                        test += 1
                        break
            if test == 1:
                break
    return list1[target_sum]
print(can_sum2(7, [2, 3])) #True
print(can_sum2(7, [5, 3, 4, 7])) #True
print(can_sum2(7, [2, 4])) #False
print(can_sum2(8, [2, 3, 5])) #True
print(can_sum2(300, [7, 14])) #False


# ### How Sum tabulation

# In[321]:


def how_sum1(target_sum, numbers):
    list1 = [None] * (target_sum + 1)
    list1[0] = []
    for k, x in enumerate(list1):
        if x != None:
            for a in numbers:
                if k + a < len(list1):
                    list1[k + a] = x + [a]
    return list1[target_sum]
print(how_sum1(7, [2, 3])) #[3, 2, 2]
print(how_sum1(7, [5, 3, 4, 7])) #[4, 3]
print(how_sum1(7, [2, 4])) #None
print(how_sum1(8, [2, 3, 5])) #[2, 2, 2, 2]
print(how_sum1(300, [7, 14])) #None


# In[322]:


def how_sum2(target_sum, numbers):
    list1 = [None] * (target_sum + 1)
    list1[0] = []
    for k, x in enumerate(list1):
        if k == 0:
            continue
        test = 0
        for a, b in enumerate(list1[:k]):
            if b != None:
                for c in numbers:
                    if a + c == k:
                        list1[k] = b + [c]
                        test += 1
                        break
            if test == 1:
                break
    return list1[target_sum]
print(how_sum2(7, [2, 3])) #[3, 2, 2]
print(how_sum2(7, [5, 3, 4, 7])) #[4, 3]
print(how_sum2(7, [2, 4])) #None
print(how_sum2(8, [2, 3, 5])) #[2, 2, 2, 2]
print(how_sum2(300, [7, 14])) #None


# ### Best Sum tabulation

# In[351]:


def best_sum1(target_sum, numbers):
    list1 = [None] * (target_sum + 1)
    list1[0] = []
    for k, x in enumerate(list1):
        if x != None:
            for a in numbers:
                if k + a < len(list1):
                    if (list1[k + a] == None) or (len(list1[k + a]) > len(x + [a])):
                        list1[k + a] = x + [a]
    return list1[target_sum]
print(best_sum1(7, [5, 3, 4, 7])) #[7]
print(best_sum1(8, [2, 3, 5])) #[3, 5]
print(best_sum1(8, [1, 4, 5])) #[4, 4]
print(best_sum1(100, [1, 2, 5, 25])) #[25, 25, 25, 25]


# In[363]:


def best_sum2(target_sum, numbers):
    list1 = [None] * (target_sum + 1)
    list1[0] = []
    for k, x in enumerate(list1):
        if k == 0:
            continue
        test = 0
        for a, b in enumerate(list1[:k]):
            if b != None:
                for c in numbers:
                    if a + c == k:
                        if (x == None) or (len(x) > len(b + [c])):
                            list1[k] = b + [c]
                            x = list1[k]
    return list1[target_sum]
print(best_sum2(7, [5, 3, 4, 7])) #[7]
print(best_sum2(8, [2, 3, 5])) #[3, 5]
print(best_sum2(8, [1, 4, 5])) #[4, 4]
print(best_sum2(100, [1, 2, 5, 25])) #[25, 25, 25, 25]


# ### Can Construct tabulation

# In[380]:


def can_construct1(target, word_bank):
    list1 = [False] * (len(target) + 1)
    list1[0] = True
    for k, x in enumerate(list1):
        if x == True:
            for a in word_bank:
                if target[k : k + len(a)] == a:
                        list1[k + len(a)] = True
    return list1[len(target)]
print(can_construct1('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #True
print(can_construct1('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #False
print(can_construct1('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #True
print(can_construct1('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #False


# In[403]:


def can_construct2(target, word_bank):
    list1 = [False] * (len(target) + 1)
    list1[0] = True
    for k, x in enumerate(list1):
        for a, b in enumerate(list1[:k]):
            if b == True:
                for c in word_bank:
                    if target[:a] + c == target[:k]:
                        list1[k] = True
    return list1[len(target)]
print(can_construct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #True
print(can_construct2('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #False
print(can_construct2('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #True
print(can_construct2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #False


# ### Count Construct tabulation

# In[406]:


def count_construct1(target, word_bank):
    list1 = [0] * (len(target) + 1)
    list1[0] = 1
    for k, x in enumerate(list1):
        if x >= 1:
            for b in word_bank:
                if target[k : k + len(b)] == b:
                        list1[k + len(b)] += x
    return list1[len(target)]
print(count_construct1('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
print(count_construct1('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #1
print(count_construct1('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #0
print(count_construct1('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #4
print(count_construct1('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #0


# In[409]:


def count_construct2(target, word_bank):
    list1 = [0] * (len(target) + 1)
    list1[0] = 1
    for k, x in enumerate(list1):
        for a, b in enumerate(list1[:k]):
            if b >= 1:
                for c in word_bank:
                    if target[:a] + c == target[:k]:
                        list1[k] += b
    return list1[len(target)]
print(count_construct2('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
print(count_construct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #1
print(count_construct2('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #0
print(count_construct2('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #4
print(count_construct2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #0


# ### All Construct tabulation

# In[15]:


def all_construct1(target, word_bank):
    list1 = [[]] * (len(target) + 1)
    list1[0] = [[]]
    for k, x in enumerate(list1):
        if x != []:
            for b in word_bank:
                if target[k : k + len(b)] == b:
                    for a in x:
                        list1[k + len(b)] = list1[k + len(b)] + ([a + [b]])
    return list1[len(target)]
print(all_construct1('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #[['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(all_construct1('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])) #[['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(all_construct1('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #[]
print(all_construct1('aaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) #[]


# In[35]:


def all_construct2(target, word_bank):
    list1 = [[]] * (len(target) + 1)
    list1[0] = [[]]
    for k, x in enumerate(list1):
        for a, b in enumerate(list1[:k]):
            if b != []:
                for c in word_bank:
                    if target[:a] + c == target[:k]:
                        for d in b:
                            list1[k] = list1[k] + ([d + [c]])
    return list1[len(target)]
print(all_construct2('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #[['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(all_construct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])) #[['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(all_construct2('skateboard', ['bo', 'rd', 'ate', 'ska', 'sk', 'boar'])) #[]
print(all_construct2('aaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) #[]


# ## Olympiads-HW-1

# In[ ]:


'''
Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use
seven-digit phone numbers where the last four digits have three properties. Looking just at the last
four digits, these properties are:
• the first of these four digits is an 8 or 9;
• the last digit is an 8 or 9;
• the second and third digits are the same.
For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are
telemarketer numbers.
Write a program to decide if a telephone number is a telemarketer number or not, based on the
last four digits. If the number is not a telemarketer number, we should answer the phone, and
otherwise, we should ignore it.
Input Specification
The input will be 4 lines where each line contains exactly one digit in the range from 0 to 9.
Output Specification
Output either ignore if the number matches the pattern for a telemarketer number; otherwise,
output answer.
Sample Input 1
9
6
6
8
 
Output for Sample Input 1
ignore
Explanation of Output for Sample Input 1
The first digit is 9, the last digit is 8, and the second and third digit are both 6, so this is a telemarketer number.
 
Sample Input 2
5
6
6
8
 
Output for Sample Input 2
answer
Explanation of Output for Sample Input 2 The first digit is 5, and so this is not a telemarketer number.
'''


# In[470]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 8 or a == 9:
    if b == c:
        if d == 8 or d == 9:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')


# In[ ]:


'''
A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered from 1 to 4, as shown in the diagram below:
 

 
 
For example, the point A, which is at coordinates (12, 5) lies in quadrant 1 since both its x and y values are positive, and point B lies in quadrant 2 since its x value is negative and its y value is positive.
Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be 0.
 
Input Specification
The first line of input contains the integer x (−1 000 ≤ x ≤ 1 000; x ≠ 0). The second line of input contains the integer
y (−1000 ≤ y ≤ 1000; y ≠ 0).
Output Specification
Output the quadrant number (1, 2, 3 or 4) for the point (x, y).
 
Sample Input 1
12
5

Sample Output 1
1

 Sample Input 2
9
-13

Sample Output 2
4


'''


# In[472]:


x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


# In[ ]:


'''
Antonia and David are playing a game.

Each player starts with 100 points.

The game uses standard six-sided dice and is played in rounds. During one round, each player rolls one die. The player with the lower roll loses the number of points shown on the higher die. If both players roll the same number, no points are lost by either player.

Write a program to determine the ﬁnal scores.

Input
The ﬁrst line of input contains the integer n (1 ≤ n ≤ 15), which is the number of rounds that will be played. On each of the next n lines, will be two integers: the roll of Antonia for that round, followed by a space, followed by the roll of David for that round. Each roll will be an integer between 1 and 6 (inclusive).

Output
The output will consist of two lines. On the ﬁrst line, output the number of points that Antonia has after all rounds have been played. On the second line, output the number of points that David has after all rounds have been played.

Sample Input
4
5 6
6 6
4 3
5 2
Sample Output
94
91
Explanation
After the ﬁrst round, David wins, so Antonia loses 6 points. After the second round, there is a tie and no points are lost. After the third round, Antonia wins, so David loses 4 points. After the fourth round, Antonia wins, so David loses 5 points. In total, Antonia has lost 6 points and David has lost 9 points.
'''


# In[7]:


n = int(input())
list_input = []
for k in range(n):
    str1 = input()
    list1 = str1.split(' ')
    list1 = [int(s) for s in list1]
    list_input.append(list1)
player1 = 100
player2 = 100
for x in range(n):
    list1 = list_input[x]
    if list1[1] > list1[0]:
        player1 = player1 - max(list1)
    elif list1[0] > list1[1]:
        player2-=max(list1)
    else:
        continue
print(player1)
print(player2)


# In[ ]:


'''
Write a program that will read positive input from the user and print the sum of the factors of that number.

Sample input and output specifications are given below

input

2

Output

3
'''


# In[12]:


n = int(input())
list1 = []
for x in range(1, n + 1):
    if n % x == 0:
        list1.append(x)
print(sum(list1))


# In[ ]:


'''
Here (see illustration) is a game board for the game Snakes and Ladders. Each player throws a pair of dice to determine how many squares his/her game piece will advance. If the piece lands on the bottom of a ladder, the piece moves up to the square at the top of the ladder. If the piece lands on the top of a snake, the piece "slides" down to the square at the bottom of the snake. If the piece lands on the last square. The player wins. If the piece cannot advance the number of squares indicated by the dice, the piece is not moved at all.

In order to help you play this game via a cell phone while travelling, you will write a program that simulates your moves on the board shown and, of course, runs on your handheld computer. You will repeatedly throw the dice and enter the result into the program. After each throw the program will report the number of the square where your piece lands.

When the program starts it should assume the piece is on square 1. It should repeatedly read input from the user (a number between 2 and 12) and report the number of the square where the piece lands. In addition, if the piece moves to the last square, the program should print "You Win!" and terminate. If the user enters 0 instead of a number between 2 and 12, the program should print "You Quit!" and terminate.

For clarity, you are to use the board pictured above and you should note that the board has 3 snakes (from 54 to 19, from 90 to 48 and from 99 to 77) and 3 ladders (from 9 to 34, from 40 to 64 and from 67 to 86).
'''


# In[16]:


x = 1
while x != 100:
    diceroll = int(input())
    if x + diceroll > 100:
        print('You are now on square', x)
        continue
    else:
        x += diceroll
    if x == 9:
        x = 34
    if x == 40:
        x = 64
    if x == 67:
        x = 86
    print('You are now on square', x)
print('You Win!')


# In[19]:


'''
A simile is a combination of an adjective and noun that produces a phrase such as "Easy as pie" or "Cold as ice".

Write a program to input n adjectives (1 ≤ n ≤ 5) and m nouns (1 ≤ m ≤ 5), and print out all possible similes. The first two lines of input will provide the values of n and m, in that order followed, one per line, by n adjectives and m nouns.
Your program may output the similes in any order.

Sample Input
3
2
Easy
Smart
Soft
pie
rock
Sample Output
Easy as pie
Easy as rock
Smart as pie
Smart as rock
Soft as pie
Soft as rock
'''


# In[20]:


adjectives = int(input())
nouns = int(input())
list1 = []
list2 = []
for a in range(adjectives):
    list1.append(input())
for b in range(nouns):
    list2.append(input())
for x in list1:
    for y in list2:
        print(x, 'as', y)


# In[ ]:


'''
You have been asked to take a small icon that appears on the screen of a smart telephone and scale it up so it looks bigger on a regular computer screen.

The icon will be encoded as characters (x and *) in a 3 × 3 grid as follows:

*x*

 xx

* *

Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of k means that each character is replaced by a k × k grid consisting only of that character.

Input Format

The input will be a positive integer k (k < 25).

Output Format

The output will be 3k lines, which represent each individual line scaled by a factor of k and repeated k times. A line is scaled by a factor of kby replacing each character in the line with k copies of the character.

Sample Input

3

Sample Output

***xxx***

***xxx***

***xxx***

   xxxxxx

   xxxxxx

   xxxxxx

***   ***

***   ***

***   ***
'''


# In[77]:


k = int(input())
str1 = '*' * k
str2 = 'x' * k
str3 = '*' * k
str1 = str1 + str2 + str3
for x in range(k):
    print(str1)
str1 = ' ' * k
str2 = 'x' * k
str3 = 'x' * k
str1 = str1 + str2 + str3
for x in range(k):
    print(str1)
str1 = '*' * k
str2 = ' ' * k
str3 = '*' * k
str1 = str1 + str2 + str3
for x in range(k):
    print(str1)


# In[27]:


'''
Nikky and Byron are playing a silly game in gym class. Nikky is told by his teacher to walk forward a steps and then walk backward b steps, after which he repeats a forward, b backward, etc. Likewise, Byron is told to walk forward c steps and then walk backward d steps, after which he repeats c forward, d backward, etc. You may assume that a ≥ b and c ≥ d.

Byron and Nikky have the same length of step, and they are required to take their steps simultaneously (that is, Nikky and Byron will both step forward on their first steps at the same time, and this will continue for each step).

Nikky and Byron start walking from one end of a soccer field. After s steps, the gym teacher will blow the whistle. Your task is to figure out who has moved the farthest away from the starting position when the whistle is blown.

Input Format
The input will be the 5 integers a, b, c, d (1 ≤ a, b, c, d ≤ 100), and s (1 ≤ s ≤ 10000), each on a separate line.

Output Format
The output of your program will be one of three possibilities: Nikky if Nikky is farther ahead after s steps are taken; Byron if Byron is farther ahead after s steps are taken; Tied if Byron and Nikky are at the same distance from their starting position after s steps are taken.

Sample Input
4
2
5
3
12
Sample Output
Byron
Explanation
Notice that after 12 steps, Nikky has moved 4 − 2 + 4 − 2 steps, for a total of 4 steps from the starting position, whereas Byron has moved 5 − 3 + 4 steps, for a total of 6 steps from the starting position. Thus, Byron is ahead.
'''


# In[28]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
totalsteps = int(input())
cyclelength_1 = a + b
cyclelength_2 = c + d
cyclenumber_1 = totalsteps // cyclelength_1
cyclenumber_2 = totalsteps // cyclelength_2
stepincrease_1 = cyclenumber_1 * (a - b)
stepincrease_2 = cyclenumber_2 * (c - d)
remainingsteps_1 = totalsteps % cyclelength_1
remainingsteps_2 = totalsteps % cyclelength_2
if remainingsteps_1 <= a:
    stepincrease_1 += remainingsteps_1
else:
    stepincrease_1 = stepincrease_1 + 4 - (remainingsteps_1 - 4)
if remainingsteps_1 <= c:
    stepincrease_2 += remainingsteps_2
else:
    stepincrease_2 = stepincrease_2 + 4 - (remainingsteps_2 - 4)
if stepincrease_1 > stepincrease_2:
    print('Nikky')
elif stepincrease_2 > stepincrease_1:
    print('Bryon')
else:
    print('Tied')


# Margaret has looked at the wind floating over the prairies for a long time. After these observations, she has created a formula that will describe the altitude of a weather balloon launched from her house. In particular, her equation predicts the altitude A (in metres above the ground) at hour t after launching her balloon is:
# 
# $A = -6t^4 + ht^3 + 2t^2 + t$
# where h is an integer value representing the humidity as a value between 0 and 100 inclusive.
# 
# Margaret is curious at what the earliest hour is (if any) that her weather balloon will hit the ground after launch, so long as it is no more than the maximum time, M, that Margaret is willing to wait. You can assume that the weather balloon touches ground when A ≤ 0.
# 
# Input Format
# The input is two non-negative integers: h (0 ≤ h ≤ 100), the humidity factor, followed by M (0 < M < 240), the maximum number of hours Margaret will wait for the weather balloon to return to ground.
# 
# Output Format
# The output will be one of the following possibilities:
# 
# The balloon does not touch ground in the given time.
# The balloon first touches ground at hour:
# T
# where T is a positive integer value representing the earliest hour when the balloon has altitude less than or equal to zero.
# 
# where T is a positive integer value representing the earliest hour when the balloon has altitude less than or equal to zero.
# 
# Sample Cases
# Input
# 30
# 10
# 
# Output
# The balloon first touches ground at hour:
# 6
# Input
# 70
# 10
# 
# Output
# The balloon does not touch ground in the given time.
# 

# In[4]:


humidity = int(input())
time = int(input())
for t in range(1, time + 1):
    a = ((-6) * (t ** 4)) + humidity * (t ** 3) + 2 * (t ** 2) + t
    if a <= 0:
        print('The balloon first touches ground at hour:')
        print(t)
        break
if t == time:
    print('The balloon does not touch ground in the given time.')


# In[74]:


import pandas as pd
df = pd.read_csv('df_10_0.csv', sep='\t')
df.head()


# In[75]:


df['pw_score'].isnull().sum()


# An artist wants to construct a sign whose letters will rotate freely in the breeze. In order to do this, she must only use letters that are not changed by rotation of 180 degrees: I, O, S, H, Z, X, and N.
# 
# Write a program that reads a word and determines whether the word can be used on the sign.
# 
# Input
# The input will consist of one word, all in uppercase letters, with no spaces. The maximum length of the word will be 30 letters, and the word will have at least one letter in it.
# 
# Output
# Output YES if the input word can be used on the sign; otherwise, output NO.
# 
# Sample Input 1
# SHINS
# Sample Output 1
# YES
# Sample Input 2
# NOISE
# Sample Output 2
# NO

# In[84]:


count = 0
str1 = input()
list1 = list(str1)
list2 = ['I','O','S','H','Z','X','N']
for x in list1:
    if x in list2:
        count += 1
    else:
        break
if count == len(list1):
    print('YES')
else:
    print('NO')


# Americans spell differently from Canadians. Americans write "neighbor" and "color" while Canadians write "neighbour" and "colour".
# 
# Write a program to help Americans translate to Canadian.
# 
# You should input a word (not to exceed 64 letters) and if the word appears to use American spelling, the program should echo the Canadian spelling for the same word. If the word does not appear to use American spelling, it should be output without change. When the user types "quit!" the program should terminate.
# 
# The rules for detecting American spelling are quite naive: If the word has more than four letters and has a suffix consisting of a consonant followed by "or", you may assume it is an American spelling, and that the equivalent Canadian spelling replaces the "or" by "our". Note: you should treat the letter "y" as a vowel.
# 
# Sample Input
# color
# for
# taylor
# quit!
# Sample Output
# colour
# for
# taylour

# In[92]:


list1 = []
a = input()
while a != 'quit!':
    list1.append(a)
    a = input()
vowels = ['a', 'e', 'i', 'o', 'u']
for x in list1:
    if len(x) > 4:
        if x[-2:] == 'or':
            if x[-3] not in vowels:
                y = x.replace('or', 'our')
                print(y)
            else:
                print(x)
        else:
            print(x)
    else:
        print(x)


# Problem Description
# 
# You supervise a small parking lot which has N parking spaces.
# 
# Yesterday, you recorded which parking spaces were occupied by cars and which were empty.
# 
# Today, you recorded the same information.
# 
# How many of the parking spaces were occupied both yesterday and today?
# 
# Input Specification
# 
# The first line of input contains the integer N (1 ≤ N ≤ 100). The second and third lines of input
# 
# contain N characters each. The second line of input records the information about yesterday’s
# 
# parking spaces, and the third line of input records the information about today’s parking spaces.
# 
# Each of these 2N characters will either be C to indicate an occupied space or . to indicate it was
# 
# an empty parking space.
# 
# Output Specification
# 
# Output the number of parking spaces which were occupied yesterday and today.
# 
# Sample Input 1
# 
# 5
# 
# CC..C
# 
# .CC..
# 
# Output for Sample Input 1
# 
# 1
# 
# Explanation of Output for Sample Input 1
# 
# Only the second parking space from the left was occupied yesterday and today.
# 
# Sample Input 2
# 
# 7
# 
# CCCCCCC
# 
# C.C.C.C
# 
# Output for Sample Input 2
# 
# 4
# 
# Explanation of Output for Sample Input 2
# 
# The first, third, fifth, and seventh parking spaces were occupied yesterday and today

# In[95]:


n = int(input())
park1 = input()
park2 = input()
count = 0
list1 = list(park1)
list2 = list(park2)
for k, x in enumerate(list1):
    if x == 'C' and list2[k] == 'C':
        count += 1
print(count)


# A palindrome is a word which is the same when read forwards as it is when read backwards. For example, mom and anna are two palindromes.
# 
# A word which has just one letter, such as a, is also a palindrome.
# 
# Given a word, what is the longest palindrome that is contained in the word? That is, what is the longest palindrome that we can obtain, if we are allowed to delete characters from the beginning and/or the end of the string?
# 
# Input Format
# The input will consist of one line, containing a sequence of at least 1 and at most 40 lowercase letters.
# 
# Output Format
# Output the total number of letters of the longest palindrome contained in the input word.
# 
# Sample Input 1
# banana
# Sample Output 1
# 5
# Explanation 1
# The palindrome anana has 5 letters.
# 
# Sample Input 2
# abracadabra
# Sample Output 2
# 3
# Explanation 2
# The palindromes aca and ada have 3 letters, and there are no other palindromes in the input which are longer.
# 
# Sample Input 3
# abba
# Sample Output 3
# 4

# In[103]:


def checkifpalindrome(list1):
    if list1 == list1[::-1]:
        return True
    return False


# In[107]:


str1 = input()
list1 = list(str1)
listofpalindromes = []
for start in range(len(list1)+1):
    for end in range(start+1, len(list1)+1):
        if checkifpalindrome(list1[start : end]) == True:
            listofpalindromes.append(len(list1[start : end]))
print(max(listofpalindromes))


# Problem Description
# Your teacher likes to give multiple choice tests. One benefit of giving these tests is that they are easy to mark, given an answer key. The other benefit is that students believe they have a one-in-five chance of getting the correct answer, assuming the multiple choice possibilities are A,B,C,D or E.
# 
# Write a program that your teacher can use to grade one multiple choice test.
# 
#  
# 
# Input Specification
# The input will contain the number N (0 < N < 10000) followed by 2N lines. The 2N lines are composed of N lines of student responses (with one of A,B,C,D or E on each line), followed by N lines of correct answers (with one of A,B,C,D or E on each line), in the same order as the student answered the questions (that is, if line i is the student response, then line N + i contains the correct answer to that question).
# 
#  
# 
# Output Specification
# Output the integer C (0 ≤ C ≤ N ) which corresponds to the number of questions the student answered correctly.
# 
#  
# 
# Sample Input 1
# 3
# 
# A B C A C B
# 
#  
# 
# Output for Sample Input 1
# 1
# 
#  
# 
# Sample Input 2
# 3
# 
# A A A A B A
# 
#  
# 
# Output for Sample Input 2
# 2

# In[116]:


n = int(input())
str1 = input()
count = 0
list1 = str1.split(' ')
sublist1 = list1[:n]
sublist2 = list1[n:]
for k, x in enumerate(sublist1):
    if x == sublist2[k]:
        count += 1
print(count)


# In Sweden, there is a simple child’s game similar to Pig Latin called Ro¨varspra˚ket (Robbers Lan- guage).
# 
# In the CCC version of Ro¨varspra˚ket, every consonant is replaced by three letters, in the following order:
# 
#  
# 
# •   the consonant itself;
# 
# •   the vowel closest to the consonant in the alphabet (e.g., if the consonant is d, then the closest vowel is e), with the rule that if the consonant falls exactly between two vowels, then the vowel closer to the start of the alphabet will be chosen (e.g., if the consonant is c, then the closest vowel is a);
# 
# •   the next consonant in the alphabet following the original consonant (e.g., if the consonant is d, then the next consonant is f) except if the original consonant is z, in which case the next consonant is z as well.
# 
#  
# 
# Vowels in the word remain the same. (Vowels are a, e, i, o, u and all other letters are consonants.) Write a program that translates a word from English into Ro¨varspra˚ket.
# 
# Input Specification
# The input consists of one word entirely composed of lower-case letters. There will be at least one letter and no more than 30 letters in this word.
# 
#  
# 
# Output Specification
# Output the word as it would be translated into Ro¨varspra˚ket on one line.
# 
#  
# 
# Sample Input 1
# Joy
# 
#  
# 
# Output for Sample Input 1
# jikoyuz
# 
#  
# 
# Sample Input 2
# ham
# 
#  
# 
# Output for Sample Input 2
# hijamon

# In[131]:


def findclosestvowel(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_ind = [alphabet.index(s) for s in vowels]
    k = alphabet.index(x)
    distances = [abs(k - s) for s in v_ind]
    amin = min(distances)
    for m, a in enumerate(distances):
        if amin == a:
            return(vowels[m])
findclosestvowel('c')


# In[141]:


str1 = input()
str1 = str1.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in alphabet if x not in vowels]
list1 = list(str1)
str_out = ''
for x in list1:
    if x in consonants:
        str2 = x
        a = findclosestvowel(x)
        str2 += a
        consonants.append('b')
        b = consonants[consonants.index(x) + 1]
        str2 += b
        str_out += str2
    else:
        str_out += x
print(str_out)


# In[ ]:





# In[63]:


import math
intArr1 = [1,2,3,4,5]
amin = math.inf
amax = -math.inf
for x in intArr1:
    if x < amin:
        amin = x
    if x > amax:
        amax = x
print(amin)
print(amax)


# ane's family has just moved to a new city and today is her first day of school. She has a list of instructions for walking from her home to the school. Each instruction describes a turn she must make. For example, the list
# 
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# means that she must turn right onto Queen Street, then turn right onto Fourth Street, then finally turn right into the school. Your task is to write a computer program which will create instructions for walking in the opposite direction: from her school to her home.
# 
# The input and output for your program will be formatted like the samples below. You may assume that Jane's list contains at least two but at most five instructions, and you may assume that each line contains at most 10 characters, all of them capital letters. The last instruction will always be a turn into the "SCHOOL".
# 
# Sample Input 1
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# Sample Output 1
# Turn LEFT onto FOURTH street.
# Turn LEFT onto QUEEN street.
# Turn LEFT into your HOME.
# Sample Input 2
# L
# MAIN
# R
# SCHOOL
# Sample Output 2
# Turn LEFT onto MAIN street.
# Turn RIGHT into your HOME.

# In[71]:


list1 = []
a = input()
while a != 'SCHOOL':
    list1.append(a)
    a = input()
list1.append(a)
list1 = list1[::-1]
list1 = list1[1:]
a = list1.pop(-1)
for k, x in enumerate(list1):
    if x == 'R':
        print('Turn LEFT onto', list1[k + 1], 'street.')
    if x == 'L':
        print('Turn RIGHT onto', list1[k + 1], 'street.')
if a == 'R':
    print('Turn LEFT into your HOME.')
if a == 'L':
    print('Turn RIGHT into your HOME.')


# Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total.
# 
# Given a 4 × 4 square of numbers, determine if it is a magic square.
# 
# Input Format
# The input consists of four lines, each line having 4 space-separated integers.
# 
# Output Format
# Output either magic if the input is a magic square, or not magic if the input is not a magic square.
# 
# Sample Input 1
# 16 3 2 13
# 5 10 11 8
# 9 6 7 12
# 4 15 14 1
# Sample Output 1
# magic
# Explanation 1
# Notice that each row adds up to 34, and each column also adds up to 34.
# 
# Sample Input 2
# 5 10 1 3
# 10 4 2 3
# 1 2 8 5
# 3 3 5 0
# Sample Output 2
# not magic
# Explanation 2
# Notice that the top row adds up to 19, but the rightmost column adds up to 11.

# In[104]:


str1 = input()
str2 = input()
str3 = input()
str4 = input()
list1 = str1.split(' ')
list2 = str2.split(' ')
list3 = str3.split(' ')
list4 = str4.split(' ')
list1 = [int(s) for s in list1]
list2 = [int(s) for s in list2]
list3 = [int(s) for s in list3]
list4 = [int(s) for s in list4]
if sum(list1) == sum(list2) and sum(list2) == sum(list3) and sum(list3) == sum(list4):
    asum = sum(list1)
    count = 0
    for k in range(4):
        if list1[k] + list2[k] + list3[k] + list4[k] == asum:
            print(list1[k] + list2[k] + list3[k] + list4[k])
            count += 1
    if count == 4:
        print('magic')
    else:
        print('not magic')
else:
    print('not magic')


# In the CCC version of the game, there are 10 possible dollar amounts: $100, $500, $1,000, $5,000,
# $10,000, $25,000, $50,000, $100,000, $500,000, $1,000,000 sealed in imaginary briefcases. These dollar
# amounts are numbered 1 – 10 (i.e. 1 → $100, 2 → $500, 3 → $1,000, ..., 10 → $1,000,000). Before the
# game starts the contestant will have chosen one of the briefcases as his/hers to possibly keep. During the
# game, some of the ten possible dollar amounts have been eliminated from the game because the
# contestant has selected some of the other briefcases and revealed the amounts inside.
# At some point, the contestant will stop opening briefcases, and a “Banker” will offer the contestant cash in
# exchange for what might be contained in his/her chosen briefcase. Then the contestant is asked: “Deal or
# No Deal?”.
# Write a program that helps a player decide if he/she should choose “deal” or “no deal”, by calculating the
# average of the remaining amounts (i.e., all unopened briefcases, including his/her “own” briefcase), and
# comparing that value to the “Banker’s” offer. If the offer is higher than the average, then the player should
# ”deal” otherwise, the player should say “no deal”.
# Input
# The user must input a number n (1 ≤ n < 10) which indicates how many cases have been opened so far,
# followed by a list of integers between 1 and 10 representing the values in the game that have been
# eliminated, followed by the “Banker’s” offer. For example: 3 2 5 10 300 indicates that briefcases
# containing $500, $10,000, and $1,000,000 have been eliminated and the Banker’s offer is $300. You may
# assume that no duplicate case numbers are entered for the eliminated values, and you may assume that
# the “Banker’s” offer is an integer greater than 10.
# Output
# The program will print out one of two statements: “deal” or “no deal”.
# Sample Input 1
# 2
# 3
# 8
# 198000
# Sample Output 1
# no deal
# Sample Input 2
# 8
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 400
# Sample Output 2
# deal

# In[111]:


n = int(input())
list1 = []
for x in range(n):
    list1.append(int(input()))
offer = int(input())
dict1 = {1:100, 2:500, 3:1000, 4:5000, 5:10000, 6:25000, 7:50000, 8:100000, 9:500000, 10:1000000}
count = 0
for x in list1:
    count += dict1[x]
if count > offer:
    print('deal')
else:
    print('no deal')


# The CEMC is organizing a workshop with an activity involving pairs of students. They decided to assign
# partners ahead of time. You need to determine if they did this consistently. That is, whenever A is a partner
# of B, then B is also a partner of A, and no one is a partner of themselves.
# Input
# The input consists of three lines. The first line consists of an integer N (1 < N ≤ 30), which is the number of
# students in the class. The second line contains the first names of the N students separated by single
# spaces. (Names contain only uppercase or lowercase letters, and no two students have the same first
# name). The third line contains the same N names in some order, separated by single spaces.
# The positions of the names in the last two lines indicate the assignment of partners: the i-th name on the
# second line is the assigned partner of the i-th name on the third line.
# Output
# The output will be good if the two lists of names are arranged consistently, and bad if the arrangement of
# partners is not consistent.
# Sample Input 1
# 4
# Ada Alan Grace John
# John Grace Alan Ada
# Sample Output 1
# good
# Explanation for Sample 1
# Ada and John are partners, and Alan and Grace are partners. This arrangement is consistent.
# Sample Input 2
# 7
# Rich Graeme Michelle Sandy Vlado Ron Jacob
# Ron Vlado Sandy Michelle Rich Graeme Jacob
# Sample Output 2
# bad
# Explanation for Sample 1
# Graeme is partnered with Vlado, but Vlado is partnered with Rich. This is not consistent. It is also
# inconsistent because Jacob is partnered with himself.

# In[8]:


n = input()
str1 = input()
str2 = input()
def assigning_partners(n, str1, str2):
    confirmation = 0
    list1 = str1.split(' ')
    list2 = str2.split(' ')
    for k, x in enumerate(list1):
        if list2[k] == list1[(len(list1) - k - 1)]:
            confirmation += 1
    if confirmation == len(list1):
        return 'good'
    return 'bad'
result = assigning_partners(n, str1, str2)
print(result)


# You are trying to pass the time while at the optometrist. You notice there is a grid of four numbers:
# 
#  
# 
# 1
# 
# 2
# 
# 3
# 
# 4
# 
#  
# 
# You see lots of mirrors and lenses at the optometrist, and wonder how flipping the grid horizontally or vertically would change the grid.
# 
# Specifically, a “horizontal” flip (across the horizontal centre line) would take the original grid of four numbers and result in:
# 
#  
# 
# 3
# 
# 4
# 
# 1
# 
# 2
# 
#  
# 
# A “vertical” flip (across the vertical centre line) would take the original grid of four numbers and result in:
# 
#  
# 
# 2
# 
# 1
# 
# 4
# 
# 3
# 
#  
# 
# Your task is to determine the final orientation of the numbers in the grid after a sequence of hori- zontal and vertical flips.
# 
#  
# 
# Input Specification
# The input consists of one line, composed of a sequence of at least one and at most 1 000 000 characters. Each character is either H, representing a horizontal flip, or V, representing a vertical flip.
# 
# For 8 of the 15 available marks, there will be at most 1 000 characters in the input.
# 
#  
# 
# Output Specification
# Output the final orientation of the four numbers. Specifically, each of the two lines of output will contain two integers, separated by one space.
# 
#  
# 
# Sample Input 1
# HV
# 
#  
# 
# Output for Sample Input 1
# 4 3
# 
# 2 1
# 
# 
# Sample Input 2
# VVHH
# 
# 
# Output for Sample Input 2
# 1 2
# 3 4

# In[12]:


str1 = input()
list1 = list(str1)
matrix = [[1,2], [3,4]]
for x in list1:
    if x == 'H':
        a = matrix.pop(0)
        matrix.append(a)
    if x == 'V':
        matrix = [[matrix[0][1], matrix[0][0]], [matrix[1][1], matrix[1][0]]]
for x in matrix:
    x = [str(s) for s in x]
    print(' '.join(x))


# **You must solve this using ArrayList**
# 
# Jane's family has just moved to a new city and today is her first day of school. She has a list of instructions for walking from her home to the school. Each instruction describes a turn she must make. For example, the list
# 
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# means that she must turn right onto Queen Street, then turn right onto Fourth Street, then finally turn right into the school. Your task is to write a computer program which will create instructions for walking in the opposite direction: from her school to her home.
# 
# The input and output for your program will be formatted like the samples below. You may assume that Jane's list contains at least two but at most five instructions, and you may assume that each line contains at most 10 characters, all of them capital letters. The last instruction will always be a turn into the "SCHOOL".
# 
# Sample Input 1
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# Sample Output 1
# Turn LEFT onto FOURTH street.
# Turn LEFT onto QUEEN street.
# Turn LEFT into your HOME.
# Sample Input 2
# L
# MAIN
# R
# SCHOOL
# Sample Output 2
# Turn LEFT onto MAIN street.
# Turn RIGHT into your HOME.

# In[18]:


list1 = []
a = input()
while a != 'SCHOOL':
    list1.append(a)
    a = input()
list1.append(a)
list1 = list1[::-1]
list1 = list1[1:]
a = list1.pop(-1)
for k, x in enumerate(list1):
    if x == 'R':
        print('Turn LEFT onto', list1[k + 1], 'street.')
    if x == 'L':
        print('Turn RIGHT onto', list1[k + 1], 'street.')
if a == 'R':
    print('Turn LEFT into your HOME.')
if a == 'L':
    print('Turn RIGHT into your HOME.')


# Write a program that will read a sentence from the user and print all the words in the sentence. You are nor allowed to use the split function in a y language.
# 
# Sample input and output specifications are given below.
# 
# Input
# 
# the red cat sat on the mat
# 
# Output
# 
# the
# 
# red
# 
# cat
# 
# sat
# 
# on
# 
# the
# 
# mat

# In[21]:


str1 = input()
list1 = list(str1)
list1.append(' ')
str1 = ''
for x in list1:
    if x != ' ':
        str1 += x
    else:
        print(str1)
        str1 = ''


# Problem Description You decide to go for a very long drive on a very straight road. Along this road are five cities. As you travel, you record the distance between each pair of consecutive cities. You would like to calculate a distance table that indicates the distance between any two of the cities you have encountered. Input Specification The first line contains 4 positive integers less than 1000, each representing the distances between consecutive pairs of consecutive cities: specifically, the ith integer represents the distance between city i and city i + 1. Output Specification The output should be 5 lines, with the ith line (1 ≤ i ≤ 5) containing the distance from city i to cities 1, 2, ... 5 in order, separated by one space. 
# 
# Sample Input 
# 
# 3 10 12 5 
# 
# Output for Sample Input
# 
#  0 3 13 25 30 
# 
#  3 0 10 22 27 
# 
# 13 10 0 12 17
# 
#  25 22 12 0 5 
# 
#  30 27 17 5 0 
# 
# Explanation of Output for Sample Input The first line of output contains:
# 
#  • 0, since the distance from city 1 to city 1 is 0; 
# 
# • 3, since the distance between city 1 and city 2 is 3; 
# 
# • 13, since the distance between city 1 and city 3 is 3 + 10 = 13; 
# 
# • 25, since the distance between city 1 and city 4 is 3 + 10 + 12 = 25; 
# 
# • 30, since the distance between city 1 and city 5 is 3 + 10 + 12 + 5 = 30.

# In[29]:


str1 = input()
list1 = str1.split()
list1 = [int(s) for s in list1]
for start in range(len(list1) + 1):
    for end in range(len(list1) + 1):
        dist = sum(list1[min(start, end) : max(start, end)])
        print(dist, end = ' ')
    print('\r')


# Boring is a type of drilling, specifically, the drilling of a tunnel, well, or hole in the earth. With some recent events, such as the Deepwater Horizon oil spill and the rescue of Chilean miners, the public became aware of the sophistication of the current boring technology. Using the technique known as geosteering, drill operators can drill wells vertically, horizontally, or even on a slant angle.
# 
# A well plan is prepared before drilling, which specifies a sequence of lines, representing a geometrical shape of the future well. However, as new information becomes available during drilling, the model can be updated and the well plan modified.
# 
# Your task is to write a program that verifies validity of a well plan by verifying that the borehole will not intersect itself. A two-dimensional well plan is used to represent a vertical cross-section of the borehole, and this well plan includes some drilling that has occurred starting at (0, −1) and moving to (−1, −5). You will encode in your program the current well plan shown in the figure below:
# 
# 
# 
# Input Format
# The input consists of a sequence of drilling command pairs. A drilling command pair begins with one of four direction indicators (d for down, u for up, l for left, and r for right) followed by a positive length. There is an additional drilling command indicated by q (quit) followed by any integer, which indicates the program should stop execution. You can assume that the input is such that the drill point will not:
# 
# rise above the ground, nor
# be more than 200 units below ground, nor
# be more than 200 units to the left of the original starting point, nor
# be more than 200 units to the right of the original starting point.
# Output Format
# The program should continue to monitor drilling assuming that the well shown in the figure has already been made. As we can see (−1, −5) is the starting position for your program. After each command, the program must output one line with the coordinates of the new position of the drill, and one of the two comments safe, if there has been no intersection with a previous position or DANGER if there has been an intersection with a previous borehole location. After detecting and reporting a self-intersection, your program must stop.
# 
# Sample Cases
# Input
# l 2
# d 2
# r 1
# q 0
#  
# 
# Output
# -3 -5 safe
# -3 -7 safe
# -2 -7 safe
# Input
# r 2
# d 10
# r 4
#  
# 
# Output
# 1 -5 safe
# 1 -15 DANGER
# 

# In[55]:


b = input()
list1 = []
list_done = [[0,-1], [0,-2], [0,-3], [1,-3], [2,-3], [3,-3], [3,-4], [3,-5], [4,-5], [5,-5], [5,-4], [5,-3],
           [6,-3], [7,-3], [7,-4], [7,-5], [7,-6], [7,-7], [6,-7], [5,-7], [4,-7], [3,-7], [2,-7], [1,-7],
           [0,-7], [-1,-7], [-1,-6], [-1,-5]]
start = [-1, -5]
while list(b)[0] != 'q':
    list1.append(b)
    str1 = b
    a = 0
    list2 = str1.split(' ')
    list2 = [list2[0], int(list2[1])]
    if list2[0] == 'r':
        for x in range(1, list2[1] + 1):
            if [start[0] + x, start[1]] in list_done:
                print(start[0] + list2[1], start[1], 'DANGER')
        start = [start[0] + list2[1], start[1]]
        print(start[0], start[1], 'safe')
    if list2[0] == 'l':
        for x in range(1, list2[1] + 1):
            if [start[0] - x, start[1]] in list_done:
                a = 1
                print(start[0] - list2[1], start[1], 'DANGER')
        if a == 1:
            break
        start = [start[0] - list2[1], start[1]]
        print(start[0], start[1], 'safe')           
    if list2[0] == 'd':
        for x in range(1, list2[1] + 1):
            if [start[0], start[1] - x] in list_done:
                a = 1
                print(start[0], start[1] - list2[1], 'DANGER')
                break
        if a == 1:
            break
        start = [start[0], start[1] - list2[1]]
        print(start[0], start[1], 'safe')
    if list2[0] == 'u':
        for x in range(1, list2[1] + 1):
            if [start[0], start[1] + x] in list_done:
                a = 1
                print(start[0], start[1] + list2[1], 'DANGER')
                break
        if a == 1:
            break
        start = [start[0], start[1] + list2[1]]
        print(start[0], start[1], 'safe')
    b = input()


# In[ ]:


l 2
d 2
r 1
q 0


# In[49]:


list1 = ['l 2', 'd 2', 'r 1']
list1 = ['r 2', 'd 10', 'r 4']

list_done = [[0,-1], [0,-2], [0,-3], [1,-3], [2,-3], [3,-3], [3,-4], [3,-5], [4,-5], [5,-5], [5,-4], [5,-3],
           [6,-3], [7,-3], [7,-4], [7,-5], [7,-6], [7,-7], [6,-7], [5,-7], [4,-7], [3,-7], [2,-7], [1,-7],
           [0,-7], [-1,-7], [-1,-6], [-1,-5]]
start = [-1, -5]
a = 0
for str1 in list1:
    list2 = str1.split(' ')
    list2 = [list2[0], int(list2[1])]
    print(list2)
    if list2[0] == 'r':
        for x in range(1, list2[1] + 1):
            if [start[0] + x, start[1]] in list_done:
                print([start[0] + list2[1], start[1]], 'DANGER')
        start = [start[0] + list2[1], start[1]]
        print(start, 'safe')
    if list2[0] == 'l':
        for x in range(1, list2[1] + 1):
            if [start[0] - x, start[1]] in list_done:
                a = 1
                print([start[0] - list2[1], start[1]], 'DANGER')
        if a == 1:
            break
        start = [start[0] - list2[1], start[1]]
        print(start, 'safe')            
    if list2[0] == 'd':
        for x in range(1, list2[1] + 1):
            if [start[0], start[1] - x] in list_done:
                a = 1
                print([start[0], start[1] - list2[1]], 'DANGER')
                break
        if a == 1:
            break
        start = [start[0], start[1] - list2[1]]
        print(start, 'safe')
    if list2[0] == 'u':
        for x in range(1, list2[1] + 1):
            if [start[0], start[1] + x] in list_done:
                a = 1
                print([start[0], start[1] + list2[1]], 'DANGER')
                break
        if a == 1:
            break
        start = [start[0], start[1] + list2[1]]
        print(start, 'safe')


# You are hosting a party and do not have room to invite all of your friends. You use the following unemotional mathematical method to determine which friends to invite.
# 
# Number your friends 1, 2, …, K and place them in a list in this order. Then perform m rounds. In each round, use a number to determine which friends to remove from the ordered list.
# 
# The rounds will use numbers r1, r2, …, rm. In round i remove all the remaining people in positions that are multiples of ri (that is, ri, 2ri, 3ri, …) The beginning of the list is position 1.
# 
# Output the numbers of the friends that remain after this removal process.
# 
# Input
# The first line of input contains the integer K (1 ≤ K ≤ 100). The second line of input contains the integer m (1 ≤ m ≤ 10), which is the number of rounds of removal. The next m lines each contain one integer. The i-th of these lines (1 ≤ i ≤ m) contains ri (2 ≤ ri ≤ 100) indicating that every person at a position which is multiple of ri should be removed.
# 
# Output
# The output is the integers assigned to friends who were not removed. One integer is printed per line in increasing sorted order.
# 
# Sample Input
# 10
# 2
# 2
# 3
# Sample Output
# 1
# 3
# 7
# 9
# Explanation
# Initially, our list of invitees is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. There will be two rounds of removals. After the first round of removals, we remove the even positions (i.e., every second position), which causes our list of invitees to be 1, 3, 5, 7, 9. After the second round of removals, we remove every 3rd remaining invitee: thus, we keep 1 and 3, remove 5 and keep 7 and 9, which leaves us with an invitee list of 1, 3, 7, 9.

# In[92]:


n = int(input())
m = int(input())
list1 = []
for x in range(m):
    list1.append(int(input()))
list_friends = []
for k in range(1, n + 1):
    list_friends.append(k)
for a in list1:
    list2 = []
    for k, b in enumerate(list_friends):
        if (k + 1) % a != 0:
            list2.append(b)
    list_friends = list2
for x in list_friends:
    print(x)


# '''
# 
# Return the Nth Prime Number
# 
# 
# 
# '''
# 
# def intNthPrime(intN):
# 
#     pass
# 
# 
# 
# copy and paste the following along with your function definition to test your program
# 
# print(intNthPrime(1))
# 
# print(intNthPrime(2))
# 
# print(intNthPrime(100))

# In[105]:


def isitprime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


# In[111]:


def NthPrime(n):
    a = 2
    count = 0
    while True:
        if isitprime(a) == True:
            count += 1
        if count == n:
            return a
        a += 1


# '''
# 
# Taking three string parameters str1, str2 and str3 replace
# 
# every occurance of str2 in str1 by str3
# 
# '''
# 
# def replaceAll(str1, str2, str3):
# 
#     pass
# 
# Copy and paste the following test cases to test your program
# 
# print(replaceAll("the red cat sat on the mat", "the", "tiger"))
# 
# print(replaceAll("the red cat sat on the mat","the", ""))

# In[136]:


def mysplit(str1):
    list2 = []
    list1 = list(str1)
    list1.append(' ')
    str1 = ''
    for x in list1:
        if x != ' ':
            str1 += x
        else:
            list2.append(str1)
            str1 = ''
    return list2
mysplit('the red cat sat on the mat')


# In[139]:


def replaceAll(str1,str2,str3):
    list1 = mysplit(str1)
    list2 = []
    for x in list1:
        if x == str2:
            list2.append(str3)
        else:
            list2.append(x)
    newstr = ' '.join(list2)
    return newstr


# In[140]:


print(replaceAll("the red cat sat on the mat", "the", "tiger"))
print(replaceAll("the red cat sat on the mat","the", ""))


# ou've been snowed in at your summer residence. And without the Internet! Unfortunately, this means you're going to have rely on using the phone to get what you need to survive: pizza, pop, and the latest video games.
# 
# Often times, companies replace the digits in their phone numbers with characters to make their phone numbers more memorable. Because apparently, it's easier to remember 416-BUY-MORE than it is to remember 416-289-6673. Some companies even add extra digits or characters (like 604-PIZZABOX) but any digits after the 10th are irrelevant.
# 
# Since it's getting tedious to do the conversion by hand, write a program to help change all the phone numbers in your phone book to the form xxx-xxx-xxxx, using the below image to assist you.
# 
# 1 ABC2 DEF3 GHI4 JKL5 MNO6 PQRS7 TUV8 WXYZ9 * 0 #
# 
# Input
# Input consists of a series of test cases. The first line consists of an integer t, the number of test cases. Following this are t lines consisting of alpha-numeric characters separated by hyphens, representing valid phone numbers. All letters will be in uppercase. No line is longer than 40 characters.
# 
# Output
# For each test case, output the phone number in the form xxx-xxx-xxxx to the screen.
# 
# Sample Input
# 5
# 88-SNOW-5555
# 519-888-4567
# BUY-MORE-POP
# 416-PIZZA-BOX
# 5059381123
# 
# Sample Output
# 887-669-5555
# 519-888-4567
# 289-667-3767
# 416-749-9226
# 505-938-1123

# In[153]:


n = int(input())
list_phones = []
for x in range(n):
    list_phones.append(input())
list_phones = ['88-SNOW-5555', '519-888-4567', 'BUY-MORE-POP', '416-PIZZA-BOX', '5059381123']
dict1 = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6,
        'o':6, 'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
for x in list_phones:
    x = x.lower()
    list1 = list(x)
    for y in list1:
        if y in alphabet:
            x = x.replace(y, str(dict1[y]))
    list1 = list(x)
    list1 = [m for m in list1 if m != '-']
    list1.insert(3, '-')
    list1.insert(7, '-')
    list1 = list1[:12]
    str1 = ''.join(list1)
    print(str1)


# In[2]:


def find_last_syllable(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list1 = list(str1)
    list_reverse = list1[::-1]
    count = 0
    for b in list_reverse:
        if b == ' ':
            count += 1
    if count > 0:
        list_reverse = list_reverse[:list_reverse.index(' ')]
        list1 = list_reverse[::-1]
    count = 0
    for x in list1:
        if x not in vowels:
            count += 1
    if count == len(list1):
        return str1
    for a in list_reverse:
        if a in vowels:
            index = list_reverse.index(a)
            break
    str2 = list_reverse[:index + 1][::-1]
    return ''.join(str2)


# In[185]:


def rhyme(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if find_last_syllable(str1) == find_last_syllable(str2):
        return True
    return False


# In[189]:


def find_last_syllable(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list1 = list(str1)
    list_reverse = list1[::-1]
    count = 0
    for b in list_reverse:
        if b == ' ':
            count += 1
    if count > 0:
        list_reverse = list_reverse[:list_reverse.index(' ')]
        list1 = list_reverse[::-1]
    count = 0
    for x in list1:
        if x not in vowels:
            count += 1
    if count == len(list1):
        return str1
    for a in list_reverse:
        if a in vowels:
            index = list_reverse.index(a)
            break
    str2 = list_reverse[:index + 1][::-1]
    return ''.join(str2)
def rhyme(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if find_last_syllable(str1) == find_last_syllable(str2):
        return True
    return False
n = int(input())
for x in range(n):
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    if rhyme(line1, line2) == True and rhyme(line2, line3) == True and rhyme(line3, line4) == True:
        print('perfect')
        continue
    elif rhyme(line1, line2) == True and rhyme(line3, line4) == True:
        print('even')
        continue
    elif rhyme(line1, line3) == True and rhyme(line2, line4) == True:
        print('cross')
        continue
    elif rhyme(line1, line4) == True and rhyme(line2, line3) == True:
        print('shell')
        continue
    else:
        print('free')
        continue


# Write a recursive method called nthFactorial() that will take an integer argument n and return the nth Factorial. nthFactorial = 1 * 1 * 2 * .. * n.
# 
# Java: Once you finished writing your method copy and paste the following in the main to test your method
# 
# System.out.println(nthFactorial(5));
# 
# System.out.println(nthFactorial(3));
# 
# System.out.println(nthFactorial(0));
# 
# Python:
# 
# print(nthFactorial(5))
# 
# print(nthFactorial(3))
# 
# print(nthFactorial(0))

# In[8]:


def nthFactorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return(nthFactorial(n - 1) * n)
print(nthFactorial(5))

print(nthFactorial(3))

print(nthFactorial(0))


# Read a positive integer from the user and use a recursive function convert into into a binary. 
# 
# Sample input and output specifications are below
# 
# Input
# 
# 2
# 
# Output
# 
# 10
# 
# Input
# 
# 8
# 
# Output
# 
# 1000

# In[20]:


def decimal_to_binary(n):
    if n == 1:
        return '1'
    else:
        if n % 2 == 0:
            return(decimal_to_binary(n // 2) + '0')
        else:
            return(decimal_to_binary(n // 2) + '1')
n = int(input())
print(int(decimal_to_binary(n)))


# Write a recursive java method called removeall() which takes two string arguments and remove every occurrence of the second string from the first string and return the first string.
# 
# Java: Copy and paste the following test cases test your program in the main.
# 
# System.out.println(removeAll("the red cat sat on the mat", "the"));
# 
# System.out.println(removeAll("the red cat sat on the mat", "blue"));
# 
# Python:
# print(removeAll("the red cat sat on the mat", "the"))
# 
# print(removeAll("the red cat sat on the mat", "blue"))

# In[36]:


def removeAll(str1, str2):
    if str2 not in str1:
        return str1
    else:
        index = str1.index(str2)
        str1 = str1[:index] + str1[index + len(str2):]
        return(removeAll(str1, str2))
print(removeAll("the red cat sat on the mat", "the"))

print(removeAll("the red cat sat on the mat", "blue"))


# Write a recursive java method  called nthFibonacci()that takes an integer argument n and return the nth Fibonacci number. 
# 
# Java: Copy and paste the following test cases in your main to test your method
# 
# System.out.println(nthFibonacci(2));
# 
# System.out.println(nthFibonacci(12));
# 
# System.out.println(nthFibonacci(1));
# 
# Pyhon:
# 
# print(nthFibonacci(2))
# 
# print(nthFibonacci(12))
# 
# print(nthFibonacci(1))

# In[35]:


def nthFibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return(nthFibonacci(n - 1) + nthFibonacci(n - 2))
print(nthFibonacci(2))

print(nthFibonacci(12))

print(nthFibonacci(1))


# Write a recursive functions called isPalindrome that takes a string as a parameter and return 1 is that string is a palindrome else return false. Your program should read the input and test call the function to test it.
# 
# Sample Input and Output Specification (Java)
# 
# Input
# 
# bananan
# 
# Output
# 
# 0
# 
# Input
# 
# racecar
# 
# Output
# 
# 1

# In[44]:


def isPalindrome(str1):
    if len(str1) == 1 or len(str1) == 0:
        return 1
    else:
        if str1[0] == str1[-1]:
            str1 = str1[1:-1]
            return(isPalindrome(str1))
        else:
            return 0
str1 = input()
print(isPalindrome(str1))


# Bridge transport
# 
# A train of railway cars attempts to cross a bridge. The length of each car is 10 m but their weights might be different. The bridge is 40 m long (thus can hold 4 train cars at one time). The bridge will crack if the total weight of the cars on it at one time is greater than a certain weight. The cars are numbered starting at 1, going up to N, and they cross the bridge in that order (i.e., 1 immediately followed by 2, which is immediately followed by 3, and so on).
# 
# What is the largest number T of railway cars such that the train of cars 1…T (in order) can cross the bridge?
# 
# Input
# 
# The first line of input is the maximum weight W (1 ≤ W ≤ 100000) that the bridge can hold at any particular time. The second line of input is the number N (1 ≤ N ≤ 100000) which is the number of railway cars that we wish to move across the bridge. On each of the next N lines of input, there will be a positive integer wi (1 ≤ i ≤ N, 1 ≤ wi ≤ 100000) which represents the weight of the ith railway car in the sequence.
# 
# Output
# 
# Your output should be a non-negative integer representing the maximum number of railway cars that can be brought across the bridge in the order specified.
# 
# Sample Input 1
# 
# 100
# 
# 6
# 
# 50
# 
# 30
# 
# 10
# 
# 10
# 
# 40
# 
# 50
# 
# Sample Output 1
# 
# 5
# 
# Explanation
# 
# The first four railway cars have total weight 50 + 30 + 10 + 10 = 100, which is not greater than what the bridge can hold. When the first railway car leaves, and the next comes on, we have a total weight of 30 + 10 + 10 + 40 = 90, which is not greater than what the bridge can hold. The last four cars would cause the bridge to break, since 10 + 10 + 40 + 50 = 110 which is greater than the bridge can hold. So, only the first 5 railway cars can be taken across the bridge.
# 
# Sample Input 2
# 
# 100
# 
# 3
# 
# 150
# 
# 1
# 
# 1
# 
# Sample Output 2
# 
# 0
# 
# Explanation
# 
# When the first railway car enters the bridge, its weight of 150 will exceed the maximum weight the bridge can hold. Thus, we cannot bring any railway cars across the bridge.

# In[13]:


max_weight = int(input())
n = int(input())
list1 = []
for x in range(n):
    list1.append(int(input()))
def bridge(max_weight, list1):
    result = 0
    if len(list1) < 4:
        if list1[0] > max_weight:
            return 0
    for k in range(0, len(list1) - 3):
        sublist = list1[k : k + 4]
        result += 1
        if sum(sublist) > max_weight:
            if k == 0:
                result -= 1
            return k + result
print(bridge(max_weight, list1))


# In order to increase your performance on the ABC (Another Buying Contest), you decide that you need a new computer. When determining which computer to buy, you narrow your search categories to:
# 
# RAM (in gigabytes), denoted as R;
# CPU speed (in megahertz), denoted as S;
# disk drive space (in gigabytes), denoted as D.
# You perform some analysis and determine that the most preferred machine is the machine that has the largest value of the expression 2R+3S+D. Your task is to read a given list of computers and output the top two computers in order of preference, from highest preference to lowest preference.
# 
# Input
# The first line of input will be an integer n (0 ≤ n ≤ 10000). Each of the remaining n lines of input will contain a computer specification. A computer specification is of the form:
# 
# computer name (a string of less than 20 characters)
# the RAM available (an integer R with 1 ≤ R ≤ 128)
# the CPU speed (an integer S with 1 ≤ S ≤ 4000)
# the disk drive space (an integer D with 1 ≤ D ≤ 3000)
# There is one space between the name, RAM, CPU speed, and disk drive space on each line.
# 
# Output
# The output is the name of the top two preferred computers, one name per line, sorted in decreasing order of preference. If there is a tie in the rankings, pick the computer(s) whose name(s) are lexicographically smallest (i.e., "Apple" is smaller than "Dell"). If there is only one computer, output that computer on one line (i.e., do not print it twice). If there are no computers, print nothing.
# 
# Sample Input
# 4
# ABC 13 22 1
# DEF 10 20 30
# GHI 11 2 2
# JKL 20 20 20
# Sample Output
# JKL
# DEF
# Explanation
# Computer ABC has a computed value of 93. Computer DEF has a computer value of 110. Computer GHI has a computed value of 30. Computer JKL has a computed value of 120. Therefore, computer JKL is the most preferred, followed by computer DEF.

# In[39]:


n = int(input())
list1 = []
for x in range(n):
    list1.append(input())
def computers(n, list1):
    list2 = []
    list3 = []
    for x in list1:
        x = x.split(' ')
        list2.append(x)
        list1 = list2
    if len(list1) == 1:
        return list1[0]
    for a in list1:
        total = 2 * int(a[1]) + 3 * int(a[2]) + int(a[3])
        list3.append(total)
    first = max(list3)
    index = list3.index(first)
    pop = list3.pop(index)
    print(list1[index][0])
    first = max(list3)
    index = list3.index(first)
    pop = list3.pop(index)
    return list1[index][0]
print(computers(n, list1))


# In[38]:


n = 4
list1 = ['ABC 13 22 1', 'DEF 10 20 30', 'GHI 11 2 2', 'JKL 20 20 20']
def computers(n, list1):
    list2 = []
    list3 = []
    for x in list1:
        x = x.split(' ')
        list2.append(x)
        list1 = list2
    if len(list1) == 1:
        return list1[0]
    for a in list1:
        total = 2 * int(a[1]) + 3 * int(a[2]) + int(a[3])
        list3.append(total)
    first = max(list3)
    index = list3.index(first)
    pop = list3.pop(index)
    print(list1[index][0])
    first = max(list3)
    index = list3.index(first)
    pop = list3.pop(index)
    return list1[index][0]
print(computers(n, list1))


# Eric likes interesting numbers like 64. It turns out that 64 is both a square and a cube, since 64 = 8^2 and 64 = 4^3. Eric calls these numbers cool.
# 
# Write a program that helps Eric figure out how many integers in a given range are cool.
# 
# Input Description
# 
# On the first line of input, you are given an integer a such that a >=1 and a <=108. On the second line of input, you are given an integer b such that a <b and b<=108.
# 
# Output Description
# 
# The output should be the number of cool numbers in the range a to b (inclusively: that is, a and b would count as cool numbers in the range if they were actually cool).
# 
# Sample Input 1
# 
# 1
# 
# 100
# 
# Output for Sample Input 1
# 
# 2
# 
# Sample Input 2
# 
# 100
# 
# 1000
# 
# Output for Sample Input2
# 
# 1

# In[71]:


a = int(input())
b = int(input())
count = 0
for x in range(a, b + 1):
    if round(x ** (1 / 2)) ** 2 == x:
        if round(x ** (1 / 3)) ** 3 == x:
            count += 1
print(count)


# Sheldon and Leonard are physicists who are fixated on the the BIG BANG theory. In order to exchange secret insights they have devised a code that encodes UPPERCASE letters by shifting their letters forward.
# 
# Shifting a letter by S positions means to go forward S letters in the alphabet. For example, shifting B by S = 3 positions gives E. However, sometimes this makes us go past Z, the last letter of the alphabet. Whenever this happens we wrap around, treating A as the letter that follows Z. For example, shifting Z by S = 2 positions gives B.
# 
# Sheldon and Leonard's code depends on a parameter K and also varies depending on the position of each letter in the word. For the letter at position P, they use the shift value of $S = 3P + K$.
# 
# For example, here is how ZOOM is encoded when K = 3. The first letter Z has a shift value of $S = 3 \times 1 + 3 = 6$; it wraps around and becomes the letter F. The second letter, O, has $S = 3 \times 2 + 3 = 9$ and becomes X. The last two letters become A and B. So Sheldon sends Leonard the secret message: FXAB
# 
# Write a program for Leonard that will decode messages sent by Sheldon.
# 
# Input Format
# The input will be two lines. The first line will contain the positive integer K (K < 10), which is used to compute the shift value. The second line of input will be the word, which will be a sequence of consecutive uppercase characters of length at most 20.
# 
# Output Format
# The output will be the decoded word of uppercase letters.
# 
# Sample Input 1
# 3
# FXAB
# Sample Output 1
# ZOOM
# Sample Input 2
# 5
# JTUSUKG
# Sample Output 2
# BIGBANG

# In[78]:


k = int(input())
word = input()
list1 = list(word)
str2 = ''
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = list(alpha)
for a, x in enumerate(list1):
    s = 3 * (a + 1) + k
    index = alpha.index(x)
    letter = str(alpha[index - s])
    str2 += letter
print(str2)


# Most likely, you will notice that you have a mouse attached to your computer, which lets you move the cursor around the screen. Your job is to get between the mouse and the cursor.
# 
# Suppose that the bottom left-hand corner of your screen is (0,0), and all points on the screen are given by integer co-ordinates (x, y) where 0 ≤ x ≤ c and 0 ≤ y ≤ r. Thus, the top-right corner of the screen is at position (c, r), bottom-right corner is (c, 0), and top-left corner is (0, r).
# 
# When a mouse is moved, it sends a pair of integers (a, b), indicating that the cursor should be moved a units in the x-direction and b units in the y-direction. It is worth noting that this is relative motion (i.e., how far to move) rather than absolute motion (i.e., where to move). It is also worth noting that a and b may be positive, negative or zero.
# 
# You can assume the mouse starts at position (0,0). You job is to read input messages (i.e., relative motion positions sent by the mouse) and update the cursor to the new position on the screen. Your output (to the screen) will be the position of the mouse after each move.
# 
# If the mouse hits the screen boundary, it stops moving in that direction. For example, if the mouse is supposed to move (-100, -10) from its current position (30, 40), the final positions will be (0, 30): the mouse will hit the left-hand side boundary, but still manages to move down.
# 
# Input is listed as pairs, the first pair being (c, r), followed by the relative motion pairs (x, y). The input is terminated when the mouse moves (0,0).
# 
# Sample Input 1
# 100 200
# 10 40
# -5 15
# 30 -30
# 0 0
# Sample Output 1
# 10 40
# 5 55
# 35 25
# Sample Input 2
# 30 40
# 30 40
# -100 -10
# 0 0
# Sample Output 2
# 30 40
# 0 30

# In[87]:


list1 = []
boundary = input()
boundary = boundary.split(' ')
boundary = [int(s) for s in boundary]
a = input()
starting = [0, 0]
while a != '0 0':
    a = a.split(' ')
    a = [int(s) for s in a]
    if starting[0] + a[0] > boundary[0]:
        starting = [boundary[0], starting[1]]
    elif starting[0] + a[0] < 0:
        starting = [0, starting[1]]
    else:
        starting = [starting[0] + a[0], starting[1]]
    if starting[1] + a[1] > boundary[1]:
        starting = [starting[0], boundary[1]]
    elif starting[1] + a[1] < 0:
        starting = [starting[0], 0]
    else:
        starting = [starting[0], starting[1] + a[1]]
    str1 = str(starting[0]) + ' ' + str(starting[1])
    print(str1)
    a = input()


# An anagram is a word or a phrase formed by rearranging the letters of another phrase such as “ITEM” and “TIME”. Anagrams may be several words long such as “CS AT WATERLOO” and “COOL AS WET ART”. Note that two phrases may be anagrams of each other even if each phrase has a different number of words (as in the previous example). Write a program to determine if two phrases are anagrams of each other.
# 
# Input
# The program should input two phrases, each entered on a separate line. You may assume that the input only contains upper case letters and spaces.
# 
# Output
# The program will print out one of two statements: ”Is an anagram.” or ”Is not an anagram.”
# 
# Sample Input
# CS AT WATERLOO
# COOL AS WET ART
# 
# Sample Output
# Is an anagram.

# In[91]:


str1 = input()
str2 = input()
list1 = list(str1)
list2 = list(str2)
list1 = sorted(list1)
list1 = [s for s in list1 if s != ' ']
list2 = sorted(list2)
list2 = [s for s in list2 if s != ' ']
if list1 == list2:
    print('Is an anagram')
else:
    print('Is not an anagram.')


# Your boss has asked you to add up a sequence of positive numbers to determine how much money your company made last year.
# 
# Unfortunately, your boss reads out numbers incorrectly from time to time.
# 
# Fortunately, your boss realizes when an incorrect number is read and says "zero", meaning "ignore the current last number."
# 
# Unfortunately, your boss can make repeated mistakes, and says "zero" for each mistake.
# 
# For example, your boss may say "One, three, five, four, zero, zero, seven, zero, zero, six", which means the total is 7 as explained in the following chart:
# 
# Boss statement(s)
# 
# Current numbers
# 
# Explanation
# 
# "One, three, five, four"
# 
# 1, 3, 5, 4
# 
# Record the first four numbers.
# 
# "zero, zero"
# 
# 1, 3
# 
# Ignore the last two numbers.
# 
# "seven"
# 
# 1, 3, 7
# 
# Record the number 7 at the end of our list.
# 
# "zero, zero"
# 
# 1
# 
# Ignore the last two numbers.
# 
# "six"
# 
# 1, 6
# 
# We have read all numbers, and the total is 7.
# 
# At any point, your boss will have said at least as many positive numbers as "zero" statements. If all positive numbers have been ignored, the sum is zero.
# 
# Write a program that reads the sequence of boss statements and computes the correct sum.
# 
# Input
# 
# The first line of input contains the integer K (1 ≤ K ≤ 100 000) which is the number of integers (including "zero") your boss will say. On each of the next K lines, there will be either one integer between 1 and 100 (inclusive), or the integer 0.
# 
# Output
# 
# The output is one line, containing the integer which is the correct sum of the integers read, taking the "zero" statements into consideration. You can assume that the output will be an integer in the range 0 and 1 000 000 (inclusive).
# 
# Sample Input 1
# 
# 4
# 
# 3
# 
# 0
# 
# 4
# 
# 0
# 
# Sample Output 1
# 
# 0
# 
# Sample Input 2
# 
# 10
# 
# 1
# 
# 3
# 
# 5
# 
# 4
# 
# 0
# 
# 0
# 
# 7
# 
# 0
# 
# 0
# 
# 6
# 
# Sample Output 2
# 
# 7

# In[106]:


n = int(input())
list1 = []
for x in range(n):
    list1.append(input())
list1 = [s for s in list1 if (s != ' ') and (s != '')]
list1 = [int(s) for s in list1]
list2 = []
for x in list1:
    if x == 0:
        list2 = list2[:-1]
    else:
        list2.append(x)
print(sum(list2))


# /**
# 
#      * 
# 
#      * @param intArr is an sorted  Integer array 
# 
#      * @param intTarget is a value to be found in intArr
# 
#      * @return the index of intTarget if found in intArr else return -1;
# 
#      */
# 
#     public static int BinarySearch(int [] intArr, int intTarget){
# 
#         return 1;
# 
#     }
# 
# 
# 
# Copy and paste the following test case in the main
# 
#  int [] intArr1 = {1,2,3,4,5,6,7,8,9,10};
# 
#   System.out.println(BinarySearch(intArr1, 1));
# 
#  System.out.println(BinarySearch(intArr1, -100));
# 
# 
# Pyhhon Version
# 
# 
# 
# def BinarySearch(intArr, intTarget):
# 
#  pass
# 
# 
# 
# Python Test Case:
# 
# intArr1 = [1,2,3,4,5,6,7,8,9,10]
# 
# print(BinarySearch(intArr1, 1))
# 
# print(BinarySearch(intArr1,-100))

# In[131]:


def BinarySearch(list1, target):
    low = 0
    high = len(list1) - 1
    while high>=low:
        middle = int((low + high) / 2)
        if list1[middle] < target:
            low = middle + 1
        elif list1[middle] > target:
            high = middle - 1
        else:
            return middle
    return -1
intArr1 = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(intArr1, 1))

print(BinarySearch(intArr1,-100))


# /**
# 
#      * 
# 
#      * @param strArr is an sorted  String array 
# 
#      * @param strTarget is a value to be found in intArr
# 
#      * @return the index of strTarget if found in strArr else return -1;
# 
#      */
# 
#     public static int BinarySearch(String []  strArr, String strTarget){
# 
#         return 1;
# 
#     }
# 
# 
# 
# Copy and paste the following test case in the main
# 
#  int [] strArr1 = {"A","B","C","Z"};
# 
#   System.out.println(BinarySearch(strArr1, "B));
# 
#  System.out.println(BinarySearch(strArr1, "D));
# 
# 
# Python Version
# 
# 
# 
# def BinarySearch(intArr, intTarget):
# 
#  pass
# 
# 
# 
# Python Test Case:
# 
# strArr1 = ["A","B","C","Z"]
# 
# print(BinarySearch(strArr1, "B))
# 
# print(BinarySearch(strArr1,"D))

# In[136]:


def BinarySearch(list1, target):
    low = 0
    high = len(list1) - 1
    while high>=low:
        middle = int((low + high) / 2)
        if list1[middle] < target:
            low = middle + 1
        elif list1[middle] > target:
            high = middle - 1
        else:
            return middle
    return -1
strArr1 = ["A","B","C","Z"]
print(BinarySearch(strArr1, "B"))

print(BinarySearch(strArr1,"D"))


#  /**
# 
#      * 
# 
#      * @param intArr  is an unsorted array
# 
#      * sort the intArr1 from least to greatest 
# 
#      */
# 
#     public static void selectionSort(int [] intArr){
# 
#         
# 
#     }
# 
# public static void printArray(int [] intArr){
# 
#         for(int i = 0; i < intArr.length; i++){
# 
#             System.out.print(intArr[i] +" ");
# 
#         }
# 
#         System.out.println("");
# 
#     }
# 
# 
# 
# Copy and paste the printArray method aling with the selection Sort method along with the following test cases
# 
# int [] intArr1 = {10,9,8,7,6,5,4,3,2,1};
# 
# int [] intArr2 = -1,-2,-3,-4,-5,-6};
# 
# printArray(intArr1);
# 
# printArray(intArr2);

# In[154]:


def maxnumber(list1, m):
    n = list1[0]
    index = 0
    for k, x in enumerate(list1[:m]):
        if x > n:
            n = x
            index = k
    return index


# In[165]:


def SelectionSort(list1):
    x = len(list1)
    while x > 0:
        n = maxnumber(list1, x)
        a = list1[n]
        list1[n] = list1[x - 1]
        list1[x - 1] = a
        x -= 1
    list1 = [str(s) for s in list1]
    return ' '.join(list1)
list1 = [10,9,8,7,6,5,4,3,2,1]
list2 = [-1,-2,-3,-4,-5,-6]
print(SelectionSort(list1))

print(SelectionSort(list2))


#  /**
# 
#      * 
# 
#      * @param intArr  is an unsorted array
# 
#      * sort the intArr1 from least to greatest 
# 
#      */
# 
#     public static void insertionSort(int [] intArr){
# 
#         
# 
#     }
# 
# public static void printArray(int [] intArr){
# 
#         for(int i = 0; i < intArr.length; i++){
# 
#             System.out.print(intArr[i] +" ");
# 
#         }
# 
#         System.out.println("");
# 
#     }
# 
# 
# 
# Copy and paste the printArray method along with the selection Sort method along with the following test cases
# 
# int [] intArr1 = {10,9,8,7,6,5,4,3,2,1};
# 
# int [] intArr2 = -1,-2,-3,-4,-5,-6};
# 
# insertionSort(intArr1);
# 
# insertionSort(intArr2);
# 
# printArray(intArr1);
# 
# printArray(intArr2);

# In[185]:


def swap1(list1, ind):
    while ind>0:
        if list1[ind]<list1[ind-1]:
            tmp = list1[ind]
            list1[ind] = list1[ind-1]
            list1[ind-1] = tmp
        ind -= 1
    return list1
swap1([4, 3, 2, 1], 3)


# In[188]:


def insertion_sort(list1):
    c = 0
    for k in range(1, len(list1)):
        if list1[k] < list1[k - 1]:
            list1 = swap1(list1, k)
    list1 = [str(s) for s in list1]
    return ' '.join(list1)
list1 = [10,9,8,7,6,5,4,3,2,1]
list2 = [-1,-2,-3,-4,-5,-6]
print(insertion_sort(list1))

print(insertion_sort(list2))


# At an old railway station, you may still encounter one of the last remaining "train swappers". A train swapper is an employee of the railroad, whose sole job it is to rearrange the carriages of trains.
# 
# Once the carriages are arranged in the optimal order, all the train driver has to do is drop the carriages off, one by one, at the stations for which the load is meant.
# 
# The title "train swapper" stems from the first person who performed this task, at a station close to a railway bridge. Instead of opening up vertically, the bridge rotated around a piller in the center of the river. After rotating the bridge 90 degrees, boats could pass left or right. The first train swapper had discovered that the bridge could be operated with at most two carriages on it. By rotating the bridge 180 degrees, the carriages switched place, allowing him to rearrange the carriages (as a side effect, the carriages then faced the opposite directions, but train carriages can move either way, so who cares).
# 
# Now that almost all train swappers have died out, the railway company would like to automate their operation. Part of the program to be developed is a routine which decides, for a given train, the least number of swaps of two adjacent carriages necessary to order the train. Your assignment is to create a routine that computes the minimal number of swaps.
# 
# Input specification
# The input contains on the first line the number of test cases (N). Each test case consists of two input lines. The first line of a test case contains an integer L, determining the length of the train (0 ≤ L ≤ 50). The second line of a test case contains a permutation of the numbers 1 through L, indicating the current order of the carriages. The carriages should be ordered such that carriage 1 comes first, then 2, etc., with carriage L coming last.
# 
# Output specification
# For each test case output the sentence: "Optimal train swapping takes S swap(s)." where S is an integer representing the minimal number of swaps to order the train.
# 
# Sample input
# 3
# 3
# 1 3 2
# 4
# 4 3 2 1
# 2
# 2 1
# Sample output
# Optimal train swapping takes 1 swap(s).
# Optimal train swapping takes 6 swap(s).
# Optimal train swapping takes 1 swap(s).
# 

# In[194]:


def swap1(list1, ind):
    count = 0
    while ind>0:
        if list1[ind]<list1[ind-1]:
            tmp = list1[ind]
            list1[ind] = list1[ind-1]
            list1[ind-1] = tmp
            count += 1
        ind -= 1
    return(list1, count)
swap1([4, 3, 2, 1], 3)


# In[195]:


def insertion_sort_count(list1):
    c = 0
    for k in range(1, len(list1)):
        if list1[k] < list1[k - 1]:
            list1, count = swap1(list1, k)
            c += count
    return c


# In[196]:


n = int(input())
list1 = []
for x in range(n):
    a = int(input())
    list1.append(input())
for k in list1:
    list2 = k.split(' ')
    count = insertion_sort_count(list2)
    print('Optimal train swapping takes', count, 'swap(s).')


# Since time immemorial, the citizens of Dmojistan and Pegland have been at war. Now, they have finally signed a truce. They have decided to participate in a tandem bicycle ride to celebrate the truce. There are N citizens from each country. They must be assigned to pairs so that each pair contains one person from Dmojistan and one person from Pegland.
# 
# Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem bicycle while the slower person simply enjoys the ride. In other words, if the members of a pair have speeds a and b, then the bike speed of the pair is max(a, b). The total speed is the sum of the N individual bike speeds.
# 
# For this problem, in each test case, you will be asked to answer one of the two questions:
# 
# Question 1: what is the minimum total speed, out of all possible assignments into pairs?
# Question 2: what is the maximum total speed, out of all possible assignments into pairs?
# Input Format
# The first line will contain the type of question you are to solve, which is either 1 or 2.
# The second line contains N (1 ≤ N ≤ 100).
# The third line contains N space-separated integers: the speeds of the citizens of Dmojistan.
# The fourth line contains N space-separated integers: the speeds of the citizens of Pegland.
# Each person's speed will be an integer between 1 and 1 000 000.
# For 8 of the 15 available marks, questions of type 1 will be asked. For 7 of the 15 available marks, questions of type 2 will be asked.
# 
# Output Format
# Output the maximum and minimum total speed that answers the question asked.
# 
# Sample Input 1
# 1
# 3
# 5 1 4
# 6 2 4
# Sample Output 1
# 12
# Explanation 1
# There is a unique optimal solution:
# 
# Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 6.
# Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 2.
# Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.
# Sample Input 2
# 2
# 3
# 5 1 4
# 6 2 4
# Sample Output 2
# 15
# Explanation 2
# There are multiple possible optimal solutions. Here is one optimal solution:
# 
# Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 2.
# Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 6.
# Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.
# Sample Input 3
# 2
# 5
# 202 177 189 589 102
# 17 78 1 496 540
# Sample Output 3
# 2016
# Explanation 3
# There are multiple possible optimal solutions. Here is one optimal solution:
# 
# Pair the citizen from Dmojistan with speed 202 and the citizen from Pegland with speed 1.
# Pair the citizen from Dmojistan with speed 177 and the citizen from Pegland with speed 540.
# Pair the citizen from Dmojistan with speed 189 and the citizen from Pegland with speed 17.
# Pair the citizen from Dmojistan with speed 589 and the citizen from Pegland with speed 78.
# Pair the citizen from Dmojistan with speed 102 and the citizen from Pegland with speed 496.
# This sum yields 202 + 540 + 189 + 589 + 496 = 2016.

# In[4]:


a = int(input())
n = int(input())
list1 = []
for x in range(2):
    list1.append(input())
list2 = []
count = 0
for x in list1:
    list2.append(x.split(' '))
for k, b in enumerate(list2):
    b = [int(s) for s in b]
    if k == 1:
        sublist1 = sorted(b)
    else:
        sublist2 = sorted(b)
if a == 1:
    for c in range(len(sublist1)):
        count += int(max(sublist1[c], sublist2[c]))
    print(count)
if a == 2:
    while sublist1:
        if max(sublist1) > max(sublist2):
            b = max(sublist1)
            sublist1 = sublist1[:-1]
            count += int(b)
            sublist2 = sublist2[1:]
        else:
            b = max(sublist2)
            sublist2 = sublist2[:-1]
            count += int(b)
            sublist1 = sublist1[1:]  
    print(count)


# In[1]:


a = 2
n = 5
list1 = ['202 177 189 589 102', '17 78 1 496 540']
list2 = []
count = 0
for x in list1:
    list2.append(x.split(' '))
for k, b in enumerate(list2):
    b = [int(s) for s in b]
    if k == 1:
        sublist1 = sorted(b)
    else:
        sublist2 = sorted(b)
if a == 1:
    for c in range(len(sublist1)):
        count += int(max(sublist1[c], sublist2[c]))
    print(count)
if a == 2:
    while sublist1:
        if max(sublist1) > max(sublist2):
            b = max(sublist1)
            sublist1 = sublist1[:-1]
            count += int(b)
            sublist2 = sublist2[1:]
        else:
            b = max(sublist2)
            sublist2 = sublist2[:-1]
            count += int(b)
            sublist1 = sublist1[1:]  
    print(count)


# You have been asked by a parental unit to do your chores.
# 
# Each chore takes a certain amount of time, but you may not have enough time to do all of your chores, since you can only complete one chore at a time. You can do the chores in any order that you wish.
# 
# What is the largest amount of chores you can complete in the given amount of time?
# 
# Input
# The first line of input consists of an integer T (0 ≤ T ≤ 100000), which is the total number of minutes you have available to complete your chores.
# 
# The second line of input consists of an integer C (0 ≤ C ≤ 100), which is the total number of chores that you may choose from. The next C lines contain the (positive integer) number of minutes required to do each of these chores. You can assume that each chore will take at most 100000 minutes.
# 
# Output
# The output will be the maximum number of chores that can be completed in time T.
# 
# Sample Input 1
# 6
# 3
# 3
# 6
# 3
# Sample Output 1
# 2
# Explanation
# Chores must be completed in at most 6 minutes. There are 3 chores available. The first chore takes 3 minutes. The second chore takes 6 minutes. The third chore takes 3 minutes. The answer is 2 since only 2 of these chores can be completed in 6 minutes of time. Specifically, the first and last chore can be completed in the allowable time. It is not possible to complete all 3 chores in 6 minutes.
# 
# Sample Input 2
# 6
# 5
# 5
# 4
# 3
# 2
# 1
# Sample Output 2
# 3
# Explanation
# Tasks 3, 4, and 5 can be completed in 6 minutes. It is not possible to complete more than 3 tasks in 6 minutes.

# In[24]:


t = int(input())
n = int(input())
list1 = []
for x in range(n):
    list1.append(int(input()))
list1 = sorted(list1)
count1 = 0
count2 = 0
for x in list1:
    if count1 + list1[0] < t:
        count1 += list1[0]
        list1 = list1[1:]
        count2 += 1
    elif count1 + list1[0] > t:
        break
    else:
        count2 += 1
        break
print(count2)


# In[22]:


intStack = [1,2,3,4,5]
list1 = []
while intStack:
    list1.append(intStack.pop())
for x in list1[::-1]:
    print(x, end = ' ')


# In[28]:


intStack = [1,2,3,4,5]
s = 0
while len(intStack)>0:
    s = s + intStack.pop()
print(s)


# In[33]:


def splitStack(stack1):
    bottom = []
    top = []
    while len(stack1) > 0:
        a = stack1.pop()
        if a < 0:
            bottom.append(a)
        else:
            top.append(a)
    return bottom + top


# In[40]:


def shutter(stack1):
    stack2 = []
    while len(stack1) > 0:
        a = stack1.pop()
        stack2.append(a)
        stack2.append(a)
    return stack2[::-1]


# Your boss has asked you to add up a sequence of positive numbers to determine how much money your company made last year.
# 
# Unfortunately, your boss reads out numbers incorrectly from time to time.
# 
# Fortunately, your boss realizes when an incorrect number is read and says "zero", meaning "ignore the current last number."
# 
# Unfortunately, your boss can make repeated mistakes, and says "zero" for each mistake.
# 
# For example, your boss may say "One, three, five, four, zero, zero, seven, zero, zero, six", which means the total is 7 as explained in the following chart:
# 
# Boss statement(s)
# 
# Current numbers
# 
# Explanation
# 
# "One, three, five, four"
# 
# 1, 3, 5, 4
# 
# Record the first four numbers.
# 
# "zero, zero"
# 
# 1, 3
# 
# Ignore the last two numbers.
# 
# "seven"
# 
# 1, 3, 7
# 
# Record the number 7 at the end of our list.
# 
# "zero, zero"
# 
# 1
# 
# Ignore the last two numbers.
# 
# "six"
# 
# 1, 6
# 
# We have read all numbers, and the total is 7.
# 
# At any point, your boss will have said at least as many positive numbers as "zero" statements. If all positive numbers have been ignored, the sum is zero.
# 
# Write a program that reads the sequence of boss statements and computes the correct sum.
# 
# Input
# 
# The first line of input contains the integer K (1 ≤ K ≤ 100 000) which is the number of integers (including "zero") your boss will say. On each of the next K lines, there will be either one integer between 1 and 100 (inclusive), or the integer 0.
# 
# Output
# 
# The output is one line, containing the integer which is the correct sum of the integers read, taking the "zero" statements into consideration. You can assume that the output will be an integer in the range 0 and 1 000 000 (inclusive).
# 
# Sample Input 1
# 
# 4
# 
# 3
# 
# 0
# 
# 4
# 
# 0
# 
# Sample Output 1
# 
# 0
# 
# Sample Input 2
# 
# 10
# 
# 1
# 
# 3
# 
# 5
# 
# 4
# 
# 0
# 
# 0
# 
# 7
# 
# 0
# 
# 0
# 
# 6
# 
# Sample Output 2
# 
# 7

# In[56]:


n = int(input())
list1 = []
for x in range(2 * n):
    list1.append(input())
list1 = [int(s) for s in list1 if s != '']
stack1 = []
for x in list1:
    if x == 0:
        stack1.pop()
    else:
        stack1.append(x)
print(sum(stack1))


# In[63]:


stack1 = [1,2,3,2,1]
def isPalindrome(stack1):
    n = stack1.copy()
    stack2 = []
    while len(stack1) > 0:
        a = stack1.pop()
        stack2.append(a)
    if n == stack2:
        return True
    else:
        return False


# In order to ensure peace and prosperity for future generations, the United Nations is creating the world’s largest candy. The ingredients must be taken in railway cars from the top of a mountain and poured into Lake Geneva. The railway system goes steeply from the mountaintop down to the lake, with a T-shaped branch in the middle as shown below.
# 
# 
# 
# Right now, each of the N ingredients is in its own railway car. Each railway car is assigned a positive integer from 1 to N. The ingredients must be poured into the lake in the order 1, 2, 3, …, N but the railway cars are lined up in some random order. The difficulty is that, because of the especially heavy gravity today, you can only move cars downhill to the lake, or sideways on the branch line. Is it still possible to pour the ingredients into the lake in the order 1, 2, 3, …, N?
# 
# 
# For example, if the cars were in the order 2, 3, 1, 4, we can slide these into the lake in order as described below:
# 
# Slide car 4 out to the branch
# Slide car 1 into the lake
# Slide car 3 out to the branch
# Slide car 2 into the lake
# Slide car 3 from the branch into the lake
# Slide car 4 from the branch into the lake
# Input
# The first line will contain the number T (1 ≤ T ≤ 10) which is the number of different tests that will be run. Each test has the form of an integer N (1 ≤ N ≤ 100 000) on the first line of the test, followed by a list of the N cars listed from top to bottom. The cars will always use the numbers from 1 to N in some order.
# 
# Output
# For each test, output one line which will contain either Y (for "yum") if the recipe can be completed, and N otherwise.
# 
# Sample Input
# 2
# 4
# 2
# 3
# 1
# 4
# 4
# 4
# 1
# 3
# 2
# Sample Output
# Y
# N

# In[76]:


t = int(input())
for x in range(t):
    stack1 = []
    n = int(input())
    for a in range(n):
        stack1.append(int(input()))
    stack2 = []
    for b in stack1[::-1]:
        if b == min(stack1):
            stack1.pop()
        else:
            stack2.append(stack1.pop())
    if stack2[::-1] == sorted(stack2):
        print('Y')
    else:
        print('N')


#  // TODO code application logic here
#         //Read a sentence form the user and display the frequeency of each letters
#         //in that sentence. You can assume all the letters are in lower case and
#         //ignore the punctuation and space
#         //the red cat sat on the mat
#         /**
#          * a 3
#          * c 1
#          */

# In[96]:


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
sentence = input()
sentence_list = list(sentence)
list1 = []
for x in alphabet:
    list1.append([x, 0])
for a in sentence_list:
    if a in alphabet:
        list1[ord(a) - 97][1] += 1
for (a, b) in list1:
    if b > 0:
        print(a, b)


# Write a program that will reads 10 integers and print their mode. (You can assume there is only one mode)
# 
# Sample input and output specifications are given below.
# 
# Input
# 
# 1 1 1 2 3 4 5 6 7 8 
# 
# Output
# 
# 1

# In[104]:


str1 = input()
list1 = str1.split(' ')
dict1 = {}
for x in list1:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1
m = max(dict1.values())
for a in dict1.keys():
    if dict1[a] == m:
        print(a)
        break


# Read a program that will read a sentence and print the most frequent word in the sentence. (Ignore the white spaces). Sample input and output specifications are given below. You can assume there is only word appears most of the time.
# 
# Input
# 
# the red cat sat on the mat
# 
# Output
# 
# the

# In[102]:


str1 = input()
list1 = str1.split(' ')
dict1 = {}
for x in list1:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1
m = max(dict1.values())
for a in dict1.keys():
    if dict1[a] == m:
        print(a)
        break


# Write a program that will read 10 integers and print the number of unique integers.
# 
# Sample input and output specifications are below.
# 
# Input
# 
# 1
# 
# 1
# 
# 1
# 
# 1
# 
# 1
# 
# 1
# 
# 1
# 
# 2
# 
# 2
# 
# Output
# 
# 2

# In[106]:


list1 = []
for x in range(9):
    list1.append(int(input()))
dict1 = {}
for a in list1:
    if a not in dict1:
        dict1[a] = 0
    else:
        continue
print(len(dict1))


# It has been said that the most common letter in the English alphabet is the letter "E". In actual messages that is not always the case. In this program you are asked to write a program that will find the most common letter in a message, ignoring upper case or lower case, not counting any non‐ alphabetic characters such as spaces, commas or numbers. State the number of occurrences of the letter, and if there is a tie, list each letter in the tie in alphabetic order. (The input is always five lines)
# 
#  
# 
# 
# 
# Sample Input
# 
# Beware the Jabberwock, my son!
# 
# the jaws that bite,
# 
# and the claws that catch!
# 
# Beware the Jujub bird, and shun 
# 
# This frumious Bandersnatch!
# 
#  
# 
#  
# 
# Sample Output
# 
# E occur(s) 4 times.  
# 
# T occur(s) 4 times.  
# 
# A T occur(s) 4 times.
# 
# B E U occur(s) 3 times. 
# 
# S occur(s) 3 times.

# In[145]:


list1 = []
for x in range(5):
    list1.append(input())
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
list2 = []
for x in list1:
    dict1 = {}
    current_list = list(x)
    current_list = [s.lower() for s in current_list if s in alphabet]
    for a in current_list:
        if a not in dict1:
            dict1[a] = 1
        else:
            dict1[a] += 1
    max_value = max(dict1.values())
    list3 = []
    for b in dict1:
        if dict1[b] == max_value:
            max_key = b
            list3.append(max_key)
    list3 = sorted(list3)
    list3 = [s.upper() for s in list3]
    str1 = ' '.join(list3)
    list2.append(str1 + ' occur(s) ' + str(max_value) + ' times.')
for d in list2:
    print(d)
    print('\r')


# You have a sequence of lowercase characters that you want to encrypt.
# 
# The first k characters will be encoded as plain-text. All characters after the first k characters will be shifted by the most frequently occuring character that appeared in the previous k characters, with ties broken by the character which occurs first in the alphabet. By "shifted by", we mean that if c was the most frequently occuring character, the character would be shifted ahead by 3 positions (since c is the third letter of the alphabet), modulo 26 (e.g., b becomes e, and z becomes c).
# 
# Input Specification
# 
# On the first line of input contains k (1 ≤ k ≤ 10 000). The next line contains c characters (1 ≤ c ≤ 100 000).
# 
# Output Specification
# 
# One line, containing the encrypted version of the c characters from the input.
# 
# Sample Input
# 
# 5
# 
# abbaabbacdecde
# 
# Output for Sample Input
# 
# abbaacdcdegdgh

# In[29]:


def most_frequent(str1):
    list1 = list(str1)
    dict1 = {}
    list2 = []
    for x in list1:
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1
    max_value = max(dict1.values())
    for x in dict1.keys():
        if dict1[x] == max_value:
            list2.append(x)
    return min(list2)
k = int(input())
str1 = input()
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
str2 = ''
list1 = list(str1)
for x in range(k):
    str2 += list1[x]
for a in range(k, len(list1)):
    up = most_frequent(''.join(list1[a - k: a]))
    index = alphabet.index(up)
    new = alphabet[alphabet.index(list1[a]) + index + 1]
    str2 += new
print(str2)


# In[ ]:


n = int(input())
list1 = []
for x in matrix[n]:
    if x != 0:
        list1.append(x)
print(len(list1))


# In a certain school, it has been decided that students are spending too much time studying and not enough time socializing. To address this situation, it has been decided to give every student a friend. Friendship is one-way. That is, if Janet is assigned to be Sarah’s friend, Janet must be friendly to Sarah, but Sarah is not required to reciprocate.
# 
# The assignment of friends is done by computer using student numbers. Every student is assigned exactly one friend. Sometimes, a ‘circle of friends’ occurs. For example, if Marc is assigned Fred, Fred is assigned Lori, Lori is assigned Jean, and Jean assigned Marc, we have a circle of 4 friends containing Marc, Fred, Lori, and Jean. In the circle, we can say that Marc has a separation of 0 from Fred, of 1 from Lori, of 2 from Jean, and of 3 from Marc.
# 
# Your task it to identify, given the computer assignment of friends, whether two students are in the same circle of friends, and if so, determine their separation.
# 
# Input
# 
# Input begins with a single integer n (2 ≤ n ≤ 9999), on a line by itself, indicating the number of students in the class. The next n lines contain the computer assignment of friendship. An assignment is of the form x y (where 1 ≤ x ≤ 9999, 1 ≤ y ≤ 9999, x ≠ y). For example, 1234 8765 is a possible friendship assignment indicating that student 1234 must be friends with student 8765.
# 
# Following the friendship assignments, there are a series of lines containing two student numbers, separated by a single whitespace. These lines represent the pairs of students that you will determine if they are in same circle of friends and, if so, their separation. The last line of input can be identified by the use of the 0 0 as the friend assignment.
# 
# Output
# 
# For each case, you are to print, on a separate line, either Yes or No depending on whether they are in the same circle of friends. If the answer is Yes, follow the output Yes with a single whitespace and then an integer indicating the friend’s separation.
# 
# Sample Input
# 
# 6
# 1 2
# 2 3
# 3 1
# 10 11
# 100 10
# 11 100
# 1 100
# 2 3
# 0 0
# 
# Sample Output
# 
# No
# Yes 0

# In[2]:


def bfs(starting_node, end_node):
    list_visited = []
    list_paths = []
    list_paths.append([starting_node])
    while list_paths:
        current_path = list_paths.pop(0)
        current_node = current_path[-1]
        if current_node not in list_visited:
            list_visited.append(current_node)
            list_friends = friends[current_node]
            for c in list_friends:
                path = current_path + [c]
                if path[-1] == end_node:
                    return path
                else:
                    list_paths.append(path)
    return None

friends = {}
n = int(input())
str1 = input()
list_inputs = []
while str1 != '0 0':
    list_inputs.append(str1)
    str1 = input()

list_inputs_1 = list_inputs[:n]
list_inputs_2 = list_inputs[n:]

for s in list_inputs_1:
    sublist = s.split(' ')
    if sublist[1] not in friends:
        friends[sublist[1]] = [sublist[0]]
    else:
        friends[sublist[1]].append(sublist[0])
        
tests = list_inputs_2

for x in tests:
    sublist = x.split(' ')
    start_node = sublist[1]
    end_node = sublist[0]
    shortest_path = bfs(start_node, end_node)
    if shortest_path == None:
        print('No')
    else:
        print('Yes ' + str(len(shortest_path) - 2))


# In[ ]:


## friends = {}
n = int(input())
str1 = input()
list_inputs = []
while str1 != '0 0':
    list_inputs.append(str1)
    sublist = str1.split(' ')

list_inputs_1 = list_inputs[:n]
list_inputs_2 = list_inputs[n:]


# In[34]:


tests


# In[27]:


friends = {'2': ['1'], '3': ['2'], '1': ['3'], '11': ['10'], '10': ['100'], '100': ['11']}
tests = ['1 100', '2 3']
def bfs(starting_node, end_node):
    list_visited = []
    list_paths = []
    list_paths.append([starting_node])
    while list_paths:
        current_path = list_paths.pop(0)
        current_node = current_path[-1]
        if current_node not in list_visited:
            list_visited.append(current_node)
            list_friends = friends[current_node]
            for c in list_friends:
                path = current_path + [c]
                if path[-1] == end_node:
                    return path
                else:
                    list_paths.append(path)
    return None
for x in tests:
    sublist = x.split(' ')
    start_node = sublist[1]
    end_node = sublist[0]
    shortest_path = bfs(start_node, end_node)
    if shortest_path == None:
        print('No')
    else:
        print('Yes ' + str(len(shortest_path) - 2))


# In[90]:


friends = {}
friends['1'] = ['6']
friends['2'] = ['6']
friends['3'] = ['4', '5', '6', '15']
friends['4'] = ['3', '5', '6']
friends['5'] = ['3', '4', '6']
friends['6'] = ['1', '2', '3', '4', '5', '7']
friends['7'] = ['6', '8']
friends['8'] = ['7', '9']
friends['9'] = ['8', '10', '12']
friends['10'] = ['9', '11']
friends['11'] = ['10', '12']
friends['12'] = ['9', '11', '13']
friends['13'] = ['12', '14', '15']
friends['14'] = ['13']
friends['15'] = ['3', '13']
friends['16'] = ['17', '18']
friends['17'] = ['16', '18']
friends['18'] = ['16', '17']
def bfs(starting_node, end_node):
    list_visited = []
    list_paths = []
    list_paths.append([starting_node])
    while list_paths:
        current_path = list_paths.pop(0)
        current_node = current_path[-1]
        if current_node not in list_visited:
            list_visited.append(current_node)
            list_friends = friends[current_node]
            for c in list_friends:
                path = current_path + [c]
                if path[-1] == end_node:
                    return path
                else:
                    list_paths.append(path)
    return None
a = input()
list_incomplete = []
list_input = []
while a != 'q':
    list_incomplete.append(a.split(' '))
    a = input()
for c in list_incomplete:
    for d in c:
        list_input.append(d)
for k, x in enumerate(list_input):
    if x == 'i':
        if list_input[k + 1] not in friends:
            friends[list_input[k + 1]] = [list_input[k + 2]]
        else:
            friends[list_input[k + 1]].append(list_input[k + 2])
        if list_input[k + 2] not in friends:
            friends[list_input[k + 2]] = [list_input[k + 1]]
        else:
            friends[list_input[k + 2]].append(list_input[k + 1]) 
    if x == 'd':
        index = friends[list_input[k + 1]].index(list_input[k + 2])
        friends[list_input[k + 1]] = friends[list_input[k + 1]][:index] + friends[list_input[k + 1]][index + 1:]
        index = friends[list_input[k + 2]].index(list_input[k + 1])
        friends[list_input[k + 2]] = friends[list_input[k + 2]][:index] + friends[list_input[k + 2]][index + 1:]
    if x == 'n':
        print(len(friends[list_input[k + 1]]))
    if x == 'f':
        list_of_friends = [list_input[k + 1]]
        friends_of_friends = []
        for a in friends[list_input[k + 1]]:
            list_of_friends.append(a)
        for a in friends[list_input[k + 1]]:
            for b in friends[a]:
                if b not in list_of_friends:
                    friends_of_friends.append(b)
        print(len(list(set(friends_of_friends))))
    if x == 's':
        print(len(bfs(list_input[k + 1], list_input[k + 2])) - 1)


# In[88]:


friends = {}
friends['1'] = ['6']
friends['2'] = ['6']
friends['3'] = ['4', '5', '6', '15']
friends['4'] = ['3', '5', '6']
friends['5'] = ['3', '4', '6']
friends['6'] = ['1', '2', '3', '4', '5', '7']
friends['7'] = ['6', '8']
friends['8'] = ['7', '9']
friends['9'] = ['8', '10', '12']
friends['10'] = ['9', '11']
friends['11'] = ['10', '12']
friends['12'] = ['9', '11', '13']
friends['13'] = ['12', '14', '15']
friends['14'] = ['13']
friends['15'] = ['3', '13']
friends['16'] = ['17', '18']
friends['17'] = ['16', '18']
friends['18'] = ['16', '17']
def bfs(starting_node, end_node):
    list_visited = []
    list_paths = []
    list_paths.append([starting_node])
    while list_paths:
        current_path = list_paths.pop(0)
        current_node = current_path[-1]
        if current_node not in list_visited:
            list_visited.append(current_node)
            list_friends = friends[current_node]
            for c in list_friends:
                path = current_path + [c]
                if path[-1] == end_node:
                    return path
                else:
                    list_paths.append(path)
    return None
list_input = ['i', '1', '2', 'd', '1', '2', 'i', '20', '10', 'i', '20', '9', 'i', '9', '8', 'i', '8', '7', 
              'i', '7', '6', 'i', '10', '11', 'i', '10', '12', 'n', '20', 'f', '20', 's', '20', '6']
for k, x in enumerate(list_input):
    if x == 'i':
        if list_input[k + 1] not in friends:
            friends[list_input[k + 1]] = [list_input[k + 2]]
        else:
            friends[list_input[k + 1]].append(list_input[k + 2])
        if list_input[k + 2] not in friends:
            friends[list_input[k + 2]] = [list_input[k + 1]]
        else:
            friends[list_input[k + 2]].append(list_input[k + 1]) 
    if x == 'd':
        index = friends[list_input[k + 1]].index(list_input[k + 2])
        friends[list_input[k + 1]] = friends[list_input[k + 1]][:index] + friends[list_input[k + 1]][index + 1:]
        index = friends[list_input[k + 2]].index(list_input[k + 1])
        friends[list_input[k + 2]] = friends[list_input[k + 2]][:index] + friends[list_input[k + 2]][index + 1:]
    if x == 'n':
        print(len(friends[list_input[k + 1]]))
    if x == 'f':
        list_of_friends = [list_input[k + 1]]
        friends_of_friends = []
        for a in friends[list_input[k + 1]]:
            list_of_friends.append(a)
        for a in friends[list_input[k + 1]]:
            for b in friends[a]:
                if b not in list_of_friends:
                    friends_of_friends.append(b)
        print(len(list(set(friends_of_friends))))
    if x == 's':
        print(len(bfs(list_input[k + 1], list_input[k + 2])) - 1)


# In[24]:


list_1=[]
with open('11.text', 'r') as f:
    for line in f:
        list_1.append(line)
list_1 = [s.strip() for s in list_1]
print(list_1)


# In[41]:


new_line='eleventh line'
with open('11.text', 'a') as f:
    f.write(new_line+'\n')
list_1=[]
with open('11.text', 'r') as f:
    for line in f:
        list_1.append(line)
list_1 = [s.strip() for s in list_1]
for line in list_1:
    print(line)


# In[42]:


new_line='eleventh line'
with open('11.text', 'w') as f:
    f.write(new_line+'\n')


# Freckles
# In an episode of the Dick Van Dyke show, little Richie connects the freckles on his
# Dad’s back to form a picture of the Liberty Bell. Alas, one of the freckles turns out to
# be a scar, so his Ripley’s engagement falls through.
# Consider Dick’s back to be a plane with freckles at various (x, y) locations. Your job
# is to tell Richie how to connect the dots so as to minimize the amount of ink used.
# Richie connects the dots by drawing straight lines between pairs, possibly lifting the
# pen between lines. When Richie is done there must be a sequence of connected lines
# from any freckle to any other freckle.
# Input
# The input begins with a single positive integer on a line by itself indicating the number
# of test cases, followed by a blank line.
# The first line of each test case contains 0 < n ≤ 100, giving the number of freckles on
# Dick’s back. For each freckle, a line follows; each following line contains two real numbers
# indicating the (x, y) coordinates of the freckle.
# There is a blank line between each two consecutive test cases.
# Output
# For each test case, your program must print a single real number to two decimal places:
# the minimum total length of ink lines that can connect all the freckles. The output of
# each two consecutive cases must be separated by a blank line.
# Sample Input
# 1
# 3
# 1.0 1.0
# 2.0 2.0
# 2.0 4.0
# Sample Output
# 3.41

# In[69]:


def distance_formula(str1, str2):
    list1 = str1.split()
    list2 = str2.split()
    list1 = [float(s) for s in list1]
    list2 = [float(s) for s in list2]
    distance = (((list2[0] - list1[0])**2) + ((list2[1] - list1[1])**2)) ** (1/2)
    return distance
def min_cost_neighbour(graph, visited_nodes):
    min_cost = float('inf')
    min_node = None
    for x in visited_nodes:
        for y in graph[x].keys():
            if graph[x][y] < min_cost and y not in visited_nodes:
                min_cost = graph[x][y]
                min_node_start = x
                min_node_end = y
    return (min_node_start, min_node_end)
def prim(graph):
    while len(visited) != len(graph.keys()):
        min_node_start, min_node_end = min_cost_neighbour(graph, visited)
        visited.append(min_node_end)
        parents[min_node_end] = min_node_start
    s = 0
    for k, v in parents.items():
        s += graph[v][k]
    return s
cases = int(input())
for x in range(cases):
    hello = input()
    freckles = int(input())
    list_coordinates = []
    for a in range(freckles):
        hello = input()
        list_coordinates.append(input())
    visited = [list_coordinates[0]]
    parents = {}
    graph = {}
    for b in list_coordinates:
        for c in list_coordinates:
            if b == c:
                continue
            if b not in graph:
                graph[b] = {}
                graph[b][c] = distance_formula(b, c)
            else:
                graph[b][c] = distance_formula(b, c)
            if c not in graph:
                graph[c] = {}
                graph[c][b] = distance_formula(c, b)
            else:
                graph[c][b] = distance_formula(c, b)
    print(round(prim(graph), 2))
    if x != cases - 1:
        print('\r')


# In[108]:


with open('a.txt', 'w') as t:
    t.write('Hi daddy!\n')


# In[109]:


with open('a.txt', 'a') as t:
    for x in range(2):
        t.write('Hi daddy!\n')


# In[115]:


list1 = []
with open('a.txt', 'r') as t:
    for line in t:
        list1.append(line.strip())


# In[116]:


list1


# In[119]:


count = 0
with open('mobi.txt', 'r') as t:
    for line in t:
        count += len(line.split(' '))
print(count)


# In[125]:


list1 = []
with open('j1/j1.1.in', 'r') as t:
    for line in t:
        list1.append(line.strip())
list1 = [int(s) for s in list1]
if sum(list1) != 180:
    print('Error')
elif list1[0] == list1[1] and list1[1] == list1[2]:
    print('Equilateral')
elif list1[0] == list1[1] or list1[0] == list1[2] or list1[1] == list1[2]:
    print('Isosceles')
else:
    print('Scalene')


# In[152]:


count = 0
for x in range(1, 6):
    file_name_in = 'j3/j3.{}.in'.format(x)
    file_name_out = 'j3/j3.{}.out'.format(x)
    list1 = []
    with open(file_name_in, 'r') as t:
        for line in t:
            list1.append(line.strip())
    a = list1.pop(0)
    p1 = 100
    p2 = 100
    for x in range(int(a)):
        numbers = list1[x].split(' ')
        if int(numbers[0]) > int(numbers[1]):
            p2 -= int(numbers[0])
        if int(numbers[1]) > int(numbers[0]):
            p1 -= int(numbers[1])
    print(p1)
    print(p2)
    with open(file_name_out, 'r') as t:
        list1 = [str(p1), str(p2)]
        for line in t:
            list1.append(line.strip())
    if list1[:2] == list1[2:]:
        count += 1
        print('You got that right!')
print('You got ' + str(count) + ' out of 5 inputs right!')


# wo important stats in baseball are the team batting average and the team slugging average. Batting average is defined as the total number of hits (this includes 1 base hits, 2 base hits, 3 base hits and home runs combined) divided by the total number of times at bat (“at bats”) for all players on the team. The team slugging average is defined using the following equation:
# 
# Sa = (A + 2B + 3C + 4*D )/E
# 
# Where A is the number of 1 base hits, B is 2 base hits, C is 3 base hits, D is home runs, and E is the number of at bats for all players on the team. Both slugging and batting averages are always presented as decimals rounded to 3 places, leaving off the leading 0 (in theory batting averages can be as high as 1.000, and slugging averages as high as 4.000 but in practice they are both usually well below 1).
# 
# The input contains the raw data on the top 10 teams during a regular season of Major League Baseball. The first line is the season name, followed by 10 lines for each of the top 10 teams. Each of these lines starts with a team name (single word) followed by 7 integers: Games Played, At Bats, Runs, Hits (total), two-base hits, three-base hits, and home runs. One space character separates each item on each line.
# 
# Write a program to produce a report showing the batting and slugging averages for each team in the order they appeared in the input file, and formatted EXACTLY as shown below, including all punctuation and matching upper and lower case exactly. All spacing is done with a single space character. All batting and slugging averages will be less than 1. The final line shows the same averages for all 10 teams combined (computed from the sum of all at bats, hits, etc. for all 10 teams). Note that the two lines of “=” characters each contain 20 characters.
# 
# 2011 Regular Season
# 
# Boston 162 5710 875 1600 352 35 203
# 
# NY_Yankees 162 5518 867 1452 267 33 222
# 
# Texas 162 5659 855 1599 310 32 210
# 
# Detroit 162 5563 787 1540 297 34 169
# 
# St.Louis 162 5532 762 1513 308 22 162
# 
# Toronto 162 5559 743 1384 285 34 186
# 
# Cincinnati 162 5612 735 1438 264 19 183
# 
# Colorado 162 5544 735 1429 274 40 163
# 
# Arizona 162 5421 731 1357 293 37 172
# 
# Kansas_City 162 5672 730 1560 325 41 129
# 
# Output
# 
# 2011 Regular Season
# 
# ====================
# 
# Boston: .280 .461
# 
# NY_Yankees: .263 .444
# 
# Texas: .283 .460
# 
# Detroit: .277 .434
# 
# St.Louis: .273 .425
# 
# Toronto: .249 .413
# 
# Cincinnati: .256 .408
# 
# Colorado: .258 .410
# 
# Arizona: .250 .413
# 
# Kansas_City: .275 .415
# 
# Big 10 Av: .267 .428
# 

# In[341]:


import math
#Games Played, At Bats, Runs, Hits (total), two-base hits, three-base hits, and home runs
season = input()
print(season)
print('====================')
list1 = []
batting = []
sluggish = []
for x in range(12):
    list1.append(input())
for k, x in enumerate(list1):
    if k == 2 or k == 7:
        continue
    sublist = x.split(' ')
    b = int(sublist[5])
    c = int(sublist[6])
    d = int(sublist[7])
    a = int(sublist[4]) - b - c - d
    e = int(sublist[2])
    ba = (int(sublist[4]))/e
    sa = (a + 2*b + 3*c + 4*d )/e
    batting.append(ba)
    sluggish.append(sa)
    ba = round(ba, 3)
    sa = round(sa, 3)
    str1 = str(ba)
    str1 = str1[1:]
    if len(str1) == 3:
        str1 += '0'
    if len(str1) == 2:
        str1 += '00'
    str2 = str(sa)
    str2 = str2[1:]
    if len(str2) == 3:
        str2 += '0'
    if len(str2) == 2:
        str2 += '00'
    print(sublist[0] + ':', str1, str2)
batting_score = (sum(batting))/10
batting_score = math.ceil(batting_score * 1000)/1000
sluggish_score = (sum(sluggish))/10
sluggish_score = round(sluggish_score, 3)
str1 = str(batting_score)
str1 = str1[1:]
if len(str1) == 3:
    str1 += '0'
if len(str1) == 2:
    str1 += '00'
str2 = str(sluggish_score)
str2 = str2[1:]
if len(str2) == 3:
    str2 += '0'
if len(str2) == 2:
    str2 += '00'
print('Big 10 Av:', str1, str2)


# Given a sequence of m words from a newspaper article and an integer k, find the kth most common word.
# 
# Input Specification
# 
# Input will consist of an integer n followed by n data sets. Each data set begins with a line containing m and k, followed by m lines, each containing a word of up to 20 lower case letters. There will be no more than 1000 words per data set.
# 
# Output Specification
# 
# For each input data set, determine the kth most common word(s). To be precise, a word w is the kth most common if exactly k-1 distinct words occur more frequently than w in the data set. Note that w might be multiply defined (i.e. there is a tie for the kth most common word) or w might not exist (i.e. there is no kth most common word). For each data set, print a title line indicating k using normal ordinal notation (1st, 2nd, 3rd, 4th, 5th, ...) followed by a number of lines giving all the possible values for the kth most common word. A blank line should follow the last word for each data set.
# 
# Sample Input
# 
# 3
# 
# 7 2
# 
# the
# 
# brown
# 
# the
# 
# fox
# 
# red
# 
# the
# 
# red
# 
# 1 3
# 
# the
# 
# 2 1
# 
# the
# 
# wash
# 
# Output for Sample Input
# 
# 2nd most common word(s):
# 
# red
# 
# 
# 
# 3rd most common word(s):
# 
# 
# 
# 1st most common word(s):
# 
# the
# 
# wash

# In[27]:


n = int(input())
aa = True
while aa:
    str1 = input()
    if str1=='':
        continue
    else:
        n = n-1
        if n==0:
            aa=False
                
    list_input = str1.split(' ')
    m, k = int(list_input[0]), int(list_input[1])
    dict1 = {}
    list1 = []
    do = True
    while do:
        word = input()
        if word=='':
            continue
        else:
            m = m-1
            if m==0:
                do=False
                
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
    if k == 1:
        print('1st most common word(s):')
    elif k == 2:
        print('2nd most common word(s):')
    elif k == 3:
        print('3rd most common word(s):')
    else:
        print(str(k) + 'th most common word(s):')
    list2 = sorted(dict1.values(), reverse = True)
    if k > len(list2):
        print('\r')
        continue
    for key, value in dict1.items():
        if value == list2[k - 1]:
            print(key)
    if do==False:
        print('\r')


# You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits, since the digit 2 is repeated.
# 
# Given a year, what is the next year with distinct digits?
# 
# Input
# The input consists of one integer Y (0 ≤ Y ≤ 10000), representing the starting year.
# 
# Output
# The output will be the single integer D, which is the next year after Y with distinct digits.
# 
# Sample Input 1
# 1987
# Sample Output 1
# 2013
# Sample Input 2
# 999
# Sample Output 2
# 1023

# In[30]:


year = int(input())
year += 1
while len(list(set(list(str(year))))) != 4:
    year += 1
print(year)


# You are a mouse that lives in a cage in a large laboratory. The laboratory is composed of one rectangular grid of square cages, with a total of R rows and C columns of cages.
# 
# To get your exercise, the laboratory owners allow you to move between cages. You can move between cages either by moving right between two adjacent cages in the same row, or by moving down between two adjacent cages in the same column. You cannot move diagonally, left or up.
# 
# Your cage is in one corner of the laboratory, which has the label (1,1) (to indicate top-most row, left-most column). You would like to visit your brother who lives in the cage labelled (R,C) (bottom-most row, right-most column), which is in the other corner diagonally. However, there are some cages which you cannot pass through, since they contain cats.
# 
# Your brother, who loves numbers, would like to know how many different paths there are between your cage and his that do not pass through any cat cage. Write a program to compute this number of cat-free paths.
# 
# Input Format
# The first line of input contains two integers R and C (1 ≤ R, C ≤ 25), separated by one space representing the number of rows and columns (respectively). On the second line of input is the integer K, the number of cages that contain cats. The next K lines each contain the row and column positions (in that order) for a cage that contains a cat. None of the K cat cages are repeated, and all cages are valid positions. Note that (1,1) and (R,C) will not be cat cages.
# 
# Output Format
# Output the non-negative integer value representing the number of paths between your cat cage at position (1,1) and your brother's cage at position (R,C). You can assume the output will be strictly less than 109.
# 
# Sample Input 1
# 2 3
# 1
# 2 1
# Sample Output 1
# 2
# Sample Input 2
# 3 4
# 3
# 2 3
# 2 1
# 1 4
# Sample Output 2
# 1

# In[51]:


str1 = input()
list1 = str1.split(' ')
rows = int(list1[0])
cols = int(list1[1])
num_cats = int(input())
list_cats = []
for x in range(num_cats):
    list_cats.append(input())
list_arr = []
for m in range(rows):
    lis_tmp = [0]*cols
    list_arr.append(lis_tmp)
list_arr[0][0]=1
for m in range(rows):
    for n in range(cols):
        current_cell = str(m+1)+' '+str(n+1)
        if current_cell in list_cats:
            list_arr[m][n]=0
        elif current_cell=='1 1':
            list_arr[m][n]=1
        else:
            left_cell_row = m
            left_cell_col = n-1
            upper_cell_row = m-1
            upper_cell_col = n
            if left_cell_row>=0 and left_cell_row<rows and left_cell_col>=0 and left_cell_col<cols:
                left_value = list_arr[left_cell_row][left_cell_col]
            else:
                left_value = 0
            if upper_cell_row>=0 and upper_cell_row<rows and upper_cell_col>=0 and upper_cell_col<cols:
                upper_value = list_arr[upper_cell_row][upper_cell_col]
            else:
                upper_value = 0  
            list_arr[m][n] = left_value + upper_value
print(list_arr[rows-1][cols-1])


# In[46]:


list_arr = []
for m in range(rows):
    lis_tmp = [0]*cols
    list_arr.append(lis_tmp)
print(list_arr)
list_arr[0][0]=1


# In[47]:


for m in range(rows):
    for n in range(cols):
        current_cell = str(m+1)+' '+str(n+1)
        if current_cell in list_cats:
            print(m, n, 'cat')
            list_arr[m][n]=0
        elif current_cell=='1 1':
            list_arr[m][n]=1
        else:
            left_cell_row = m
            left_cell_col = n-1
            upper_cell_row = m-1
            upper_cell_col = n
            if left_cell_row>=0 and left_cell_row<rows and left_cell_col>=0 and left_cell_col<cols:
                left_value = list_arr[left_cell_row][left_cell_col]
            else:
                left_value = 0
            if upper_cell_row>=0 and upper_cell_row<rows and upper_cell_col>=0 and upper_cell_col<cols:
                upper_value = list_arr[upper_cell_row][upper_cell_col]
            else:
                upper_value = 0  
            list_arr[m][n] = left_value + upper_value
print(list_arr[rows-1][cols-1])


# In[48]:


for m in range(rows):
    for n in range(cols):
        print(m, n, list_arr[m][n])


# Messages can be ciphered (encrypted) by systematically replacing letters of the alphabet by other letters. A simple cipher known as the Caesar cipher replaces each letter in the alphabet by the letter k positions later in the alphabet, where A is considered to follow Z . For example, if k = 6, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, and Z would be replaced by G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C, D, E, and F respecively. The message
# 
# 
# 
# 
# 
# 
# 
#    THE FULL MOON RISING IS A BAD SIGN
# 
# 
# 
# would be ciphered as
# 
# 
# 
#    ZNK LARR SUUT XOYOTM OY G HGJ YOMT
# 
# 
# 
# The inverse of the cipher is again a Caesar cipher with 26-k replacing k.
# 
# 
# 
# Your job as cryptanalist is to decode lines of text that have been encoded with a Ceasar cipher, each using a different unknown value of k. For example, if the input were
# 
# 
# 
# 
# 
# 
# 
#    ZNK LARR SUUT XOYOTM OY G HGJ YOMT
# 
# 
# 
#    FA NQ AD ZAF FA NQ FTMF UE FTQ CGQEFUAZ
# 
# 
# 
# the output would be
# 
# 
# 
#    THE FULL MOON RISING IS A BAD SIGN
# 
# 
# 
#    TO BE OR NOT TO BE THAT IS THE QUESTION
# 
# 
# 
# (the first line was ciphered with k=6 and the second line with k=12).
# 
# 
# 
# Of course there are 26 possible values of k and therefore 26 possible ciphers, so you will have to "guess" by selecting the most probable deciphering. The probability of a particular deciphering can be estimated using the probabilities of the letters it contains. In English, E is the most common letter, with probability 0.127, T is the next more common with probability 0.091, and so on. A complete table of letter probabilities is given below. The probability of a complete line of text can be approximated by the product of the probabilities of the letters it contains.
# 
# 
# 
# 
# 
# 
# 
# Input Specification
# 
# 
# 
# The input to your program consists of a line containing a positive integer n, followed by n lines each consisting of of upper case letters and spaces only. Each line is an English phrase or sentence, encrypted with a Caesar cipher with unknown k.
# 
# 
# 
# Output Specification
# 
# 
# 
# For each line of input, give the most probable deciphering.
# 
# 
# 
# Sample Input
# 
# 
# 
# 2
# 
# ZNK LARR SUUT XOYOTM OY G HGJ YOMT
# 
# FA NQ AD ZAF FA NQ FTMF UE FTQ CGQEFUAZ
# 
# 
# 
# Output for Sample Input
# 
# THE FULL MOON RISING IS A BAD SIGN
# 
# TO BE OR NOT TO BE THAT IS THE QUESTION
# 
# 
# 
# Probabilities of Letters in English Text
# 
# 
# 
#        Letter     Probability       Letter   Probability
# 
# 
# 
#           A          .082             N          .067
# 
# 
# 
#           B          .015             O          .075
# 
# 
# 
#           C          .028             P          .019
# 
# 
# 
#           D          .043             Q          .001
# 
# 
# 
#           E          .127             R          .060
# 
# 
# 
#           F          .022             S          .063
# 
# 
# 
#           G          .020             T          .091
# 
# 
# 
#           H          .061             U          .028
# 
# 
# 
#           I          .070             V          .010
# 
# 
# 
#           J          .002             W          .023
# 
# 
# 
#           K          .008             X          .001
# 
# 
# 
#           L          .040             Y          .020
# 
# 
# 
#           M          .024             Z          .001

# In[62]:


dict_p = {'A': 0.082, 'N': 0.067, 'B': 0.015, 'O': 0.075, 'C': 0.028, 'P': 0.019, 'D': 0.043, 'Q': 0.001, 'E': 0.127, 'R': 0.06, 'F': 0.022, 'S': 0.063, 'G': 0.02, 'T': 0.091, 'H': 0.061, 'U': 0.028, 'I': 0.07, 'V': 0.01, 'J': 0.002, 'W': 0.023, 'K': 0.008, 'X': 0.001, 'L': 0.04, 'Y': 0.02, 'M': 0.024, 'Z': 0.001}
print(dict_p)


# In[81]:


dict_p = {'A': 0.082, 'N': 0.067, 'B': 0.015, 'O': 0.075, 'C': 0.028, 'P': 0.019, 'D': 0.043, 'Q': 0.001, 'E': 0.127, 'R': 0.06, 'F': 0.022, 'S': 0.063, 'G': 0.02, 'T': 0.091, 'H': 0.061, 'U': 0.028, 'I': 0.07, 'V': 0.01, 'J': 0.002, 'W': 0.023, 'K': 0.008, 'X': 0.001, 'L': 0.04, 'Y': 0.02, 'M': 0.024, 'Z': 0.001}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
list_r = []
n = int(input())
hi = input()
for x in range(n):
    str1 = input()
    list2 = []
    possible_ciphers = []
    list_compare = []
    for k in range(1,27):
        list_original = list(str1)
        list_encoded =  []
        for s in list_original:
            if s!=' ':
                encoded_char = alphabet[alphabet.index(s)+k]
            else:
                encoded_char = ' '
            list_encoded.append(encoded_char)
        product = 1
        for a in list_encoded:
            if a != ' ':
                product *= dict_p[a]
        possible_ciphers.append(list_encoded)
        list_compare.append(product)
    index = list_compare.index(max(list_compare))
    list_r.append(possible_ciphers[index])
for b in list_r:
    print(''.join(b))


# In Doubleclickland, there are N cities (N ≤ 5,000), with each city having various trade routes to other cities. In total, there are T trade routes (0 ≤ T ≤ 25,000,000). in Doubleclickland. For each trade route between two cities x and y, there is a transportation cost C(x; y) to ship between the cities, where C(x, y) > 0, C(x, y) ≤ 10,000 and C(x, y) = C(y, x). Out of the N cities, K (1 ≤ K ≤ N) of these cities have stores with really nice pencils that can be purchased on-line. The price for each pencil in city x is Px (0 ≤ Px ≤ 10,000).
# 
# Find the minimal price to purchase one pencil on-line and have it shipped to a particular city D (1 ≤ D ≤ N) using the cheapest possible trade-route sequence. Notice that it is possible to purchase the pencil in city D and thus require no shipping charges.
# 
# Input
# The first line of input contains N, the number of cities. You can assume the cities are numbered from 1 to N. The second line of input contains T, the number of trade routes. The next T lines each contain 3 integers, x y C(x, y), to denote the cost of using the trade route between cities x and y is C(x, y). The next line contains the integer K, the number of cities with a store that sells really nice pencils on-line. The next K lines contains two integers, z and Pz, to denote that the cost of a pencil in city z is Pz. The last line contains the integer D, the destination city.
# 
# Output
# Output the minimal total cost of purchasing a pencil on-line and shipping it to city D.
# 
# Sample Input
# 3
# 3
# 1 2 4
# 2 3 2
# 1 3 3
# 3
# 1 14
# 2 8
# 3 3
# 1
# Sample Output
# 6

# In[20]:


def find_lowest_cost_node(costs, processed):
    list_pairs = costs.items()
    list_valid_pairs = [s for s in list_pairs if s[0] not in processed]
    if len(list_valid_pairs)>0:
        lowest_cost_node = min(list_valid_pairs, key=lambda x: x[1])
        return lowest_cost_node[0]
    return None
def min_cost(start, end, graph):
    costs = {}
    for x in list_nodes:
        if x != start:
            costs[x] = float('inf')
    costs[start] = 0
    parents = {}
    processed = []   
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs[end]
cities = int(input())
trade_routes = int(input())
graph = {}
for x in range(trade_routes):
    a = input()
    a = a.split(' ')
    a = [int(s) for s in a]
    if a[0] not in graph:
        graph[a[0]] = {}
    graph[a[0]][a[1]] = a[2]
    if a[1] not in graph:
        graph[a[1]] = {}
    graph[a[1]][a[0]] = a[2]
num_pencil_costs = int(input())
pencil_costs = {}
for a in range(num_pencil_costs):
    b = input()
    b = b.split()
    b = [int(s) for s in b]
    pencil_costs[b[0]] = b[1]
destination = int(input())
list_nodes = graph.keys()
total_costs = []
for c in list_nodes:
    if c != destination:
        cost = min_cost(c, destination, graph)
        total_costs.append(cost + pencil_costs[c])
print(min(total_costs))


# In[15]:


def find_lowest_cost_node(costs, processed):
    list_pairs = costs.items()
    list_valid_pairs = [s for s in list_pairs if s[0] not in processed]
    if len(list_valid_pairs)>0:
        lowest_cost_node = min(list_valid_pairs, key=lambda x: x[1])
        return lowest_cost_node[0]
    return None
def min_cost(start, end, graph):
    costs = {}
    for x in list_nodes:
        if x != start:
            costs[x] = float('inf')
    costs[start] = 0
    parents = {}
    processed = []   
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs[end]


# In[18]:


graph = {1: {2: 4, 3: 3}, 2: {1: 4, 3: 2}, 3: {2: 2, 1: 3}}
pencil_costs = {1: 14, 2: 8, 3: 3}
destination = 1
list_nodes = graph.keys()
total_costs = []
for c in list_nodes:
    if c != destination:
        cost = min_cost(c, destination, graph)
        total_costs.append(cost + pencil_costs[c])
print(min(total_costs))


# In[170]:


str1 = input()
list1 = []
for a in range(len(str1)):
    for b in range(a + 1, len(str1) + 1):
        list1.append(str1[a:b])
print(list(set(list1)))


# How many distinct substrings does a given string SS have?
# 
# For example, if SS= abc, SS has 7 distinct substrings: , a, b, c, ab, bc, abc. Note that the empty string and SS itself are considered substrings of SS.
# 
# On the other hand, if SS= aaa. SS has only 4 distinct substrings: , a, aa, aaa.
# 
# Input Specification
# The first line of the input file contains NN, the number of test cases. For each test case, a line follows giving SS, a string of from 11 to 50005000 alphanumeric characters.
# 
# Output Specification
# Your output consists of one line per case, giving the number of distinct substrings of SS.
# 
# Grading
# 50% of test cases will have ll (the length of the string) where l≤1000l≤1000. For all cases, l≤5000l≤5000.
# 
# Sample Input
# 2
# abc
# aaa
# Output for Sample Input
# 7
# 4

# In[174]:


num = int(input())
for x in range(num):
    str1 = input()
    list1 = []
    for a in range(len(str1)):
        for b in range(a + 1, len(str1) + 1):
            list1.append(str1[a:b])
    print(len(list(set(list1))) + 1)


# Given a list of unique words, print the all the possible palindrome pairs
# 
# The input will start with an integer n followed by n words. 
# 
# The output will consist of all the palindrome pairs
# 
# Example 1:
# 
# Input: words "abcd","dcba","lls","s","sssll"
# The palindromes are "dcbaabcd","abcddcba","slls","llssssll"
# Input Specification
# 5
# 
# abcd
# 
# dcba
# 
# lls
# 
# s
# 
# sssll
# 
# Output
# 
# dcbaabcd
# abcddcba
# slls
# llssssll

# In[185]:


def check_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False
num = int(input())
words = []
for x in range(num):
    words.append(input())
for a in range(len(words) - 1):
    for b in range(a+1, len(words)):
        if a == b:
            continue
        if check_palindrome(words[b] + words[a]) == True:
            print(words[b] + words[a])
        if check_palindrome(words[a] + words[b]) == True:
            print(words[a] + words[b])


# A string is a palindrome if and only if it reads the same forwards and backwards.
# 
# 
# 
# A substring of a string s is a nonempty sequence of consecutive characters from s.
# 
# 
# 
# Define a string to be odd if and only if all substrings of the string that are palindromes have odd length.
# 
# 
# 
# Given a string s, determine if it is odd.
# 
# 
# 
# Constraints
# 
# 1≤|S|≤100
# 
# 
# 
# S will only contain lowercase ASCII letters.
# 
# 
# 
# Input Specification
# 
# The input consists of a single line containing the string s
# 
# 
# 
# Output Specification
# 
# Print on a single line, if the string is odd, Odd; if not, Even.
# 
# 
# 
# Sample Input
# 
# amanaplanacanalpanama
# 
# Sample Output
# 
# odd
# 
# Sample Input
# 
# madamimadam
# 
# Sample Output
# 
# odd
# 
# Sample Input
# 
# annamyfriend
# 
# Sample Output
# 
# even
# 
# Sample Input
# 
# nopalindromes
# 
# Sample Output
# 
# odd

# In[201]:


def check_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False
str1 = input()
list1 = []
for a in range(len(str1)):
    for b in range(a + 1, len(str1) + 1):
        list1.append(str1[a:b])
test = 0
list2 = []
for x in list1:
    if check_palindrome(x) == True:
        list2.append(x)
for c in list2:
    if len(c) % 2 == 1:
        test += 1
if test == len(list2):
    print('odd')
else:
    print('even')


# Your new cellphone plan charges you for every character you send from your phone. Since you
# 
# tend to send sequences of symbols in your messages, you have come up with the following compression technique: for each symbol, write down the number of times it appears consecutively,
# 
# followed by the symbol itself. This compression technique is called run-length encoding.
# 
# More formally, a block is a substring of identical symbols that is as long as possible. A block will
# 
# be represented in compressed form as the length of the block followed by the symbol in that block.
# 
# The encoding of a string is the representation of each block in the string in the order in which they
# 
# appear in the string.
# 
# Given a sequence of characters, write a program to encode them in this format.
# 
# Input Specification
# 
# The first line of input contains the number N, which is the number of lines that follow. The next
# 
# N lines will contain at least one and at most 80 characters, none of which are spaces.
# 
# Output Specification
# 
# Output will be N lines. Line i of the output will be the encoding of the line i + 1 of the input.
# 
# The encoding of a line will be a sequence of pairs, separated by a space, where each pair is an
# 
# integer (representing the number of times the character appears consecutively) followed by a space,
# 
# followed by the character.
# 
# Sample Input
# 
# 4
# 
# +++===!!!!
# 
# 777777......TTTTTTTTTTTT
# 
# (AABBC)
# 
# 3.1415555
# 
# Output for Sample Input
# 
# 3 + 3 = 4 !
# 
# 6 7 6 . 12 T
# 
# 1 ( 2 A 2 B 1 C 1 )
# 
# 1 3 1 . 1 1 1 4 1 1 4 5
# 
# Explanation of Output for Sample Input
# 
# To see how the first message (on the second line of input) is encoded, notice that there are 3 +
# 
# symbols, followed by 3 = symbols, followed by 4 ! symbols.

# In[276]:


n = int(input())
for x in range(n):
    line = input()
    list1 = list(line)
    list2 = []
    current = 0
    while True:
        unique_char = list1[current]
        list_c = []
        for k in range(current, len(list1)):
            if list1[k] != unique_char:
                break
            list_c.append(list1[k])
        if k == (len(list1) - 1):
            if list1[k] == unique_char:
                list2.append(list_c)
                break
            else:
                current = k
                list2.append(list_c)
        if k != (len(list1) - 1):
            current = k
            list2.append(list_c)
    for x in list2[:len(list2) - 1]:
        print(str(len(x)) + ' ' + str(x[0]), end = ' ')
    print(str(len(list2[-1])) + ' ' + str(list2[-1][0]))


# In[279]:


def is_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False
str1 = input()
list1 = []
for a in range(len(str1)):
    for b in range(a + 1, len(str1) + 1):
        list1.append(str1[a:b])
list2 = []
for x in list1:
    if is_palindrome(x) == True:
        list2.append(len(x))
print(max(list2))


# In[304]:


list_chars = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'], ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '‘'], ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']]
str1 = input()
list1 = list(str1)
str2 = ''
for x in list1:
    if x == ' ':
        str2 += ' '
        continue
    for a in list_chars:
        if x in a:
            index = a.index(x)
            new = a[index - 1]
            str2 += new
            break
print(str2)


# In[302]:


list_chars = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'], ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '‘'], ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'], 
              [' ']]
print(list_chars)


# Jane's family has just moved to a new city and today is her first day of school. She has a list of instructions for walking from her home to the school. Each instruction describes a turn she must make. For example, the list
# 
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# means that she must turn right onto Queen Street, then turn right onto Fourth Street, then finally turn right into the school. Your task is to write a computer program which will create instructions for walking in the opposite direction: from her school to her home.
# 
# The input and output for your program will be formatted like the samples below. You may assume that Jane's list contains at least two but at most five instructions, and you may assume that each line contains at most 10 characters, all of them capital letters. The last instruction will always be a turn into the "SCHOOL".
# 
# Sample Input 1
# R
# QUEEN
# R
# FOURTH
# R
# SCHOOL
# Sample Output 1
# Turn LEFT onto FOURTH street.
# Turn LEFT onto QUEEN street.
# Turn LEFT into your HOME.
# Sample Input 2
# L
# MAIN
# R
# SCHOOL
# Sample Output 2
# Turn LEFT onto MAIN street.
# Turn RIGHT into your HOME.

# In[2]:


list1 = []
a = input()
while a != 'SCHOOL':
    list1.append(a)
    a = input()
list1.append(a)
list1 = list1[::-1]
list1 = list1[1:]
a = list1.pop(-1)
for k, x in enumerate(list1):
    if x == 'R':
        print('Turn LEFT onto', list1[k + 1], 'street.')
    if x == 'L':
        print('Turn RIGHT onto', list1[k + 1], 'street.')
if a == 'R':
    print('Turn LEFT into your HOME.')
if a == 'L':
    print('Turn RIGHT into your HOME.')


# In[20]:


def binary(n):
    if n == 1:
        return [1]
    else:
        child = n // 2
        remainder = n % 2
        return binary(child) + [remainder]
num = int(input())
for b in range(num):
    c = int(input())
    list1 = binary(c)
    if len(list1) <= 4:
        length = len(list1)
        list2 = [0] * (4 - length) + list1
        list2 = [str(s) for s in list2]
        str1 = ''.join(list2)
        print(str1)
    if len(list1) > 4:
        list2 = [list1[i:i + 4] for i in range(0, len(list1), 4)]
        str2 = ''
        for list1 in list2:
            list1 = [str(s) for s in list1]
            str1 = ''.join(list1)
            str2 += str1
            str2 += ' '
        print(str2)


# We are familiar with infix notation for representing expressions, where the operator is placed infix between the operands, as in 5 * 5 . Given an expression in postfix notation, such as 5 5 * , evaluate the expression and print it to standard output, rounded to one decimal place. Valid operands are * (multiplication), / (division), + (addition), - (subtraction), % (mod), and ^ (exponentiation).
# 
# Input Format
# 
# A valid postfix expression. The input will have no more than characters, and the value of each number in the input
# 
# and each intermediate result will be less than or equal to .
# 
# Output Format
# 
# The result of the evaluation. The answer will be considered correct if its absolute or relative error does not exceed .
# 
# Sample Input
# 
# 5 5 +
# 
# Sample Output
# 
# 10.0
# 
# Sample Input
# 
# 5 5 + 6 * 8 -
# 
# Sample Output
# 
# 52.0

# In[44]:


str1 = input()
list1 = str1.split(' ')
list2 = ['+', '-', '*', '/', '%', '^']
for k, x in enumerate(list1):
    if x not in list2:
        list1[k] = int(x)
stack = []
for a in list1:
    if type(a) == int:
        stack.append(a)
    else:
        if a == '+':
            count = 0
            count += stack.pop(-1)
            count += stack.pop(-1)
        if a == '-':
            count = stack.pop(-1)
            count = stack.pop(-1) - count
        if a == '*':
            count = 1
            count *= stack.pop(-1)
            count *= stack.pop(-1)
        if a == '/':
            count = stack.pop(-1)
            count = stack.pop(-1) / count
        if a == '%':
            number1 = stack.pop(-1)
            number2 = stack.pop(-1)
            count = number2 % number1
        if a == '^':
            number1 = stack.pop(-1)
            number2 = stack.pop(-1)
            count = number2 ^ number1
        stack.append(count)
print(float(stack[0]))


# Standard web browsers contain features to move backward and forward among the pages recently visited.
# 
# One way to implement these features is to use two stacks to keep track of the pages that can be reached by
# 
# moving backward and forward. In this problem, you are asked to implement this.
# 
# The following commands need to be supported:
# 
# BACK: Push the current page on the top of the forward stack. Pop the page from the top of the backward
# 
# stack, making it the new current page. If the backward stack is empty, the command is ignored.
# 
# FORWARD: Push the current page on the top of the backward stack. Pop the page from the top of the
# 
# forward stack, making it the new current page. If the forward stack is empty, the command is ignored.
# 
# VISIT : Push the current page on the top of the backward stack, and make the URL specified the new
# 
# current page. The forward stack is emptied.
# 
# QUIT: Quit the browser.
# 
# Assume that the browser initially loads the web page at the URL http://www.acm.org/
# 
# Input Specification
# 
# Input is a sequence of commands. The command keywords BACK, FORWARD, VISIT, and QUIT are
# 
# all in uppercase. URLs have no whitespace and have at most 70 characters. You may assume that no
# 
# problem instance requires more than 100 elements in each stack at any time. The end of input is indicated
# 
# by the QUIT command.
# 
# Output Specification
# 
# For each command other than QUIT, print the URL of the current page after the command is executed if
# 
# the command is not ignored. Otherwise, print "Ignored". The output for each command should be printed
# 
# on its own line. No output is produced for the QUIT command.
# 
# Sample Input
# 
# VISIT http://acm.ashland.edu/
# 
# VISIT http://acm.baylor.edu/acmicpc/
# 
# BACK
# 
# BACK
# 
# BACK
# 
# FORWARD
# 
# VISIT http://www.ibm.com/
# 
# BACK
# 
# BACK
# 
# FORWARD
# 
# FORWARD
# 
# FORWARD
# 
# QUIT
# 
# Sample Output
# 
# http://acm.ashland.edu/
# 
# http://acm.baylor.edu/acmicpc/
# 
# http://acm.ashland.edu/
# 
# http://www.acm.org/
# 
# Ignored
# 
# http://acm.ashland.edu/
# 
# http://www.ibm.com/
# 
# http://acm.ashland.edu/
# 
# http://www.acm.org/
# 
# http://acm.ashland.edu/
# 
# http://www.ibm.com/
# 
# Ignored

# In[166]:


a = input()
list_input = []
while a != 'QUIT':
    list_input.append(a)
    a = input()
backward = ['http://www.acm.org/']
forward = []
current = 'http://www.acm.org/'
for x in list_input:
    if x[:5] == 'VISIT':
        backward.append(x[6:])
        current = x[6:]
        forward = [current]
        print(x[6:])
    if x == 'BACK':
        if len(backward)<=1:
            print('Ignored')
        else:
            a = backward.pop(-1)
            current = backward[-1]
            forward.append(current)
            print(current)
    if x == 'FORWARD':
        if len(forward)<=1:
            print('Ignored')
        else:
            a = forward.pop(-1)
            current = forward[-1]
            backward.append(current)
            print(current)


# In[ ]:


VISIT http://acm.ashland.edu/

VISIT http://acm.baylor.edu/acmicpc/

BACK

BACK

BACK

FORWARD

VISIT http://www.ibm.com/

BACK

BACK

FORWARD

FORWARD

FORWARD

QUIT


# In[163]:


list_input = ['VISIT http://acm.ashland.edu/', 'VISIT http://acm.baylor.edu/acmicpc/', 'BACK', 'BACK', 
              'BACK', 'FORWARD', 'VISIT http://www.ibm.com/', 'BACK', 'BACK', 'FORWARD', 'FORWARD', 'FORWARD']
backward = ['http://www.acm.org/']
forward = []
current = 'http://www.acm.org/'
for x in list_input:
    if x[:5] == 'VISIT':
        backward.append(x[6:])
        current = x[6:]
        forward = [current]
        print(x[6:])
        print('\r')
    if x == 'BACK':
        if len(backward)<=1:
            print('Ignored')
            print('\r')
        else:
            a = backward.pop(-1)
            current = backward[-1]
            forward.append(current)
            print(current)
            print('\r')
    if x == 'FORWARD':
        if len(forward)<=1:
            print('Ignored')
            print('\r')
        else:
            a = forward.pop(-1)
            current = forward[-1]
            backward.append(current)
            print(current)
            print('\r')

