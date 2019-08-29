import os
import csv

employeeAttendanceFile = "employee_attendance.csv"
currentEmployeeFile = "sheets_current_employees.csv"

class Employee:
    def __init__(self, emp_id, name, phone, age):
        self.ID = emp_id
        self.name = name
        self.phone = phone
        self.age = age

    def addEmployee(self, file):
        with open(file, "a") as theFile:
            #beacuse I used a comma to seperate the values, they were automaticaly placed in the correct coloms in the csv file.
            #instead of using csv writer.
            theFile.write("%d,%s,%d,%d \n" %(self.ID, self.name, self.phone, self.age))


    def deletEmployee(self, currentEmployeeFile):
        fileAfterDeleting = "current_employees_after_delete.csv"

        # add headers to fileAFterDeleting
        with open(fileAfterDeleting, 'w', newline="") as reportFile:
            csv_writer = csv.writer(reportFile, delimiter=',')
            csv_writer.writerow(['ID', "name", 'phone','age'])

        with open(currentEmployeeFile, 'r', newline="") as readFile, open(fileAfterDeleting,'a', newline="")as writeFile:
            reader = csv.reader(readFile, delimiter=',')
            writer = csv.writer(writeFile, delimiter=',')

            line_count = 0
            for row in reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if (int(row[0]) != self.ID):
                        writer.writerow(row)

        #replace old employee file with the updated file
        os.remove(currentEmployeeFile)
        os.rename(fileAfterDeleting, currentEmployeeFile)


    #checkID returns TURE if the ID of the employee object already exists the file
    #accepts csv files only
    def checkID(self,file):
        with open(file, "r") as theFile:
            csv_reader = csv.reader(theFile, delimiter=',')
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

def employeeManualInput():
    valid_value = False
    # if input for name is an int, then valid_value stays False, we enter the else clause, and return the the beginning of the loop
    #if input for name is not an int, then we enter the exceptuon, valid_value is changes to true, and we exit the loop
    while valid_value == False:
        try:
            name = input("enter employee's name")
            check_name = int(name)
        except ValueError:
            valid_value = True
        else:
            print("A name can not be a number")

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
    if temp.checkID(currentEmployeeFile):
        print("ID number %d already exists in the file, and will not be added again")
    else:
      temp.addEmployee(currentEmployeeFile)

#adding empployee from file not in employee class, because the action is not on a instance of the employee class
#format for file: each line in the file is 1 employee, following this format: ID name phone age (each seperated by 1 space)
# add option to add employees from csv file
def addEmpFormFIle():
    newEmployeeFile = "sheets_new_employees.csv"

    with open(newEmployeeFile,'r') as csv_file:
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
                        if temp.checkID(currentEmployeeFile):
                            print("ID number %d already exists in the file, and will not be added again" %temp.ID)
                            line_count += 1
                        else:
                            temp.addEmployee(currentEmployeeFile)
                            line_count += 1

def deleteEmpManual():
    valid_ID = False
    while valid_ID is False:
        ID = inputID()
        tempEmp = Employee(ID, "a", 0, 0)
        if tempEmp.checkID(currentEmployeeFile):
            valid_ID = True
            print("employee ID %d is deleted from current enployees file" %ID)
            tempEmp.deletEmployee(currentEmployeeFile)
        else:
            print("the ID you entered is not in the current employees file")
            user_choice = input("to enter different ID, enter 1, to exit enter 2")
            if user_choice == '2':
                valid_ID = True


def deletEmpFromFile():
    deleteEmpFile = "delete_employees.csv"

    with open(deleteEmpFile, 'r') as csv_file:
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
                    if not temp.checkID(currentEmployeeFile):
                        print("ID number %d does not exist in file, and will be skipped" % temp.ID)
                    else:
                        temp.deletEmployee(currentEmployeeFile)
                        line_count += 1

def inputID():
    valid_value = False
    while valid_value == False:
        try:
            ID = int(input("enter employee ID number:"))
        except ValueError:
            print("ID must be whole numeber")
        else:
            valid_value = True

    return ID

#deleteEmpManual()
#addEmpFormFIle()
deletEmpFromFile()
