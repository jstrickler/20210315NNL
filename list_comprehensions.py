fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for fruit in fruits:
    f0.append(fruit.upper())
print("f0:", f0, '\n')

# [EXPR for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]   #  list comprehension
print("f1:", f1, '\n')

f2 = [f[:3].title() for f in fruits]
print("f2:", f2, '\n')

f3 = []
for f in fruits:
    if f.startswith('p'):
        f3.append(f.upper())

f3 = [f.upper() for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam',
        'eggs','spam', 'spam', 'spam', 'spam', 'spam', 'toast', 'spam', 'spam', 'spam']

good_food = [f for f in food if f != 'spam']
print("good_food:", good_food, '\n')

good_food = [f for f in food if f != 'spam' if f != 'eggs']
print("good_food:", good_food, '\n')

good_food = [f for f in food if f not in ('spam', 'eggs')]
print("good_food:", good_food, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [n / 10 for n in nums]
print("n1:", n1, '\n')

powers = [(i, i**2, i**3) for i in range(1, 11)]
print("powers:", powers, '\n')

fgen = (f.upper() for f in fruits)
print(fgen)

#  ID10T

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

dob_list = [p[3] for p in people]
dob_gen = (p[3] for p in people)
print("dob_list:", dob_list, '\n')
for dob in dob_gen:
    print(dob, end=' ')
print('\n')

flags = [True] * 10
print(f"flags: {flags}")
print(f"dob: {dob}")
