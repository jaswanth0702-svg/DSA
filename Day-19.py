#circular linked list traversal 
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("Enter The Elements: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
start=int(input("Enter the starting node value : "))
current=head
while current.data != start:
    current=current.next
    if current ==head:
        print("Value not found . ")
        exit()
temp=current
print("Traversal : ")
while True:
    print(temp.data, end=' ')
    temp=temp.next
    if temp==current:
        break'''

#circular linked list traversal by position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("Enter The Elements: ").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
pos=int(input("Enter poistion : "))
current=head
for i in range(pos-1):
    current=current.next
print("Traversal : ")
temp=current
while True:
    print(temp.data, end=' ')
    temp=temp.next
    if temp==current:
        break'''

#
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("enter elements:").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
x=int(input("enter value to be deleted:"))
current=head
previous=tail
while True:
    if current.data==x:
        if current==current.next:
            head=None
        elif current==head:
            head=head.next
            tail.next=head
        else:
            previous.next=current.next
        break
    previous=current
    current=current.next
    if current==head:
        print("value not found")
        break
print("Traversal : ")
if head is None:
    print("CLL Empty ")
else:
    print("After Deletion ")
    current=head
    while True:
        print(current.data,end=' ')
        current=current.next
        if current==head:
            break