# s = [ 1 , 5, 3, 7, 4, 6]

# k = int(input("Enter the Number: "))
# remainder = []
# for x in s:
#     divide = x % k
#     remainder.append(divide)

# print("The remainder of array are: ", remainder)

s = [ 1 , 5, 3, 7, 4, 6]
k = 3
for i in range(len(s)):
    for j in range(i + 1 , len(s)):
        a = s[i]
        b = s[j]
        if (a % k + b % k) % k == 0:
            print(f"{a} and {b} are divisible by value of K")
        else:
            print(f"{a} and {b} are not divisible by value of K")