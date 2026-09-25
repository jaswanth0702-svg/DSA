#sum of digits of a given number
'''n=int(input("Enter a Number : "))
sum = 0
copy = n
while n!=0:
    digit = n%10
    sum+=digit
    n//=10
print("Sum of Digits of ", copy , "is ",sum)'''

#reverse of a given number
'''n=int(input("Enter the Number "))
reverse = 0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n//=10
print(reverse)'''

#Niven's number
'''n=int(input("Enter the number "))
s=0
c=n
while n!=0:
    d=n%10
    s+=d
    n//=10
if c%s==0:
    print("Niven's Number")
else:
    print("Not Niven's Number")'''