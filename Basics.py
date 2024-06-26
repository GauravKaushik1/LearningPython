# output
# print("Hello Gaurav, Python is case-sensitive")
# supports charcterSet
# letters - A to Z, a to z
# Digits - 0 to 0
# Special Symbols - * + / etc.
# Whitespaces - Blank Space, tab, carriage return, newline, formfeed
# Other characters - Python can process all ASCII and Unicode characters(emojies included) as a part of data or literals
# Escape Characters
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed
# print("Backslash\\")
# print("New Line\n")
# print("Carriage Return\r")
# print("Tab\t")
# print("Backspace\b next is")
# print("Form Feed\f")
# #the string and numeric values can operate together
# print("Gaurav is great! "*3)

# A,B=2,3
# Txt = "@"
# print(2*Txt*3)

# A,B="2",3#here 2 is a string
# Txt="@"
# print((A+Txt)*B)

# Data Type
# Integers
# Float
# A,B=12,-5
# C=A//B#floor division meaning the smallest integer less than or equal to the float value
'''
0.1->0
5.2->5
7.99->7
11.2->11
-5.2->-6# negative value gets lower
5.0->5
'''
'''
remainder values(%):
n + - + - (ve)
/
d + - - + (ve)
=
r + + - + (ve)
'''
# print(C)
# Boolean
# None
# String

# format string in python
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

# This prints out "Hello, John!"
# name = "Gaurav"
# print("Hello, %s!" % name)
# Run
# To use two or more argument specifiers, use a tuple (parentheses):
# This prints out "John is 23 years old."
# name = "Gaurav"
# age = 23
# print("%s is %d years old." % (name, age))

# Run
# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string. For example:
# This prints out: A list: [1, 2, 3]
# mylist = [1,2,3]
# print("A list: %s" % mylist)

# Run
# Here are some basic argument specifiers you should know:
# data = ("Gaurav", "Kaushik", 53.44)
# format_string = "Hello "

# Using f-string for formatting
# print(f"{format_string}{data}")

# data = ("Gaurav", "Kaushik", 53.44)
# format_string = "Hello {}"

# Using format() method for formatting
# print(format_string.format(data))

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
# string functions
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

#Take user input

# #string input
# name = input("name : ")
# print(name)

# # int input
# age = int(input("age : "))
# print(age)

# # float input
# price = float(input("price : "))
# print(price)

# #None
# a = None
# print(type(a))

# age = 23
# old = False
# a = None
# print("type of age is ",type(age))
# print("type of old is ",type(old))
# print("type of a is ",type(a))
# print("** is a valid operator in python i.e., 2**3 is 2^3 or ",2**3)

'''
Types of Operators
Arithmetic Operators(+, -, *, /, %, **)
Relational / Comparision Operators(==, !=, >, <, >=, <= )
Assignment Operators(=, -=, *=, /=, %=, //=, **=)
Logical Operators(not, and, or)
Membership Operators(in, in not)
Identity Operators(is, is not)
Bitwise Operators(&, |, ^)

Operator precedence
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR	
If two operators have the same precedence, the expression is evaluated from left to right.
not>and>or
'''

'''
# Ternary Operator
<var> = (false_val, true_val)[<condition>] 
'''
# age = int(input("age :"))
# vote = ("false", "true") [age<18]
# print(vote)

'''
#Ternary Operator to add the postfix to numbers(st,nd,rd,th) ###
as per the number to the custom input taken several times through loops
'''

movies = []
for i in range(5):
    result_str = "Enter "+ str(i + 1)
    #str method converts to string the result
    # if((i+1)==1):
    #     result_str += "st"
    # elif((i+1)==2):
    #     result_str += "nd"
    # elif((i+1)==3):
    #     result_str += "rd"
    # else:
    #     result_str += "th"
    # result_str += " Movie name" 

    # first attempt at shorthand
    # movies.append(input("enter ",i,(((("th", "rd") [i==3], "nd") [i==2], "st") [i==1])," movie: "))
    
    # second attempt at shorthand that works

    result_str = "Enter "+ str(i + 1) + str(((("th","rd")[(i+1) == 3],"nd")[(i+1)==2],"st") [(i+1) == 1])  + " Movie name"
    # used the string concatenation and also the ternary operator
    movies.append(input(result_str))
