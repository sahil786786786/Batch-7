'''
n = int(input("enter the number of inputs: "))
for i in range(0,n):
    a,b = list(map(int,input().split()))
    print(a,b)


# ! ---->common functions for list


lst1 = [6, 7, 8, 9, 0]
print(len(lst1))


print(max(lst1))
print(min(lst1))


lst1 = [6, 8, 9,"p", "u"]
print(max(lst1)) #----> error occurs becaues it is a combination of int and string
print(min(lst1)) #----> error occurs becaues it is a combination of int and string



lst1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
print(min(lst1))

lst1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#index()
print(lst1.index(9))

lst1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#count()
print(lst1.count(6))


# ! some function which is specifically used for list


# To add element inside list
# ? insert(index_value,element)---> to add element at specific index postion
lst1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
lst1.insert(2,"cars")
print(lst1)

# ? To delete element from list
lst1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
#pop()
lst1.pop()
print(lst1)

# pop(index_value) ---> used to delete element at specific inde
lst1.pop(4) #--->4 is index value
print(lst1)


# *remove(element) ---> used to delete element directly
lst1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# remove()
lst1.remove(8.89)
print(lst1)
  
# * clear() --> to complete delete all element in list
lst1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# clear()
lst1.clear()
print(lst1)

# del -> to delete the list
# del l1 # or del(l1)
# print(l1)

# ? join 2  lists

lst1 = [9, 0, 8]
lst2 = ["p", "0", "t", 34]
print(lst1+lst2)


# ! or


# * extend() ---> to combine 2 lists
lst1.extend(lst2)
print(lst1)

# ? ---> copy()
lst1 = [6, 7, 8,9, 3]
lst2 = lst1.copy()
print(lst2)
print(lst1)

print(id(lst1))
print(id(lst2))

# ! diff between shallow copy and deep copy
# shallow copy
import copy
lst1 = [8,9,0,[5,6],[3,2,1]]
lst2 = copy.copy(lst1)
lst1.append(890)
print(lst1)
print(lst2)



# * deep copy --> used to copy the list with nested list
# * --> deep copy
import copy
lst1 = [8,9,0,[5,6],[3,2,1]]
print(lst1[-1][1])#---> to index nested list

lst2 = copy.deepcopy(lst1)
lst1[-1].append('cars')
print(lst1)
print(lst2)


# ? sort ---> arrange elements in list in ascending or descending order
lst1 = [9, 7, 45, 0,-6, 5, 12]
lst1.sort() # to arrange in ascending order
print(lst1)

lst1.sort(reverse=True) # to sort in ascending order
print(lst1)

lst1 = ['z','i', 'o', 'p', 9]
lst1.sort()
print(lst1) # ---> error

#list constructor
list() #--> to conver other collection datatype to list
lst3 = ((8, 9, 0))
print(list(lst3))

lst4 = (8, 9)
print(list(lst4))

# ! ---> nested list
lst1 = [8, 9, [0, 8, 7],['p', 'o', 'y'],[8,'t']]
print(lst1[-2]) # ---> o

print(lst1[1:4])
print(lst1[1:-1])

# ? to delete "t" from l1

lst1[-1].remove('t')
print(lst1)

# combine these ['p', 'o', 'y'],[8, 't'] list in l1 to ['p', 'o','y', 8, 't']
lst1[-2].extend(lst1[-1])
lst1.pop(-1)
print(lst1)

# ! -----> Tuple
# * char of tuple

# 1.)Tuple have to be surrounded by()
# 2.) The elements inside tuple are not changable
# 3.) The elements inside tuple are indexed
# 4.) The element will execute in order
# 5.) It is hetrogenous
# 6.) It allow duplicate elements

# eg:
t1 = (8, 8, 9, 6, 5.78, [9,0],(6, 8), "hey", 9+6j)
print(t1)
print(type(t1))
# ? indexing, slicing are all same as list

# ? ways to create tuple
lst1 = (8)
print(type(lst1)) # int

lst1 = (8,)
print(type(lst1)) # tuple

t1 = 8,9
print(type(t1))  # tuple

t1 = 8,
print(type(t1))  # tuple
 
# len(), min(), max(), index(), count() ---> all same as list

# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples

t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)


# To add all element inside list and tuple
# sum()
lst1 = (8, 9, 7, 6)
print(sum(lst1))

# * sort tuple
t1 = (8, 9,0, 89, 12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# Iterate based on Elements

lst1 = [9, 8, 0, 6, 5]
for i in lst1:
    print(i)

# * Iterate based on Index value
lst1 = [9, 8, 0, 6, 5]
for i in range(0,5):
    print(i)


lst1 = [9, 8, 0, 6, 5]
print(lst1[2])

# ! ---> Strings

s1 = 'o'
print(type(s1))


s1 ="u"
print(type(s1))


s1 = "hello world"
# * To access string
print(s1)


# Indexing and slicing --> same as list and tuple
# print(s1[0:5])

# --> len(), min(),max(), index(),count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord() ---> used to find the ASCII value of character
s1 = 'u'
print(ord(s1))


# Functions of string
s1 = "hello world"


# ? to convert all character to upper case
print(s1.upper())


#?
#? to convert to lower case
s1 = "HFREDiou"
print(s1.lower())


# ? strip() ---> to eliminate the space in beginning and end of string

s1 = " where are you?"
print(s1.lstrip())
print(s1.lstrip())
print(s1.strip())




# Split() --->
s1 = " where are you ?"
print(s1.split())
print(s1.split("r"))

s1 = " where are you ?"
print(s1.count('e'))


# * replace() ---> to replace a specific char in the string
s1 = "Where are you?"
print(s1.replace('r', '&&'))

# Swapcase () ---> to convert
s1 = "HEY there "
print(s1.swapcase())


# * title() --> to write the string in format of title
s1 = 'never giveup'
print(s1.title())


# * capitalize() --> 1st character of string will be converted to capital
s1 = 'never giveup'
print(s1.capitalize())


# * Join the strings
s1 = " hello"
s2 = 'world'
print(s1+s2)



s1 = how are you
i am fine
hey there



# splitlines() --> used to split the string based on lines
print(s1.splitline())

# * find() --> to find the index based o

s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))



# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswitch('1'))
print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1[::-1])


# ---->Eg:-1:
# wap to find the number of lower case letters
s1 = "HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters: ",count)
'''

s1 = Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop p

characters =len(s1)
#print(characters)
'''
words = s1.split(" ")
print(words)


words = s1.split(" ")
print(len(words))

'''
#sentences = s1.split('.')
#print(len(sentences))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))










































































































