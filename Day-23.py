#insert operation in queue
''''from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter value: "))
    q.put(value)
print(list(q.queue))'''

#insert operation in queue and delete operation
'''from queue import Queue
q=Queue()
n=int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter value: "))
    q.put(value)
print(list(q.queue))
removed = q.get()
print(list(q.queue))'''

#insert operation in queue check whether it is empty or not
from queue import Queue
q=Queue()
n=int(input("Enter the number of elements: "))
for i in range(n):
  value=int(input("Enter the value: "))
  q.put(value)
if q.empty():
  print("Queue is Empty ")
else:
  print(list(q.queue))

#insert operation in queue check whether it is full or not
from queue import Queue,Full
size=int(input("enter queue size:"))
q=Queue(maxsize=size)
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("enter value:"))
    try:
        q.put_nowait(value)
        print(value,"inserted")
    except Full:
        print("Queue is Full")
        break
    print(list(q.queue))

#insert operation in queue check whether it is empty or not
from queue import Queue
q=Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter values:"))
    q.put(value)
print(list(q.queue))
while not q.empty():
    removed=q.get()
    print(removed,"deleted")
if q.empty():
    print("Queue is Empty")
else:
    print(list(q.queue))