from pprint import pprint

knight_data = {}
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment  # add tuple of data to dictionary element with key=name

pprint(knight_data)
print('-' * 60)
for name, data in knight_data.items():
    print("{:4s} {:9s} {}".format(data[0], name, data[1]))