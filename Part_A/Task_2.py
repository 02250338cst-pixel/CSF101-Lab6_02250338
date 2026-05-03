import math

lst = [5, 10, 15, 20, 25, 30]
key = int(input("Enter element: "))

n = len(lst)
step = int(math.sqrt(n))
prev = 0

while lst[min(step, n) - 1] < key:
    prev = step
    step += int(math.sqrt(n))
    if prev >= n:
        print("Element not found")
        exit()

for i in range(prev, min(step, n)):
    if lst[i] == key:
        print("Element found")
        break
else:
    print("Element not found")