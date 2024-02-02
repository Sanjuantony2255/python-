class Rectangle:
   def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
      
   def area(self):    
      return self.length * self.breadth
   def perimeter(self):
      return 2*(self.length+self.breadth)
   

l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter breadth of rectangle1:"))
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter breadth of rectangle2:"))

rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)

a1=rect1.area()
a2=rect2.area()
print("Area of rectangle1:",a1)
print("Area of rectangle2:",a2)
print("Perimeter of rectangle1:",rect1.perimeter())
print("Perimeter of rectangle2:",rect2.perimeter())

if a1>a2:
   print("Rectangle1 is larger.")
if a1<a2:
   print("Rectangle2 is larger.")
if a1==a2:
   print("Both have same area.")
