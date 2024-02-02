s=int(input("Enter start year"))
e=int(input("Enter end year"))
years=[]
for i in range(s,e+1):
    if i%400==0:
        years.append(i)
    elif i%4==0 and i%100!=0:
        years.append(i)
print("Leap years are:-\n")
print(years)
