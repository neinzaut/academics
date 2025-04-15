#class 1
class Manager:
    def __init__(self, name, department, post="Manager"):
        self.name = name
        self.department = department
        self.post = post

    def post_detail(self):
        self.house_rent = 10000
        self.transport = 5000

        if self.department == "HR":
            self.basic_salary = 30000
        else:
            self.basic_salary = 25000
        print(f"The post of", self.name, " is ", self.post)

    def salary(self):

        totalsalary = self.basic_salary + self.house_rent + self.transport
        return totalsalary

#class 2
class Clerk:
    def __init__(self, name, post="Clerk"):
        self.name = name
        self.post = post

    def post_detail(self):
        self.basic_salary = 10000
        self.transport = 2000
        print(f"The post of ", self.name, " is ", self.post)

    def salary(self):

        totalsalary = self.basic_salary + self.transport

        return totalsalary

mr = Manager("Juan", "HR")
mr1 = Manager("Maria", "Accounting")
ck = Clerk("Pedro")


workers = [mr, mr1, ck]

#iterates output
for wrk in workers:
    wrk.post_detail()
    print("The salary is", wrk.salary())
    print()
