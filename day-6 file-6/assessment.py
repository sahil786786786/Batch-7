# 1.) Python program to capitalize the first and last character of each
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


# 1.) program
'''
s1 = input("enter string: ")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

'''
# 2.) program
'''
n = 128
for i in n:
    print(i)


n = 128
while n!=0:
    rem = n%10
    print(rem)
    n = n/10

n = 128
for i in str(n):
    print(i)

n = 128
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp % rem
    if check!= 0:
        f1 = 1
    n = n//10

if f1==0:
    print("yes")
else:
    print("no")

# 3.)program
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

# Add corresponding elements of l1 and l2
ans = [l1[i] + l2[i] for i in range(len(l1))]

print("ans =", ans)
'''
# ! -----> set
# characteristics of set
#1.) set can be created using{}
#2.) The element inside set are not indexed
#3.) Does not allow duplicate values
#4.) it unordered
#5.) heterogenous
#6.) mutable or changable

# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)



