class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i

            item = self.queue[max_val]
            del self.queue[max_val]

            return item

        except IndexError:
            print()
            exit()


if __name__ == '__main__':

    print("1.Dodaj element")
    print("2.Usuń element")
    print("3.Wyswietl kolejkę")
    print("4.Wyjscie z programu")

    while True:
        wybor=input("Wybierz: ")

        if wybor=='1':
            x=float(input("Podaj liczbę do wpisania do kolejki: "))
            y=int(input("Podaj priorytet elementu: "))
            dodaj(x,y)

        if wybor=='2':
            usun()

        if wybor=='3':
            print(kolejka)

        if wybor=='4':
            break
        if wybor!='1' and wybor!='2' and wybor!='3' and wybor !='4':
            print("Nie wybrano poprawnej opcji z menu!")