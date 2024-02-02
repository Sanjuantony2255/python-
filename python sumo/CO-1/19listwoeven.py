li=[]
n=int(input("Enter size of list:"))
print("Enter integers:-")
for i in range(0,n):
    li.append(int(input()))
print("List=",li)

for i in li:
    if i%2==0:
        li.remove(i)
print("New list= ",li)






