# %%
"""
### Final Exam Code Template ###
__This template will guide you to complete the final exam. Grading rubrics are also provided.__

__Please follow the guidelines closely when you type in your own code and test your program.__

__Before working on your own code, save the template as "Final_firstname_lastname" so you don't change the original file and can refer to the template when necessary.__

__The number of arguments mentioned below doesn't count "self".__
"""

# %%
#define your own Vehicle class here
#the order of the four required positional arguments should be: make,model,year,mileage
#please use the conventional way to define function names and refer to the following test to adjust function names 
#no need to handle exceptions here

class Vehicle:
    def __init__(self,make,model,year,mileage):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_mileage(self):
        return self.__mileage
    def set_make(self,make):
        self.__make = make
    def set_model(self,model):
        self.__model = model
    def set_year(self,year):
        self.__year = year
    def set_mileage(self,mileage):
        self.__mileage = mileage
        
    def __str__(self):
        vehicleInput = "Make: {0}; Model: {1}; Year of Manufacture: {2}; Mileage: {3} ".format(self.get_make(),self.get_model(),self.get_year(),self.get_mileage())
        return vehicleInput
    

# %%
#do a quick test on the Vehicle class before moving forward (5 points)
#don't change this code
vehicle1=Vehicle("Honda","Civic",2014,50000)
print(vehicle1)
print("The mileage of this vehicle is:", vehicle1.get_mileage())
vehicle1.set_year(2012)
print("The year of manufacture of this vehicle is:", vehicle1.get_year())

# %%
#define your own Employee class here
#the order of the three required positional arguments should be: name,address,vehicle object
#please use the conventional way to define function names and refer to the following test to adjust function names
#use emp for short of employee in naming attributes and functions
#no need to handle exceptions here

class Employee:
    def __init__(self,emp_name,emp_address,vehicle):
        self.__emp_name = emp_name
        self.__emp_addr = emp_address
        self.__vehicle = vehicle
        
    def get_emp_name(self):
        return self.__emp_name
    def get_emp_addr(self):
        return self.__emp_addr
    def get_vehicle(self):
        return self.__vehicle
    def set_emp_name(self,emp_name):
        self.__emp_name = emp_name
    def set_emp_addr(self,emp_address):
        self.__emp_addr = emp_address
    def set_vehicle(self,vehicle):
        self.__vehicle = vehicle
        
    def __str__(self):
        empInput = "Employee Name: {0}; Employee Address: {1}; \n{2}".format(self.get_emp_name(),self.get_emp_addr(),self.__vehicle)
        return empInput
  

# %%
#do a quick test on the Employee class before moving forward (5 points)
#don't change this code
emp1=Employee("Amy", "100 W Campbell Road, Richardson, Texas, 75080",vehicle1)
print(emp1)
print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))
print("{0} owns a {1} {2} vehicle.".format(emp1.get_emp_name(),emp1.get_vehicle().get_make(),emp1.get_vehicle().get_model()))
emp1.set_emp_addr("800 E Campbell Road, Richardson, Texas, 75080")
print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))

# %%
#define your own Full Time Employee class here
#Full Time Employee class inherits from Employee class
#the order of the four required positional arguments should be: name,address,vehicle object,salary
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class FullTimeEmployee(Employee):
    def __init__(self,emp_name,emp_addr,vehicle1,emp_salary):
        Employee.__init__(self,emp_name,emp_addr,vehicle1)
        self.__salary = float(emp_salary)
    
   
    def get_salary(self):
        return self.__salary
  
    def set_salary(self,salary):
        self.__salary = float(salary)
    
    def compute_compensation(self):
        if self.__salary>55000:
            self.compensation=((0.18*25000)+(0.28*30000)+(0.33*(self.__salary-55000)))
        elif self.__salary>25000 and self.__salary<=55000:
            self.compensation=(0.18*25000)+(0.28*(self.__salary-25000))
        else:
            self.compensation=0.18*self.__salary
        
        return ((self.__salary - self.compensation)/52)
   # Tax calculation based on salary ranges
        if self.__salary <= 25000:
            tax = 0.18
            self.compensation = self.__salary * (1 - tax)
        elif 25000 < self.__salary <= 55000:
            self.compensation = (25000 * 0.82) + ((self.__salary - 25000) * 0.72)
        else:
            self.compensation = (25000 * 0.82) + (30000 * 0.72) + ((self.__salary - 55000) * 0.67)
        
        # Convert annual compensation to weekly
        return self.compensation / 52
    
    def compute_reimbursement(self,annual_expense):
        if(annual_expense<=10000):
            return (annual_expense/52)
        elif(annual_expense>10000):
                annual_expense = 10000 + 0.5*(annual_expense-10000)
                return (annual_expense/52)     
    
    def __str__(self):
        festr = "Details of this Full Time Employee are: \n"
        festr += super().__str__()
        festr += "\nSalary:{0}".format(format(self.__salary,'.2f'))
        return festr
    

