row=int(input("Enter step number(no.of rows):"))
print("Enter items:-")
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("\n")
