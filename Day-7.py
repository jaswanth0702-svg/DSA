#Linear Data Structures
#1. Arrays
#2. Create and Display
#3. Insert
#4. Delete 
#5. Appened
#6. Remove

#create and print a array
'''arr = list(map(int,input("Enter Elements: ").split()))
print(*arr)'''

#Access an Element with index value
'''arr = list(map(int,input("Enter Elements: ").split()))
index = int(input("Enter your index value: "))
print("Element: ",arr[index]+55)
print(*arr)'''

#Create and insert an element print an array
'''arr = list(map(int,input("Enter Elements : ").split()))
print(arr)
index = int(input("Enter your index value : "))
value = int(input("Enter the value to be placed at index :"))
arr.insert(index, value)
print(arr)'''

#Create and insert an element at index and last - print an array
'''arr= list(map(int, input("Enter elements : ").split()))
print(arr)
index = int(input("Enter your index value : "))
value = int(input("Enter the value to be placed at index :"))
arr.insert(index, value)
print(arr)
arr.append(value)
print(arr)'''

#Create and delete an element at index and last - print an array
'''arr= list(map(int, input("Enter elements : ").split()))
print(*arr)
index = int(input("Enter your index value : "))
value = int(input("Enter the value to be DELETED :"))
arr.remove(value)
print(*arr)
index= int(input("Enter index"))
arr.pop(index)
print(*arr)'''

#Search an element and return index value
'''arr= list(map(int,input("Enter Elements : ").split()))
print(*arr)
value= int(input("Enter the Value to be searched: "))
found= False
for i in range(len(arr)):
    if arr[i]==value:
        found= True
        print(value,"found at index: ",i)
        break
    if found==False:
        print("Element not in array..............!")'''

#Minimum value
'''arr=list(map(int,input("Enter Elements: ").split()))
minimum = arr[0]
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]<minimum:
            minimum=arr[j]
print(minimum)'''

#without using Sort methods u have to sort
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(*a)