n = 10
a = 0
b = 1

# print("Fibonacci Series: ")
# for i in range(n):
#     print(a , end=" ")
#     a , b = b , a + b

# n = int(input("Enter the Number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print(f"The Factorial is {fact}")

# string = input("Enter the String: ")
reverse = ""
# for i in string:
#     reverse = i + reverse

# print(reverse)

# numb = input("Enter the Number: ")

total = 0
# for i in numb:
#     new_int = int(i)
#     total = total + new_int

# print(total)

for num in range(2 , 51):
    is_prime = True
    for i in range(2 , num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"The Prime Number is {num}")