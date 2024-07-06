import os 
clear = lambda :os.system("clear")

def Calcultor(operation, a,b):
    for i in operation:
        if operation =='add' or operation == '+':
            return a+b
        elif operation == 'subtract' or operation== '-':
            return a-b
        elif operation == 'multiply' or operation=='*':
            return a*b
        elif operation=='divide' or operation=='/':
            return a/b
        

start_again = True
while start_again:
    pick1 = float(input("Enter first number: "))
    operation = input("Enter the operation: ")
    pick2 = float(input("Enter second number: "))
    print(Calcultor(operation,pick1,pick2))
    if input(f"press y to start again and n to stop?")=='y':
        continue

    else:
         break
        
