import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73]]
)  # <1>

def triple(x):
    return 3 * x

result = triple(a)
print(result)