print(movies)

'''
Best Practices
simple instructions
one instruction per task
short & meaningful variable names
use appropriate comments
avoid complex expressions
'''
'''
conditional statements
if -always checks
elif -only checks when if does not match
else -if all are false run this default case
'''

'''
String
'''
# str1 = "This is a string"
# str2 = 'ApnaCollege'
# str3 = """this is a string"""
# use escape sequence characters to print the next line, etc and the "
# " is not supported in the python
# str1 = "Gaurav"
# str2 = "Kaushik"
# final_str = str1 + str2
# print(final_str)
# final_str = str1+ " "+ str2#the length also includes spaces and special characterstics
# print(final_str)
'''
Index
'''
# str = "Gaurav"
# ch = str[2]
# print(ch)
#cannot change the string using assignment using index
# str[0]='g'
'''
Slicing
Accessing the parts of a string
str[starting_index : ending_index] #ending idx is not included
'''
# str = "Gaurav Kaushik"
# print(str[5:12])#usefull in machine learing
# print(str[:4])
# print(str[1:])
# print(str[5:len(str)])# the last index is len(str) i.e.m length of str
'''
-ve index in Slicing
-ve indexes is limited to slicing
'''
# str = "Apple"
# print(str[-5:-2])#count to the last

'''
String Functions
'''
# str = "I am a coder. The software engineer in the making"
# print(str.endswith("er."))#returns true if string ends with substr
# print(str.capitalize())#capitalizes 1st char
# old = "coder"
# new = "programmer"
# print(str.replace(old, new))#replaces all occurrences of old with new
# print(str)
# word ="engineer"
# print(str.find(word))#returns 1st index of 1st occurence
# print(str.count("am"))
# userFirstName = input("Enter your name: ")
# print(len(userFirstName))
# str = "$ sojroe $sjklf $"
# print(str.count("$"))
# num = int(input("Enter a number"))
# if (num%2 == 0):
#     print("even")
# else:
#     print("odd")
# a =int(input("Enters first number"))
# b =int(input("Enters second number"))
# c =int(input("Enters third number"))
# if(a >= b and a >= c):
#     print("first number is largest",a)
# elif(b >= c):
#     print("second number is largest",b)
# else:
#     print("third is largest",c)

# x = int(input("enter number: "))

# if(x % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple")
'''
Lists - uses []
List and tupples are eqivalent of arrays
A built-in data type that stores set of values
It can store elements of different types(interger, float, string, etc)
'''
# marks = [87,64,33,95,76] #marks[0], marks[1]
# student = ["Karan",85,"Delhi"] #student[0], student[1]
# student[0] = "Arjun" #allowed in python
# len(student) #returns length
# print(marks)
# print(type(marks))
# print(marks[3])
# print(marks[1:])
# print(marks[:3])
# print(marks[2:4])#last index is not included
# print(marks[-3:-1])
'''
Python lists are different from C++ and Java as the different data types can be merged together
list string does not allow the changing of the string
lists are mutable
'''
'''
List specific Methods
'''
# list = [2, 1, 3]
# print(list.append(4))#adds one element at the end [2, 1, 3, 4]
# print(list.sort())#sorts in ascending order [1, 2, 3]
# # print(list.sort(reverse==True))#sorts in descending order [3, 2, 1]
# print(list.reverse())#reverse list [3, 1, 2]
# print(list.insert(index,element))#insert element at index
'''
Tupples in Python - uses ()
A built-in data type that lets us create immutable sequences of values.
These are immutable
'''
# tup = (87, 64, 33, 95, 76) #tup[0], tup[1]
# tup[0] = 43 #NOT allowed in python

