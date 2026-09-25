#Bubble Sort
'''arr=list(map(int,input("Enter the number (space-separated): ").split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array: ",*arr)'''

#selection sort
'''arr=list(map(int,input("Enter Elements: ").split()))
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)'''
