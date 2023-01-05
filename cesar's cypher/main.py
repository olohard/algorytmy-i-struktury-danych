def cesar_cypher(mess, key):
    encrypted_mess = ""

    for letter in mess:
        encrypted = ord(letter) - key
        encrypted_mess += chr(encrypted)

    return encrypted_mess

if __name__ == '__main__':
    key = int(input("Podaj klucz: "))

    print('Podaj wiadomość do zaszyfrowania: ')

    mess = ""

    while True:
        a = input()

        if a == '1234':
            break

        mess += a

    print(cesar_cypher(mess, key))