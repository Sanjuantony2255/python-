string=input("Enter string:")
freq ={} 
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Character frequency is:\n "+ str(freq))