# %%
#do a quick test on the Full Time Employee class before moving forward (5 points)
#don't change this code
emp2=FullTimeEmployee("Amy", "100 W Campbell Road, Richardson, Texas, 75080", vehicle1, 40000)
print(emp2)
print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_reimbursement(12000)))
emp2.set_salary(50000)
print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))


# %%
#define your own Hourly Employee class here
#Hourly Employee class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,hourly rate
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class HourlyEmployee(Employee):
    def  __init__(self,emp_name,emp_addr,vehicle,hoursWorked,hourlyRate):
        Employee.__init__(self,emp_name,emp_addr,vehicle)
        self.__hours_wrkd = int(hoursWorked)
        self.__hourly_rate = float(hourlyRate)
        self.compensation=0
        
    def set_hours_worked(self,hw):
        self.__hours_wrkd = int(hw)
        
    def set_hourly_rate(self,hr):
        self.__hourly_rate = float(hr)
        
    def get_hours_worked(self):
        return self.__hours_wrkd
    
    def get_hourly_rate(self):
        return self.__hourly_rate
    
    def compute_compensation(self):
        if self.__hours_wrkd > 40:
            # Regular pay for the first 40 hours plus 1.8 times the hourly rate for overtime
            regular_pay = 40 * self.__hourly_rate
            overtime_pay = (self.__hours_wrkd - 40) * self.__hourly_rate * 1.8
            weekly_compensation = regular_pay + overtime_pay
        else:
            # Regular pay for all hours worked if 40 or less
            weekly_compensation = self.__hours_wrkd * self.__hourly_rate
        
        return weekly_compensation
    
    def compute_reimbursement(self,weekly_expense):
        # Reimbursement is limited to $100 per week
        if weekly_expense > 100:
            return 100
        else:
            return weekly_expense
    def __str__(self):
        hestr = "Details of this Hourly Employee are: \n"
        hestr += super().__str__()
        hestr+= "\nHours Worked: {0}; Hourly Rate: {1}".format(self.__hours_wrkd,int(self.__hourly_rate))
        return hestr

# %%
#do a quick test on the Hourly Employee class before moving forward (5 points)
#don't change this code
emp3=HourlyEmployee("Grace", "400 W Campbell Road, Richardson, Texas, 75080", vehicle1,50,20)
print(emp3)
print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_reimbursement(120)))
emp3.set_hourly_rate(22)
print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))


# %%
#define your own Consultant class here
#Consultant class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here



class Consultant(Employee):
    def __init__(self, emp_name, emp_address, vehicle, hours_worked, project_type):
        super().__init__(emp_name, emp_address, vehicle)
        self.__hours_worked = hours_worked
        self.__project_type = project_type

    def get_hours_worked(self):
        return self.__hours_worked

    def get_project_type(self):
        return self.__project_type

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def set_project_type(self, project_type):
        self.__project_type = project_type

    def compute_compensation(self):
        hourly_rates = {1: 55.00, 2: 70.00, 3: 85.00}
        if self.__project_type in hourly_rates:
            hourly_rate = hourly_rates[self.__project_type]
            return self.__hours_worked * hourly_rate
        return 0  # Default case if project type is not defined

    def compute_reimbursement(self, weekly_expense):
        reimbursement_rates = {1: 1.0, 2: 0.9, 3: 0.8}
        if self.__project_type in reimbursement_rates:
            return weekly_expense * reimbursement_rates[self.__project_type]
        return 0  # Default case if project type is not defined

    def __str__(self):
        return "Details of the consultant are" + super().__str__() + f"; Hours Worked: {self.get_hours_worked()}; Project Type: {self.get_project_type()}"



