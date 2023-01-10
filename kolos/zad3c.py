import random
import time

arr = [x for x in range(10000)]

min_value = max(arr)

random.shuffle(arr)

start = time.time()

for i in range(len(arr)):
    for j in range(len(arr)):
        if abs(arr[i] - arr[j]) < min_value and arr[i] != arr[j]:
            min_value = abs(arr[i] - arr[j])

end = time.time()

print(end-start)

print(min_value)

# dla O(n^2) czas = 24.026705741882324 s