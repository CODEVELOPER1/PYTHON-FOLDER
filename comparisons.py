def max_num(num1, num2, num3): #passing 3 numbers and the function will return the largest of the 3
    if num1 != num2 and num1 >= num3: #bool statement
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(10,450,564))
