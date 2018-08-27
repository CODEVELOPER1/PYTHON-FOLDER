#classes and object, allows us to create our own data types
# class define your own data type

class Student: #overview of what the student value really is, representing a student, student data type, can use strings, int, bool's
    
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        
         
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


