# Huffman Coding
import heapq
from collections import defaultdict

def calculate_frequency(chars, freq):
    return dict(zip(chars, freq))

def huffman_encode(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Your data
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [7, 8, 1, 40, 54, 68]

# Calculate frequency
frequency = calculate_frequency(chars, freq)

# Apply Huffman encoding
huff = huffman_encode(frequency)
print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print(str(p[0]).ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
