arr = [7, 7, 2, 2, 3, 5, 1, 6, 3, 4]

def most_frequent(arr):
    counter = 0
    dominant = []

    for i in arr:
        curr_frequency = arr.count(i)

        if curr_frequency >= counter:
            counter = curr_frequency
            dominant.append(i)

    dominants = []

    for one_dominant in dominant:
        if one_dominant not in dominants:
            dominants.append(one_dominant)

    print(dominants)

most_frequent(arr)

