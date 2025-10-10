# ye technique choti queries k liye thk ha lekin jb queries zyada hu jay gi to is solution ko apply krna possible ni rhy ga
# n = 5
# arr = [0] * n
# print(arr)

# a , b , k =  1, 2 , 100

# for i in range(a-1 , b):
#     arr[i] += k

# print(arr)

# c , d , p = 2 , 5 , 100

# for i in range(c-1 , d):
#     arr[i] +=p

# print(arr)

# e , f , g =  3 , 4, 100

# for i in range(e-1 , f):
#     arr[i] += g

# print(max(arr))
# ----------------******************---------------
# ab agli technique dekhty ha ju bri queries ko handle kr sky
n = 5
arr = [0] * (n + 1)
print(arr)

a , b, k = 1 , 2, 100
arr[a-1] += k
arr[b] -= k

diff_arr = arr
final_arr = [0] *n 
current = 0
for i in range(n):
    current += diff_arr[i]

    final_arr[i] += current

print(final_arr)
