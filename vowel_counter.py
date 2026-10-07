total = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

word = input("Enter a word: ").lower()

for character in word:    
    if character == "a":
        a_count += 1
    elif character == "e":
        e_count += 1
    elif character == "i":
        i_count += 1  
    elif character == "o":
        o_count += 1  
    elif character == "u":
        u_count += 1      

print(f"\nVowel Counts for {word}:")
print(f"a: {a_count}")
print(f"e: {e_count}")
print(f"i: {i_count}")
print(f"o: {o_count}")
print(f"u: {u_count}")

total = a_count + e_count + i_count + o_count + u_count    
print(f"There are {total} vowels in {word}")

# Modify your program to count each vowel separately. Uppercase and lowercase vowels should count together.

# Vowel counts for Education:
# A: 1
# E: 1
# I: 1
# O: 1
# U: 1
# Total vowels: 5

