dict={}
n=int(input("Enter size of dict:"))
for i in range(n):
    k=input("Enter key:")
    v=input("Enter value:")
    dict[k]=v
print("Sorted dict in ascending order=",sorted(dict.items()))
print("Sorted dict in descending order=",sorted(dict.items(),reverse=True))






