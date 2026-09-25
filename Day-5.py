#Direct Recursion
'''def number(n):
    if n == 0:
        print("Done")
        return
    print(n,end=' ')
    number(n-1)
n = int(input("Enter a value: "))
number(n)'''

#InDirect Recursion
'''def even(n):
    if n == 0:
        print(copy,"Is Even")
        return
    odd(n-1)
def odd(n):
    if n == 0:
        print(copy,"Is Odd")
        return
    even(n-1)
n=int(input("Enter a Value: "))
copy = n
even(n)'''

#Tree recurssion
'''def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter a Number: "))
for i in range(n):
    print(fib(i),end=" ")'''

'''def tree(n):
    if n <= 0:
        return 
    print(n,end=" ")
    tree(n-1)
    tree(n-1)
n=int(input("Enter a Number: "))
tree(n)'''

'''def tree(n):
    if n <= -1:
        return 
    print(n,end=" ")
    tree(n-1)
    tree(n-1)
n=int(input("Enter a Number: "))
tree(n)'''

#head recursion
def head(n):
    if n==0:
        return
    print(n,end=" ")
    head(n-1)
n=int(input("Enter A Value: "))
head(n)

def head(n):
    if n==0:
        return
    head(n-1)
    print(n,end=" ")
n=int(input("Enter A Value: "))
head(n)