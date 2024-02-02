str=input("Enter string:")
occurns=dict()
words=str.split()
for i in words:
    if i in occurns:
        occurns[i]+=1
    else:
        occurns[i]=1
print("The occurrences of each word is:-\n",occurns)





