arr = [2, 4, 5, 6]
A = {2, 6}
B = {5}
# set_a = list(A)
# set_b = list(B)

happiness = 0
# print(set_a)
# print(set_b)
# for i in arr:
#     print(i)

# for j in A:
#     print(j)

for i in arr :
    if i in A:
        happiness +=1
    elif i in B:
        happiness -=1
    else:
        happiness = 0

print(happiness)