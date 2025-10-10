a = 5
range = [7 , 11]
b = [-2 , 1, 3]

for i in b:
    p = a + i
    print(f"The Position of apples are {p}")
    if p >=7 and p<=11:
        print("Apple fall in range")
    else:
        print("Apple does not fall in range")