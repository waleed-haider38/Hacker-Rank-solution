def closure(x , y):
    def inner():
        # print("Assalam o Alaikum!")
        return x + y
    return inner
x = 4 
y = 5
sum = closure(x , y)
# print(sum())

def add_count(count):
    def inner_count():
        nonlocal count
        count +=1
        return count
    return inner_count
count = 0
counter = add_count(count)
# print(counter())

def multi_plier(x):
    def final_multi_plier(n):
        return x *n
    return final_multi_plier

times3 = multi_plier(3)
# print(times3(32))

def make_power(exp):
    def cube(num):
        return num ** exp
    return cube

square = make_power(3)
print(square(4))