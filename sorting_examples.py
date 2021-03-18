fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]


print(sorted(fruits), '\n')

print(sorted(fruits, key=str.lower), '\n')

def sortall(e):
    return str(e).lower()

print(sorted(fruits, key=sortall), '\n')

def wacky(s):
    return s[-1]

print(sorted(fruits, key=wacky), '\n')

print(sorted(fruits, key=len), '\n')

def len_and_name(f):
    return len(f), f.lower()

print(sorted(fruits, key=len_and_name), '\n')

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
for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    return p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def by_lname(p):
    return p[1], p[0]

for person in sorted(people, key=by_lname):
    print(person)
print('-' * 60)


for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print('-' * 60)

#  lambda param-list: return-value

nums = [800,80,1000,32,255,400,5,5000]

print(sorted(nums))
print(sorted(nums, key=str))  # DO THIS
print(sorted(nums, key=lambda x: str(x)))  # NOT THIS

print(max(nums))
print(max(nums, key=str))