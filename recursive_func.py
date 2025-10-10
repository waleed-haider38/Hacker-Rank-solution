def print_numbers(n):
    if n == 0:   # Base case (jab n=0 ho to ruk jao)
        return
    print_numbers(n-1)   # Pehle chhota kaam karo
    print(n)             # Phir current number print karo

# print_numbers(5)

def count_numbers(n):
    if n == 0:
        return
    print(n)
    return count_numbers(n-1)

# count_numbers(5)

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)

n = int(input("Enter the Number to find the factorial: "))

factorial = recursive_factorial(n)
# print(f"The factorial of number is: {factorial}")

def sum_digits(n):
    if n == 0:   # base case
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

# Example
print(sum_digits(1234))   # Output: 10
