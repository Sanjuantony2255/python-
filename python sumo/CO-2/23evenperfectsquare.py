a=int(input("Enter start value:"))
b=int(input("Enter end value:"))
for i in range(a,b+1):
    for j in range(32,100):
        if j*j==i:
            li=str(i)
            if int(li[0])%2==int(li[1])%2==int(li[2])%2==int(li[3])%2==0:
                print(i)
        


