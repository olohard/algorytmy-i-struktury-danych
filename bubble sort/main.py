import random

list1 = [x for x in range(2000)]

print("Przemieszana lista: ")
random.shuffle(list1)

def bubble_sort(option):
    flag = False

    if int(option) == 1:
        for i in range(len(list1)):
            for j in range(0, len(list1) - 1):
                flag = True
                if list1[j] < list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]

            if not flag:
                break

    elif int(option) == 2:
        for i in range(len(list1)):
            for j in range(0, len(list1) - 1):
                flag = True
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]

            if not flag:
                break
    else:
        print("Nie ma takiej opcji")


if __name__ == '__main__':
    print("Jak chcesz posortować zbiór?")
    print("1. Rosnąco")
    print("2. Malejąco")

    option = input("Podaj opcję: ")

    bubble_sort(option)


