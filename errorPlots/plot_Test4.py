import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from matplotlib import rc

# for Palatino and other serif fonts use:
# plt.style.use("ggplot")
rc('font', **{'family': 'serif', 'serif': ['Palatino']})
rc('text', usetex=True)
# test1
x = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]
y = [1.35, 3.19, 3.31, 1.67, 1.94, 1.41, -3.91, -
     2.02, 1.80, -0.64, 0.45, -1.14, -0.81, 1.71, 0.05]
yerrormin = [3.35, 6.19, 6.31, 4.67, 4.94, 5.41, -0.91,
             0.98, 5.80, 3.36, 3.45, 2.86, 3.19, 4.71, 4.05]
yerrormax = [0.65, -0.19, -0.31, 1.33, 1.06, 2.59, 6.91,
             5.02, 2.20, 4.64, 2.55, 5.14, 4.81, 1.29, 3.95]
yerror = [yerrormin, yerrormax]


# generate the data-points labels
text_Test4 = [(r'$5/0^o$'), (r'$5/90^o$'), (r'$5/270^0$'), (r'$5/180^0$'), (r'$5\sum$'), (r'$6/0^o$'), (r'$6/90^o$'),
              (r'$6/270^o$'), (r'$6/180^o$'), (r'$6\sum$'), (r'$10/0^o$'), (r'$10/90^o$'), (r'$10/270^o$'), (r'$20/180^o$'), (r'$10\sum$')]

pos_Test4 = []
textpos_Test4 = []

for id in range(len(y)):
    if(id % 2 == 0):
        xyPointEven = (x[id]-0.2, yerrormax[id]+y[id]+0.8)
        pos_Test4.append(xyPointEven)
        textpos_Test4.append(xyPointEven)
    else:
        xyPointOdd = (x[id]-0.2, -yerrormax[id]-y[id]-0.8)
        pos_Test4.append(xyPointOdd)
        textpos_Test4.append(xyPointOdd)

fig, ax = plt.subplots()
ax.plot(x, y, 'o', color='b', label="Test4")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='b', linewidth=1)
ax.set_ylim(-8, 8)
ax.set_xlabel(r'Puncte de măsură')
ax.set_ylabel(r'Deviația ( $\%$)')


# function to annotate points
# function takes as input the text to be annotated, and its coresponding coordinates)


def anno(text, pos, textpos, xcolor):
    for id in range(len(text)):
        plt.annotate(text[id], xy=pos[id], xytext=textpos[id], color=xcolor)


anno(text_Test4, pos_Test4, textpos_Test4, 'b')

# ax.set_title('Plot Title')
ax.legend(ncol=4)
ax.grid(axis='y', linestyle='--', color='silver')
plt.savefig("test4.pdf", bbox_inches='tight')
