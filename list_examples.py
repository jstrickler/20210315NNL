
list1 = list()  # empty list
list2 = ['a', 'b', 'c']
list3 = []  # empty list
fields = 'a:b:c'
list4 = fields.split(':')

cities = ['Pittsburgh', 'Schenectady', 'Albany', 'McKeesport', 'Boston', 'Homestead',
          'Colonie']
print(cities[0], cities[5], cities[-1])
cities.append('Sewickley')
cities.append('Camelot')
print(cities)
cities.insert(0, 'Rochester')
cities.insert(5, 'Poughkeepsie')
print(cities)
more_cities = ['Monroeville', 'Moon', 'Fox Chapel']
cities.extend(more_cities)  # append one at a time
print(cities)

del cities[-2]
print(cities)

c = cities.pop(4)
print(c)
print(cities)

c = cities.pop()
print(c)
print(cities)

cities.remove('Boston')
print(cities)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam'
        , 'spam', 'spam', 'spam', 'eggs', 'spam']
print(food.count('spam'))
print(food.count('eggs'))
print(food.count('lobster thermidor'))

print(cities)
print(cities[0], cities[1], cities[-3])
print(cities[0:4])
print(cities[5:8])
x = "wombat love"
print(x[3:6], x[8:11])
print()

for city in cities:
    # city = <next-element-of> cities
    print(city)
print()

m = "abc"
for char in m:
    print(char)
print()

print(len(cities), min(cities), max(cities))
print(sorted(cities))
print()


for i, city in enumerate(cities):
    print(i, city)

print(list(enumerate(cities)))

enum_cities = enumerate(cities)
cities.append('Durham')

print(type(enum_cities))

for i, city in enum_cities:
    print(i, city)
print()

for i in range(3):
    print(i)
print()

for i in range(1, 11):
    print(i)

for i in range(5, 101, 5):
    print(i, end=' ')
print("\n\n")







