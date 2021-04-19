class Book:
    def __init__(self,Library_name,book_name,author,pages):
        self.L_name=Library_name
        self.b_name=book_name
        self.author=author
        self.page=pages
    def printdetails(self):
        print(self.L_name)
        print(self.b_name)
        print(self.author)
        print(self.page)
c=Book("MGU","Big data","Reema",156)
c.printdetails()