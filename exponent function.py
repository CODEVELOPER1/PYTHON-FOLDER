#allow us to take a certain number and raise it to it's power

#print(2**3)

def raised_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raised_to_power(5, 6))