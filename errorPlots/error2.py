import matplotlib.pyplot as plt
import numpy as np
x = [1, 3, 5, 9, 10]
y = [0.59, 0.15, 0.77, 0.30, 0.78]
yerrormin = [-2, -2, -2, -4, -3]
yerrormax = [2, 2, 2, 4, 3]
cool = np.subtract(yerrormax, yerrormin)

# yerror = []
# for id in range(len(yerrormax)):
#     diff=yerrormax[id]-yerrormin[id]
#     yerror.append(diff)


# print(cool)
plt.errorbar(x, y, yerr=cool, fmt='o')
plt.savefig("plot2.pdf", bbox_inches='tight')
