{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Final Exam Code Template ###\n",
    "__This template will guide you to complete the final exam. Grading rubrics are also provided.__\n",
    "\n",
    "__Please follow the guidelines closely when you type in your own code and test your program.__\n",
    "\n",
    "__Before working on your own code, save the template as \"Final_firstname_lastname\" so you don't change the original file and can refer to the template when necessary.__\n",
    "\n",
    "__The number of arguments mentioned below doesn't count \"self\".__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Vehicle class here\n",
    "#the order of the four required positional arguments should be: make,model,year,mileage\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names \n",
    "#no need to handle exceptions here\n",
    "\n",
    "class Vehicle:\n",
    "    def __init__(self,make,model,year,mileage):\n",
    "        self.__make = make\n",
    "        self.__model = model\n",
    "        self.__year = year\n",
    "        self.__mileage = mileage\n",
    "    def get_make(self):\n",
    "        return self.__make\n",
    "    def get_model(self):\n",
    "        return self.__model\n",
    "    def get_year(self):\n",
    "        return self.__year\n",
    "    def get_mileage(self):\n",
    "        return self.__mileage\n",
    "    def set_make(self,make):\n",
    "        self.__make = make\n",
    "    def set_model(self,model):\n",
    "        self.__model = model\n",
    "    def set_year(self,year):\n",
    "        self.__year = year\n",
    "    def set_mileage(self,mileage):\n",
    "        self.__mileage = mileage\n",
    "        \n",
    "    def __str__(self):\n",
    "        vehiclestr1 = \"Make: {0}; Model: {1}; Year of Manufacture: {2}; Mileage: {3} \".format(self.get_make(),self.get_model(),self.get_year(),self.get_mileage())\n",
    "        return vehiclestr1\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Make: Honda; Model: Civic; Year of Manufacture: 2014; Mileage: 50000 \n",
      "The mileage of this vehicle is: 50000\n",
      "The year of manufacture of this vehicle is: 2012\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Vehicle class before moving forward (5 points)\n",
    "#don't change this code\n",
    "vehicle1=Vehicle(\"Honda\",\"Civic\",2014,50000)\n",
    "print(vehicle1)\n",
    "print(\"The mileage of this vehicle is:\", vehicle1.get_mileage())\n",
    "vehicle1.set_year(2012)\n",
    "print(\"The year of manufacture of this vehicle is:\", vehicle1.get_year())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Employee class here\n",
    "#the order of the three required positional arguments should be: name,address,vehicle object\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names\n",
    "#use emp for short of employee in naming attributes and functions\n",
    "#no need to handle exceptions here\n",
    "\n",
    "class Employee:\n",
    "    def __init__(self,emp_name,emp_address,vehicle):\n",
    "        self.__emp_name = emp_name\n",
    "        self.__emp_addr = emp_address\n",
    "        self.__vehicle = vehicle1\n",
    "        \n",
    "    def get_emp_name(self):\n",
    "        return self.__emp_name\n",
    "    def get_emp_addr(self):\n",
    "        return self.__emp_addr\n",
    "    def get_vehicle(self):\n",
    "        return self.__vehicle\n",
    "    def set_emp_name(self,emp_name):\n",
    "        self.__emp_name = emp_name\n",
    "    def set_emp_addr(self,emp_address):\n",
    "        self.__emp_addr = emp_address\n",
    "    def set_vehicle(self,vehicle):\n",
    "        self.__vehicle = vehicle\n",
    "        \n",
    "    def __str__(self):\n",
    "        empstr = \"Employee Name: {0}; Employee Address: {1}; \\n{2}\".format(self.get_emp_name(),self.get_emp_addr(),self.__vehicle)\n",
    "        return empstr\n",
    "\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee Name: Amy; Employee Address: 100 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2012; Mileage: 50000 \n",
      "Amy lives at 100 W Campbell Road, Richardson, Texas, 75080.\n",
      "Amy owns a Honda Civic vehicle.\n",
      "Amy lives at 800 E Campbell Road, Richardson, Texas, 75080.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Employee class before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp1=Employee(\"Amy\", \"100 W Campbell Road, Richardson, Texas, 75080\",vehicle1)\n",
    "print(emp1)\n",
    "print(\"{0} lives at {1}.\".format(emp1.get_emp_name(),emp1.get_emp_addr()))\n",
    "print(\"{0} owns a {1} {2} vehicle.\".format(emp1.get_emp_name(),emp1.get_vehicle().get_make(),emp1.get_vehicle().get_model()))\n",
    "emp1.set_emp_addr(\"800 E Campbell Road, Richardson, Texas, 75080\")\n",
    "print(\"{0} lives at {1}.\".format(emp1.get_emp_name(),emp1.get_emp_addr()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Full Time Employee class here\n",
    "#Full Time Employee class inherits from Employee class\n",
    "#the order of the four required positional arguments should be: name,address,vehicle object,salary\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names\n",
    "#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file\n",
    "#no need to handle exceptions here\n",
    "\n",
    "\n",
    "class FullTimeEmployee(Employee):\n",
    "    def __init__(self,emp_name,emp_addr,vehicle1,emp_salary):\n",
    "        Employee.__init__(self,emp_name,emp_addr,vehicle1)\n",
    "        self.__salary = float(emp_salary)\n",
    "    \n",
    "   \n",
    "    def get_salary(self):\n",
    "        return self.__salary\n",
    "  \n",
    "    def set_salary(self,salary):\n",
    "        self.__salary = float(salary)\n",
    "    \n",
    "    def compute_compensation(self):\n",
    "        if self.__salary>55000:\n",
    "            self.compensation=((0.18*25000)+(0.28*30000)+(0.33*(self.__salary-55000)))\n",
    "        elif self.__salary>25000 and self.__salary<=55000:\n",
    "            self.compensation=(0.18*25000)+(0.28*(self.__salary-25000))\n",
    "        else:\n",
    "            self.compensation=0.18*self.__salary\n",
    "        \n",
    "        return ((self.__salary - self.compensation)/52)\n",
    "    \n",
    "    def compute_reimbursement(self,annual_expense):\n",
    "        if(annual_expense<=10000):\n",
    "            return (annual_expense/52)\n",
    "        elif(annual_expense>10000):\n",
    "                annual_expense = 10000 + 0.5*(annual_expense-10000)\n",
    "                return (annual_expense/52)     \n",
    "    \n",
    "    def __str__(self):\n",
    "        str1 = \"Details of this Full Time Employee are: \\n\"\n",
    "        str1 += super().__str__()\n",
    "        str1 += \"\\nSalary:{0}\".format(format(self.__salary,'.2f'))\n",
    "        return str1\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Full Time Employee are: \n",
      "Employee Name: Amy; Employee Address: 100 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2012; Mileage: 50000 \n",
      "Salary:40000.00\n",
      "Amy has an annual salary of $40000.0.\n",
      "Amy has a weekly compensation of $601.92.\n",
      "Amy has a weekly reimbursement of $211.54.\n",
      "Amy has an annual salary of $50000.0.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Full Time Employee class before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp2=FullTimeEmployee(\"Amy\", \"100 W Campbell Road, Richardson, Texas, 75080\", vehicle1, 40000)\n",
    "print(emp2)\n",
    "print(\"{0} has an annual salary of ${1}.\".format(emp2.get_emp_name(),emp2.get_salary()))\n",
    "print(\"{0} has a weekly compensation of ${1:0.2f}.\".format(emp2.get_emp_name(),emp2.compute_compensation()))\n",
    "print(\"{0} has a weekly reimbursement of ${1:0.2f}.\".format(emp2.get_emp_name(),emp2.compute_reimbursement(12000)))\n",
    "emp2.set_salary(50000)\n",
    "print(\"{0} has an annual salary of ${1}.\".format(emp2.get_emp_name(),emp2.get_salary()))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Hourly Employee class here\n",
    "#Hourly Employee class inherits from Employee class\n",
    "#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,hourly rate\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names\n",
    "#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file\n",
    "#no need to handle exceptions here\n",
    "\n",
    "class HourlyEmployee(Employee):\n",
    "    def  __init__(self,emp_name,emp_addr,vehicle,hoursWorked,hourlyRate):\n",
    "        Employee.__init__(self,emp_name,emp_addr,vehicle)\n",
    "        self.__hours_wrkd = int(hoursWorked)\n",
    "        self.__hourly_rate = float(hourlyRate)\n",
    "        self.compensation=0\n",
    "        \n",
    "    def set_hours_worked(self,hw):\n",
    "        self.__hours_wrkd = int(hw)\n",
    "        \n",
    "    def set_hourly_rate(self,hr):\n",
    "        self.__hourly_rate = float(hr)\n",
    "        \n",
    "    def get_hours_worked(self):\n",
    "        return self.__hours_wrkd\n",
    "    \n",
    "    def get_hourly_rate(self):\n",
    "        return self.__hourly_rate\n",
    "    \n",
    "    def compute_compensation(self):\n",
    "        self.compensation =0\n",
    "        if   self.__hours_wrkd>40:\n",
    "            self.compensation = (self.__hourly_rate*40) + (self.__hourly_rate*(self.__hours_wrkd - 40)*1.8)\n",
    "        else:\n",
    "            self.compensation = (self.__hourly_rate*self.__hours_wrkd)  \n",
    "        return self.compensation\n",
    "    \n",
    "    def compute_reimbursement(self,weekly_expense):\n",
    "        if(weekly_expense<100):\n",
    "            return weekly_expense\n",
    "        elif(weekly_expense>100):\n",
    "                return 100    \n",
    "    def __str__(self):\n",
    "        str2 = \"Details of this Hourly Employee are: \\n\"\n",
    "        str2 += super().__str__()\n",
    "        str2+= \"\\nHours Worked: {0}; Hourly Rate: {1}\".format(self.__hours_wrkd,int(self.__hourly_rate))\n",
    "        return str2\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Hourly Employee are: \n",
      "Employee Name: Grace; Employee Address: 400 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2012; Mileage: 50000 \n",
      "Hours Worked: 50; Hourly Rate: 20\n",
      "Grace works 50 hours per week at an hourly rate of $20.0.\n",
      "Grace has a weekly compensation of $1160.00.\n",
      "Grace has a weekly reimbursement of $100.00.\n",
      "Grace works 50 hours per week at an hourly rate of $22.0.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Hourly Employee class before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp3=HourlyEmployee(\"Grace\", \"400 W Campbell Road, Richardson, Texas, 75080\", vehicle1,50,20)\n",
    "print(emp3)\n",
    "print(\"{0} works {1} hours per week at an hourly rate of ${2}.\".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))\n",
    "print(\"{0} has a weekly compensation of ${1:0.2f}.\".format(emp3.get_emp_name(),emp3.compute_compensation()))\n",
    "print(\"{0} has a weekly reimbursement of ${1:0.2f}.\".format(emp3.get_emp_name(),emp3.compute_reimbursement(120)))\n",
    "emp3.set_hourly_rate(22)\n",
    "print(\"{0} works {1} hours per week at an hourly rate of ${2}.\".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Consultant class here\n",
    "#Consultant class inherits from Employee class\n",
    "#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,project type\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names\n",
    "#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file\n",
    "#no need to handle exceptions here\n",
    "\n",
    "class Consultant(Employee):\n",
    "    def __init__(self, emp_name, emp_addr, vehicle, hoursWorked, ProjectType):\n",
    "        if ProjectType not in (1, 2, 3):\n",
    "            print(\"Invalid Project Type\")\n",
    "        else:\n",
    "            super().__init__(emp_name, emp_addr, vehicle)\n",
    "            self.__hours_wrkd = int(hoursWorked)\n",
    "            self.__project_type = int(ProjectType)\n",
    "            self.compensation = 0\n",
    "\n",
    "    def set_hours_worked(self, hw):\n",
    "        self.__hours_wrkd = hw\n",
    "\n",
    "    def set_project_type(self, pt):\n",
    "        if pt not in (1, 2, 3):\n",
    "            print(\"Invalid Project Type\")\n",
    "        else:\n",
    "            self.__project_type = pt\n",
    "\n",
    "    def get_hours_worked(self):\n",
    "        return self.__hours_wrkd\n",
    "    \n",
    "    def get_project_type(self):\n",
    "        return self.__project_type\n",
    "\n",
    "            \n",
    "    def compute_compensation(self):\n",
    "        if self.__project_type == 1:\n",
    "            self.compensation = 55 * self.__hours_wrkd\n",
    "        elif self.__project_type == 2:\n",
    "            self.compensation = 70 * self.__hours_wrkd\n",
    "        elif self.__project_type == 3:\n",
    "            self.compensation = 85 * self.__hours_wrkd\n",
    "        return self.compensation\n",
    "\n",
    "    def compute_reimbursement(self, weekly_expense):\n",
    "        if self.__project_type == 1:\n",
    "            return weekly_expense\n",
    "        elif self.__project_type == 2:\n",
    "            return 0.9 * weekly_expense\n",
    "        elif self.__project_type == 3:\n",
    "            return 0.8 * weekly_expense\n",
    "\n",
    "   \n",
    "    def __str__(self):\n",
    "        str3 = \"Details of this Consultant are: \\n\"\n",
    "        str3 += super().__str__()\n",
    "        str3 += \"\\nHours worked:{0}; Project Type: {1}\".format(self.__hours_wrkd, self.__project_type)\n",
    "        return str3\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Consultant are: \n",
      "Employee Name: Michael; Employee Address: 700 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2012; Mileage: 50000 \n",
      "Hours worked:40; Project Type: 2\n",
      "Michael works 40 hours per week for type 2 project.\n",
      "Michael has a weekly compensation of $2800.00.\n",
      "Michael has a weekly reimbursement of $270.00.\n",
      "Michael works 35 hours per week for type 2 project.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Consultant class before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp4=Consultant(\"Michael\", \"700 W Campbell Road, Richardson, Texas, 75080\",vehicle1,40,2)\n",
    "print(emp4)\n",
    "print(\"{0} works {1} hours per week for type {2} project.\".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))\n",
    "print(\"{0} has a weekly compensation of ${1:0.2f}.\".format(emp4.get_emp_name(),emp4.compute_compensation()))\n",
    "print(\"{0} has a weekly reimbursement of ${1:0.2f}.\".format(emp4.get_emp_name(),emp4.compute_reimbursement(300)))\n",
    "emp4.set_hours_worked(35)\n",
    "print(\"{0} works {1} hours per week for type {2} project.\".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#define your own Management class here\n",
    "#Management class inherits from both Full Time Employee class and Consultant class\n",
    "#the order of the six required positional arguments should be: name, address,vehicle object, salary, hours worked, project type\n",
    "#please use the conventional way to define function names and refer to the following test to adjust function names\n",
    "#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file\n",
    "#no need to handle exceptions here\n",
    "\n",
    "class Management(FullTimeEmployee,Consultant):\n",
    "    def __init__(self,emp_name,emp_address,vehicle1,emp_salary,hoursworked,projecttype):\n",
    "        FullTimeEmployee.__init__(self,emp_name,emp_address,vehicle1,emp_salary)\n",
    "        Consultant.__init__(self,emp_name,emp_address,vehicle1,hoursworked,projecttype)\n",
    "\n",
    "       \n",
    "    def compute_reimbursement(self,annual,weekly):\n",
    "        a=FullTimeEmployee.compute_reimbursement(self,annual)\n",
    "        b=Consultant.compute_reimbursement(self,weekly)\n",
    "        return a+b\n",
    "    def compute_compensation(self):\n",
    "        a=FullTimeEmployee.compute_compensation(self)\n",
    "        b=Consultant.compute_compensation(self)\n",
    "        return a+b\n",
    "    def __str__(self):\n",
    "        str1 = \"Details of this Management are: \\n\"\n",
    "        str1+= \"Employee Name: {0}; Employee Address: {1}; \\n{2} \\n\".format(FullTimeEmployee.get_emp_name(self),FullTimeEmployee.get_emp_addr(self),FullTimeEmployee.get_vehicle(self)) \n",
    "        str1+= \"Salary: {0}; Hours Worked: {1}; Project Type{2}\".format(FullTimeEmployee.get_salary(self),Consultant.get_hours_worked(self),Consultant.get_project_type(self))\n",
    "        return str1\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Management are: \n",
      "Employee Name: Jane; Employee Address: 1000 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2012; Mileage: 50000  \n",
      "Salary: 120000.0; Hours Worked: 10; Project Type3\n",
      "\n",
      "\n",
      "Jane has an annual salary of $120000.0.\n",
      "Jane works 10 hours per week for type 3 project.\n",
      "Jane has a weekly compensation of $2497.12.\n",
      "Jane has a weekly reimbursement of $393.85.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the Management class before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp5=Management(\"Jane\", \"1000 W Campbell Road, Richardson, Texas, 75080\",vehicle1,120000,10,3)\n",
    "print(emp5)\n",
    "print(\"\\n\")\n",
    "print(\"{0} has an annual salary of ${1}.\".format(emp5.get_emp_name(),emp5.get_salary()))\n",
    "print(\"{0} works {1} hours per week for type {2} project.\".format(emp5.get_emp_name(),emp5.get_hours_worked(),emp5.get_project_type()))\n",
    "print(\"{0} has a weekly compensation of ${1:0.2f}.\".format(emp5.get_emp_name(),emp5.compute_compensation()))\n",
    "print(\"{0} has a weekly reimbursement of ${1:0.2f}.\".format(emp5.get_emp_name(),emp5.compute_reimbursement(8000,300)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_emp_input() function to prepare for the main menu application\n",
    "#this function is used to ask for basic employee information and then return them: name and address\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions here\n",
    "def get_emp_input():\n",
    "    name = input(\"Enter the employee's name: \")\n",
    "    address = input(\"Enter the employee's address: \")\n",
    "    return (name,address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the employee's name:  Bob\n",
      "Enter the employee's address:  350 E Campbell Road, Richardson, Texas, 75080\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bob lives at 350 E Campbell Road, Richardson, Texas, 75080.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_emp_input() function before moving forward\n",
    "#don't change this code and please use the sample input\n",
    "#sample input: Bob; 350 E Campbell Road, Richardson, Texas, 75080\n",
    "name, address=get_emp_input()\n",
    "print(\"{0} lives at {1}.\".format(name,address))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_vehicle_input() function to prepare for the main menu application\n",
    "#this function is used to ask for vehicle information and then return them: make,model,year,mileage\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions of make input and model input\n",
    "#handle exceptions to make sure year is a 4-digit positive number between 1900 and 2024\n",
    "#handle exceptions to make sure mileage is a positive number\n",
    "def get_vehicle_input():\n",
    "    veh_make = input('Enter the vehicle make: ')\n",
    "    veh_model = input('Enter the vehicle model: ')\n",
    "    veh_year = int(input('Enter the year of manufacture(yyyy): '))\n",
    "    if(not(veh_year>=1900 and veh_year<=2024)):\n",
    "        print(\"\\nPlease enter an integer value for year in the format of yyyy between 1900 and 2024.\")\n",
    "        veh_year = input('Enter the vehicle year: ')\n",
    "    veh_mileage = int(input('Enter the mileage: '))\n",
    "    if(veh_mileage<=0):\n",
    "        print(\"\\nPlease enter a positive integer for vehicle mileage\")\n",
    "        veh_mileage = input('Enter the vehicle mileage: ')\n",
    "    \n",
    "    return (veh_make, veh_model, veh_year, veh_mileage)\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the vehicle make:  Ford\n",
      "Enter the vehicle model:  Ranger\n",
      "Enter the year of manufacture(yyyy):  2025\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Please enter an integer value for year in the format of yyyy between 1900 and 2024.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the vehicle year:  2015\n",
      "Enter the mileage:  80000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The vehicle entered is a Ford Ranger made in 2015 with 80000 mileage curently.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_vehicle_input() function before moving forward (5 points)\n",
    "#don't change this code and please use the sample input\n",
    "#sample input:Ford; Ranger; 2025 (when asked to enter again enter 2015); 80000\n",
    "vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()  \n",
    "print(\"The vehicle entered is a {0} {1} made in {2} with {3} mileage curently.\".format(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_full_time_input() function to prepare for the main menu application\n",
    "#this function is used to ask for specific information of full time employees and then return it: annual salary\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions\n",
    "def get_full_time_input():\n",
    "    salary = int(input(\"Enter the annual salary:\"))\n",
    "    return salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the annual salary: 80000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The annual salary entered is 80000.00\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_full_time_input() function before moving forward\n",
    "#don't change this code and please use the sample input\n",
    "#sample input:80000\n",
    "salary=get_full_time_input()\n",
    "print(\"The annual salary entered is {0:0.2f}\".format(salary))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_hourly_input() function to prepare for the main menu application\n",
    "#this function is used to ask for specific information of hourly employees and then return them: hours worked, hourly rate\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions\n",
    "def get_hourly_input():\n",
    "    hours_worked = int(input(\"Enter the hours worked:\"))\n",
    "    hourly_rate = int(input(\"Enter the hourly rate:\"))\n",
    "    return (hours_worked,hourly_rate)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the hours worked: 30\n",
      "Enter the hourly rate: 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This hourly employee works 30 hours per week at an hourly rate of $20.00\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_hourly_input() function before moving forward\n",
    "#don't change this code and please use the sample input\n",
    "#sample input: 30; 20\n",
    "hours_worked, hourly_rate = get_hourly_input()\n",
    "print(\"This hourly employee works {0} hours per week at an hourly rate of ${1:0.2f}\".format(hours_worked,hourly_rate))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_consultant_input() function to prepare for the main menu application\n",
    "#this function is used to ask for specific information of consultants and then return them: hours worked, project type\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions\n",
    "def get_consultant_input():\n",
    "    hours_worked = int(input(\"Enter the hours worked:\"))\n",
    "    project_type = int(input(\"Project Type? (Enter a number between 1 and 3):\"))\n",
    "    return (hours_worked,project_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the hours worked: 40\n",
      "Project Type? (Enter a number between 1 and 3): 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This consultant works 40 hours per week for type 2 project.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_consultant_input() function before moving forward\n",
    "#don't change this code and please use the sample input\n",
    "#sample input: 40; 2\n",
    "\n",
    "hours_worked, project_type = get_consultant_input()\n",
    "print(\"This consultant works {0} hours per week for type {1} project.\".format(hours_worked,project_type))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this get_management_input() function to prepare for the main menu application\n",
    "#this function is used to ask for specific information of managements and then return them: annual salary, hours worked, project type\n",
    "#this function doesn't take arguement(s)\n",
    "#no need to handle exceptions\n",
    "def get_management_input():\n",
    "    annual_salary = int(input(\"Enter the annual salary:\"))\n",
    "    hours_worked = int(input(\"Enter the hours worked:\"))\n",
    "    project_type = int(input(\"Project Type? (Enter a number between 1 and 3):\"))\n",
    "    return (annual_salary,hours_worked,project_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the annual salary: 100000\n",
      "Enter the hours worked: 8\n",
      "Project Type? (Enter a number between 1 and 3): 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This management has an annual salary of $100000.00. This management also works 8 hours per week additionally for type 3 project.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the get_management_input() function before moving forward\n",
    "#don't change this code and please use the sample input\n",
    "#sample input: 100000; 8; 3\n",
    "salary, hours_worked, project_type = get_management_input()\n",
    "print(\"This management has an annual salary of ${0:0.2f}. This management also works {1} hours per week additionally for type {2} project.\".format(salary, hours_worked,project_type))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete this read_file_data() function to prepare for the main menu application\n",
    "#this function is used to read information from an existing databse/binary file, which is empdata.dat in the final exam\n",
    "#this function doesn't take argument(s)\n",
    "#this function returns a list containing all employee objects stored in the database; each employ object is an element in the list; the list will also be used and updated later\n",
    "#need to handle exceptions if file doesn't exist\n",
    "import pickle\n",
    "\n",
    "\n",
    "\n",
    "def read_file_data():\n",
    "    emplist = []\n",
    "    with open('empdata.dat', 'rb') as file:\n",
    "        try:\n",
    "            while (True):\n",
    "                fd = pickle.load(file)\n",
    "                emplist.append(fd)\n",
    "        except EOFError:\n",
    "            print(\"End of file is reached\")\n",
    "        except FileNotFoundError:\n",
    "            print(\"File not found. Returning an empty list.\")\n",
    "            return emplist\n",
    "    return emplist\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "    #type in your code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": true,
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "End of file is reached\n",
      "There are 9 employees stored in the database.\n",
      "\n",
      "Below is the information of the first employee in the database: Details of this Full Time Employee are: \n",
      "Employee Name: Amy; Employee Address: 100 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2014; Mileage: 50000 \n",
      "Salary:40000.00\n",
      "\n",
      "Amy is the first employee.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on the read_file_data() function before moving forward (5 points)\n",
    "#don't change this code\n",
    "emp_list=read_file_data()\n",
    "print(\"There are {} employees stored in the database.\".format(len(emp_list)))\n",
    "print(\"\\nBelow is the information of the first employee in the database: {}\".format(emp_list[0]))\n",
    "print(\"\\n{} is the first employee.\".format(emp_list[0].get_emp_name()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#complete option 1 related code here\n",
    "#the idea is to walk through users to input required information\n",
    "#the first and foremost step is to ask for emloyee type\n",
    "#this function doesn't take arguement(s)\n",
    "#this function prints the entered object and also returns the entered object\n",
    "#some parts are provided so you don't need to change them (but you still can if you want to)\n",
    "\n",
    "def run_option1():\n",
    "    sel = input(\"Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management):\")\n",
    "    while((sel not in (\"1\",\"2\",\"3\",\"4\"))):\n",
    "              print(\"Please select an option from 1, 2, 3, and 4.\")\n",
    "              sel = input(\"Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management):\")\n",
    "    sel = int(sel)        \n",
    "    #ask for employee type\n",
    "    #exceptions need to be handled here to accept valid input \n",
    "    \n",
    "    ##################\n",
    "    #type in your code\n",
    "    ##################\n",
    "      \n",
    "    #call the previous get_emp_input() to ask for employee information and store the values      \n",
    "    name, address = get_emp_input()\n",
    "    \n",
    "    #call the previous get_vehicle_input() to ask for vehicle information and store the values\n",
    "    vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()    \n",
    "    \n",
    "    #create an object of Vehicle class using the prervious information\n",
    "    a_vehicle = Vehicle(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage)\n",
    "    \n",
    "    #depending on previous input, call the prervious functions to ask for corresponding information\n",
    "    #then use all the required information to create an object of a certain class \n",
    "    #type 1:annual salary\n",
    "    #type 2:hours worked,hourly rate\n",
    "    #type 3:hours worked, project type\n",
    "    #type 4:annual salary, hours worked, project type\n",
    "\n",
    "    if sel == 1:\n",
    "        sal = get_full_time_input()\n",
    "        an_emp = FullTimeEmployee(name, address, a_vehicle,sal)\n",
    "    elif sel == 2:\n",
    "        hw, hr = get_hourly_input()\n",
    "        an_emp = HourlyEmployee(name, address, a_vehicle, hw, hr)\n",
    "    elif sel == 3:\n",
    "        hw, pt = get_consultant_input()\n",
    "        an_emp = Consultant(name, address, a_vehicle, hw, pt)\n",
    "    elif sel ==4:\n",
    "        sal, hw, pt = get_management_input()\n",
    "        an_emp = Management(name, address, a_vehicle, sal, hw, pt)\n",
    "    \n",
    "    print(an_emp)\n",
    "    \n",
    "    print(\"\\n============================================================\")        \n",
    "    print(\"New employee entered successfully! Now going to the main menu.\")\n",
    "    print(\"===================================D===========================\",) \n",
    "    \n",
    "    \n",
    "    return an_emp    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please select an option from 1, 2, 3, and 4.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): zzz\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please select an option from 1, 2, 3, and 4.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): 4\n",
      "Enter the employee's name:  David\n",
      "Enter the employee's address:  103 E Campbell Road, Richardson, Texas, 75080\n",
      "Enter the vehicle make:  BMW\n",
      "Enter the vehicle model:  X3\n",
      "Enter the year of manufacture(yyyy):  2018\n",
      "Enter the mileage:  5000\n",
      "Enter the annual salary: 110000\n",
      "Enter the hours worked: 5\n",
      "Project Type? (Enter a number between 1 and 3): 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Management are: \n",
      "Employee Name: David; Employee Address: 103 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: BMW; Model: X3; Year of Manufacture: 2018; Mileage: 5000  \n",
      "Salary: 110000.0; Hours Worked: 5; Project Type2\n",
      "\n",
      "============================================================\n",
      "New employee entered successfully! Now going to the main menu.\n",
      "===================================D===========================\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<__main__.Management at 0x216d6d95890>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#do a quick test on the run_option1() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input\n",
    "#example input: 5 (then zzz then 4); David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3;2018;5000;110000;5;2\n",
    "run_option1()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### do a quick test on the run_option1() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input\n",
    "#example input: 5 (then zzz then 4); David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3;2018;5000;110000;5;2\n",
    "run_option1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 2 related code here\n",
    "#the function is to print centain number of employees as required by users\n",
    "#first choice:print all employees; second choice: print first 5 employees when there are at least 5 employees (print all if fewer than 5)\n",
    "#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)\n",
    "#this function doesn't return anything\n",
    "#needs to handle exceptions when taking user seletions\n",
    "def run_option2(my_lst):\n",
    "    option = input(\"Do you want to see information of all employees (input 1) or the first 5 employees (input 2)?\")\n",
    "    while(option not in (\"1\",\"2\")):\n",
    "             print(\"Please Select 1 or 2\")\n",
    "             option = input(\"Do you want to see information of all employees (input 1) or the first 5 employees (input 2)?\")\n",
    "    option = int(option)\n",
    "    \n",
    "    if(option==1):\n",
    "        print(\"\\n============================================================\")   \n",
    "        print(\"Below is the information of all the Employees stored in the database.\")\n",
    "        print(\"==============================================================\")  \n",
    "        for a in my_lst:\n",
    "            print(\"\\n\")\n",
    "            print(a)\n",
    "            \n",
    "    elif(option==2):\n",
    "        print(\"\\n============================================================\")   \n",
    "        print(\"Below is the information of the first 5 Employees stored in the database.\")\n",
    "        print(\"==============================================================\")  \n",
    "        for i in range(0,5):\n",
    "            print(\"\\n\")\n",
    "            print(my_lst[i])\n",
    "            \n",
    "        \n",
    "          \n",
    "        \n",
    "          \n",
    "    #type in "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Select 1 or 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? zzz\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please Select 1 or 2\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "============================================================\n",
      "Below is the information of the first 5 Employees stored in the database.\n",
      "==============================================================\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Amy; Employee Address: 100 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2014; Mileage: 50000 \n",
      "Salary:40000.00\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Bob; Employee Address: 200 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Toyota; Model: Camry; Year of Manufacture: 2010; Mileage: 60000 \n",
      "Salary:80000.00\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Evan; Employee Address: 300 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: BMW; Model: X3; Year of Manufacture: 2016; Mileage: 30000 \n",
      "Salary:120000.00\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: Grace; Employee Address: 400 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Kia; Model: Rio; Year of Manufacture: 2005; Mileage: 150000 \n",
      "Hours Worked: 50; Hourly Rate: 20\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: James; Employee Address: 500 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Mazda; Model: Mazda3; Year of Manufacture: 2010; Mileage: 80000 \n",
      "Hours Worked: 30; Hourly Rate: 25\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option2() function before moving forward (5 points)\n",
    "#don't change this code and please use the sample input\n",
    "#sample input: 3 (then zzz then 2)\n",
    "run_option2(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 3 related code here\n",
    "#the function is used to print compensations of all Employees\n",
    "#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)\n",
    "#this function doesn't return anything\n",
    "#no need to handle exceptions\n",
    "def run_option3(my_lst):\n",
    "    print(\"\\nEmployee name and Compensation of all Employees\")\n",
    "    print(\"=================================================\")\n",
    "    for a in my_lst:\n",
    "        print(\"{0}'s weekly compensation is ${1:0.2f}.\".format(a.get_emp_name(),a.compute_compensation()))\n",
    "    \n",
    "    #type in your code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Employee name and Compensation of all Employees\n",
      "=================================================\n",
      "Amy's weekly compensation is $601.92.\n",
      "Bob's weekly compensation is $1131.73.\n",
      "Evan's weekly compensation is $1647.12.\n",
      "Grace's weekly compensation is $1160.00.\n",
      "James's weekly compensation is $750.00.\n",
      "Luna's weekly compensation is $300.00.\n",
      "Michael's weekly compensation is $2200.00.\n",
      "Tom's weekly compensation is $3500.00.\n",
      "Zoey's weekly compensation is $2550.00.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option3() function before moving forward (5 points)\n",
    "#don't change this code and please use the sample input\n",
    "run_option3(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 4 related code here\n",
    "#the function is used to search for an employee by name and the searching is NOT case sensitive\n",
    "#if there are some matching cases, print the information of all matched employees\n",
    "#if no matchng cases, print \"There is no employee matching the name you entered.\"\n",
    "#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)\n",
    "#this function also returns a list of objects of the matched employees\n",
    "#no need to handle exceptions\n",
    "\n",
    "def run_option4(my_lst):\n",
    "    emplist = []\n",
    "    b=0\n",
    "    names = input(\"Please enter the name of the employee you want to search\")\n",
    "    for a in my_lst:\n",
    "        if (names.upper() == a.get_emp_name().upper()):\n",
    "            emplist.append(a)\n",
    "            b=1\n",
    "    if (b==1):\n",
    "          print(\"=========================================================================\")   \n",
    "          print(\"Below is the information of all employees that match the name you entered\")\n",
    "          print(\"==========================================================================\")  \n",
    "          for a in emplist:\n",
    "                print(\"\\n\")\n",
    "                print(a)\n",
    "    else:\n",
    "        print(\"There is no employee matching the name you entered\")\n",
    "    return emplist\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    #type in your code       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the name of the employee you want to search TOM\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=========================================================================\n",
      "Below is the information of all employees that match the name you entered\n",
      "==========================================================================\n",
      "\n",
      "\n",
      "Details of this Consultant are: \n",
      "Employee Name: Tom; Employee Address: 800 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Mercedes-Benz; Model: GLE350; Year of Manufacture: 2018; Mileage: 30000 \n",
      "Hours worked:50; Project Type: 2\n",
      "\n",
      "There are 1 employees matching your search.\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option4() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input (all upper cases)\n",
    "#example input: TOM\n",
    "#part 1\n",
    "matched_emp_list=run_option4(emp_list)\n",
    "print(\"\\nThere are {} employees matching your search.\".format(len(matched_emp_list)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the name of the employee you want to search Hongchang\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There is no employee matching the name you entered\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#do a quick test on run_option4() function before moving forward \n",
    "#don't change this code and please use the example input\n",
    "#example input: Hongchang\n",
    "#part 2\n",
    "run_option4(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 5 related code here\n",
    "#the function is used to show some basic statistics. They are: \n",
    "#(1) the number of employees stored in the database\n",
    "#(2) the highest weekly compensation\n",
    "#(3) the mean weekly compensation\n",
    "#(4) the number of employees who have a vehicle with over 100,000 mileage\n",
    "#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)\n",
    "#this function doesn't return anything\n",
    "#no need to handle exceptions\n",
    "def run_option5(my_lst):\n",
    "    sum=0\n",
    "    count=0\n",
    "    print(\"There are {0} employees stored in this employee database\".format(len(my_lst)))\n",
    "    max = 0\n",
    "    for a in my_lst:\n",
    "          sum+=a.compute_compensation()\n",
    "          if(a.compute_compensation()>max):\n",
    "                 max = a.compute_compensation()\n",
    "          if(a.get_vehicle().get_mileage()>100000):\n",
    "             count+=1\n",
    "    print(\"The highest weekly compensation is  ${0:0.2f}\".format(max))\n",
    "    average = (sum/len(my_lst))\n",
    "    print(\"The mean weekly compensation is  ${0:0.2f}\".format(average))\n",
    "    print(\"The number of employees who have a vehicle with over 100,000 mileage is {0}\".format(count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 9 employees stored in this employee database\n",
      "The highest weekly compensation is  $3500.00\n",
      "The mean weekly compensation is  $1537.86\n",
      "The number of employees who have a vehicle with over 100,000 mileage is 2\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option5() function before moving forward (5 points)\n",
    "#don't change this code \n",
    "run_option5(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 6 related code here\n",
    "#the function is used to compute weekly reimbursement (assuming the user has the requirerd information)\n",
    "#the first step is to ask for the name of the employee (you can call run_option4() here)\n",
    "#the second step is to select one employee from the matched employees\n",
    "#the third step is to ask for required information \n",
    "#this function doesn't return anything\n",
    "#no need to handle exceptions\n",
    "def run_option6(emp_list):\n",
    "    matched_list=run_option4(emp_list)\n",
    "    choice=int(input(\"Which employee do you want to check (enter a number)?\"))\n",
    "    emp=matched_list[choice-1]\n",
    "    weekly = int(input(\"What is the weekly expense?\"))\n",
    "    weekly_input = emp.compute_reimbursement(weekly)\n",
    "    print(\"##############################################################\")  \n",
    "    print(\"The employee should have a weekly reimbursement of ${0:0.2f}\".format(weekly_input))\n",
    "    \n",
    "    \n",
    "    #type in your code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the name of the employee you want to search bob\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=========================================================================\n",
      "Below is the information of all employees that match the name you entered\n",
      "==========================================================================\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Bob; Employee Address: 200 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Toyota; Model: Camry; Year of Manufacture: 2010; Mileage: 60000 \n",
      "Salary:80000.00\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Which employee do you want to check (enter a number)? 1\n",
      "What is the weekly expense? 8000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "##############################################################\n",
      "The employee should have a weekly reimbursement of $153.85\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option6() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input (all lower cases)\n",
    "#example input: bob;1;8000\n",
    "#part 1\n",
    "\n",
    "run_option6(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the name of the employee you want to search james\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=========================================================================\n",
      "Below is the information of all employees that match the name you entered\n",
      "==========================================================================\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: James; Employee Address: 500 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Mazda; Model: Mazda3; Year of Manufacture: 2010; Mileage: 80000 \n",
      "Hours Worked: 30; Hourly Rate: 25\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Which employee do you want to check (enter a number)? 1\n",
      "What is the weekly expense? 130\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "##############################################################\n",
      "The employee should have a weekly reimbursement of $100.00\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option6() function before moving forward \n",
    "#don't change this code and please use the sample input (all lower cases)\n",
    "#sample input: james;1;130\n",
    "#part 2\n",
    "\n",
    "run_option6(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete option 7 related code here\n",
    "#the function is used to store changes into a new file/database (i.e. empdata_updated.dat) and exit the program\n",
    "#the first step is to double check with the user if he/she does want to exit (not case sensitive)\n",
    "#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)\n",
    "#this function doesn't return anything\n",
    "#no need to handle exceptions\n",
    "\n",
    "import sys\n",
    "\n",
    "def run_option7(my_lst):\n",
    "    print(\"You chose to exit the program.\")\n",
    "    res = input(\"Are you sure (Y?N)?\")\n",
    "    if(res not in (\"Y\",\"N\",\"n\",\"y\")):\n",
    "        print(\"Your input doesn't match any valid option and has been considered as 'N'.\")\n",
    "        print(\"Going back to the selection menu\\n\")\n",
    "    elif(res in (\"N\",\"n\")):\n",
    "        print(\"============================================================\")   \n",
    "        print(\"Going back to the selection menu\")\n",
    "        print(\"==============================================================\")  \n",
    "    elif(res in (\"Y\",\"y\")):\n",
    "        sys.exit(\"Exiting the program\")\n",
    "    #type in your code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? b\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your input doesn't match any valid option and has been considered as 'N'.\n",
      "Going back to the selection menu\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option7() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input\n",
    "#example input: b\n",
    "#part 1\n",
    "run_option7(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? n\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      "Going back to the selection menu\n",
      "==============================================================\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option7() function before moving forward \n",
    "#don't change this code and please use the example input\n",
    "#example input: n\n",
    "#part 2\n",
    "run_option7(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? y\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "Exiting the program",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m Exiting the program\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "D:\\anacondas\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3534: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "#do a quick test on run_option7() function before moving forward \n",
    "#don't change this code and please use the example input\n",
    "#example input: y\n",
    "#part 3\n",
    "run_option7(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "#complete the main application\n",
    "#the application menu provides 7 options\n",
    "#when user selects a valid option (except for 7), execute that option and come back to the menu again\n",
    "#need to handle exceptions when taking user's choices\n",
    "#this function doesn't take any arguments\n",
    "#it will work on the employ object list which is read from file empdata.dat\n",
    "def run_menu_options():\n",
    "    #read employee objects in to a list\n",
    "    emp_list = read_file_data()\n",
    "    #display 7 options and ask users to select from them and execute the selection\n",
    "    sel = 1\n",
    "    while sel <=  7 and sel >= 1:\n",
    "        #display options\n",
    "        print(\"\\n==== Menu ====\")\n",
    "        print(\"1. To add an employee\")\n",
    "        print(\"2. To print the name and address of employees\")\n",
    "        print(\"3. To print the employee name and compensation of all employees\")\n",
    "        print(\"4. To search for employees by name\")\n",
    "        print(\"5. To check the basic statistics of employees\")\n",
    "        print(\"6. To calculate the reimbursement of one employee\")\n",
    "        print(\"7. To exit program\")\n",
    "        \n",
    "        sels = input(\"Select an option from the menu\")\n",
    "        while(sels not in (\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\")):\n",
    "              print(\"Your selection is {0}\".format(sels))\n",
    "              print(\"============================================================\")   \n",
    "              print(\"You must enter an integer between 1 and 7!\")\n",
    "              print(\"==============================================================\")  \n",
    "              print(\"\\n==== Menu ====\")\n",
    "              print(\"1. To add an employee\")\n",
    "              print(\"2. To print the name and address of employees\")\n",
    "              print(\"3. To print the employee name and compensation of all employees\")\n",
    "              print(\"4. To search for employees by name\")\n",
    "              print(\"5. To check the basic statistics of employees\")\n",
    "              print(\"6. To calculate the reimbursement of one employee\")\n",
    "              print(\"7. To exit program\")\n",
    "              sels = input(\"Select an option from the menu\")\n",
    "              \n",
    "        sel=int(sels)    \n",
    "        \n",
    "        ##################\n",
    "        #type in your code\n",
    "        ##################\n",
    "        \n",
    "        #execute selection\n",
    "        if sel == 1:\n",
    "            emp_list.append(run_option1())\n",
    "        elif sel == 2:\n",
    "            run_option2(emp_list)\n",
    "        elif sel == 3:\n",
    "            run_option3(emp_list)\n",
    "        elif sel == 4:\n",
    "            run_option4(emp_list)\n",
    "        elif sel == 5:\n",
    "            run_option5(emp_list)\n",
    "        elif sel == 6:\n",
    "            run_option6(emp_list)\n",
    "        elif sel == 7:  \n",
    "            run_option7(emp_list)\n",
    "        else:\n",
    "            print(\"Invalid choice!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "End of file is reached\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your selection is 0\n",
      "============================================================\n",
      "You must enter an integer between 1 and 7!\n",
      "==============================================================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your selection is 8\n",
      "============================================================\n",
      "You must enter an integer between 1 and 7!\n",
      "==============================================================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu zzz\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your selection is zzz\n",
      "============================================================\n",
      "You must enter an integer between 1 and 7!\n",
      "==============================================================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? n\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============================================================\n",
      "Going back to the selection menu\n",
      "==============================================================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? y\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "Exiting the program",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m Exiting the program\n"
     ]
    }
   ],
   "source": [
    "#do a quick test run_menu_options() function before moving forward (5 points)\n",
    "#don't change this code and please use the example input\n",
    "#example inputs in this order: 0;8;zzz;7;n;7;y\n",
    "run_menu_options()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "End of file is reached\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 1\n",
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): 4\n",
      "Enter the employee's name:  David\n",
      "Enter the employee's address:  103 E Campbell Road, Richardson, Texas, 75080\n",
      "Enter the vehicle make:  BMW\n",
      "Enter the vehicle model:  X3\n",
      "Enter the year of manufacture(yyyy):  2018\n",
      "Enter the mileage:  5000\n",
      "Enter the annual salary: 110000\n",
      "Enter the hours worked: 5\n",
      "Project Type? (Enter a number between 1 and 3): 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Management are: \n",
      "Employee Name: David; Employee Address: 103 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: BMW; Model: X3; Year of Manufacture: 2018; Mileage: 5000  \n",
      "Salary: 110000.0; Hours Worked: 5; Project Type2\n",
      "\n",
      "============================================================\n",
      "New employee entered successfully! Now going to the main menu.\n",
      "===================================D===========================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 1\n",
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): 4\n",
      "Enter the employee's name:  Grace\n",
      "Enter the employee's address:  105 E Campbell Road, Richardson, Texas, 75080\n",
      "Enter the vehicle make:  Porsche\n",
      "Enter the vehicle model:  Cayenne\n",
      "Enter the year of manufacture(yyyy):  2019\n",
      "Enter the mileage:  3000\n",
      "Enter the annual salary: 180000\n",
      "Enter the hours worked: 8\n",
      "Project Type? (Enter a number between 1 and 3): 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Management are: \n",
      "Employee Name: Grace; Employee Address: 105 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Porsche; Model: Cayenne; Year of Manufacture: 2019; Mileage: 3000  \n",
      "Salary: 180000.0; Hours Worked: 8; Project Type1\n",
      "\n",
      "============================================================\n",
      "New employee entered successfully! Now going to the main menu.\n",
      "===================================D===========================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 1\n",
      "Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management): 4\n",
      "Enter the employee's name:  Zoey\n",
      "Enter the employee's address:  107 E Campbell Road, Richardson, Texas, 75080\n",
      "Enter the vehicle make:  Audi\n",
      "Enter the vehicle model:  A3\n",
      "Enter the year of manufacture(yyyy):  2022\n",
      "Enter the mileage:  3000\n",
      "Enter the annual salary: 90000\n",
      "Enter the hours worked: 10\n",
      "Project Type? (Enter a number between 1 and 3): 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Details of this Management are: \n",
      "Employee Name: Zoey; Employee Address: 107 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Audi; Model: A3; Year of Manufacture: 2022; Mileage: 3000  \n",
      "Salary: 90000.0; Hours Worked: 10; Project Type3\n",
      "\n",
      "============================================================\n",
      "New employee entered successfully! Now going to the main menu.\n",
      "===================================D===========================\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 2\n",
      "Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "============================================================\n",
      "Below is the information of all the Employees stored in the database.\n",
      "==============================================================\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Amy; Employee Address: 100 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Honda; Model: Civic; Year of Manufacture: 2014; Mileage: 50000 \n",
      "Salary:40000.00\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Bob; Employee Address: 200 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Toyota; Model: Camry; Year of Manufacture: 2010; Mileage: 60000 \n",
      "Salary:80000.00\n",
      "\n",
      "\n",
      "Details of this Full Time Employee are: \n",
      "Employee Name: Evan; Employee Address: 300 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: BMW; Model: X3; Year of Manufacture: 2016; Mileage: 30000 \n",
      "Salary:120000.00\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: Grace; Employee Address: 400 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Kia; Model: Rio; Year of Manufacture: 2005; Mileage: 150000 \n",
      "Hours Worked: 50; Hourly Rate: 20\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: James; Employee Address: 500 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Mazda; Model: Mazda3; Year of Manufacture: 2010; Mileage: 80000 \n",
      "Hours Worked: 30; Hourly Rate: 25\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: Luna; Employee Address: 600 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Nissan; Model: Sentra; Year of Manufacture: 2005; Mileage: 160000 \n",
      "Hours Worked: 20; Hourly Rate: 15\n",
      "\n",
      "\n",
      "Details of this Consultant are: \n",
      "Employee Name: Michael; Employee Address: 700 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Ford; Model: Ranger; Year of Manufacture: 2011; Mileage: 80000 \n",
      "Hours worked:40; Project Type: 1\n",
      "\n",
      "\n",
      "Details of this Consultant are: \n",
      "Employee Name: Tom; Employee Address: 800 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Mercedes-Benz; Model: GLE350; Year of Manufacture: 2018; Mileage: 30000 \n",
      "Hours worked:50; Project Type: 2\n",
      "\n",
      "\n",
      "Details of this Consultant are: \n",
      "Employee Name: Zoey; Employee Address: 900 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Tesla; Model: Model3; Year of Manufacture: 2018; Mileage: 15000 \n",
      "Hours worked:30; Project Type: 3\n",
      "\n",
      "\n",
      "Details of this Management are: \n",
      "Employee Name: David; Employee Address: 103 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: BMW; Model: X3; Year of Manufacture: 2018; Mileage: 5000  \n",
      "Salary: 110000.0; Hours Worked: 5; Project Type2\n",
      "\n",
      "\n",
      "Details of this Management are: \n",
      "Employee Name: Grace; Employee Address: 105 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Porsche; Model: Cayenne; Year of Manufacture: 2019; Mileage: 3000  \n",
      "Salary: 180000.0; Hours Worked: 8; Project Type1\n",
      "\n",
      "\n",
      "Details of this Management are: \n",
      "Employee Name: Zoey; Employee Address: 107 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Audi; Model: A3; Year of Manufacture: 2022; Mileage: 3000  \n",
      "Salary: 90000.0; Hours Worked: 10; Project Type3\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Employee name and Compensation of all Employees\n",
      "=================================================\n",
      "Amy's weekly compensation is $601.92.\n",
      "Bob's weekly compensation is $1131.73.\n",
      "Evan's weekly compensation is $1647.12.\n",
      "Grace's weekly compensation is $1160.00.\n",
      "James's weekly compensation is $750.00.\n",
      "Luna's weekly compensation is $300.00.\n",
      "Michael's weekly compensation is $2200.00.\n",
      "Tom's weekly compensation is $3500.00.\n",
      "Zoey's weekly compensation is $2550.00.\n",
      "David's weekly compensation is $1868.27.\n",
      "Grace's weekly compensation is $2860.19.\n",
      "Zoey's weekly compensation is $2110.58.\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 4\n",
      "Please enter the name of the employee you want to search grace\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=========================================================================\n",
      "Below is the information of all employees that match the name you entered\n",
      "==========================================================================\n",
      "\n",
      "\n",
      "Details of this Hourly Employee are: \n",
      "Employee Name: Grace; Employee Address: 400 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Kia; Model: Rio; Year of Manufacture: 2005; Mileage: 150000 \n",
      "Hours Worked: 50; Hourly Rate: 20\n",
      "\n",
      "\n",
      "Details of this Management are: \n",
      "Employee Name: Grace; Employee Address: 105 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Porsche; Model: Cayenne; Year of Manufacture: 2019; Mileage: 3000  \n",
      "Salary: 180000.0; Hours Worked: 8; Project Type1\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 12 employees stored in this employee database\n",
      "The highest weekly compensation is  $3500.00\n",
      "The mean weekly compensation is  $1723.32\n",
      "The number of employees who have a vehicle with over 100,000 mileage is 2\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 6\n",
      "Please enter the name of the employee you want to search ZOEY\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=========================================================================\n",
      "Below is the information of all employees that match the name you entered\n",
      "==========================================================================\n",
      "\n",
      "\n",
      "Details of this Consultant are: \n",
      "Employee Name: Zoey; Employee Address: 900 W Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Tesla; Model: Model3; Year of Manufacture: 2018; Mileage: 15000 \n",
      "Hours worked:30; Project Type: 3\n",
      "\n",
      "\n",
      "Details of this Management are: \n",
      "Employee Name: Zoey; Employee Address: 107 E Campbell Road, Richardson, Texas, 75080; \n",
      "Make: Audi; Model: A3; Year of Manufacture: 2022; Mileage: 3000  \n",
      "Salary: 90000.0; Hours Worked: 10; Project Type3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Which employee do you want to check (enter a number)? 1\n",
      "What is the weekly expense? 120\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "##############################################################\n",
      "The employee should have a weekly reimbursement of $96.00\n",
      "\n",
      "==== Menu ====\n",
      "1. To add an employee\n",
      "2. To print the name and address of employees\n",
      "3. To print the employee name and compensation of all employees\n",
      "4. To search for employees by name\n",
      "5. To check the basic statistics of employees\n",
      "6. To calculate the reimbursement of one employee\n",
      "7. To exit program\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Select an option from the menu 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You chose to exit the program.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Are you sure (Y?N)? Y\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "Exiting the program",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m Exiting the program\n"
     ]
    }
   ],
   "source": [
    "#here comes the main test, which is splitted into several steps (20 points in total)\n",
    "\n",
    "#step 1: choose option 1 three times and enter the following three employees (5 points)\n",
    "#type 4 employee: David; 103 E Campbell Road, Richardson, Texas, 75080; BMW; X3; 2018;5000;110000;5;2\n",
    "#type 4 employee: Grace; 105 E Campbell Road, Richardson, Texas, 75080; Porsche; Cayenne; 2019;3000;180000;8;1\n",
    "#type 4 employee: Zoey; 107 E Campbell Road, Richardson, Texas, 75080; Audi; A3; 2022;3000;90000;10;3\n",
    "\n",
    "#step 2: choose option 2\n",
    "#then choose 1\n",
    "\n",
    "#step 3:choose option 3 (5 points)\n",
    "\n",
    "#step 4:choose option 4 \n",
    "#then type in: grace (all lower cases)\n",
    "\n",
    "#step 5:choose option 5 (5 points)\n",
    "\n",
    "#step 6:choose option 6 (5 points)\n",
    "#then type in: ZOEY (all upper cases); then 1; then 120\n",
    "\n",
    "#step 7:choose option 7\n",
    "#then type in: y\n",
    "run_menu_options()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
