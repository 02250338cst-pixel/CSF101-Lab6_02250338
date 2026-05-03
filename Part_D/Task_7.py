stack = []
stack.append(34)
stack.append(12)
stack.append(9)
stack.append(56)

print("Stack:", stack)

lst = stack.copy()

for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Sorted Stack:", lst)