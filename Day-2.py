#generating numbers n times and finding their sum
'''n=int(input("Enter a Number: "))
sum=0
for i in range(n):
    sum+=i
    print(i,end=' ')
    print()
print("Sum: ",sum)'''

#generating numbers n times and finding their divide by 2 and find their sum
'''n=int(input("Enter a Number: "))
sum=0
for i in range(n):
    sum+=i/2
    print(i,end=' ')
    print()
print("Sum: ",sum)'''

#print number patterns
n=int(input("Enter the Number: "))
for i in range(n):
    for j in range(n):
        print(i,j,end=' ')
    print()