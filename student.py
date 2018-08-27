#classes and object, allows us to create our own data types
# class define your own data type

class Student: #overview of what the student value really is, representing a student, student data type, can use strings, int, bool's
    
    def __init__(self, name, major, gpa, is_on_probation): #values are being store via init function "__init__(self):"
        #basically map out what attributes a student can have, SELF representing the student, SELF is the STUDENT OBJECT via Student-app.py
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
