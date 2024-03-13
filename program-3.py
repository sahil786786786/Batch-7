# ! Eg:-3
# ? take values of length and breadth of a
# ? from user and check if it is square or not.
length =int(input("enter the length= "))
breadth=int(input("enter the breadth= "))
if (length==breadth):
    print("it is a square")
else:
    print("it is not a sqaure")
# ! Eg:-4
# python program to check whether the
# given integer is a multiple of both 5 and 7
n=int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
# ! Eg:-5
# ? Accept the age of 4 people and display the oldest one.
a=int(input("enter the age of the person: "))
b=int(input("enter the age of the person: "))
c=int(input("enter the age of the person: "))
d=int(input("enter the age of the person: "))
if (a>b and a>c and a>d):
    print("A is greater")
elif(b>a and b>c and b>d):
    print("B is greater")
elif(c>a and c>b and c>d):
    print("C is greater")
elif(c>a and c>b and c>d):
    print("C is greater")
elif(d>a and d>b and d>c):
    print("D is greater")

    

# Eg-6
price=int(input("Enter the price: "))
total = 0
if price>=1000000:
    discount = price*(6/100)
    value = price-discount
    tax = value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is: ",total)


# Eg:-7
# a school has following rules for grading system:
# 1.) below 25-F
# 2.) 25 to 45-E
# 3.) 45 to 50-D
# 4.) 50 to 60-C
# 5.) 60 to 80-B
# 6.) above 80-A
# ask user to enter marks and print the corresponding grade.


marks=int(input("enter the marks"))
if (marks>=80):
    print("A")
elif (marks<=80 and marks>=60):
    print("B")
elif (marks<=60 and marks>=50):
    print("C")
elif (marks<=50 and marks>=45):
    print("D")
elif (marks<=45 and marks>=25):
    print("E")
elif (marks>=25):
    print("F,FAil")



# ! --->short hand if else
# Eg:-1
a =int(input("enter the age"))
b =int(input("enter the age"))
if a>b:
    print("A")
else:
    print("B")

#? ---> using short hand if else
# * Rules
# 1.)statement inside the if condition have to be present at first
# 2.)elif cannot be used in short hand if else
# 3.)always it have to end with else

#print("A")if a>b else print("B")

# ! code to check the given char is vowel or consonent

char = input("Enter the char:  ")
'''
if char=="a" or char =="e" or char =="i" or char =="o" or char=="u":
    print("is a vowel")
else:
    print("is a consonent")
'''
# ? or

str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

# shorthand if else
char = input("enter the char; ")
str1 ="aeiouAEIOU"
print("vowels") if char in str1 else print("consonent:")
        
# Find greatest among 3 variables using short
a = 8
b = 5
c = 9

#print("A is greater") if a>b and a>c else print ("B is greater")
# if b>a and b>c else print(" c is greater")




# ! -------> looping

# for loop
# while loop


# ! ----> for loop
# ? for loop is used for iteartion, if we know the number of times the loop have to run
# ? it is used to iterate the iterables eg(string, list, tuple,etc...)


# todo---> syntax for loop


# ! for syntax in c
#for(1=0;i<10;i++){
#   printf("hello");
#}

# ! for syntax in python
#for userdefined_variable in range(start, end,step):default step value is 1
# statement
# statement
# statement



# ? Eg:-1
# to print the value from 1 to 10 using for loop

for i in range(0, 10):
    print(i)
    print("hello")





# Eg:-2:-
for val in range(23, 50, 1):
    print(val)

for val in range(1, 15, 2):
    print(val)

for val in range(1, 15, 3):
    print(val)



# ! print the output of 7th multiplication table from 21 to 43
for i in range(1, 10+1,):
    print('7','X',i,'=',i*7)





#----> Method-2
ans="7 x {} = {}"
print(ans.format(i, i*7))

          
  
