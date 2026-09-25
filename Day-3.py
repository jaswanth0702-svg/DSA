#hollow square 
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

# square
'''
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()'''
#daigonal and anti-diagonal
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or (i+j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#timer pattern 
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or (i+j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#butterfly
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or (i+j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#plus 
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#right angle triangle
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#left angle triangle
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n-1 or j+i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#revers
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j+i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j+i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input("Enter n: "))
for i in range((n+1)//2):
    for j in range(n):
        if i==0 or j==i or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#print a pyramid
n = int(input("enter the n:"))
for i in range(1,n+1):
  print(' '*(n-i),end=" ")
  print('*'*(2*i-1))

print()
