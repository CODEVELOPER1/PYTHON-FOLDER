#classes and object, allows us to create our own data types
# class define your own data type

class Student: #overview of what the student value really is, representing a student, student data type, can use strings, int, bool's
    
    def __init__(self, name, major, gpa, is on probation): #__init__(self): basically map out what attributes a student can have, SELF representing the student
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is on probation = is on probation
        
        
#student object which has Students information, and ACTUAL student

from student import Student # from student file, import student class

# create object for classs like you would a normal variable

Student1 = Student("James", "Business", 3.1, False) #creating a student with respective fields
Student2 = Student("Erin", "Art", 4.1, True) #creating a student with respective fields
Student3 = Student("Tommy", "Mechanic", 2.8, False) #creating a student with respective fields

print(Student2.is_on_probation)



# DO NOT RUN

#DO NOT RUN

# DO NOT RUN

##IS A REFERENCE PAGE FOR BELOW APP


# LOOK AT STUDENT AND STUDENT-APP.PY TO WORK PROGRAM APP