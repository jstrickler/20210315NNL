from pprint import pprint

knight_data = {}
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_data)
print('-' * 60)
for name, data in knight_data.items():
    print(f"{data['title']:4s} {name:9s} {data['color']}")