# %%
#do a quick test on the Consultant class before moving forward (5 points)
#don't change this code
emp4=Consultant("Michael", "700 W Campbell Road, Richardson, Texas, 75080",vehicle1,40,2)
print(emp4)
print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_reimbursement(300)))
emp4.set_hours_worked(35)
print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))


# %%
#define your own Management class here
#Management class inherits from both Full Time Employee class and Consultant class
#the order of the six required positional arguments should be: name, address,vehicle object, salary, hours worked, project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class Management(FullTimeEmployee,Consultant):
    def __init__(self,emp_name,emp_address,vehicle1,emp_salary,hoursworked,projecttype):
        FullTimeEmployee.__init__(self,emp_name,emp_address,vehicle1,emp_salary)
        Consultant.__init__(self,emp_name,emp_address,vehicle1,hoursworked,projecttype)

       
    def compute_reimbursement(self,annual,weekly):
        a=FullTimeEmployee.compute_reimbursement(self,annual)
        b=Consultant.compute_reimbursement(self,weekly)
        return a+b
    def compute_compensation(self):
        a=FullTimeEmployee.compute_compensation(self)
        b=Consultant.compute_compensation(self)
        return a+b
    def __str__(self):
        mgmtstr = "Details of this Management are: \n"
        mgmtstr+= "Employee Name: {0}; Employee Address: {1}; \n{2} \n".format(FullTimeEmployee.get_emp_name(self),FullTimeEmployee.get_emp_addr(self),FullTimeEmployee.get_vehicle(self)) 
        mgmtstr+= "Salary: {0}; Hours Worked: {1}; Project Type{2}".format(FullTimeEmployee.get_salary(self),Consultant.get_hours_worked(self),Consultant.get_project_type(self))
        return mgmtstr    

# %%
#do a quick test on the Management class before moving forward (5 points)
#don't change this code
emp5=Management("Jane", "1000 W Campbell Road, Richardson, Texas, 75080",vehicle1,120000,10,3)
print(emp5)
print("\n")
print("{0} has an annual salary of ${1}.".format(emp5.get_emp_name(),emp5.get_salary()))
print("{0} works {1} hours per week for type {2} project.".format(emp5.get_emp_name(),emp5.get_hours_worked(),emp5.get_project_type()))
print("{0} has a weekly compensation of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_compensation()))
print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_reimbursement(8000,300)))


# %%
#complete this get_emp_input() function to prepare for the main menu application
#this function is used to ask for basic employee information and then return them: name and address
#this function doesn't take arguement(s)
#no need to handle exceptions here
def get_emp_input():
    name = input("Enter the employee's name: ")
    address = input("Enter the employee's address: ")
    return (name,address)

# %%
#do a quick test on the get_emp_input() function before moving forward
#don't change this code and please use the sample input
#sample input: Bob; 350 E Campbell Road, Richardson, Texas, 75080
name, address=get_emp_input()
print("{0} lives at {1}.".format(name,address))

# %%
#complete this get_vehicle_input() function to prepare for the main menu application
#this function is used to ask for vehicle information and then return them: make,model,year,mileage
#this function doesn't take arguement(s)
#no need to handle exceptions of make input and model input
#handle exceptions to make sure year is a 4-digit positive number between 1900 and 2024
#handle exceptions to make sure mileage is a positive number
def get_vehicle_input():
    make = input('Enter the vehicle make: ')
    model = input('Enter the vehicle model: ')
