class Stack(list):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def push_item(self, item):
        if len(self) < self.size:
            self.append(item)

        else:
            print("Nie można dodać elementu do pełnego stosu")

    def pop_item(self):
        if len(self) > 0:
            self.pop()

        else:
            print("Nie można usunąć elementu z pustego stosu.")

    def check_if_stack_is_full(self):
        if len(self) == self.size:
            print("Stos jest pełny.")

        else:
            print("Stos nie jest pełny.")

    def check_if_stack_is_empty(self):
        if len(self) <= 0:
            print("Stos jest pusty.")

        else:
            print("Stos nie jest pusty.")


if __name__ == "__main__":
    stack = Stack(100)

    while True:
        print("Wybierz jedną z opcji:")
        print("1. Wyjście")
        print("2. Dodaj element")
        print("3. Usuń element")
        print("4. Sprawdź, czy stos jest pełny")
        print("5. Sprawdź, czy stos jest pusty")
        print("6. Wyświetl elementy stosu")

        a = input("Opcja: ")

        if a == "1":
            break

        if a == "2":
            b = input("Podaj element do dodania: ")
            stack.push_item(b)

        if a == "3":
            stack.pop_item()

        if a == "4":
            stack.check_if_stack_is_full()

        if a == "5":
            stack.check_if_stack_is_empty()

        if a == "6":
            print(stack)

        else:
            print("Nie ma takiej opcji!")
            continue