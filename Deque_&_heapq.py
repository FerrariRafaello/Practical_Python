from collections import deque  # deque is a double-ended queue

"""
A deque (double-ended queue) is a structure that allows removing elements from both the beginning and the end of the queue.
A queue usually follows the FIFO (First In First Out) pattern, like a line at a bank.
"""

# Creating a deque with a maximum length of 4
queue = deque(maxlen=4)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)  # Output: deque([1, 2, 3, 4], maxlen=4)

# If you add more numbers than the prescribed maxlen, the first value will be dropped (FIFO order)
queue.append(5)
print(queue)  # Output: deque([2, 3, 4, 5], maxlen=4)

# Removing specific elements
queue.remove(3)  # Remove value 3
print(queue)     # Output: deque([2, 4, 5], maxlen=4)

# Creating a deque with no size limit and showing how to add elements to the left and right
f = deque()
f.append(1)
f.append(2)
f.append(3)
print(f)  # deque([1, 2, 3])

f.appendleft(4)  # Add 4 to the left side (front) of the deque
print(f)         # deque([4, 1, 2, 3])

# Removing elements from deque
f.pop()          # Removes from the right (last element)
print(f)         # deque([4, 1, 2])
f.popleft()      # Removes from the left (first element)
print(f)         # deque([1, 2])

# If you want to remove a specific value:
f.remove(2)      # Removes value 2
print(f)         # deque([1])

# ---------------------------------------
# Priority Queue (heapq)
import heapq

"""
The heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
It is useful for finding the smallest/largest elements efficiently.
"""

ages = [15, 10, 18, 25, 8, 19]
print(heapq.nsmallest(3, ages))  # Output: [8, 10, 15] (3 smallest)
print(heapq.nlargest(3, ages))   # Output: [25, 19, 18] (3 largest)
print(max(ages))                 # Output: 25 (max value in list)

heapq.heapify(ages)              # Transform the list into a heap in-place
print(ages)                      # Heap-ordered list

# Another example with numbers
numbers = [10, 5, 20, 30, 6, 8, 15]
print("Numbers before heapify: {}".format(numbers))
heapq.heapify(numbers)
print("Numbers after heapify: {}".format(numbers))
heapq.heappop(numbers)           # Always removes the smallest number
print("After heappop:", numbers)

numbers.sort()                   # Sorts the list (ascending)
print("Sorted numbers:", numbers)

# Adding a number with heapq
heapq.heappush(numbers, 90)
"""
With this method, the largest numbers tend to go to the right and the smallest to the left,
following the properties of a binary heap.
"""
print(numbers)