# Input validation for the year
    while True:
        try:
            year = int(input("Enter the vehicle year (1900-2024): "))
            if year < 1900 or year > 2024:
                raise ValueError("Year must be between 1900 and 2024.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        else:
            break

    # Input validation for the mileage
    while True:
        try:
            mileage = int(input("Enter vehicle mileage: "))
            if mileage < 0:
                raise ValueError("Mileage must be a positive number.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        else:
            break

    return make, model, year, mileage

# %%
#do a quick test on the get_vehicle_input() function before moving forward (5 points)
#don't change this code and please use the sample input
#sample input:Ford; Ranger; 2025 (when asked to enter again enter 2015); 80000
vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()  
print("The vehicle entered is a {0} {1} made in {2} with {3} mileage curently.".format(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage))

# %%
#complete this get_full_time_input() function to prepare for the main menu application
#this function is used to ask for specific information of full time employees and then return it: annual salary
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_full_time_input():
    salary = int(input("Enter the annual salary:"))
    return salary

# %%
#do a quick test on the get_full_time_input() function before moving forward
#don't change this code and please use the sample input
#sample input:80000
salary=get_full_time_input()
print("The annual salary entered is {0:0.2f}".format(salary))

# %%
#complete this get_hourly_input() function to prepare for the main menu application
#this function is used to ask for specific information of hourly employees and then return them: hours worked, hourly rate
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_hourly_input():
    hours_worked = int(input("Enter the hours worked:"))
    hourly_rate = int(input("Enter the hourly rate:"))
    return (hours_worked,hourly_rate)

# %%
#do a quick test on the get_hourly_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 30; 20
hours_worked, hourly_rate = get_hourly_input()
print("This hourly employee works {0} hours per week at an hourly rate of ${1:0.2f}".format(hours_worked,hourly_rate))

# %%
#complete this get_consultant_input() function to prepare for the main menu application
#this function is used to ask for specific information of consultants and then return them: hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_consultant_input():
    hours_worked = int(input("Enter the hours worked:"))
    project_type = int(input("Project Type? (Enter a number between 1 and 3):"))
    return (hours_worked,project_type)

# %%
#do a quick test on the get_consultant_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 40; 2

hours_worked, project_type = get_consultant_input()
print("This consultant works {0} hours per week for type {1} project.".format(hours_worked,project_type))

# %%
#complete this get_management_input() function to prepare for the main menu application
#this function is used to ask for specific information of managements and then return them: annual salary, hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_management_input():
    annual_salary = int(input("Enter the annual salary:"))
    hours_worked = int(input("Enter the hours worked:"))
    project_type = int(input("Project Type? (Enter a number between 1 and 3):"))
    return (annual_salary,hours_worked,project_type)

# %%
#do a quick test on the get_management_input() function before moving forward
#don't change this code and please use the sample input
#sample input: 100000; 8; 3
salary, hours_worked, project_type = get_management_input()
print("This management has an annual salary of ${0:0.2f}. This management also works {1} hours per week additionally for type {2} project.".format(salary, hours_worked,project_type))

# %%
#complete this read_file_data() function to prepare for the main menu application
#this function is used to read information from an existing databse/binary file, which is empdata.dat in the final exam
#this function doesn't take argument(s)
#this function returns a list containing all employee objects stored in the database; each employ object is an element in the list; the list will also be used and updated later
#need to handle exceptions if file doesn't exist

import pickle

def read_file_data():
    employee_list = []
    try:
        with open('empdata.dat', 'rb') as file:
            while True:  
                try:
                    employee = pickle.load(file)
                    employee_list.append(employee)
                except EOFError:
                    print("End of file is reached.")
                    break  
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    
    return employee_list

# %%
#do a quick test on the read_file_data() function before moving forward (5 points)
#don't change this code
emp_list=read_file_data()
print("There are {} employees stored in the database.".format(len(emp_list)))
print("\nBelow is the information of the first employee in the database: {}".format(emp_list[0]))
print("\n{} is the first employee.".format(emp_list[0].get_emp_name()))

# %%
#complete option 1 related code here
#the idea is to walk through users to input required information
#the first and foremost step is to ask for emloyee type
#this function doesn't take arguement(s)
#this function prints the entered object and also returns the entered object
#some parts are provided so you don't need to change them (but you still can if you want to)

def run_option1():
    #ask for employee type
    #exceptions need to be handled here to accept valid input 
    sel = input("Type of Employee?\n1-Full Time\n2-Hourly\n3-Consultant\n4-Management\n")
    while((sel not in ("1","2","3","4"))):
              print("Please select an option from 1, 2, 3, and 4.")
              sel = input("Type of Employee?\n1-Full Time\n2-Hourly\n3-Consultant\n4-Management\n")
    sel = int(sel)        
    
    #call the previous get_emp_input() to ask for employee information and store the values      
    name, address = get_emp_input()
    
    #call the previous get_vehicle_input() to ask for vehicle information and store the values
    vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()    
    
    #create an object of Vehicle class using the prervious information
    a_vehicle = Vehicle(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage)
    
    #depending on previous input, call the prervious functions to ask for corresponding information
    #then use all the required information to create an object of a certain class 
    #type 1:annual salary
    #type 2:hours worked,hourly rate
    #type 3:hours worked, project type
    #type 4:annual salary, hours worked, project type
    if sel == 1:
        sal = get_full_time_input()
        an_emp = FullTimeEmployee(name, address, a_vehicle,sal)
    elif sel == 2:
        hw, hr = get_hourly_input()
        an_emp = HourlyEmployee(name, address, a_vehicle, hw, hr)
    elif sel == 3:
        hw, pt = get_consultant_input()
        an_emp = Consultant(name, address, a_vehicle, hw, pt)
    elif sel ==4:
        sal, hw, pt = get_management_input()
        an_emp = Management(name, address, a_vehicle, sal, hw, pt)
    
    print(an_emp)
    
    print("\n============================================================")        
    print("New employee entered successfully! Now going to the main menu.")
    print("==============================================================")     
    return an_emp    


# %%
#do a quick test on the run_option1() function before moving forward (5 points)
#don't change this code and please use the example input
#example input: 5 (then zzz then 4); David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3;2018;5000;110000;5;2
run_option1()

# %%
#complete option 2 related code here
#the function is to print centain number of employees as required by users
#first choice:print all employees; second choice: print first 5 employees when there are at least 5 employees (print all if fewer than 5)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#needs to handle exceptions when taking user seletions
def run_option2(my_lst):
    # Check if the list is empty first to provide a clear message if no data is available
    if not my_lst:
        print("There are no employees stored in the database.")
        return
    
    print("Choose an option:")
    print("1: Print all employees")
    print("2: Print the first 5 employees")
    while True:  # Continue looping until a valid input is received
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                raise ValueError("Please select either 1 or 2.")
            break  # Exit the loop
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Process based on user choice
    if choice == 1:
        # Print all employees
        for emp in my_lst:
            print(f'{emp} \n')
    elif choice == 2:
        # Print the first 5 employees, or fewer if less than 5 exist
        for emp in my_lst[:5]:  
            print(f'{emp} \n')    

# %%
#do a quick test on run_option2() function before moving forward (5 points)
#don't change this code and please use the sample input
#sample input: 3 (then zzz then 2)
run_option2(emp_list)

# %%
#complete option 3 related code here
#the function is used to print compensations of all Employees
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions
def run_option3(my_lst):
    print("\nEmployee name and Compensation of all Employees")
    print("=================================================")
    for a in my_lst:
        print("{0}'s weekly compensation is ${1:0.2f}.".format(a.get_emp_name(),a.compute_compensation()))
    
    #type in your code

# %%
#do a quick test on run_option3() function before moving forward (5 points)
#don't change this code and please use the sample input
run_option3(emp_list)

# %%
#complete option 4 related code here
#the function is used to search for an employee by name and the searching is NOT case sensitive
#if there are some matching cases, print the information of all matched employees
#if no matchng cases, print "There is no employee matching the name you entered."
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function also returns a list of objects of the matched employees
#no need to handle exceptions
def run_option4(my_lst):
    
    #type in your code       

# %%
#do a quick test on run_option4() function before moving forward (5 points)
#don't change this code and please use the example input (all upper cases)
#example input: TOM
#part 1
matched_emp_list=run_option4(emp_list)
print("\nThere are {} employees matching your search.".format(len(matched_emp_list)))

# %%
#do a quick test on run_option4() function before moving forward 
#don't change this code and please use the example input
#example input: Hongchang
#part 2
run_option4(emp_list)

# %%
#complete option 5 related code here
#the function is used to show some basic statistics. They are: 
#(1) the number of employees stored in the database
#(2) the highest weekly compensation
#(3) the mean weekly compensation
#(4) the number of employees who have a vehicle with over 100,000 mileage
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

def run_option5(my_lst):
    
    #type in your code

# %%
#do a quick test on run_option5() function before moving forward (5 points)
#don't change this code 
run_option5(emp_list)

# %%
#complete option 6 related code here
#the function is used to compute weekly reimbursement (assuming the user has the requirerd information)
#the first step is to ask for the name of the employee (you can call run_option4() here)
#the second step is to select one employee from the matched employees
#the third step is to ask for required information 
#this function doesn't return anything
#no need to handle exceptions
def run_option6(emp_list):
    matched_list=run_option4(emp_list)
    choice=int(input("Which employee do you want to check (enter a number)?"))
    emp=matched_list[choice-1]
    
    #type in your code

# %%
#do a quick test on run_option6() function before moving forward (5 points)
#don't change this code and please use the example input (all lower cases)
#example input: bob;1;8000
#part 1

run_option6(emp_list)

# %%
#do a quick test on run_option6() function before moving forward 
#don't change this code and please use the sample input (all lower cases)
#sample input: james;1;130
#part 2

run_option6(emp_list)

# %%
#complete option 7 related code here
#the function is used to store changes into a new file/database (i.e. empdata_updated.dat) and exit the program
#the first step is to double check with the user if he/she does want to exit (not case sensitive)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

import sys

def run_option7(my_lst):
    
    #type in your code

# %%
#do a quick test on run_option7() function before moving forward (5 points)
#don't change this code and please use the example input
#example input: b
#part 1
run_option7(emp_list)

# %%
#do a quick test on run_option7() function before moving forward 
#don't change this code and please use the example input
#example input: n
#part 2
run_option7(emp_list)

# %%
#do a quick test on run_option7() function before moving forward 
#don't change this code and please use the example input
#example input: y
#part 3
run_option7(emp_list)

# %%
#complete the main application
#the application menu provides 7 options
#when user selects a valid option (except for 7), execute that option and come back to the menu again
#need to handle exceptions when taking user's choices
#this function doesn't take any arguments
#it will work on the employ object list which is read from file empdata.dat
def run_menu_options():
    #read employee objects in to a list
    emp_list = read_file_data()
    
    #display 7 options and ask users to select from them and execute the selection
    sel = 1
    while sel <=  7 and sel >= 1:
        #display options
        print("\n==== Menu ====")
        print("1. To add an employee")
        print("2. To print the name and address of employees")
        print("3. To print the employee name and compensation of all employees")
        print("4. To search for employees by name")
        print("5. To check the basic statistics of employees")
        print("6. To calculate the reimbursement of one employee")
        print("7. To exit program")
        
        #take selection
        
        ##################
        #type in your code
        ##################
        
        #execute selection
        if sel == 1:
            emp_list.append(run_option1())
        elif sel == 2:
            run_option2(emp_list)
        elif sel == 3:
            run_option3(emp_list)
        elif sel == 4:
            run_option4(emp_list)
        elif sel == 5:
            run_option5(emp_list)
        elif sel == 6:
            run_option6(emp_list)
        elif sel == 7:  
            run_option7(emp_list)
        else:
            print("Invalid choice!")

# %%
#do a quick test run_menu_options() function before moving forward (5 points)
#don't change this code and please use the example input
#example inputs in this order: 0;8;zzz;7;n;7;y
run_menu_options()

# %%
#here comes the main test, which is splitted into several steps (20 points in total)

#step 1: choose option 1 three times and enter the following three employees (5 points)
#type 4 employee: David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3; 2018;5000;110000;5;2
#type 4 employee: Grace; 105 E Campbell Road, Richardson, Texas, 75080; Porsche; Cayenne; 2019;3000;180000;8;1
#type 4 employee: Zoey; 107 E Campbell Road, Richardson, Texas, 75080; Audi; A3; 2022;3000;90000;10;3

#step 2: choose option 2
#then choose 1

#step 3:choose option 3 (5 points)

#step 4:choose option 4 
#then type in: grace (all lower cases)

#step 5:choose option 5 (5 points)

#step 6:choose option 6 (5 points)
#then type in: ZOEY (all upper cases); then 1; then 120

#step 7:choose option 7
#then type in: y
run_menu_options()

# %%
