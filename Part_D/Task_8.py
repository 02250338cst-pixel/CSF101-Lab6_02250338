queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", queue)

key = int(input("Enter element to search: "))

if key in queue:
    print("Element found")
else:
    print("Element not found")