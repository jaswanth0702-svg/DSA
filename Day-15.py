#Linked List
#1. Single LL
#2. Double LL DoublyLL
#3. Circular LL

#Single LL Operations
#1. Insert at end
#2. Insert at begin
#3. Delete at end
#4. Delete at begin
#5. Insert at pos
#6. Delete at pos

#SLL insert at end
'''class node:
    def __init__(self,data):
        self.data= data
        self.next= None
head= None
tail= None
values= list(map(int,input("Enter values: ").split()))
for value in values:
    newnode= node(value)
    if head is None:
        head= newnode
        tail= newnode
    else:
        tail.next= newnode
        tail= newnode
current= head
while current is not None:
    print(current.data, end='->')
    current= current.next
print("Tail")'''

#SLL insert at begin
'''class node:
    def __init__(self,data):
        self.data= data
        self.next= None
head= None
tail= None
values= list(map(int,input("Enter values: ").split()))
for value in values:
    newnode= node(value)
    newnode.next=head
    head= newnode
current= head
while current is not None:
    print(current.data, end='->')
    current= current.next
print("Tail")'''

#SSL Delete at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values =list(map(int,input("Enter elements:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
print("SLL Before Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')
if head is None:
    print("SLL is Empty...")
elif head.next is None:
    head=None
else:
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None 
print("SLL After Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')'''

#SLL delete at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values =list(map(int,input("Enter elements:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
print("SLL Before Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')
if head is None:
    print("SLL is Empty...")
else:
    head=head.next
print("SLL After Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')