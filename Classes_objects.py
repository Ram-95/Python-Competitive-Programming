#Classes and Objects Employee details

class Employee:
    incr = 1.05
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first + '' + last + '@company.com'
        Employee.no_of_emps += 1 

    def display_details(self):
        print('First Name: {}\nLast Name: {}\nPay: {}\nEmail: {}'.format(self.fname, self.lname, self.pay, self.email))
        print('==================================================')

    def apply_incr(self):
        self.pay = int(self.pay * self.incr)


#Creating Objects

emp1 = Employee('Ram','babu',50000)
emp2 = Employee('Jack','jones',14200)
emp3 = Employee('Tim', 'Cook', 58000)

emp1.display_details()      #this and also the below one does the same
Employee.display_details(emp2)

#printing the employee data
#print(Employee.no_of_emps)

    

