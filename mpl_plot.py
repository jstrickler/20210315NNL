import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1,11)
# fig = plt.figure()   # get the current figure
for i in range(1,10):
    data = np.random.random_sample((10,)) * 10
#    sub = fig.add_subplot(3,3,i)
    plt.plot(y, data)

plt.show()