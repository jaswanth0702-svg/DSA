#Time Complexity and Space Complexity
# 1. Constant T.c - O(1)
# 2. Linear T.c - O(n)
# 3. Quadratic T.c - O(n^2)
# 4. Logarithmic T.c - O(log n)
# 5. Exponential T.c - O(2^n)

#Constant Time Complexity
'''n=int(input("Enter a Number: "))
print("Number: ",n)'''

#Linear Time Complexity
'''n=int(input("Enter a Number: "))
for i in range(n):
    print(i,end=' ')'''

#Quadratic time complexity
'''n = int(input("Enter a Number: "))
for i in range(n):
    for j in range(n):
        print(i,j,end=" ")
    print()

n = int(input("Enter a Number: "))
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k,end=" ")
        print()
    print()'''

'''n = int(input("Enter thwe Number: "))
for i in range(n):
    for j in range(n):
        print("😂",end = ' ')
    for k in range(n):
        print("😘",end = " ")
    print()'''

'''n = int(input("Enter the Number: "))
for j in range(n):
    print("😂",end = ' ')
for k in range(n):
    print("😘",end = " ")
print()'''

# Logarithmic Time Complexity - O(log n)
'''n=int(input("Enter N : "))
while n>1:
    print(n)
    n//=2'''

'''import math
n=int(input("Enter N: "))
while n>2:
    print(n)
    n=math.sqrt(n)'''