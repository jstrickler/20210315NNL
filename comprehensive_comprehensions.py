from pprint import pprint

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f1 = [f.upper() for f in fruits]
print(f"f1: {f1}")

f2 = [(f, f.upper()) for f in fruits if 'e' in f]
print(f"f2: {f2}")

d1 = {f[:3]: len(f) for f in fruits}
print(f"d1: {d1}", '\n')

import os
file_sizes = {f:os.path.getsize(f) for f in os.listdir() if f.endswith('.py')}
print(f"file_sizes:", end=' ')
pprint(file_sizes)
print()

data = ['blue  ', '   blue', 'green', 'red', 'green', '   green    ', 'purple', 'blue', '  purple  ']
s1 = set(data)
print(f"s1: {s1}")
s2 = {s.strip() for s in data}
print(f"s2: {s2}", '\n')

f1 = [f.upper() for f in fruits]
print(f"f1: {f1}", '\n')

fgen = (f.upper() for f in fruits)

for fruit in fgen:
    print(fruit)
print()
