# hybried Inheritance ith student example sessional + theory
class Student:
    def __init__(self, name="", roll=0):
        self.name = name
        self.roll = roll
    def display(self):
        return self.name, self.roll
class TheoryMarks(Student):
    def __init__(self, name, roll, Physics, Chemistry, Math):
        Student.__init__(self, name, roll)
        self.p = Physics
        self.c = Chemistry
        self.m = Math
    def tcal(self):
        self.obtained = self.p + self.c + self.m
        return self.obtained
class SessionalMarks:
    def __init__(self, Physics, Chemistry, Math):
        self.p1 = Physics
        self.c1 = Chemistry
        self.m1 = Math
    def scal(self):
        self.obtained = self.p1 + self.c1 + self.m1
        return self.obtained
class Result(TheoryMarks, SessionalMarks):
    def __init__(self, name="", roll=0, p1=0, c1=0, m1=0, p2=0, c2=0, m2=0, total=0):
        TheoryMarks.__init__(self, name, roll, p1, c1, m1)
        SessionalMarks.__init__(self, p2, c2, m2)
    def final(self):
        #print(SessionalMarks.scal(self), TheoryMarks.tcal(self))
        self.obtainen = SessionalMarks.scal(self)+TheoryMarks.tcal(self)
        return (self.obtainen, (self.obtainen/300)*100)
name = input("Enter Name: ")
Roll = int(input("Roll No. "))
tp = int(input("Enter Physics Theory Marks: "))
tc = int(input("Enter Chemistry Theory Marks: "))
tm = int(input("Enter Math Theory Marks: "))
pp = int(input("Enter Physics Practical Marks: "))
pc = int(input("Enter Chemistry Practical Marks: "))
pm = int(input("Enter Math Practical Marks: "))
tota = int(input("Enter Total Marks: "))
r1  = Result(name, Roll, tp, tc, tm, pp, pc, pm, tota)
stuList = []
stuList.append(r1)
print(stuList)
r1.display()
print("Theory Marks Obtained:", r1.tcal())  
print("Sessional Marks Obtained:", r1.scal())
print("Final Total and Percentage:", r1.final())
print("Student Result:")
print("Name \t Roll No \t Theory Marks \t Sessional Marks \t Total Marks \t Percentage")
print("{} \t {} \t {} \t\t {} \t\t {} \t\t {:.2f}%".format(r1.name, r1.roll, r1.tcal(), r1.scal(), r1.final()[0], r1.final()[1]))
    