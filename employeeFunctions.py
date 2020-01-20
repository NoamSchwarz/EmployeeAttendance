import os
import csv

current_employee_file = "current_employees.csv"

class Employee:
    def __init__(self, emp_id, name, phone, age):
        self.ID = emp_id
        self.name = name
        self.phone = phone
        self.age = age

    def add_employee(self, file):
        with open(file, "a") as the_file:
            #beacuse I used a comma to seperate the values, they were automaticaly placed in the correct coloms in the csv file.
            #instead of using csv writer.
            the_file.write("%d,%s,%d,%d \n" %(self.ID, self.name, self.phone, self.age))


    def delete_employee(self, current_employee_file):
        file_after_deleting = "current_employees_after_delete.csv"

        # add headers to fileAFterDeleting
        with open(file_after_deleting, 'w', newline="") as report_file:
            csv_writer = csv.writer(report_file, delimiter=',')
            csv_writer.writerow(['ID', "name", 'phone','age'])

        with open(current_employee_file, 'r', newline="") as read_file, open(file_after_deleting,'a', newline="")as write_file:
            reader = csv.reader(read_file, delimiter=',')
            writer = csv.writer(write_file, delimiter=',')

            line_count = 0
            for row in reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if (int(row[0]) != self.ID):
                        writer.writerow(row)

        #replace old employee file with the updated file
        os.remove(current_employee_file)
        os.rename(file_after_deleting, current_employee_file)


    #check_ID returns TURE if the ID of the employee object already exists the file
    #accepts csv files only
    def check_ID(self,file):
        with open(file, "r") as the_file:
            csv_reader = csv.reader(the_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if int(row[0]) == self.ID:
                        return True
                        break
                    else:
                        continue
            return False

def employee_manual_input():

    valid_value = False
    while valid_value == False:
        name = input("enter employee's name")
        if name.isalpha():
            valid_value = True
        else:
            print("names must be comprised of letters only")

    #if input for ID, Phone or age is not an int, we enter the except and valid_value stays False
    # if input is and int, we enter the else clause, valid_value is changed to True and we exit the loop
    valid_value = False
    while valid_value == False:
        try:
            ID = int(input("enter employee ID number"))
            phone = int(input("enter employees phone number"))
            age = int(input("enter employees age"))
        except ValueError:
            print("ID, Phone and age must be a whole number")
        else:
            valid_value = True

    #while loop does not exit before all inputs are correct, so all attributes are of correct values.
    temp = Employee(ID, name, phone, age)
    if temp.check_ID(current_employee_file):
        print("ID number %d already exists in the file, and will not be added again")
    else:
      temp.add_employee(current_employee_file)


def add_emp_from_file():
    new_employee_file = "new_employees.csv"

    with open(new_employee_file,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #skip column headers
            if line_count == 0:
                line_count += 1
            else:
                try:
                    ID= int(row[0])
                    phone = int(row[2])
                    age = int(row[3])
                except ValueError:
                    print("in row #%d the ID, phone or age are not an int" %line_count)
                    print("input prosses stopping. fix problem and try again")
                    return
                else:
                    name = row[1]
                    if name.isdigit() is True :
                        print("in row #%d, a name containse a number. a name connot contain a number" %line_count)
                        print("input prosses stopping. fix problem and try again")
                        return
                    else:
                        temp = Employee(ID,name,phone,age)
                        if temp.check_ID(current_employee_file):
                            print("ID number %d already exists in the file, and will not be added again" %temp.ID)
                            line_count += 1
                        else:
                            temp.add_employee(current_employee_file)
                            line_count += 1

def delete_emp_manual():
    valid_ID = False
    while valid_ID is False:
        ID = input_ID()
        temp_emp = Employee(ID, "a", 0, 0)
        if temp_emp.check_ID(current_employee_file):
            valid_ID = True
            print("employee ID %d is deleted from current enployees file" %ID)
            temp_emp.delete_employee(current_employee_file)
        else:
            print("the ID you entered is not in the current employees file")
            user_choice = input("to enter different ID, enter 1, to exit enter 2")
            if user_choice == '2':
                valid_ID = True


def delet_emp_from_file():
    delete_emp_file = "delete_employees.csv"

    with open(delete_emp_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                line_count += 1
            else:
                try:
                    ID = int(row[0])
                except ValueError:
                    print("in row #%d of deletion file, ID value is not an int" %line_count)
                    print("deleting process has stopped. fix problem and try again")
                    return
                else:
                    temp = Employee(ID, 'a', 0, 0)
                    if not temp.check_ID(current_employee_file):
                        print("ID number %d does not exist in file, and will be skipped" % temp.ID)
                    else:
                        temp.delete_employee(current_employee_file)
                        line_count += 1

def input_ID():
    valid_value = False
    while valid_value == False:
        try:
            ID = int(input("enter employee ID number:"))
        except ValueError:
            print("ID must be whole numeber")
        else:
            valid_value = True

    return ID

#delete_emp_manual()
#add_emp_from_file()
#delet_emp_from_file()
#employee_manual_input()
