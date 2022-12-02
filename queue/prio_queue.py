kolejka=[]
prio=[]

def dodaj(elem,p):
    if len(prio)==0:
        prio.insert(0,p)
        kolejka.insert(0,elem)
    elif p >= prio[len(prio) - 1]:
        prio.append(p)
        kolejka.append(elem)
    else:
        for x in range(len(prio)):
            if p<prio[x]:
                prio.insert(x,p)
                kolejka.insert(x,elem)
                break


def usun():
    if(len(prio)==0):
        print("Kolejka jest pusta!")
    else:
        kolejka.pop(0)
        prio.pop(0)

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