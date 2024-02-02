li1=[]
li2=[]
li3=[]
n1=int(input("Enter size of list 1:"))
print("Enter elements:-")
for i in range(0,n1):
    li1.append(int(input()))
n2=int(input("Enter size of list 1:"))
print("Enter elements:-")
for i in range(0,n2):
    li2.append(int(input()))

if len(li1)==len(li2):
    print("Lists are of same length.")
if sum(li1)==sum(li2):
    print("List sums are of same value.")
for i in li1:
    if i in li2:
        li3.append(i)

print("values occuring in both r: ",li3)






