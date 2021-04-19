m1=float(input("Enter mark1"))
m2=float(input("Enter mark2"))
m3=float(input("Enter mark3"))
m4=float(input("Enter mark4"))
per=int(((m1+m2+m3+m4)/200)*100)
if(per>=90):
    print("percentage - ",per,"Grade A+")
elif(per>=80):
    print("Grade A")
elif (per >=70 & per <= 79):
    print("Grade B+")
elif(per>=60 & per<=69):
    print("Grade B")
elif(per>=50 & per<=59):
    print("Grade C+")
elif(per>=40 & per<=49):
    print("Grade C")
elif(per>=30 & per<=39):
    print("Grade D")
else:
    print("Failed")