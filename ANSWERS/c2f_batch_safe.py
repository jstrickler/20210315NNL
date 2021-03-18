#!/usr/bin/env python
import sys

try:
    celsius = float(sys.argv[1])
except (ValueError, IndexError) as err:
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]
    print("{} is not a valid number".format(value))
    while True:
        try:
            raw_celsius = input("Enter a Celsius value (or q to quit): ")
            if raw_celsius == 'q':
                exit()
            celsius = float(raw_celsius)
        except ValueError as err:
            print("Error!", err)
        else:
            break

fahrenheit = ((9 * celsius) / 5) + 32
print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))
