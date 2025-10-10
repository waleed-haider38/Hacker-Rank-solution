# n = [66 , 74 , 89]
# sum  = 0
# for i in n:
#     sum += i
#     avg = sum / 3

# print(avg)

students = {
    'Waleed': [90 , 89 , 94],
    'Sara': [90 , 81 , 93]
}
person = students['Sara']
print("Sara marks from subjects are: ",person)
sum = 0
for i in person:
    sum += i

avg = sum / 3
avg_marks=round(avg , 2 )
print(f"The average of sara marks is: {avg_marks}")
# print(students["Waleed"])

