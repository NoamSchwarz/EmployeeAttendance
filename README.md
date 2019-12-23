# EmployeeAttendance
This is a system designed to track employees of a company.
Employees can enter their arrival 
Employers can manage a list of current employees, add/delete employees manually or by csv file, and generate reports on 
employee arrival times.
Employess exit times tracking isn't in the programm at this time. 

Prerequisites
You have installed python 3.6 or the latest version
You have installed a code editor to run the project files on. The project does not have a GUI at the
moment and is run through the code editor.

Using Employee Attendance
The project does not have a GUI at the moment and is run through the code editor or IDE. 

In order to use the functions, 4 csv files must exist in the project directory:
current _employees.csv
new_employess.csv
delete_employees.csv
Employee_attendance.csv (can be empty except for column heads)

The first row is the heading of each column, and should be in this order:
ID, name, phone, age
Example files can be found in the repository.

To use each function in employeeFunctions.py ,run the function in the code editor.
In case of incorrect input in the new_employees.csv or delete_employees.csv files, follow the instructions,
and then run again with the corrected files.
The programs will skip data that has already been entered in the first run.  

To use each function in reportFuncions.py, run the function in the code editor and enter data using the keyboard when asked for it.
The reports will appear in the project directory.
