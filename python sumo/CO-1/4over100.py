li=[]
n=int(input("Enter size of list:"))
print("Enter integers:")
for i in range(0,n):
    e=int(input())
    if e>100:
        li.append('over')
    else:
        li.append(e)
print("List is:-\n",li)






