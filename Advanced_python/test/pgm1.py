class Vechicle:
    def __init__(self,type,model):
        self.type_name=type
        self.model_name=model
    def print_details(self):
        print("Type name-",self.type_name)
        print("Model name-",self.model_name)
class Car(Vechicle):
    def __init__(self,company_name,model_no,type,model):
        super().__init__(type,model)
        self.c_name=company_name
        self.model_n=model_no
    def printvals(self):
            print("Type-",self.type_name)
            print("Model name",self.model_name)
            print("Company name-", self.c_name)
            print("Model_no", self.model_n)
ob = Car("Maruti","HashBack","C1546","Swift")
ob.print_details()
ob.printvals()
