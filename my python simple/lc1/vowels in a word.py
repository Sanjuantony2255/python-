word=input("Enter a word:")
print("vowels in a word:")
for char in word:
    if char.lower() in "aeiou":
        print(char)
