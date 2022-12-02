queue = []
size = 100


def push_item(item):
    if len(queue) < size:
        queue.append(item)

    else:
        print("Nie można dodać elementu do pełnej kolejki")


def pop_item(param):
    if len(param) > 0:
        param.pop()

    else:
        print("Nie można usunąć elementu z pustej kolejki.")


def check_if_queue_is_full():
    if len(queue) == size:
        print("Kolejka jest pełna.")

    else:
        print("Kolejka nie jest pełna.")


def check_if_queue_is_empty():
    if len(queue) <= 0:
        print("Kolejka jest pusta.")

    else:
        print("Kolejka nie jest pusta.")


if __name__ == "__main__":
    print("Wybierz jedną z opcji:")
    print("1. Wyjście")
    print("2. Dodaj element")
    print("3. Usuń element")
    print("4. Sprawdź, czy kolejka jest pełna")
    print("5. Sprawdź, czy kolejka jest pusta")
    print("6. Wyświetl elementy kolejki")
    print("7. Wyświetl pierwszy element kolejki")
    print("8. Wyświetl ostatni element kolejki")


    while True:
        a = input("Opcja: ")

        if a == "1":
            break

        if a == "2":
            b = input("Podaj element do dodania: ")
            push_item(b)

        if a == "3":
            b = queue[::-1]
            pop_item(b)
            queue = b[::-1]

            print(queue)

        if a == "4":
            check_if_queue_is_full()

        if a == "5":
            check_if_queue_is_empty()

        if a == "6":
            print(queue)

        if a == "7":
            print(queue[0])

        if a == "8":
            print(queue[::-1][0])

