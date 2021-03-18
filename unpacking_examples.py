# the wonderful world of *

def spam(*things):
    print(things)

spam('a', 'wombat', 12, 32)
spam('hello')
spam()
print()

def ham(a, b, c):
    print(a)
    print(b)
    print(c)
    print('-' * 4)

ham(5, 10, 15)
data = [10, 100, 1000]
ham(*data)  # same as ham(10, 100, 1000)

values = 'a', 'b', 'c', 'd', 'e'
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)