# tup1 = ()
# tup1 = (1,)
# tup3 = (1, 2, 3)
# print(tup[0])
# print(tup[1])
# print(type(tup))
# tup = (1)#integer wrapped in ()
# print(type(tup))
# tup = (1,)#add , to make it behave like tupple
# print(type(tup))
# tup = (2, 1, 3, 1)
# el=1
# print(tup.index(el))#returns index of first occurrence tup.index(1) is 1
# el=1
# print(tup.count(el))#tup.count(1) is 2
'''
First Approach
'''
# movies = []

# mov1 = input("enter 1st movie: ")
# mov2 = input("enter 2nd movie: ")
# mov3 = input("enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

'''
Second Approach
'''
# movies = []

# mov = input("enter 1st movie: ")
# movies.append(mov)
# mov = input("enter 2nd movie: ")
# movies.append(mov)
# mov = input("enter 3rd movie: ")
# movies.append(mov)

# print(movies)
'''
Third Approach
'''
# movies = []

# movies.append(input("enter 1st movie: "))
# movies.append(input("enter 2nd movie: "))
# movies.append(input("enter 3rd movie: "))

# print(movies)
'''
Forth Approach -yet to be done
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

'''

# Check if the list is a palindrome of elements. (Hint: use copy() method)
# list = [1, 2, 1]
# copy_list = list.copy()#copy() makes a shallow copy
# copy_list.reverse()
# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not palindrome")
# count the number of students with the "A" grade in the following tuple.
# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))
# store the above values in a list & sort them "A" to "D"
# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)

'''
Dictionary
Dictionary are used to store data values in key:value pairs
They are unordered, mutable(changeable) & don't allow duplicate keys
key can be float
tupple is the key only and not value
no duplicate keys okay
'''
'''
dict = {
    "name": "Gaurav",
    "cgpa": 9.6,
    "marks": [98, 97, 95],
}
dict["name"], dict["cgpa"], dict["marks"]
dict["key"] = "value" #to assign or add new
'''
# info = {
#     "key": "value",
#     "name": "apnacollege",
#     "learning": "coding"
# }
# print(info)
'''
nested Dictionary
'''
# student = {
#     "name": "Gaurav Kaushik",
#     "subjects": {
#         "phy": 100,
#         "chem": 100,
#         "math": 100
#     }
# }
# print(student["subjects"]["chem"])
# print(students.keys())#returns all keys but not nested keys
# print(list(students.keys()))#using type casting to convert to list
# print(len(list(student.keys())))#using the len to get the total number of keys
# print(students.values())#returns all values 
# print(list(students.values()))#dictionary inside of list
# print(students.items())#returns all(key, val) pairs as tuples
# print(students.get("key"))#returns the key according to value
# print(students.update("city": "delhi"))#inserts the specified items{key: value pair} to the dictionary
# new_dict = {"newsLetter": "yes"}
# student.update(new_dict)
# print(student)

'''
Sets-uses {} like dictionary
set is the collection of the unordered items.
Each element in the set must be unique & immutable.
nums = {1,2,3,4}
set2={1,2,2,2}

#repeated elments stored only once, so it resolved to {1,2}
null_set = set() #empty set syntax
'''
collection = {1,2,3,4,"word","string",10}#repeated ones will be ignored also it seems set does not have a fixed order

print(collection)
print(type(collection))
'''
Difference between ditionary and set dictionary has key value pairs also this syntax of empty dictionary and empty set:
'''
collection = {}#not an empty set it is empty dictionary
print(type(collection))

collection = set()#empty set
print(type(collection))

