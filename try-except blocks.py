


try:
 #   answer = 10/0 # equation
    number = int(input("Please enter a number: ")) #user input
    print(number) #prints user number
#except ZeroDivisionError as err: #determines err message
    #print(err) #prints err message
except ValueError: #invalid value
    print("Invalid Error") #invalid value message