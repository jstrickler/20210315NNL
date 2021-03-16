
mary_in = open('DATA/mary.txt')
# ...
mary_in.close()

with open('DATA/mary.txt', 'r') as mary_in:
    for raw_line in mary_in:  # raw_line = mary_in.readline()
        line = raw_line.rstrip()  # remove trailing \n
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()  # read entire file into string
    print("NORMAL:")
    print(contents)
    print("RAW:")
    print(repr(contents))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_no_nl = [line.rstrip("\n\r") for line in mary_in]
    print(all_lines_no_nl)
