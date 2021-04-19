salary=int(input("Enter your salary"))
year=int(input("Enter your year of service"))
if(year>5):
    bonus=salary*5/100
    print("Your Net Bonus - ",bonus)
else:
    print("Your year of service is less than 5 years")
