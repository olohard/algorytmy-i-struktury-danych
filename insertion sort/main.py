import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = [x for x in range(100)]
random.shuffle(arr)
print("Przetasowana lista: ", arr)

insertion_sort(arr)

print("Posortowana lista: ", arr)

