NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS

    for i in range(size):
        badChar[ord(string[i])] = i

    return badChar

def boyer_moore(txt, patt):

    m = len(patt)
    n = len(txt)

    badChar = badCharHeuristic(patt, m)

    s = 0
    while s <= n-m:
        j = m-1

        while j>=0 and patt[j] == txt[s+j]:
            j -= 1

        if j<0:
            print(f"Wzorzec znajduje się na pozycji = {s}")
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)

        else:
            s += max(1, j-badChar[ord(txt[s+j])])

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