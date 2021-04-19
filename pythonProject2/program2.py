total_class=int(input("Enter the total number of classes"))
attended_class=int(input("Enter the total number of attended classes"))
per=attended_class/total_class*100
print("Your attendance percentage -",per,"%")
if(per>75):
    print("You are allowed to attend the exam")
else:
    print("You are  Not allowed to attend the exam")
