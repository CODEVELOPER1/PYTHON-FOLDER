from Chef import Chef #inherit attributes from one class into another class, and can still overide attributes

class ChineseChef(Chef): #can use all function contained inside the Chef class rather than having to copy and pass like below

   # def make_chicken(self):
 #       print("The chef makes a chicken")
              
 #   def make_salad(self):
 #       print("The chef makes a salad")
              
    def make_special_dish(self):
        print("The Chinese Chef makes Orange Chicken")
        
    def make_fried_rice(self):
        print("The Chinese Chef makes Fried Rice")
