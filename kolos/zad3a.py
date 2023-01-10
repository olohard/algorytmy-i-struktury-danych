arr = [1, 5, 7, 12, 2, 6]

max_value = arr[0]
min_value = arr[0]

for i in range(len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]

    if arr[i] < min_value:
        min_value = arr[i]

print(max_value - min_value)

