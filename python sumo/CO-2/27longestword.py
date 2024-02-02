li=[]
n=int(input("Enter size of list:"))
print("Enter words:-")
for i in range(0,n):
    li.append(input())
print("List of words is:",li)
li= sorted(li, key = len)

print("Longest word is",li[-1],",with length=",len(li[-1]))