'''
set - are mutable but
elements of set - are immutable
we can pass tupple to it but not the values of list or dictionary.
we can add or remove the elements but not change the element's value
'''
# set.add(el) #adds an element
# set.remove(el) #removes the element
# set.clear() #empties the set
# set.pop() #removes a random value

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add("Gaurav Kaushik")
# collection.add((1,2,"Gaurav","is","great"))
# collection.add([1,2,3,"Gaurav",6])
# collection.add({"Gaurav":"Kaushik"})
#hashable values means the conversion to hash and that hash will not change otherwise the immutable values that can not be muted or changed in lifetime
# collection.remove(7)#scince the 7 is not in the set it will result in key error
# print(collection)
# #pop removes the random value
# print(collection.pop())
# print(collection.pop())#use to generate random values from given set
# set.union(set2)#combines both set values & returns new
# set.intersection(set2)#combines common values & returns new

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))#{1,2,3,4}
print(set1)
print(set2)

print(set1.intersection(set2))
dictionary ={
    "table": ["a piece of furniture", "list of facts&figures"],
    "cat":"a small animal"
}
#unique subject is the classroom so 
subject = set()
subject = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}
print(len(subject))
marks = {}
x = int(input("enter phy : "))
marks.update({"phy":x})

x = int(input("enter maths : "))
marks.update({"maths":x})

x = int(input("enter chem : "))
marks.update({"chem":x})

print(marks)

#store the 9 and 9.0 in a set
# values = {9,9.0}#both are a single value as their hash is the same
# one methodsave as a string
#values = {9,"9.0"}
#save them with the data type so use tpples
values = {
    ("float",9.0),
    ("int",9)
}
'''
Loops in python-try not to make an infinite loop
    while condition :
        some work
    for condition :
        some work
'''
count = 1
while count <= 5:
    print(count)
    count += 1
i = 1
while i <= 100:#stop condition
    print(i)
    i += 1
i = 100
while i >= 1:#stop condition
    print(i)
    i -= 1
n = 3
i = 1
while i<=10:
    print(n + " * " + i + " = " + n*i)
    i += 1
nums = [1,4,3,16,25,31,43,64,80,100]
heroes = ["volverine","aquaman","spiderman","","ironman", "thor", "superman", "batman"]
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
i = 0
# while i<= len(nums)-1:
while (i < len(nums)) :
    print(nums[i])
    i += 1
i = 0
while (i < len(heroes)) :
    print(heroes[i])
    i += 1
#search for a number in a tupple using loops
nums = (1,4,3,16,25,31,43,64,80,100)
x = 16
i = 0
while i < len(nums):
    if(nums[i] == x) :
        print("FOUND at index", i)
        break
    else:
        print("finding...")
    i += 1
print("end of loop")
'''
Break - used to terminate the loop when encountered
continue - terminates execution in the current iteration & continues execution of the loop with the next iteration.
'''
i = 0
while i <= 10:
    if(i == 3):
        i +=1
        continue #skip
    print(i)
    i += 1
'''
for loop - for loops for sequential traversal. For traversing list, string, tuples etc.
'''
# #for loops
# for el in list:
#     #some work
# list = [1, 2, 3]
# for el in list:
#     print(el)

# #for loop with else
# for el in list:
#     #some work
# else:
#     #work when loop ends
# for el in list:
#     print(el)
# else:
#     print("END")

# list =[1,2,3,4,5]

# for val in nums:
#     print(val)

veggies =["ladyfinger", "potato", "cucumber", "eggPlant"]
for val in veggies:
    print(val)

tup = (1,2,3,4,5,6,7,8)

for num in tup:
    print(num)

str = "apnacollege"

for char in str:
    print(char)
for char in str:
    if(char == '0'):
        print("o found")
        break
    print("")
else:
    print("END of loop reached")#where break is used is not executed if broken in the middle without finishing
print("End")

nums = [1,4,3,16,25,31,43,64,80,100]
for el in nums:
    print(el)

nums= (1,4,3,16,25,31,43,64,80,100)

x = 43
index = 0
for el in nums:
    if(x == el):
        print(x+" found in the list at :" + index)
        break
    index += 1
'''
range()
Range functions return a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.
range(start?, stop, step?)
'''
# for el in range(5):
#     print(el)

# for el in range(1,5):
#     print(el)

# for el in range(1,5,2):
#     print(el)

