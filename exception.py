# Enter your code here. Read input from STDIN. Print output to STDOUT
try:
    x = int(input("Enter the 1st Number: "))
    y = int(input("Enter the 2nd Number: "))
    
    z = x /y
    print("Result: ", z)
except ZeroDivisionError as e:
    print("Error Code: ", e)
except ValueError as e:
    print("Error Code: ",e)