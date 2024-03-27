import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10,1000)
y =  x**2
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = x^2')
plt.show()
    