class Publisher:
   def __init__(self,title,author):
      self.title=title
      self.author=author

   def display(self,):
      return self.title,self.author

class Book(Publisher):
   def __init__(self,title,author,price,pages):
      super().__init__(title,author)
      self.price=price
      self.no_of_pages=pages

   def display(self):
      return self.title,self.author,self.price,self.no_of_pages

t=input("Enter title:")
a=input("Enter author:")
p=int(input("Enter price:"))
pgs=int(input("Enter no.of pages:"))

details=Book(t,a,p,pgs)

print("Book details:",details.display())
