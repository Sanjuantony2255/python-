string=input("Enter string:")
if string[-3:]=="ing":
   string=string+'ly'
else:
   string=string+'ing'

print("New string:"+ string)
