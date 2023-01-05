from queue import PriorityQueue

if __name__ == '__main__':
    prio_queue = PriorityQueue()

    print("1.Dodaj element")
    print("2.Usuń wszystkie elementy i wyświetl je")
    print("3.Wyjscie z programu")

    while True:
        wybor=input("Wybierz: ")

        if wybor=='1':
            x=float(input("Podaj liczbę do wpisania do kolejki: "))
            y=int(input("Podaj priorytet elementu: "))
            prio_queue.put((x, y))

        if wybor=='2':

            print(prio_queue.get())

        if wybor=='3':
            break

        if wybor!='1' and wybor!='2' and wybor!='3' and wybor !='4':
            print("Nie wybrano poprawnej opcji z menu!")