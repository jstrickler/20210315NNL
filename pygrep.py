import fileinput
import argparse

parser = argparse.ArgumentParser(description="Python grep")
parser.add_argument("-i", dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument("-f", dest="show_name", action="store_true", help="show file name")
parser.add_argument("term", help="search term")
parser.add_argument("file", nargs="+", help="files to search")
args = parser.parse_args()  # parsers sys.argv by default
print(args)

if args.ignore_case:
    args.term = args.term.lower()

for raw_line in fileinput.input(args.file):
    original_line = raw_line.rstrip()
    if args.ignore_case:
        search_line = original_line.lower()
    else:
        search_line = original_line

    if args.term in search_line:
        if args.show_name:
            print(fileinput.filename(), end=' ')
        print(original_line)