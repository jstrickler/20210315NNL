import lxml.etree as et

doc = et.parse('DATA/solar.xml')

print(doc, type(doc))

root = doc.getroot()
print(root, root.tag)
for section in root:
    # print(section.tag)
    if 'planets' in section.tag:
        for planet in section.findall('planet'):
            print(planet.get('planetname'))
            for moon in planet.findall('moon'):
                print("\t{}".format(moon.text))
print('-' * 60)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print("\t{}".format(moon.text))