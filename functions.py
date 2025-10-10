def even_odd(nmb):
    if nmb % 2 == 0:
        print("This Number is an Even Number")
    else:
        print("This Number is an Odd Number")

# print(even_odd(11))

def factorial(nmb):
    fact = 1
    for i in range(1 , nmb+1):
        fact = fact * i
    
    print(f"The Factorial of {nmb} is: {fact}")

# print(factorial(5))

def palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        print(f"{string} is Palindrome")
    else:
        print(f"{string} is not Palindrome")

# our_str = palindrome("level")

def max_min(numbers):
    return max(numbers) , min(numbers)

lis = [14, 56, 75, 32,11 , 32]

maximun_min_number = max_min(lis)
# print(maximun_min_number)

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():   # lowercase me check karna easy hai
        if char in vowels:
            count += 1
    return count

vowels_count = count_vowels("Hi I am Waleed")
# print(f"{vowels_count} Number of vowels in the string")

def remove_duplicates(lis):
    string = set()
    for i in lis:
        string.add(i)
    return string

num = [2 ,2, 1, 1, 3, 4,5,5,6,4]
remove = remove_duplicates(num)
# print(remove)

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def check_prime(lis):
    primes = []
    for i in lis:
        if is_prime(i):
            primes.append(i)
    return primes

nmbr = [12, 3, 5, 43, 27]
prime_number = check_prime(nmbr)
print(prime_number)
       
