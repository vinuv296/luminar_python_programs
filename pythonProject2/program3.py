age=int(input("Enter your age"))
gender=input("Enter your gender")

if(gender == 'F'):
    print("Employed in urban area")
elif(gender=='M' & age>20<40):
    print("Work any where")
elif(gender=="M" & age>40<60):
    print("Work any where in urban areas")
else:
    print("ERROR")