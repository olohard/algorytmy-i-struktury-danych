def build_tab(patt):
    arr_len = len(patt) + 1
    arr = [0] * arr_len
    pos = arr[0] = -1

    for i in range(1, arr_len):
        while pos > -1 and patt[pos] != patt[i - 1]:
            pos = arr[pos]
        pos += 1

        if i == arr_len - 1 or patt[i] != patt[pos]:
            arr[i] = pos
        else:
            arr[i] = arr[pos]
    return arr


def knuth_morris_pratt(txt, patt):
    tab = build_tab(patt)
    dop = 0
    final_idx = -1

    for index, sign in enumerate(txt):
        while dop > -1 and patt[dop] != sign:
            dop = tab[dop]
        dop += 1

        if dop == len(patt):
            final_idx = index - len(patt) + 1
            break

    return final_idx


if __name__ == '__main__':
    print("Podaj tekst: ")
    txt = ""
    while True:
        a = input()

        if a == "1234":
            break

        txt += a

    patt = input("Podaj wzorzec do wyszukania: ")

    print(knuth_morris_pratt(txt, patt))
