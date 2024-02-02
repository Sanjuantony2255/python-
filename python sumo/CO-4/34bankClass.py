class Bank:
   def __init__(self,acno,name,actype,bal):
      self.acno=acno
      self.name=name
      self.actype=actype
      self.bal=bal
      
   def deposit(self,amt):    
      self.bal+=amt
      print("Done! Balance:",self.bal)
   def withdraw(self,amt):
      if self.bal<amt:
         return print("Insufficient balance")
         
      self.bal-=amt
      print("Done! Balance:",self.bal)


num=int(input("Enter account no.:"))
name=input("Enter holder name:")
typ=input("Enter account type:")
bal=int(input("Enter initial balance:"))
acc=Bank(num,name,typ,bal)

while(True):
   ch=int(input("Enter choice(1.Deposit,2.Withdraw,3.ViewBalance,4.Exit):"))
   if ch==1:
      amt=int(input("Enter deposit amount:"))
      acc.deposit(amt)
   elif ch==2:
      amt=int(input("Enter withdraw amount:"))
      acc.withdraw(amt)
   elif ch==3:
      print("Balance=",acc.bal)
   elif ch==4:
      print("Exiting..")
      break
   else:
      print("Invalid choice.")
