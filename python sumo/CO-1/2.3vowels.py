li=[]
vowels=['a','e','i','o','u']
w=input("Enter word:");
for i in w:
    if i in vowels and i not in li:
        li.append(i)
print("Vowels in the given word are:",li)

