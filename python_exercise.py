import math


# name = "Yonas"
# print(name)

# # 2 ------------------------------------
# # Write a program to swap values of two variables.


# def swaps(a, b):
#     return b, a


# a, b = 5, 7
# a, b = swaps(a, b)
# print(f"a: {a}, b: {b}")

# # 3 ------------------------------------
# # Convert a float to an integer and print the result.

# num = 7.6245
# print(int(num))

# # 4 ------------------------------------
# # Take user input and check if it is a string, integer, or float.

# # val = input("Enter a value: ")

# # if val.isnumeric():
# #     print("val is numeric")

# # if isinstance(val, float):
# #     print("f: {val} is fstring")
# # elif isinstance(val, int):
# #     print("f: {val} is int")
# # elif isinstance(val, float):
# #     print("f: {val} is float")
# # else:
# #     print("f: {val} is unknown")


# # 5 ------------------------------------
# # Write a program to calculate the area of a circle (given radius)


# def area(r):
#     return math.pi * r**2


# print(area(5))


# # 1 ------------------------------------
# # Write a program to check if a number is positive, negative, or zero.


# def isPositive(num):
#     if num < 0:
#         print(f"num {num} is negative")
#     elif num == 0:
#         print(f"num {num} is zero")
#     else:
#         print(f"num {num} is positive")


# isPositive(25)


# # 2 ------------------------------------
# # Print the first 10 even numbers using a `for` loop.
# for i in range(0, 10):
#     print(i)

# # 3 ------------------------------------
# # Ask the user for a number and check if it is divisible by both 3 and 5.

# # try:
# #     val = input("Enter a number: ")
# #     val = int(val)
# #     if val % 3 == 0 and val % 5 == 0:
# #         print(f"{val} is divisible by both 3 and 5.")
# #     else:
# #         print(f"{val} is not divisible by both 3 and 5.")
# # except Exception as e:
# #     print(f"{val} is an {e}")

# # 4 ------------------------------------
# # Write a program that prints the factorial of a number using a loop.
# fact = 1
# num = 5

# for i in range(1, num + 1):
#     fact = fact * i
# print(fact)

# # 5 ------------------------------------
# # Print all numbers from 1 to 100 that are divisible by 7
# for i in range(1, 100):
#     if i % 7 == 0:
#         print(i)


# ################################ FUNCTIONS ################################


# # 1 ------------------------------------
# # Write a function that returns the square of a number.
# def squared(num):
#     return num**2


# print(squared(27))


# # 2 ------------------------------------
# # Create a function that checks if a number is prime.
# def is_prime(num):
#     return num


# # 3 ------------------------------------
# # Define a function to return the maximum of three numbers.
# def max_of_three(a, b, c):
#     # return max(a, b, c)
#     if (a >= b) and (a >= c):
#         return a
#     elif (b >= a) and (b >= c):
#         return b
#     else:
#         return c


# print(max_of_three(34, 75, 12))


# # 4 ------------------------------------
# # Write a recursive function to calculate factorial.
# def factorial(num):
#     if num < 1:
#         return 1
#     else:
#         return num * factorial(num - 1)


# print(factorial(5))


# # 5 ------------------------------------
# # Create a function that takes a string and returns the number of vowels in it
# def count_vowels(myString):
#     vowels = ["a", "e", "i", "o", "u"]

#     counter = 0
#     for i in myString:
#         if i in vowels:
#             counter += 1
#     return counter


# print(count_vowels("this is a test"))

# ################################ LISTS ################################


# # 1 ------------------------------------
# # Create a list of 5 numbers and print their sum.
# nums = [1, 2, 3, 4, 5]
# s = 0
# for i in nums:
#     s += i
# print(f"sum of {nums}: {s}")


# # 2 ------------------------------------
# # Append an item to a list and remove an element.
# nums = [1, 2, 3, 4, 5]
# nums.append(85)
# nums.remove(2)
# print(nums)

# # 3 ------------------------------------
# # Sort a list in descending order.
# nums = [1, 2, 3, 5, 7, 4, 3, 8, 2, 7]
# nums.sort(reverse=True)
# print(nums)


# # 4 ------------------------------------
# # Count how many times an element appears in a list.
# def count(myList, val):
#     counter = 0
#     for item in myList:
#         if item == val:
#             counter += 1
#     return counter


# nums = [1, 2, 3, 5, 7, 4, 3, 8, 2, 7]
# print(count(nums, 2))


# # 5 ------------------------------------
# # Write a function that takes a list and returns a new list with only the even numbers
# def even_list(nums):
#     myList = [val for val in nums if val % 2 == 0]
#     return myList


# print(even_list(nums))


# ################################ TUPLES ################################


# # 1 ------------------------------------
# # Create a tuple with at least 4 items and access the second item.
# items = ("first", "second", "third", "fourth")

# print(items[1])

# # 2 ------------------------------------
# # Convert a list to a tuple.

# myList = ["first", "second", "third", "fourth"]
# myTuple = tuple(myList)
# print(type(myTuple))


# # 3 ------------------------------------
# # Write a function that returns the first and last elements of a tuple.
# def first_last(myTuple):
#     if len(myTuple) > 1:
#         return myTuple[0], myTuple[-1]
#     else:
#         return myTuple[0]


# print(first_last(items))
# # myTuple = ("first",) # single item tuple must be followed by a comma else its a string
# print(first_last(myTuple))

# # 4 ------------------------------------
# # Check if an element exists in a tuple.

# ele = 7
# print(ele in myTuple)

