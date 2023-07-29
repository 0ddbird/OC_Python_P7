import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import scipy.integrate

def brute_force(n):
    return 1 + n * 2**n + 2**n + 1

def greedy(n):
    return n * np.log2(n) + n

def dynamic_programming(n, capacity):
    return 2 * n * capacity + n

n_values = np.linspace(1, 20, 50000)

plt.figure(figsize=[10,10])

brute_force_area = scipy.integrate.quad(brute_force, 1, 20)[0]
plt.plot(n_values, brute_force(n_values), label=f'Brute Force, area = {brute_force_area:.2f}')

greedy_area = scipy.integrate.quad(greedy, 1, 20)[0]
plt.plot(n_values, greedy(n_values), label=f'Greedy, area = {greedy_area:.2f}')

for capacity in [500, 50000]:
    dynamic_programming_area = scipy.integrate.quad(dynamic_programming, 1, 20, args=(capacity,))[0]
    plt.plot(n_values, dynamic_programming(n_values, capacity), label=f'Dynamic Programming (capacity={capacity}), area = {dynamic_programming_area:.2f}')

plt.legend()
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Time Complexity of Algorithms')
plt.grid(True)

# Set the y-axis to a logarithmic scale
plt.yscale('log')

# Set x-axis to only use integer values
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()
