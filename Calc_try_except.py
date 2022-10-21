def calc(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div
try:
    user_input = int(input("Enter the first number: "))
    user_input_2 = int(input("Enter the second numbers: "))
    result = calc(user_input,user_input_2)
    print('Addition is', result[0])
    print('Subtraction is', result[1])
    print('Multiplication is', result[2])
    print('Division is', result[3])
except:
    print("Error: Invalid input")
    