def calculation(x, y, operator):

    if operator == '+': 
        
        total = x + y 
        return total
    
    elif operator == '-':
        
        total = x - y
        return total
    elif operator == 'x':

        total = x * y

        return total
    
    elif operator == '/':
        total = x / y 
        return total
    
    num1 = float(input("please enter a number: "))
    num2 = float(input("please enter a number: "))

ops = ['+', '-', '*', '/']

while True:
    operator = input("Enter the math symbol you would like to use:")
    
    if operator not in ops:
        print('''Your selected operator is  not valid.
            Please use one of the following symbols:
            +(addition), -(subtraction), x(multiplication), /(division)''')
        
    else:
        print ("That's right")

        #trying to new make edits to make a pull request