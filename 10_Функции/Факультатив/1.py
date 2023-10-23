def main(x):
    print(x)

def countL():
    type_letter = "аеоюэяыиуАЕОЮЭЯЫИУ"
    count = 0
    str1 = input("Введите строку: ")
    for x in str1:
        if x in type_letter:
            count += 1
    return count
main(countL())