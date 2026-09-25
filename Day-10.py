#Types Of Searches
#Linear Search
#Binary Search
#Jump Search

#Binary Search
'''n=int(input("Enter Number of Elements : "))
arr=[]
print("Elements in Sorted Order : ")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter element to search: "))
left=0
right=n-1
found=-1
while left <= right:
    mid = (left+right)//2
    if arr[mid]== target:
        found=mid
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
if found != -1:
    print("Value Found at index", found)
else:
    print("Value Not Found")'''

#Binary Search(For Animals)
'''n=int(input("Enter Number of Elements : "))
arr=[]
print("Elements in Sorted Order : ")
for i in range(n):
    arr.append(input())
target=input("Enter element to search: ")
left=0
right=n-1
found=-1
while left <= right:
    mid = (left+right)//2
    if arr[mid]== target:
        found=mid
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
if found != -1:
    print("Value Found at index", found)
else:
    print("Value Not Found")'''

