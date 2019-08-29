import time
import datetime
import csv
import employeeFunctions

employeeAttendanceFile = "employee_attendance.csv"
currentEmployeeFile = "sheets_current_employees.csv"


def markAttendance():

    valid_ID = False
    while valid_ID == False:
        ID = employeeFunctions.inputID()

        currentTIme = time.strftime("%H:%M")
        currentDate =  datetime.datetime.today().strftime('%d.%m.%y')
        print(currentTIme)
        print(currentDate)

        # if the ID entered DOES exists in current employees file, mark attendance and exit loop
        tempEmp = employeeFunctions.Employee(ID, "a", 0, 0)
        if tempEmp.checkID(currentEmployeeFile):
            valid_ID = True
            print("ID accepted")

            with open(employeeAttendanceFile, 'a',newline="") as timeFile:
                writer = csv.writer(timeFile, delimiter=',')
                writer.writerow([ID,currentDate, currentTIme])
        else:
            print("the ID you entered is not in the current employees file")
            user_choice = input("to enter different ID, enter 1, to exit enter 2")
            if user_choice == '2':
                valid_ID = True


#generates csv with date and time, acording to ID of one employee.
def reportForSingleID():

    valid_ID = False
    while valid_ID == False:
        try:
            empID = int(input("enter employee ID"))
        except ValueError:
            print("employee ID must be a whole number")
        else:
            newFileName = 'reprot_for_empID_%d.csv' %empID
            tempEmp = employeeFunctions.Employee(empID, "a", 0, 0)

            if tempEmp.checkID(currentEmployeeFile):
                valid_ID = True
                print("ID accepted")
            else:
                print("the ID you entered is not in the current employees file")
                #user can enter anthing that isn't 2 and it will still go back to asking for ID. I Don't fell the need to change this.
                user_choice = input("to enter different ID, enter 1, to exit enter 2")
                if user_choice == '2':
                   return

    #add headers to employee report file
    with open(newFileName, 'w',newline="") as reportFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_writer.writerow(['ID',"date", 'time'])

    with open(newFileName, 'a',newline="") as reportFile, open(employeeAttendanceFile, 'r') as timeFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_reader = csv.reader(timeFile, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[0] == str(empID):
                    ID = row[0]
                    thisDate = row[1]
                    thisTime = row[2]
                    csv_writer.writerow([ID, thisDate, thisTime])


def reportForMonth():

    month = inputMonth()
    if month == 14:
        return

    # add headers to monthly attendance report file
    newFileName = 'reprot_for_month_%d.csv' % month
    with open(newFileName, 'w', newline="") as reportFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_writer.writerow(['ID', "date", 'time'])

    with open(newFileName, 'a', newline="") as reportFile, open(employeeAttendanceFile, 'r') as timeFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_reader = csv.reader(timeFile, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                tempDate = str(row[1])
                dateList = tempDate.split('.')
                if int(dateList[1]) == month:
                    ID = row[0]
                    thisDate = row[1]
                    thisTime = row[2]
                    csv_writer.writerow([ID, thisDate, thisTime])

def reportForLate():

    month = inputMonth()
    if month == 14:
        return

    # add headers to monthly attendance report file
    newFileName = 'late_reprot_for_month_%d.csv' % month

    with open(newFileName, 'w', newline="") as reportFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_writer.writerow(['ID', "date", 'time'])

    with open(newFileName, 'a', newline="") as reportFile, open(employeeAttendanceFile, 'r') as timeFile:
        csv_writer = csv.writer(reportFile, delimiter=',')
        csv_reader = csv.reader(timeFile, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                tempDate = str(row[1])
                dateList = tempDate.split('.')
                tempTime = str(row[2])
                timeFloat = float(tempTime.replace(':','.'))

                if int(dateList[1]) == month and timeFloat > 9.30 :
                    ID = row[0]
                    thisDate = row[1]
                    thisTime = row[2]
                    csv_writer.writerow([ID, thisDate, thisTime])


#ment to replace this block of code in reportPerMpnth and in reportForLate
def inputMonth():
    # if user enteres an unvalid value, loop repeats, or user can choose to exit
    valid_ID = False
    while valid_ID == False:
        try:
            month = int(input("enter the month you want a report for"))
        except ValueError:
            print("month must be a whole number between 1 and 12")
        else:
            if 0 < month < 13:
                #valid_ID = True
                return month
                break
            else:
                print("month input must be between 1 and 12")
                user_choice = int(input("to enter different month, enter 13, to exit enter 14"))
                #if any number other then 14 is chosen, it still restarts the loop. Dosn't seem like a problem so I didn't fix.
                if user_choice == 13 :
                    continue
                if user_choice == 14:
                    return user_choice
                    break


#reportForSingleID()
#markAttendance()
#reportForMonth()
#reportForLate()
