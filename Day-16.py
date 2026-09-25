#insert a value at a position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
values=list(map(int,input("Enter Value: ").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
value=int(input("Enter value to insert: "))
pos=int(input("Enter the position,where value has to be inserted: "))
newnode=node(value)
if pos==1:
    newnode.next=head
    head=newnode
else:
    current=head
    for i in range(pos-2):
        current=current.next
    newnode.next=current.next
    current.next=newnode
current=head
while current is not None:
    print(current.data, end="->")
    current=current.next
print("Tail")'''

'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
values=list(map(int,input("enter a 'values:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
pos=int(input("enter the position to delete"))
newnode=node(value)
if head is None:
    print("SLL Empty....")
elif pos==1:
    head=head.next
else:
    current=head
    for i in range(pos-2):
        current=current.next
    current.next=current.next.next
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')'''

#delete a value
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
values = list(map(int, input("Enter values: ").split()))
for value in values:
    new_node = Node(value)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
value = int(input("Enter the value to delete: "))
if head is None:
    print("SLL Empty.....")
elif head.data == value:
    head = head.next
else:
    current = head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            break
        current = current.next
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("Tail")