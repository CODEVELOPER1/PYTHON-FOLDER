#when we call the function we want to retrieve info back
#allow python to return info from a function
#can not execute code directly after the Return keyword

def cube(num):#cubing a number funtction
    return num*num*num #going to return the value of what's called in the function
    
result = cube(4)
print(result)
