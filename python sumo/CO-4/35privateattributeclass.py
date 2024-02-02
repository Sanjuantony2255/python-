class Rectangle:
   def __init__(self,length,width):
      self.__length=length
      self.__width=width
      
   def area(self):    
      return self.__length * self.__width

   def __lt__(self,other):
      return self.area()<other.area()

l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter width of rectangle1:"))
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter width of rectangle2:"))

rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)

a1=rect1.area()
a2=rect2.area()
print("Area of rectangle1:",a1)
print("Area of rectangle2:",a2)

if rect1<rect2:
   print("Rectangle2 is larger.")
else:
   print("Rectangle1 is larger.")
