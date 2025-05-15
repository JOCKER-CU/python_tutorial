import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

import matplotlib.pyplot as plt 


y = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(y,bins=25, alpha=0.5, color='blue', label='x')
plt.show()
