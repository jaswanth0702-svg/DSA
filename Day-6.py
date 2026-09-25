#Approaches
#Math Approach
'''n=int(input("Enter the Value of n: "))
area = 3.14159 * n * n
cir = 2*3.14159*n
print("Area: ",area)
print("Circumference: ",cir)'''

#Series Expression
'''import math
n=int(input("Enter the Value:"))
s=0
for i in range(1,n+1):
    s+=math.factorial(i)/(i+1)
print(s)'''

'''n = int(input("Enter a number: "))
s = 0
f = 1
for i in range(1,n+1):
    f = f*i
    s+= f/(i+1)
print(s)'''

# Naive Approach
# Max in a List
'''l = list(map(int,input().split()))
max = l[0]
for i in range(1,len(l)):
    if l[i] > max:
        max = l[i]
print(f"max number in the given list : {max}")'''

'''arr=list(map(int,input("Enter Elements: ").split()))
maximum = arr[0]
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>maximum:
            maximum=arr[j]
print(maximum)'''

#Brute Force
str1 = input().lower().replace(" ","")
str2 = input().lower().replace(" ","")
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("It is Anagram")
else:
    print("Not an Anagram")