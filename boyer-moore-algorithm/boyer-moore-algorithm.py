_chars = 256

def chars(string, size):
    arr = [-1] * _chars

    for i in range(size):
        arr[ord(string[i])] = i

    return arr

def boyer_moore(txt, patt):

    m = len(patt)
    n = len(txt)

    char = chars(patt, m)

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and patt[j] == txt[s + j]:
            j -= 1

        if j < 0:
            print(f"Wzorzec jest na pozycji = {s}")
            s += (m - char[ord(txt[s + m])] if s + m < n else 1)

        else:
            s += max(1, j - char[ord(txt[s + j])])

if __name__ == '__main__':
    print("Podaj tekst: ")
    txt = ""
    while True:
        a = input()

        if a == "1234":
            break

        txt += a

    patt = input("Podaj wzorzec do wyszukania: ")

    print(boyer_moore(txt, patt))