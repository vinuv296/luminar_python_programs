class student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
st1=student(123,"rajeev","BSc",300)
st2=student(145,"manu","MA",400)
st3=student(156,"jeeva","BA",420)

#print(st1)
students=[]
students.append(st1)
students.append(st2)
students.append(st3)
student_total=max(list(map(lambda stud:stud.total,students)))
print(student_total)