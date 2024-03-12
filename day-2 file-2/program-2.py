
a, b=c=7,8
print(a)
print(b)
print(c)


a=b, c = 4,2
print(a, b, c)


a = 7
b = 5
x = a
a = b
b = x

print(a,b)

a=7
b=5

a=a+b
b=a-b
a=a-b
print(a,b)

a=7
b=5
a , b=b, a
print (a,b)

a=7
b=5
a=a*b
b=a/b
a=a/b
print(a,b)

a = 7
b = 5
a=a*b
b=a/b
a=a/b
print(int(a),int(b))


a = 7
b = 45
print(id(a))
print(id(b))


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))



a = 8
b = 6
c = 9
print(a+b+c)



#n1 = input("enter the value: ")
#print(n1)

a = 4
b = 2
print(a/b)
print(a%b)


a = 8
a += 2
print(a)

a=30
a-=5
print(a)

#----> comparison---> ==, >, <, !=, <=, >=
a = 9
b = 5
print(a==b)


# ! Bitwise Operator --> &,|,^,~,<<,>>
a = 7
b = 4
print(a&b)


# a number is even or odd
n=int(input("enter the number"))
if n % 2 == 0:
    print(n , "is even")
else:
        print(n , "is odd")


name = input("enter the name: ")
age = int(input("enter the age"))
nationality=input("enter the nation: ")

if age>=18 and nationality=="Indian":
    print("eligible for vote")
else:
        print("not eligible")




















