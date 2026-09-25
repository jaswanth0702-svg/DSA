#find a square root of a number using binary
'''n=int(input("Enter a number: "))
low=0
high=n
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print("Square root ",ans)'''

#find a first occurance of a number using binary search evaluation
'''arr=list(map(int,input("Enter Numbers ").split()))
target=int(input("Enter a number : ")) 
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
        high=mid-1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
print("First occurance: ",ans)'''

#find a last occurance of a number using binary search evaluation
'''arr=list(map(int,input("Enter Numbers ").split()))
target=int(input("Enter a number : "))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
        low=mid+1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
print("First occurance: ",ans)'''
