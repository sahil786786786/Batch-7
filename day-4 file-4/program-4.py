#---->while loop
#---->break using while loop


#Eg:-1
'''
# 1.) iterate from 20 to 30 and break the loop in 27


i = 20
while i<31:
    if i == 27:
        break
    print(i)
    i+=1

# 2.)
i = 20
while i<31:
    print(i)
    i+=1
    if i == 27:
        break
    print(i)
    i+=1

# 3.)
i = 20
while i<31:
    print(i)
    if i == 27:
        break
    i+=1

# 4.)
i = 20
while i<31:
    if i == 27:
       print(i)
       break
    i+=1

# ! ---->continue


# 1.)
i = 20
while i<31:
    print(i)
    i+=1
    if i == 27:
       continue 
    print(i)
    i+=1


# 2.)
i = 20
while i<31:
    i+=1
    if i == 27:
       continue 
    print(i)

# ! Eg:5
# while to literate from 12 to 22
# find the sum of all numbers

# 1.)
i = 12
sum = 0
while i<23:
    sum = sum + i
    i+=1
print(sum)


# ! Eg:-6
# find the average of value from 20 to 25

i = 20
sum = 0
avg = 0
count = 0
while i<26:
    sum = sum+i
    count+=1
    i+=1
avg=(sum/count)
print(avg)

# ! ----->Nested for loop
# Eg:-1

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


rows=int(input("enter the rows: "))
col=int(input("enter the col: "))

for rows in range(rows):
    for col in range(col):
        print("*", end=" ")
    print()


for row in range(5):
    for col in range(5):
        print(row, end = " ")
    print()


for row in range(0,6):
    for col in range(0, rows):
        print(row, end = " ")
    print()

for row in range(6, 0, -1):
    for col in range(0, row):
        print("*", end = " ")
    print()
 

# * * * * *
# *       *
# *       *
# *       *
# *       *
# * * * * *

for row in range(5):
    for col in range(5):
        if col == 0 or col == 5-1 or row == 0 or row == 5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#      *     
#    * * *   
#  * * * * *


for row in range(0, 5):
    for col in range(0, 6):
        if ((row == 0 and col == 3) or (row == 1 and (col>=2 and col<= 4) or (row == 2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# * 
# * *
# *   *
# *     *
# *       *
# * * * * * *
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# ----> List
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary

# ----------> List

# 1.) if the collection of elements are sarounded by sqaure brackets, it is considered to be list


# eg:-1
# lst1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9,0]]


# charactristics of list
# 1.)list have to be sarounded[]
# 2.)it is muutable(the element inside list are changable)
# 3.)Every element inside list is indexed
# 4.)the elements inside list will be ordered format
# 5.)it can hold duplicate values
# 6.)its heterogenous


# to access the elements in list
lst1 = [1, 4, 1, 7, 89.7, 7, 5, "p","l"]
#print(lst1)


# ---->Indexing
#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with pre-defined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side

# ? -->Positive indexing
print(lst1[0])
print(lst1[4])
print(lst1[20])

# ---->Negative indexing
lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
print(lst1[-1])
print(lst1[-5])

# ? ----> slicing
lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
# lst1[start_index:end_index:step]
print(lst1[0:4])
print()
# lst1[start_index:end_index:step]
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

print(lst1[0:7:1])#lst1[0:7] --->both are same
print(lst1[0:7:2])


trail = int(input())



lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
print(lst1[-1:-4])
print(lst1[-4:-1])
print(lst1[-7:-1])
print(lst1[-7:-1:2])


'''
#! To insert ot add element inside list
#append()-> used to add elelement at last position of list
l1=[9, 8, 0, 6]
l1.append("car")
print(11)






