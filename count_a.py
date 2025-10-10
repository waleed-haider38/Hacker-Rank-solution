s = "abaaa"
len_s = len(s)
n = int(input("Enter the Number: "))

f = n // len(s)
print("Full repeats of String",f)
print("Length of String",len_s)

remainder = n % len_s

slic = s[:remainder]

print("Remainder String",remainder)

count = 0
for x in slic:
    if x == "a":
        count +=1
    
print(count)