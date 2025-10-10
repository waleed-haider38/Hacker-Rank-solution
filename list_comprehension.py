number = [n for n in range(1 , 11)]
# print(number)

square_nmb = [num * num for num in number]

# print(square_nmb)

odd_nmbr = [n*n for n in range(1 , 20) if n % 2 == 1]

# print(odd_nmbr)

even_number  = [n for n in range(1 , 20 ) if n % 2 == 0]

# print(even_number)

pyth = "python"
n = pyth
upper_pyth = [n.upper() for n in pyth]

print(upper_pyth)

num = [10 , 20, 30, 40, 50]

double_num = [n * 2 for n in num]

# print(double_num)

aoa = "hello world"

# vowel = [n for n in aoa if n == "aeiou"]

# print(vowel)

for s in aoa:
    if s == "aeiou":
        print(s)