# # 5 ------------------------------------
# #  Use tuple unpacking to assign values to multiple variables.

# myTuple = ("first", "second", "third", "fourth")
# a, b, c, d = myTuple
# print(a, b)


# ################################ SETS ################################


# # 1 ------------------------------------
# # Create two sets and find their intersection.

# set_a = {1, 2, 3, 4, 5, 7, 8}
# set_b = {1, 7, 9, 3}
# intersect = set()

# # for i in set_a:
# #     for j in set_b:
# #         if i == j:
# #             intersect.add(i)

# # for num in set_a:
# #     if num in set_b:
# #         intersect.add(num)

# intersect = set_a & set_b

# print(intersect)

# # 2 ------------------------------------
# # Add a new element to a set.
# set_a = {1, 2, 3, 4, 5, 7, 8}

# set_a.add(27)
# print(set_a)


# # 3 ------------------------------------
# # Remove duplicates from a list using a set.

# set_a = [1, 2, 3, 5, 7, 4, 3, 8, 2, 7]

# set_a = set(set_a)
# print(set_a)

# # 4 ------------------------------------
# # Check if one set is a subset of another.
# set_a = {1, 2, 3, 4, 5, 7, 8}
# set_b = {1, 7, 3}


# def is_subset(set_a, set_b):
#     for item in set_a:
#         if item not in set_b:
#             return False
#     return True


# print(f"{set_a} is subset of {set_b} {is_subset(set_a, set_b)}")
# print(f"{set_b} is subset of {set_a} {is_subset(set_b, set_a)}")

# # print(f'{set_a} is subset of {set_b} {set_a.issubset(set_b)}') # library function
# # print(f'{set_b} is subset of {set_a} {set_b.issubset(set_a)}')

# # print(set_a <= set_b)
# # print(set_b <= set_a)


# # 5 ------------------------------------
# # Find the union and difference of two sets.

# print(set_a | set_b)
# # print(set_a.union(set_b))

# # set_a.update(set_b)
# # print(set_a)

# # # for s in set_b:
# # #     set_a.add(s)

# # # print(set_a)

# print(set_a ^ set_b)  # difference
# print(set_a - set_b)
# print(set_a.difference(set_b))

# diff = {val for val in set_a if val not in set_b}
# print(diff)


################################ DICTIONARIES ################################


# 1 ------------------------------------
# Create a dictionary to store the name and age of 3 people.

rows = [
    {"name": "John", "age": 25, "salary": 5000},
    {"name": "Alice", "age": "", "salary": 7000},
    {"name": "Bob", "age": "abc", "salary": 3000},
    {"name": "Tom", "age": 30, "salary": ""},
]

rows = {
    0: {"name": "John", "age": 25, "salary": 5000},
    1: {"name": "Alice", "age": "", "salary": 7000},
    2: {"name": "Bob", "age": "abc", "salary": 3000},
    3: {"name": "Tom", "age": 30, "salary": 4000},
}

# 2 ------------------------------------
# Access the value of a key from a dictionary.

john = rows[0]["name"]
print(john)


# 3 ------------------------------------
# Add a new keyvalue pair to a dictionary.

rows[7] = {"name": "Marie", "age": 22, "salary": 34700}

print(rows)


# 4 ------------------------------------
# Write a function that counts the frequency of characters in a string using a dictionary.
def count_freq(myString):
    freq = {}
    words = myString.strip()

    for s in words:
        freq[s] = freq.get(s, 0) + 1
        # if s in freq:
        #     freq[s] += 1
        # else:
        #     freq[s] = 1

    return freq


print(count_freq("how about this string"))

# 5 ------------------------------------
# Merge two dictionaries into one
d1 = {"name": "John", "age": 25}
d2 = {"salary": 6000}


print(d1 | d2)  # merge

d1 = {
    0: {"name": "John", "age": 25, "salary": 5000},
    1: {"name": "Alice", "age": "", "salary": 7000},
    2: {"name": "Bob", "age": "abc", "salary": 3000},
    3: {"name": "Tom", "age": 30, "salary": 4000},
}

d2 = {6: {"name": "Marie", "age": 22, "salary": 34700}}

print(d1 | d2)

# d1.update(d2)
# print(d1)

d1 |= d2
print(d1)


################################ Algorithm ################################


# 1 ------------------------------------
# Write a program to find all the prime numbers between 1 and 50.


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = [n for n in range(1, 50) if is_prime(n)]

print(f"primes {primes}")


# 2 ------------------------------------
# Reverse a string without using builtin functions.


def reverse(myString):
    myList = list()

    for i in range(len(myString) - 1, -1, -1):
        myList.append(myString[i])

    return "".join(myList)


word = "largest"
s = word[::-1]
print(s)

print(reverse(word))

# 3 ------------------------------------
# Find the second largest number in a list.


def second_largest(nums):
    if len(nums) < 2:
        return None

    first = second = float("-inf")
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float("-inf") else None


# Example
myList = [1, 2, 3, 5, 7, 4, 3, 8, 2, 7]
print(second_largest(myList))


# 4 ------------------------------------
# Write a program to count the number of words in a sentence.
def count_words(words):
    myWords = words.split()
    return len(myWords)


sentence = "Write a program to count the number of words in a sentence"
print(count_words(sentence))

# 5 ------------------------------------
# Check if two strings are anagrams of each other


def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    # return sorted(str1) == sorted(str2)

    c1 = count_freq(str1)
    c2 = count_freq(str2)

    return c1 == c2


print(is_anagram("silent", "listen"))
