#Merge Sort
'''arr=list(map(int,input("Enter values: ").split()))
def merge(arr,left,mid,right):
    i=left
    j=mid+1
    temp=[]
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<= right:
        temp.append(arr[j])
        j+=1
    for i in range(len(temp)):
        arr[left+i]=temp[i]
def mergesort(arr,left,right):
    if left<right:
        mid=(left+right)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)
mergesort(arr,0,len(arr)-1)
print(arr)'''

#insertion sort
arr=list(map(int,input("Enter Values: ").split()))
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)