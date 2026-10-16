#web browser history using stacks and files
'''stack=[]
while True:
    print("\n1.visit website")
    print("2.Back")
    print("3.Forward")
    choice=int(input("enter your choice: "))
    if choice==1:
        website=input("enter website:")
        stack.append(website)
        with open("history.txt","a") as file:
            file.write(website+"\n")
        print("visited:",website)
    elif choice==2:
        if len(stack)==0:
            print("No previous pages.....")
        else:
            stack.pop()
            if len(stack)==0:
                print("No previous pages.....")
            else:
                print("back to",stack[-1])
    elif choice==3:
        print("Browser History")
        if len(stack)==0:
            print("History empty...")
        else:
            for website in stack:
                print(website)
    elif choice==4:
        print("Exit")
    else:
        print("Invalid input....")'''

#check whether the expression is balanced or not
expression=input("Enter The Expression: ")
stack=[]
for ch in expression:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not Balanced")

#balanced the unbalanced
expression=input("Enter The Expression: ")
stack=[]
result=''
for ch in expression:
    if ch == '(':
        stack.append(ch)
        result+=ch
    elif ch == ')':
        if len(stack)>0:
            stack.pop()
            result+=ch
        else:
            result="("+result+ch
    else:
        result+=ch
while len(stack)>0:
    result+=')'
    stack.pop()
print("Balanced expression: ",result)

#
expression=input("Enter The Expression: ")
stack=[]
result=''
for ch in expression:
    if ch == '(':
        stack.append(ch)
        result+=ch
    elif ch == ')':
        if len(stack)>0:
            stack.pop()
            result+=ch
    else:
        result+=ch
while len(stack)>0:
    temp=''
    count=0
    for ch in result:
        if ch == '(' and count<len(stack):
            count+=1
        else:
            temp+=ch
    result=temp
print(result)