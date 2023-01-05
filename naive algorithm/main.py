def search(text, patt):
    text_len = len(text)
    patt_len = len(patt)
    counter = 0

    for i in range(text_len-patt_len+1):
        if text[i] == patt[0]:
            if text[i:i + patt_len] == patt:
                print(f"Znaleziono: | {text} | {patt} | {i}")
                counter += 1

    if counter == 0:
        print(f"Nie znaleziono wzorca: {patt} w tekście {text}")

    else:
        print(f"Wzorzec znaleziono: {counter} razy")


if __name__ == '__main__':
    print("Podaj tekst:")

    text = ''

    while True:
        a = input()

        if a == "1234":
            break

        text += (a + " ")

    print(text)

    patt = input("Podaj ciąg znaków do wyszukania: ")
    search(patt, text)


open("plik.txt")