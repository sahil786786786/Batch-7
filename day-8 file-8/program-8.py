'''
# def profile(name, age, place):
#    txt = "My name is {}. I am {} years old. I am from {}."
#    print(txt.format(name, age, place))
# profile("Shashank", 21,"KSRM")



# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement


#  def f1(a,b):
#    c=a*b
#   return c
# print(f1(6,8))
# obj=f1(6,8)
# obj1=f1(4,6)


#  def gracemark(object):
#    print(object+4)
# gracemark(obj)
# gracemark(obj1

# 123
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n, "palindrome")
#     else:
#         print("Not palindrome")
# a = int(input("enter the value: "))
# palindrome(a)


# Positional args
# keyword args
# default args
# variable length args
#  keyword variable length args
#  Positional args

# Positional args

# Eg:-1
#? The position of parameter have to be same as position as argument

# def profile(name,phone,mark):
#    txt= "my name is {}. my phone number is{}.i got {}marks."
#    print(txt.format(name,phone,mark))
profile(1235467892,"sahil", 98) # unexpected output

# * Keyword args
# ! Eg:-1
# To overcome the disadvantage of position args,we use keywords args
# It is the process of initialising the parameters with the args while calling the
# function

def profile(name,phone,mark):
    txt= "my name is {}. my phone number is{}.i got {}marks."
    print(txt.format(name,phone,mark))
profile(1235467892,"sahil", 98) # unexpected output
profile(name="sahil",mark=98,phone=1235467892)
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

# (*>#): positive integer
# (#>*): negative integer
# (#=*): 0
    
# Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal


# ! Exception
# def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
#     if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#      txt="My name is{}. My phone number{}. I got{} marks{}."
#      print(txt.format(name,phone,place))
#     else:
#         print("You are not eligible to Signup")
# file("Shashank",9876543210)


# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)


# def profile(*name):
#     for val in name:
#         print(" My name is",val)
# profile("USman", 'Ussu', 'Alone')

# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1

def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    

# Eg:-2

d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)

# ! Class is a blue print of an object

#l1 = [1, 2, 3, 4, 5, 6]


# ? Eg:-1

class c1:
    name1 = "Asif"
    print(name1)

# ?Eg:2
class person:
    name = "Asif"


c = person() # c as object
the proccess of creation of an object is called as Instantiation
print(c.name)


# ? Eg:-3
#Create of a method
# When the function is created with a class is called as method

class person:
    def display():
        print("Hello Welcome to classes")
# ? eg:4
class person1:
    frame = "malli" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()

'''
# ? Eg:-3
#Create of a method
# When the function is created with a class is called as method
'''
class person:
    def display(person): # It is a method
        print("Hello Welcome to classes")
p = person()
p.display()
'''

#? Eg:4
# ! Method with parameter
'''
class person:
    def display(person, name, age):
        print(name, age)
p = person()
p.display("Asif",26)
'''

# ! Eg:-5
'''
class person1:
    fname = "Asif" # attribute or static variable
    lname = "T"


    def first_name(person):
        print(person.fname)

    def full_name(person):
        print(person.fname+" " +person.lname)

p = person1()
p.first_name()
p.full_name()
'''
#! Eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation
'''
class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught this process
p.__init__()
'''
#1.) Write a Python script to generate and print a dictionary that #contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n=5): # Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
#2.) Find the uncommon words from 2 strings
##s1 "Hello how are you"
#52 "Hello how is"
#3.) Wrire a code print the 8th fihanochi number



















