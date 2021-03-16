with open('DATA/breakfast.txt') as breakfast_in:
    foods = [f.rstrip() for f in breakfast_in]

unique_foods = set(foods)
unique_foods.add('eggs benedict')
print(f"foods: {foods}")
print(f"unique_foods: {unique_foods}")

s1 = set(['red', 'pink', 'orange', 'purple', 'blue', 'aqua', 'mauve', 'taupe'])
s2 = set(['purple', 'mauve', 'orange', 'aqua', 'green', 'brown'])

print('Both:', s1 & s2)  # intersection (common to both)
print("Just one:", s1 ^ s2)  # Xor  (not common to both)
print("Either:", s1 | s2)  # union  (all items in both, without duplicates)
print("Just s1:", s1 - s2)
print("Just s2:", s2 - s1)

#  files = {
#    'root': {set},
#    'examples': {set},
#    ...
#}
