#count the occurences inf an array
'''arr = input("Enter Fruits: ").split()
key = input("Enter a fruit: ")
count=0
for i in range(len(arr)):
    if arr[i]==key:
        count+=1
print(count)'''

#Write a code to reverse a string without using slicing
'''s = input("Enter a string: ")
rev =""
count=0
for i in s:
    rev=i+rev
print(rev)'''

#write a code to find the occuarences of character
'''s = input("Enter the string: ")
char = input("Enter a Character: ")
c=0
for i in s:
    if i == char:
        c+=1
print(c)'''

#write a code to find the largest word
arr = input("Enter Animals: ").split()
largest = arr[0]
for word in arr:
    if len(word)>len(largest):
        largest=word
print("Largest: ",largest)