# print(range(5))

# seq = range(5)#upto 4 and only the stop parameter is given

# for i in seq:
#     print(i)

# for i in range(2,10):#start and stop is given
#     print(i)

# for i in range(2, 100, 2):#start stop and step #100 is not included
#     print(i)
# for i in range(2, 101, 2):#start stop and step #to print 100 as well
#     print(i)
# for i in range(1,102,2):#print numbers upto odd numbers upto102
#     print(i)
# #print reverse numbers
# for i in range(100, 0, -1):#step size can be negative
#     print(i)
# n = 11
# for i in range(1,n):
#     print(n + " * " + i + " = " + n*i)
'''
Pass Statement - pass is a null statement that does nothing. It is used as a placeholder for future code.
for el in range(10):
    pass
'''
# for i in range(5):
#     #empty
#     pass

# if i > 5:
#     pass

# print("some useful work")

# n = 5
# sum = 0
# i=1
# ###Experiment###
# while i in range(n+1):#update statement is still needed
#     sum += i
#     i += 1

# while i <= n:
#     sum += i
#     i += 1

#  for i in range(n+1):
#     sum += i
# print(sum)

# n = 5
# fact = 1 #multipling by 0 will make factorial 0 always be 0 so use 1 instead
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print("factorial = ", fact)

# n = 5
# fact = 1


# for i in range(n+1):
#     fact *= i

# print("factorial = ", fact)

'''
Function
block of statements that perform a specific task
made to reduce function redundancy
def func_name(param1, param2..):
    #some work
    return val
func_name(arg1, arg2 ..)#function call
'''
#function definition
def calc_sum(a,b):#a and b are parameters
    # sum = a + b
    # print(sum)
    # return sum
    return a+b

print(calc_sum(2,10))#this is a function call with 2, and 10 as the arguments

print(calc_sum(12,15))

def print_hello():
    print("hello")
print_hello()
print_hello()

'''
function that does not return any thing outputs none
'''
output = print_hello()
print(output)   #none

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1, 2, 3)

'''
function types
    Built-in functions - print(), len(), type(), range()
    User defined functions -
'''
print("Gaurav Kaushik")#object - value to print, sep- separators, end- ending with this it will become
print("Gaurav","Kaushik")#function arguments do not have a gap but they will in output as it is the defalult separator #sep = " "
#below must be in different lines coz of end- the ending is "\n"
print("Gaurav")#end = "\n"
print("Kaushik")
print("is a GOAT-Greatest Of All Time")
'''
Printing 2 print functions on the same line
Printing using multiple print funtions in the same line
Pass the arguments like end = " " or something as the agrument after the text
'''
print("Gaurav", end=" ")
print("Kaushik")
print("Gaurav", "Kaushik", "doing charaity","for himself",sep="-", end=" is great ")

'''
Default parameters
Assigning a default value to parameter, which is used when no argument is passed.

'''
def cal_prod(a, b=2):#first should be the non default then default
    print(a*b)
    return a+b

print(cal_prod(1))

cities = ["delhi", "gurgaon", "noida", "pune", "chennai"]
heroes = ["volverine","aquaman","spiderman","","ironman", "thor", "superman", "batman"]
def print_len(list):
    print(len(list))

# print_len(cities)
# print_len(heroes)
def print_list(list):
    for item in list:
        print(item,end=" ")
    else:
        print()# the change in ending results in showing up of % character in output so to reduce that we will use the else to execute an empty print statement when the loop executes completely
    # print()#if not willing to use else use this

print_list(cities)
print_list(heroes)

n = 5
def cal_fact(n):
    for i in range(1, n+1):
        fact *= i     
    print(fact)

cal_fact(6)
cal_fact(n)
'''
#convert usd to inr

1 usd = 150 inr
'''
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(73)



def homeworkProblem(n):
    if (n%2 ==0):
        print("even")
    else:
        print("odd")

homeworkProblem(104)
homeworkProblem(305)

