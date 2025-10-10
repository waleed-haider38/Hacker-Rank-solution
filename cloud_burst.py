# Task 2: Take input of clouds and length

# pehle length input lo
n = int(input("Enter number of clouds: "))

# ab clouds ka array input lo
c = list(map(int, input("Enter clouds (0 safe, 1 thunder): ").split()))

# dono print kar do
# print("Length of array:", n)
# print("Clouds:", c)
jumps = 0
for x in c:
    if[x + 2] == 0:
        jumps +=1
    else:
        jumps = [x+1]
    
print("Minimum Jumps: ",jumps)