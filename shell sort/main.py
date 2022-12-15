import random

arr = [x for x in range(100)]
random.shuffle(arr)
print('Przetasowana tablica: ')
print(arr)

def shell_sort(array, n):
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


shell_sort(arr, len(arr))
print('Posortowana tablica: ')
print(arr)