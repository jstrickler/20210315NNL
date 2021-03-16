from collections import Counter
import pandas as pd

FILE_NAME = "DATA/breakfast.txt"

food_counts = {}
with open(FILE_NAME) as food_in:
    for raw_line in food_in:
        food = raw_line.rstrip()
        if food not in food_counts:
            food_counts[food] = 0  # initialize element of dict
        food_counts[food] = food_counts[food] + 1
        #  food_counts[food] += 1
print(food_counts)
print('-' * 60)

with open(FILE_NAME) as food_in:
    foods = (f.rstrip() for f in food_in)
    food_counts = Counter(foods)
    food_counts['cherry danish'] += 1
    print(food_counts.most_common())
print('-' * 60)

df = pd.read_table(FILE_NAME, names=['food'])

# print(df)
print(df.value_counts(['food']))

