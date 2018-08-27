#python read command, allows to read files outside of python files
#read, open, closing files

employee_file = open("employees.txt","r")#open file (file, mode )modes -r = read, w = write, a = append, r+ = read and write, a = add)
#store open file into var
#print(employee_file.readable())#allows us to see if file is readable
#print(employee_file.read())#allows us to see if file is readable
##print(employee_file.readline())#allows us to see if file is readable
for employee in employee_file.readlines():
   # print(employee_file.readlines()[1])#allows us to see if file is readable
   print(employee)
employee_file.close() #close function

