li=[]
n=int(input("Enter no.of names:"))
print("Enter names:")
for i in range(0,n):
    name=input()
    li.append(name)
count=0
for i in li:
     
    count+=i.count('a')
print("Occurrences of 'a' in list: ",count)






