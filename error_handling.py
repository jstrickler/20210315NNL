FILE_NAME = "DATA/wombats.txt"

try:
    with open(FILE_NAME) as file_in:
        pass
except FileNotFoundError as err:
    # log the error
    # pop up a message if in a GUI
    # print a message to the screen
    print(err)


data = [1, 10, 20, 32, 99]
try:
    print(data[9])
except IndexError as err:
    print(err)

values = 0, 5, "18.37", 8.6, 0, "a100", 41, ['foo'], 19
for v in values:
    try:  # potential runtime errors
        if v == 41:
            raise FileExistsError("file does not exist")
        result = 23 / float(v)
    except ZeroDivisionError as err:
        print(err, type(err))
    except (ValueError, TypeError) as err:
        print(err, type(err))
    except Exception as err:
        print("UNEXPECTED!", err)
    else:  # all is well, no exceptions
        print(v, result)
    finally:
        print(".")