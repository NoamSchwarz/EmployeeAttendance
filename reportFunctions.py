import time
import datetime
import csv
import employeeFunctions

employee_attendance_file = "employee_attendance.csv"
current_employee_file = "current_employees.csv"

def mark_attendance():

    valid_ID = False
    while valid_ID == False:
        ID = employeeFunctions.input_ID()

        current_time = time.strftime("%H:%M")
        current_date =  datetime.datetime.today().strftime('%d.%m.%y')
        print(current_time)
        print(current_date)

        # if the ID entered DOES exists in current employees file, mark attendance and exit loop
        temp_emp = employeeFunctions.Employee(ID, "a", 0, 0)
        if temp_emp.check_ID(current_employee_file):
            valid_ID = True
            print("ID accepted")

            with open(employee_attendance_file, 'a',newline="") as time_file:
                writer = csv.writer(time_file, delimiter=',')
                writer.writerow([ID,current_date, current_time])
        else:
            print("the ID you entered is not in the current employees file")
            user_choice = input("to enter different ID, enter 1, to exit enter 2")
            if user_choice == '2':
                valid_ID = True


#generates csv with date and time, acording to ID of one employee.
def report_for_single_ID():

    valid_ID = False
    while valid_ID == False:
        try:
            emp_ID = int(input("enter employee ID"))
        except ValueError:
            print("employee ID must be a whole number")
        else:
            new_file_name = 'reprot_for_empID_{}.csv'.format(emp_ID)
            temp_emp = employeeFunctions.Employee(emp_ID, "a", 0, 0)

            if temp_emp.check_ID(current_employee_file):
                valid_ID = True
                print("ID accepted")
            else:
                print("the ID you entered is not in the current employees file")
                #user can enter anthing that isn't 2 and it will still go back to asking for ID. I Don't fell the need to change this.
                user_choice = input("to enter different ID, enter 1, to exit enter 2")
                if user_choice == '2':
                   return

    #add headers to employee report file
    with open(new_file_name, 'w',newline="") as report_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_writer.writerow(['ID',"date", 'time'])

    with open(new_file_name, 'a',newline="") as report_file, open(employee_attendance_file, 'r') as time_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_reader = csv.reader(time_file, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[0] == str(emp_ID):
                    ID = row[0]
                    this_date = row[1]
                    this_time = row[2]
                    csv_writer.writerow([ID, this_date, this_time])


def report_for_month():

    month = input_month()
    if month == 14:
        return

    # add headers to monthly attendance report file
    new_file_name = 'reprot_for_month_{}.csv'.format(month)
    with open(new_file_name, 'w', newline="") as report_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_writer.writerow(['ID', "date", 'time'])

    with open(new_file_name, 'a', newline="") as report_file, open(employee_attendance_file, 'r') as time_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_reader = csv.reader(time_file, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                temp_date = str(row[1])
                date_list = temp_date.split('.')
                if int(date_list[1]) == month:
                    ID = row[0]
                    this_date = row[1]
                    this_time = row[2]
                    csv_writer.writerow([ID, this_date, this_time])

def report_for_late_employees():

    month = input_month()
    if month == 14:
        return

    # add headers to monthly attendance report file
    new_file_name = 'late_reprot_for_month_{}.csv'.format(month)

    with open(new_file_name, 'w', newline="") as report_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_writer.writerow(['ID', "date", 'time'])

    with open(new_file_name, 'a', newline="") as report_file, open(employee_attendance_file, 'r') as time_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        csv_reader = csv.reader(time_file, delimiter=',')

        line_count = 0
        for row in csv_reader:
            # skip column headers
            if line_count == 0:
                line_count += 1
            else:
                temp_date = str(row[1])
                date_list = temp_date.split('.')
                temp_time = str(row[2])
                #changed ':' to "." so that number can used as float for comparison
                time_float = float(temp_time.replace(':','.'))

                if int(date_list[1]) == month and time_float > 9.30 :
                    ID = row[0]
                    this_date = row[1]
                    this_time = row[2]
                    csv_writer.writerow([ID, this_date, this_time])


def input_month():
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


#report_for_single_ID()
#mark_attendance()
#report_for_month()
report_for_late_employees()
