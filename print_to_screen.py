actor = "Chris Hemsworth"
city = "Sydney"
value = 22/9

print(actor, city, value)  # print(str(actor), str(city), str(value))
print(actor, city, value, sep="/")
print(actor, city, value, sep=" <==> ")
print("Starting...", end="")
print("more stuff...", end="")
print("Done.")
print()

print("Value is", value)
print("Value is {:.3f}".format(value))
a, b, c = 1, 2, 3
print("{} {} {}".format(a, b, c))
print(f"Value is {value:.3f}")
