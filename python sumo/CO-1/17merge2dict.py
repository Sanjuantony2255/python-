d1={}
d2={}

n=int(input("Enter size of dict 1:"))
for i in range(n):
    k=input("Enter key:")
    v=input("Enter value:")
    d1[k]=v
    
n=int(input("Enter size of dict 2:"))
for i in range(n):
    k=input("Enter key:")
    v=input("Enter value:")
    d2[k]=v

merge=d1|d2
print("Merged dict=",merge)






