'''
Created on 24. mai 2019

@author: Taavi Kase
Code in LiClipse
Tutorial from:
https://www.learnpython.org/en/
'''

''' here starts first lesson '''
print("hello world")

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    

''' here starts second lesson '''
print
print("second lesson")
print #printing empty line here
numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
for n in numbers:
    print(n)

for s in strings:
    print(s)

print("The second name on the names list is %s" % second_name)

print
print("third")
print 

x = 2
y = 5

x_list = ([x] * 10)
y_list = ([y] * 10)
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

for n in big_list:
    print(n)

print
print("4")
print 

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % (data[0], data[1], data[2]))

print
print("5")
print 

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

print
print("6")
print

number = 16
second_number = 0
first_array = [1, 4]
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")
    
second_array = [5, 6]
if len(second_array) == 2:
    print("3")

second_array = [1,2,3]

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")


if not second_number:
    print("6")

print
print("6")
print

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105,
    942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
    626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
    843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857,
    440, 380, 126, 721, 328, 753, 470, 743, 527
]

# your code goes here

for number in numbers:
    if number == 237:
        break
        
    if (number % 2) == 0: # check if number is even
        print(number)
else: # in here it doesn't work, since we have break in for loop, but with continue or no keyword, it will print at the end of for loop
    print("end of sequence")
    
print("done with this lesson")

print
print("7")
print

# Modify this function to return a list of strings as defined above
def list_benefits():
    # One thing worth mentioning is how to return more than one variable here
    s1 = "More organized code"
    s2 = "More readable code"
    s3 = "Easier code reuse"
    s4 = "Allowing programmers to share and connect code together"
    
    return s1, s2, s3, s4

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    # Note here how strings are built
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

print
print("8 classes and functions come hereafter")
print

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.kind = "convertible"
car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.kind = "van"
car2.name = "Jump"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

print
print("9 Dictionaries")
print

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
#del phonebook["Jill"] # dictionary item can be deleted this way as well
phonebook.pop("Jill")
phonebook["Jake"] = 938273443

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

print
print("10 Modules & Packages")
print


import re

# Your code goes here
find_members = []
members = []
for member in dir(re):
    members.append(member)
    
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
print(sorted(members))

print
print("11 Numpy Arrays")
print

#Normal way of calculating stuff
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)
weight_lbs = []

# Create np_weight_lbs from np_weight_kg
for weight_kg in np_weight_kg:
    weight_p = weight_kg * 2.2
    weight_lbs.append(weight_p)

np_weight_lbs = np.array(weight_lbs)
# Print out np_weight_lbs
print(np_weight_lbs)

#Nicer way of doing the same thing:
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)

print
print("12 Pandas Basics")
print

'''
Here we have a problem with importing pandas

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
'''
print("pandas end here")

print
print("13 Generators")
print

def fib():
    a, b = 1, 1
    
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

print
print("14 List Comprehensions")
print

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [num for num in numbers if num > 0]

#This is the original solution, but here double is converted to int
cor_newlist = [int(num) for num in numbers if num > 0]
print(newlist)
print(cor_newlist)

print
print("15 Multiple Function Arguments")
print

# edit the functions prototype and implementation
def foo(a, b, c, *args):
    # Here we count the amount of extra arguments
    return len(args)

def bar(a, b, c, **kwargs):
    # Here we check if magic number is 7
    return kwargs["magicnumber"] == 7

# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

print
print("15 Multiple Function Arguments")
print

