d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 16, 'b': 10, 'e': 9}
d3 = {}  # empty dict 
airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
airports['PIT'] = "Pittsburgh"
airports['ALB'] = "Albany"
print(f"airports: {airports}")
print(airports['YCC'])
print(airports.get('ELM'))
print(airports.get('ELM', 'NOT FOUND'))
airports['PIT'] = "Steel City"
print(airports)

for x in 'ALB', 'PIT', 'RDU', 'PDX', 'YOW', 'RIC', 'FAY':
    print(x, x in airports)
print()

print(len(airports))
print()

for code, name in airports.items():
    print(code, name)

print(airports.items())
