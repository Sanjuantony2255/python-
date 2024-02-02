li=[]
sum=0
n=int(input("Enter size of list:"))
print("Enter items:-")
for i in range(0,n):
    li.append(int(input()))
print("List=",li)

for i in li:
    sum+=i
print("Sum of list items= ",sum)






