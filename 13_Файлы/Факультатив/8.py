filename = "8.txt"
with open(filename, "r") as f:
    lines = f.readlines()
print(f"Количество строк в файле {filename}: {len(lines)}")
vowels = "aAeEiIoOuU"
num_vowels = 0
for line in lines:
    for char in line:
        if char.lower() in vowels:
            num_vowels += 1
print(f"Количество гласных букв в файле {filename}: {num_vowels}")



