filename = '9.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
    punctuation = [',', '.', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}']
    num_punctuations = 0
    for line in lines:
        for char in line:
            if char in punctuation:
                num_punctuations += 1
                print(char)
                new_line = ''.join(['@' if char in punctuation else char for char in line])
                print(new_line)
                print(f'Количество знаков препинания в файле: {num_punctuations}')