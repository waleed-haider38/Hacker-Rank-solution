# strings = ["cat", "dog", "cat", "bird"]
# query = "cat"

# count = 0

# for i in strings:
#     if i == "cat":
#         count +=1

# print(count)

strings = ["cat", "dog", "cat", "bird"]
queries = ["dog", "cat", "fish"]
# Method no 1 to count the queries in string and it is lengthi 



# dog_count = 0
# cat_count = 0
# fish_count = 0

# for i in strings:
#     if i == "cat":
#         cat_count +=1
#     elif i == "dog":
#         dog_count +=1
#     elif i == "fish":
#         fish_count +=0

# print("Dog" , dog_count)
# print("Cat", cat_count)
# print("Fish", fish_count)

# ------------------******************----------------------
# Method no 2 to count the queries from the string

result = []
for q in queries:
    count = 0
    for s in strings:
        if s == q:
            count +=1

    result.append(count)

print(result)
