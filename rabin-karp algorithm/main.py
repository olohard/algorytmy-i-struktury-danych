def search(pattern, text, q):
    patt_len = len(pattern)
    text_len = len(text)
    p = 0
    t = 0
    h = 1
    j = 0

    for i in range(patt_len-1):
        h = (h*d) % q

    for i in range(patt_len):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    for i in range(text_len-patt_len+1):
        if p == t:
            for j in range(patt_len):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == patt_len:
                print("Pattern is found at position: " + str(i+1))

        if i < text_len-patt_len:
            t = (d*(t-ord(text[i])*h) + ord(text[i+patt_len])) % q

            if t < 0:
                t = t+q


if __name__ == '__main__':
    print("Podaj tekst:")

    text = ''

    while True:
        a = input()

        if a == "1234":
            break

        text += (a + " ")

    print(text)

    d = 256

    patt = input("Podaj ciąg znaków do wyszukania: ")
    search(patt, text, 13)