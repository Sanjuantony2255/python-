c1=[]
c2=[]
n=int(input("Enter size of list 1:"))
print("Enter colors:-")
for i in range(0,n):
    c1.append(input())
    
n=int(input("Enter size of list 2:"))
print("Enter colors:-")
for i in range(0,n):
    c2.append(input())

result=set(c1).difference(set(c2))
print("Resulting set=",result)






