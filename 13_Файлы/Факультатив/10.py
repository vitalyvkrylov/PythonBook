vowels = 'AEIOUaeiou'
vowel_count = 0
consonant_count = 0
with open('10.txt', 'r') as file:
    for line in file:
        for char in line:
            if char in vowels:
                vowel_count += 1
            elif char.isalpha():
                consonant_count += 1
result = consonant_count - vowel_count
print(consonant_count)
print(vowel_count)
print(result)