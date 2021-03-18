def get_message():
    return "Hello, world"

m = get_message()
print(m)

def print_message():
    msg  = get_message()
    print(msg)

print_message()

def cube(x):  # x is parameter
    return x ** 3

for i in range(5):
    print(i, cube(i))  # i is argument

data = [1, 2, 3, 4]
def total_a(x):
    return sum(x)
print(total_a(data))

def total_b(factor, *x):
    return sum(x) * factor

print(total_b(42, 1, 2, 3, 4))
print(total_b(75, 1, 2, 3, 4))

#      positional  |  named
#         req  opt  req req  opt
def wacky1(p1, *p2, p3, p4="artichoke", **p5):
    print(p1, p2, p3, p4, p5)

wacky1('a', 'b', 'c', 'd', 'e', 'f', p3=10, p4=42)
wacky1(5, 10, 15, p4="wombat", p3="wolverine")
wacky1(8, 16, 24, p4="laundromat", p3=100.2, file_name="dingoes.txt", country="Bolivia", cereal="shredded wheat")
# wacky1(['x','y'], {}, "foo")
wacky1(100, p3=200, p4=300)
wacky1(100, p3="zombie", p4="wallaby")



















