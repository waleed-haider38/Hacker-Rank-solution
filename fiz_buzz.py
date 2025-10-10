# for i in range(1 , 100+1):
#     if i % 3 == 0 and i % 5 == 0 :
#         print("Fizzz Buzzz")
        
#     elif i % 5 == 0:
#         print("Buzzzzzz")
#     elif i %3 == 0:
#           print("Fizzzzzzzzz")  
#     else:
#         print(i)

# n = int(input("Enter a table Number: "))

# for i in range(1 , 10+1):
#     print(f"{n} * {i} = {n * i}")

# for i in range(1 , 10+1):
#     print(i)

# for i in range(1 , 20+1):
#     if i % 2 == 0:
#         print(f"Event Number are {i}")



# for i in n:
#     print(i)

n = input("Enter the string: ")
count = 0
for i in n:
    if i in "aeiou":
        count +=1

print(f"There are {count} vowels in your string")       


for i in range(1 , 10+1):
    print(f"Square of each number is {i*i}")

lis = [2 ,3, 5, 6,7]

for i in lis:
    print(f"The double of list character is {i+i}")