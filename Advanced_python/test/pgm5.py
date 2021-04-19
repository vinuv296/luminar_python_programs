# Method overloading

class Book:

    def Details(self,name,year_publ):
        self.name=name
        self.yr=year_publ
        print("name-",self.name)
        print("year-",self.yr)
    def Author(self):
        print("Author Name- Gokul")
class Over_Book(Book):

    def Author(self):
        print("Author name- Vinu")
c=Over_Book()
c.Details("ABC",2011)
c.Author()




