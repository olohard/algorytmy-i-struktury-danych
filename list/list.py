class Element:
    def __init__(self, wartosc=None, nastepny_elem=None):
        self.wartosc = wartosc
        self.nastepny_elem = nastepny_elem


class Lista:
    def __init__(self):
        self.glowa = None

    def dodaj(self, wartosc):
        nowy_element = Element(wartosc)
        if self.glowa:
            aktualny_element = self.glowa

            while aktualny_element.nastepny_elem:
                aktualny_element = aktualny_element.nastepny_elem

            aktualny_element.nastepny_elem = nowy_element

        else:
            self.glowa = nowy_element

    def wypisz(self):
        aktualny_element = self.glowa
        lista = []

        while aktualny_element:
            lista.append(aktualny_element.wartosc)
            aktualny_element = aktualny_element.nastepny_elem

        print(lista)

    def usun(self, wartosc):
        aktualny_elem = self.glowa

        while aktualny_elem.wartosc != wartosc:
            aktualny_elem = aktualny_elem.nastepny_elem

        if aktualny_elem.wartosc == wartosc:
            aktualny_elem.wartosc = aktualny_elem.nastepny_elem.wartosc
            aktualny_elem.nastepny_elem = aktualny_elem.nastepny_elem.nastepny_elem


lista = Lista()

print("LISTA JEDNOKIERUNKOWA")
print("1. Zakończ program")
print("2. Dodaj element do listy")
print("3. Usuń element z listy")
print("4. Wypisz listę")

while True:
    a = input("Wybierz opcję: ")

    if a == "1":
        break

    elif a == "2":
        b = input("Podaj element do dodania: ")
        lista.dodaj(b)

    elif a == "3":
        b = input("Podaj element do usunięcia: ")
        lista.usun(b)

    # elif a == "4":
    #     b = input("Podaj element do usunięcia o zadanym indeksie: ")
    #     lista.usun_index(b)

    elif a == "4":
        lista.wypisz()

    else:
        print("Nie ma takiej opcji!")