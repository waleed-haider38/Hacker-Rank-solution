# name = "121"
# reverse_name = name[::-1]
# if name == reverse_name:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")


sentence  = input("Enter the sentence: ")
count = 0
for s in sentence.lower():
    if s in 'aeiou':
        count +=1
    
print(f"The numbers of vowels in your sentence are {count}")