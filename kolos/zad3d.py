arr = [0, 3, 8, 12]

counter = -2
difference = max(arr)

for i in range(len(arr)):
    counter += 1
    if abs(arr[counter] - arr[i]) < difference and arr[counter] != arr[i]:
       difference = abs(arr[counter] - arr[i])

print(difference)