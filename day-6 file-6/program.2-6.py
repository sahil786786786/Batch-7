#Day-->6


#---->Set

# ? Characteristics of Set
'''
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable
'''
# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 3
# min(), max(), len()

# * Eg: 4
# ? to add element inside set

#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
#s1.update([9, 0])
#print(s1)


# ? To delete element inside set
#s1 = {8, 78, 67, 'u'}


# pop() # ---> To delete one element randomly
#s1.pop()
#print(s1)

#  ---> remove()
#s1.remove(78)
#print(s1)

# discard()
#s1.discard(8967)
#print(s1)


# clear()
#l1 = {}
#print(type(l1)) #---> datatype is dict

#s1 = set() # to create empty set
#print(type(s1))


#s1 = {8, 9, 0}
#s1.clear()
#print(s1)


#del(s1)
#print(s1)



# * Join the sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", 't', 56}
# union() ---> to combine 2 sets
#s3 = s1.union(s2)
#print(s3)


# intersection()  ---> get common elements inside set
#s1 = { 4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.intersection(s2))

# * difference()
# s1 = { 4, 5, 6}
# print(s1.difference(s2))
# print(s1.difference(s1))
# print(s1.symmetric_difference(s2))

# isdisjoint(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}
#print(s1.issubset(s2))
#print(s1.issuperset(s1))

#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}
#for val in s1:
#   if val in s2:
#       str1 = "Its joint set"
# print(str1)


# intersection() ---> to get common elements inside set
# s1 = {4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
# print(s1.intersection(s2))

# n1 = {1,2,3} --> s1

#for val in s1:
#   if val in s2:
#        str1 = "its joint set"
# print(str)


# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered


# ? dictionary based functions
# to add element(key and value pair) in dict
# d1={1:100,2:200,3:300,4:400}
# d1[5]=500
# print(d1)

#? to replace a value in dictionary
# d1={1:100,2:200,3:300,4:400}
# d1[2]="mango"
# print(d1)

# ? delete element from dictionary
# d1 = {1:100, 2:200, 3:300,4:400}
# pop item()
# d1.popitem()
# print(d1)


#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {"a":"apple","b":"boy","g":"Game"}
# d1.update(d2)
# print(d1)


# get()
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[3])
# print(d1.get(90))


#to print the all the keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
# print(d1.values())

# Iterating dictionary
# for val in d1:
#    print(val)

#for val in d1.value():
#    print(val)

# to get both keys and values
# for key, val in d1.items():
#    print(key, val)


# ! problem:1

n=int(input("Enter of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter of times:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}





