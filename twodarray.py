arr = [[] , []]
 
print(arr)

x = 5  
lastAnswer = 0 
n = 2 
y = 5
idx = (x ^ lastAnswer) % n

print(idx)
arr[idx].append(y)

print(arr)