# a = " 5 5 5 2 4 1 3 4 2 3 1"
# lis = a.split()
# print(lis)

# newlis = list(map(int , lis))
# print(newlis)

# set_list = set(newlis)
# print(set_list)
# set_list.add(6)
# set_list.discard(5)
# set_list.remove(1)
# print(set_list)

# set_list.update([7 , 8])

# print(set_list)

nums = [1, 2, 2, 3, 4, 4, 5]

unique_set = set()

for n in nums:
    unique_set.add(n)

# print(unique_set)

countries = ["UK", "China", "USA", "France", "New Zealand", "UK", "France"]
country_set = set()

for c in countries:
    country_set.add(c)

# print(len(country_set))

English = {101, 102, 103, 104}
French  = {103, 104, 105, 106, 107}

print(English.union(French))
print(len(English.union(French)))

    