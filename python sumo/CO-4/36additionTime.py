class Time:
   def __init__(self,hour,mins,sec):
      self.hour=hour
      self.mins=mins
      self.sec=sec

   def __add__(self,other):
      h=self.hour+other.hour
      m=self.mins+other.mins
      s=self.sec+other.sec
      if m>59:
         m-=60
         h+=1
      if s>59:
         s-=60
         m+=1
      return h,m,s

h1=int(input("Enter time1-hour:"))
m1=int(input("minutes:"))
s1=int(input("seconds:"))
h2=int(input("Enter time2-hour:"))
m2=int(input("minutes:"))
s2=int(input("seconds:"))

t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)

print("Sum of both time:",t1+t2)
