class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages

b1=Book(100) # b1 is Book type object like n=int(10) here n is int type
b2=Book(200)
print(b1+b2)

# 2. Here __add__(self,other) overloaded when we use '+' operator and it will return and integer value ,here we use 3rd
# object b3  so we use tostring method __str__(self) to convert Book object to string again for addition
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return str(self.pages)

b1 = Book(100)  # b1 is Book type object like n=int(10) here n is int type
b2 = Book(200)
b3 = Book(300)
b4= Book(150)
print(b1 + b2+b3+b4)


# other operator overloading methods
# def __sub__(self,other):
#     return "overloading subtraction"
# def __mul__(self,other):
#     return "overloading multiplication"
# def __truediv__(self,other):
#     return "overloading true division"