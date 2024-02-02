li1=[]
li2=[]
n=int(input("Enter size of list:"))
print("Enter integers:-")
for i in range(0,n):
    e=int(input())
    li1.append(e)
for i in li1:
    if i>=0:
        li2.append(i)
print("List of positive integers:",li2)

