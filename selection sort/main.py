import random


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [x for x in range(100)]

random.shuffle(arr)
print("Przetasowana lista: ", arr)

selection_sort(arr)

print("Posortowana lista: ", arr)
