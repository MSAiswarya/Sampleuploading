class employee:
    def __init__(self,ename,ecode,ebs):
          self.emp_name=ename
          self.emp_basic=ebs
    def calculate(self):
          if self.emp_basic<10000:
               self.emp_da=self.emp_basic*0.2
               self.emp_hra=self.emp_basic*0.25
               self.emp_da=self.emp_basic*0.05
          else:
               self.emp_da=self.emp_basic*0.1
               self.emp_hra=self.emp_basic*0.15
               self.emp_da=self.emp_basic*0.03
          self.emp_ns=self.emp_basic+self.emp_da+self.emp_hra-self.emp_pf
    def display(self):
         print("Name :",self.emp_name)
         print("Empcode :",self.emp_code)
         print("Basic salary :",self.emp_code)
         print("DA :",self.emp_da)
         print("HRA:",self.emp_hra)
         print("PF :",self.emp_pf)
         print("Net salary :",self.emp_ns)
class teacher(employee):
    def __init__(self,enm,ecd,ebs,dept):
         employee.__init__(self,enm,ecd,ebs)
         self.department=dept
         self.student=[]
    def mark_attendance(self,n):
         self.count=n
         print("enter the attendace roll no wise (p-present/a-absent)")
         for i in range(0,n):
              att=input()
              self.student.append(att)
    def display_attendance(self):
         c=0
         print("Count of present students")
         for i in range(0,self.count):
              if self.student[i].lower()=='p':
                   c=c+1
         print(c)
    def display(self): 
         print("Name :",self.emp_name)
         print("Empcode :",self.emp_code)
         print("Basic salary :",self.emp_code)
         print("DA :",self.emp_da)
         print("HRA:",self.emp_hra)
         print("PF :",self.emp_pf)
         print("Net salary :",self.emp_ns)
    teacher_list=[]
    m=int(input("enter the name of teacher"))
    for i in range(0,m):
         name=int(input("enter the name of teacher:"))
         c=input("enter the code of teacher")
         bs=int(input("enter the basic salary of teacher"))
         no=int(input("enter the number of students :"))
         tchr=tchr(name,c,bs)
         tchr.mark_attendance(no)
         tchr.calculate()
         teacher_list.append(tchr)
    for i in range(0,m):
         print(".....")
         teacher_list[i].display()
         teacher_list[i].display_attendance()
    print(teacher_list)   
    