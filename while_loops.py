# while CONDITION:
#     code...
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# print("Done.")

while True:
    raw_base = input("Enter base (or q to quit): ")
    if raw_base == 'q':
        break
    if raw_base == '':
        print("Please enter a number or 'q'")
        continue
    raw_exponent = input("Enter exponent: ")
    base = float(raw_base)
    exponent = float(raw_exponent)
    print("{} ** {} is {}".format(base, exponent, base ** exponent))