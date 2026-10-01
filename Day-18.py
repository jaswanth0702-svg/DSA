#Double linked list
'''class node:
    def __init__(self,data):
        self.data=data 
        self.prev=None
        self.next=None
head=None
n=int(input("Enter Number of node: "))
for i in range(n):
    data=int(input("Enter the value: "))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print("Doubly Linked List: ")
temp=head
while temp is None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")'''

'''class node:
    def __init__(self,data):
        self.data=data 
        self.prev=None
        self.next=None
head=None
n=int(input("Enter Number of node: "))
for i in range(n):
    data=int(input("Enter the value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Doubly Linked List: ")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")'''

class node:
    def __init__(self,data):
        self.data=data 
        self.prev=None
        self.next=None
head=None
n=int(input("Enter Number of node: "))
for i in range(n):
    data=int(input("Enter the value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Doubly Linked List: ")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
if head is None:
    print("DDL is empty....")
else:
    head=head.next
    if head is not None:
        head.prev=None
print("Doubly Linked List: ")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")