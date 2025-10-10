# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x+y
#         yield x

# def square(nums):
#     for num in nums:
#         yield num**2

# print(sum(square(fibonacci_numbers(10))))

# # Output: 4895
def even_number(n):
    for i in range(1 , n+1):
        yield i*i


print(list(even_number(10)))