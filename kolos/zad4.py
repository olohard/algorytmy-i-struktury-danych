arr = [5, 2, 2, 3, 5, 3, 6, 4]

def dominant_finder(arr):
    some_arr = []
    dominant = {}
    dominants = []

    for i in arr:
        dominant[i] = arr.count(i)
        some_arr.append(dominant[i])

    max_amount = max(some_arr)

    for i in dominant:
        if max_amount == dominant[i] and i != max(dominant) and i != min(dominant):
            dominants.append(i)

    print(dominant)
    print(dominants)

dominant_finder(arr)

