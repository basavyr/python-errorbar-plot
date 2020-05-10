import matplotlib.pyplot as plt
import numpy as np

x,y=[],[]
for id in range(10):
    x.append(id)
    y.append(id*id)

fig, ax = plt.subplots()
ax.plot(x,y,'r-')
# ax.set_xlim(0, 1)
ax.set_ylim(min(y),max(y))
ax.set_xlabel('ok')
ax.set_ylabel('ok2')
ax.set_title('Gaussian colored noise')

plt.savefig("limited.pdf",bbox_inches='tight')

import tikzplotlib
# tikzplotlib.clean_figure()
tikzplotlib.save("../latexPlot/plot.tex")