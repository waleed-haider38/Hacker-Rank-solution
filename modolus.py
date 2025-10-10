import math
n = complex(input("Enter a complex number (like 3+4j): "))

x = n.real
y = n.imag

z = x**2 + y**2

modulus =  math.sqrt(z)
print("The Modulus of function is: ",modulus)
print(n)