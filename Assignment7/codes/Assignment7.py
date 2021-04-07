import math
from scipy.stats import binom
import matplotlib.pyplot as plt
import array as arr
import numpy as np
import random

x = np.linspace(0, 100, 100) 
fig = plt.figure() 
plt.plot(x, np.exp(-x)) 
plt.xlabel("Value of x")
plt.ylabel("Probability density function of variable X")
plt.show()