'''
Recursion 
function that calls itself repeatedly
'''
#prints n to 1 backwards
def show(n):
    if(n == 0):#Base case
        return
    print(n)
    show(n-1)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(2))

def sum(n):
    if(n == 0):
        return
    return n + sum(n-1)

print(sum(7))

def print_list(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)

lists = ["abcd","padthe","hai","aaj"]

print_list(lists)

'''
File I/O in Python
Python can be used to perform operations on a file. (read & write data)
Types of all files
1. Text Files : .txt, .docx, .log, etc.
2. Binary Files : .mp4, .mov, .png, .jpeg, etc.
RAM - is fast in execution and Code run variables are created in RAM. RAM is a volatile memory once system is shutdown the data of RAM is lost and not stored permanently into RAM. Files form storage saving in to system's scondary storage in files form.
'''

'''
Open, read & close File
We have to open a file before reading or writing.
f = open("file_name", "mode")
file_name -> sample.txt, demo.docx
mode -> r: read mode, w: write mode, x:create a new file and open it for writing, a: open for writing/appending to the end of the file if it exists, b: binary mode, t: text mode (default), +: open a disk file for updating (reading and writing). Default is read.
Also a and w modes can be used to create the file
data = f.read()
f.close()
'''
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()#always close the files that you may have opened

'''
Reading a file
data = f.read()#reads entire file
data = f.readline()#reads one line at a time
'''
f = open("demo.txt", "r")

data = f.read(5)#specify character
print(data)

f.close()

f = open("demo.txt", "r")

data = f.read()#if read one time then the readlines are returned to be empty so reopen the file to use readlines
print(data)

line1 = f.readline()#readline
print(line1)

line2 = f.readline()
print(line2)

f.close()

'''
Write to a file
'''
f = open("demo.txt", "w")
f.write("this is a new line")#overwrites the entire file
f.close()
f=open("demo.txt", "a")
f.write("this is a new line")#adds to the file
f.close()

f = open("demo.txt", "r+")#when we want to override from the beginning
f.write("abc")
f.close()
'''
______________________________________________________
| r+ | read+  | overwrite | (ptr start) | no truncate |
|----+--------+-----------+-------------+-------------|
| w+ | write+ | overwrite | (ptr start) |    truncate |
|----+--------+-----------+-------------+-------------|
| a+ | add+   | append    |   (ptr end) | no truncate |
-----+--------+-----------+-------------+--------------
'''

# with Syntax
with open("demo.txt", "a") as f:#alias same thing different name
    data = f.read()

with open("demo.txt", "w") as f:
    f.write("new data")
    
'''
# Deleting a file - needs a module named os module
# Module (like a code library) is a file written by another programmer that generally has a functions we can use.
# Some are pre installed not all. so use python's package manager:
#  pip install tensorflow,
#  pip3 install tensorflow.
# import os
# os.remove(filename)

# import os

# os.remove("sample.txt")
'''

try:    
    with open("practice.txt","w") as f:
        f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java.")
        print("file may have been written")
except Exception as e:
    print(f"An error occured: {e}")

with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)


with open("practice.txt", "w") as f:
    f.write(new_data)

word = "learning"
def checkForWord():
    with open('practice.txt', "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

checkForWord()

def check_for_line():
    word = "learing"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1

print(check_for_line())

#given a txt file filled with numbers which are separated by commas count and print count of even numbers
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
    #individual number
    #parse/casting of string to int
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == "."):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
        
    '''Split string to list in Python
    To split any string into a list we can use'''
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

'''OOP in Python
To map with real world scenarios, we started using objects in code. This is called object oriented programming.
function make the code reusable reducing the redundant code
'''
'''
Class & Object in Python
Class is a blueprint for creating objects.
#creating class
class Student:
    name = "Gauav Kaushik"

#creating object (instance)
s1 = Student()
print(s1)
print(s1.name)
'''
class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

