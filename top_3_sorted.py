from collections import Counter

n = input()

cleaned = [ch for ch in n if ch.isalpha()]
print(cleaned)

# print(n)

freq = Counter(cleaned)
# test = Counter("bnana")

# print(test)
# print(freq.most_common(3))

for key,cnt in freq.most_common(3):
    print(key,":",cnt)
    

    