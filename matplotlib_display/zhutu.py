import numpy as np
import matplotlib.pyplot as plt
 
mu = 0.0
sigma = 2.0
samples = np.random.normal(loc=mu, scale=sigma, size=1000)
plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 2', size=14)
plt.xlabel('value', size=14)
plt.ylabel('counts', size=14)
plt.hist(samples, bins=40, range=(-10, 10))
plt.text(-9, 100, r'$\mu$ = 0.0, $\sigma$ = 2.0', size=16)
plt.savefig('images/plot2.png', format='png')