'''
__init__ Function 
Constructor -invoked when the object is created
All classes have a function called __init__(), which is always executed when the class is being initiated.
_____________________________________________________________________
#creating class                    |#creating object
class Student:                     |s1 = Student("Gaurav kaushik)
    def __init__(self, fullname):  |print(s1.name)
        self.name = fullname       |
---------------------------------------------------------------------

*The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

'''
class Student:
    # name = "Gaurav Kaushik"
    def __init__(self,fullname):# self is always to be called 
        # print(self)
        self.name = fullname
        print("adding new student")

s1 = Student("Gaurav")

print(s1.name)

s2 = Student("Kaushik")
print(s2.name)

'''
self keyword avoidance or indulgence
below is also a valid syntax
'''
class Student:
    # name = "Gaurav Kaushik"
    def __init__(abcd,fullname):# self is always to be called 
        # print(self)
        abcd.name = fullname
        print("adding new student")

s1 = Student("Gaurav")

print(s1.name)

s2 = Student("Kaushik")
print(s2.name)

'''
Best Practices 
use self keyword as the current object reference
'''
class Student:
    # name = "anonymous"
    # marks = 0
    #default constructors automatically created by python
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, name, marks):# self is always to be called 
        # print(self)
        self.name = name
        self.marks = marks
        print("adding new student")
        # welcome(self)
    #Method of class or objects
    def welcome(self):
        #all methods must have a self parameter for themselves whether in used or not
        #but static methods are an exception of that
        print("welcome student,", self.name)
    def get_marks(self):#getter method
        return self.marks
s1 = Student("Gaurav",100)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())

s2 = Student("Kaushik",88)
print(s2.name, s2.marks)
s2.welcome()
print(s2.get_marks)

'''
Attributes - Class And Instance Attributes
Class And Instance Attributes

Class.attr
obj.attr

student name - change per instance so
self.name

college Name -should not be stored per object and should be same so
college_name = "ABC_College"

same name class and object attribute then object attribute has a higher precedence
'''

'''
Methods - functions that belong to objects
every method of class must have a self parameter
'''
'''
Practice - Create student class that takes name & marks of 3 subjects as arguments in constructor.
 Then create a method to print the average.
'''
#First Attempt
# class Student:
#     def __init__(self, name, eng, science, math):
#         self.name = name
#         self.eng = eng
#         self.science = science
#         self.math = math
#     def print_avg(self):
#         self.avg = (self.eng + self.science + self.math)/3
#         print("the average marks obtained is : ", self.avg)

# s1 = Student("Gauav Kaushik", 100, 100, 100)
# s1.print_avg()

#Better Attempt
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("This is a static method hello without any self parameter. made using decorator @staticmethod")
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum/len(self.marks)
        print("hi ", self.name, ", your avg score is:", avg)
    

s1 = Student("Gaurav Kaushik", [88, 80, 88])#passed the parameters as a list
s1.get_avg()
s1.hello()

s1.name = "Kaushik Gaurav"
s1.get_avg()
'''
Static Methods- Methods that don't use the self parameter (work at class level)
class Student:
    @staticmethod#decorator
    def college():
        print("ABC College")

*Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifing it
'''

'''
#IMPORTANT
Pillars of OOPS in Python - Important
    Abstraction
        Hiding the implementation details of a class and only showing the essential features to the user.
    Encapsulation
        Wrapping data and functions into a single unit (object).
                                    ____
                                    |OOP|
        ___________________________________________________________________________________
        |                                 |                      |                        |
___Abstraction______________   _____Encapsulation_________   Inheritance           Polymorphism
|Hiding unnecessary Details|   |Make a capsule of         |
---------------------------    |data and related function |
                               ----------------------------
'''

'''
Practice Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.
'''
# class Account:
#     balance = 0
#     accountno = 1234
#     def debit(self, amt):
#         self.balance = self.balance + amt
#     def credit(self, amt):
#         self.balance = self.balance - amt
#     def print_balance(self):
#         print("your account balance is : ", self.balance)

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
    
acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
