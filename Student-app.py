#student object which has Students information, and ACTUAL student

#INSTANCE OF A CLASS, 

#from student import Student # from student file, import student class
from Student1 import Student # from student file, import student class

# create object for classs like you would a normal variable

#Student1 = Student("James", "Business", 3.1, False) #creating a student with respective fields
#Student2 = Student("Erin", "Art", 4.1, True) #creating a student with respective fields
#Student3 = Student("Tommy", "Mechanic", 2.8, False) #creating a student with respective fields

Student1 = Student("James", "Business", 3.1) #creating a student with respective fields
Student2 = Student("Erin", "Art", 4.1) #creating a student with respective fields
Student3 = Student("Tommy", "Mechanic", 2.8) #creating a student with respective fields


#print(Student2.is_on_probation)
print(Student2.on_honor_roll()) #class object function from class obj functions file
