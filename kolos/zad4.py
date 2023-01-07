def dominant(A):
    x = None

    count = 0
    for i in A:
        if count == 0:
            x = i
            count += 1
        elif i == x:
            count += 1

    return x, count


print(dominant([1, 3, 3, 4, 9, 1, 1]))
print(dominant([1, 1, 4, 3, 4, 1, 1, 9]))