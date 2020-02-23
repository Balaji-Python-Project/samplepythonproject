class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def get_details(self):
        print('Employee Name:{} {} and pay is {}'.format(self.first,self.last,self.pay))
class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
class Manager(Employee):
    def __init__(self,first,last,pay,emp=None):
        super().__init__(first,last,pay)
        if emp is not None:
            self.emp=emp
        else:
            self.emp=[]
    def __str__(self):
        return self.first
    def get_employees(self):
        for emp in self.emp:
            emp.get_details()
    def add_employee(self,emp):
        if emp not in self.emp:
            self.emp.append(emp)
    def delete_employee(self,emp):
        if emp in self.emp:
            self.emp.remove(emp)
e=Employee('Balaji','Putta',600000)
e2=Employee('A','R',600000)
e3=Employee('B','R',600000)
e4=Employee('C','R',600000)
e5=Employee('D','R',600000)
m=Manager('Balaji','Putta',900000,[e,e2])
m.add_employee(e3)
m.add_employee(e4)
m.add_employee(e5)
print('manager===>',m)
m.get_employees()
