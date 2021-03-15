
t1 = tuple()
t2 = ()

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(len(person), person[0], person[-1], person[0:2])

me_tuple = ('John', 'Strickler', 64, 27705)  # tuple
me_list = ['John', 'Strickler', 64, 27705]

first_name, last_name, product, dob = person
print(product)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(type(people))
print(type(people[0]), people[0])
print(type(people[0][0]), people[0][0])

for person in people:
    print(person[0], person[1])

print("-" * 60)
for first_name, last_name, *_ in people:
    # first_name, last_name, product, dob = next-value-of people
    print(first_name, last_name)
print()

data = [('red', 5), ('green', 2), ('purple', 5), ('orange', 6)]
for color, value in data:
    print(color * value)
print()







