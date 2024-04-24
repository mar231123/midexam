print("Question no 02 ")
class person:
    def __init__(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
class students(person):
    def __init__(self,name,age,ID,grade,list):
        self.grade=grade
        self.list=list
        super().__init__(name,age,ID)
    def s_display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("ID NO:",self.ID)
        print("GRADE:",self.grade)
        print("CLASSES:",self.list)
class teachers(person):
    def __init__(self,name,age,ID,subject,list):
        self.subject=subject
        self.list=list
        super().__init__(name,age,ID)
    def t_display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("ID NO:",self.ID)
        print("SUBJECT:",self.subject)
        print("CLASSES:",self.list)
class administrators(person):
    def __init__(self,name,age,ID,departments,list):
        self.departments=departments
        self.list=list
        super().__init__(name,age,ID)
    def a_display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("ID NO:",self.ID)
        print("DEPARTMENTS:",self.departments)
        print("NO OF EMPLOYEES:",self.list)

s1 = students("Maryam",21,251788947,"B+",["maths","urdu","english"])
s1.s_display()
t1 = teachers("Maham",21,25178564,"Maths", ["class8","class9","class10"])
t1.t_display()
a1 = administrators("Ali",21,2017834,"account department",["manager","accountant"])
a1.a_display()