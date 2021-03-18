import lxml.etree as et

root = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        k = et.SubElement(root, 'knight', title=title)
        et.SubElement(k, 'name').text = name
        et.SubElement(k, "color").text = color
        et.SubElement(k, 'quest').text = quest
        et.SubElement(k, 'comment').text = comment

#  A-Z a-z 0-9 _

doc = et.ElementTree(root)  # creating XML doc from top-level tag (Element)
options = {'pretty_print': True, 'xml_declaration': True}

print(et.tostring(root, **options).decode())

doc.write('knights.xml', **options)