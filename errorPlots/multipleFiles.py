import tikzplotlib
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from matplotlib import rc

# for Palatino and other serif fonts use:
# plt.style.use("ggplot")
rc('font', **{'family': 'serif', 'serif': ['Palatino']})
rc('text', usetex=True)
# test1
x = [1, 2, 3, 4, 5]
y = [0.59, 0.15, 0.77, 0.3, 0.78]
yerrormin = [2.59, 2.15, 2.77, 4.3, 3.78]
yerrormax = [1.41, 1.75, 1.23, 3.7, 2.2]
yerror = [yerrormin, yerrormax]

# generate the data-points labels
text_Test1 = [('1'), ('3'), ('5'), ('9'), ('10')]
text_Test2 = [('1')]
text_Test3 = [('3')]
text_Test5 = [('2'), ('7')]
text_Test6 = [('3'), ('7'), ('10')]
text_Test7 = [('$5/0^o$'), ('$5/90^o$'), ('$5/270^o$'), ('$4\sum$')]
text_Test8 = [('$5/90^o$'), ('$5/270^o$'), ('$5/30^o$'), ('$4\sum$')]

pos_Test1 = []
textpos_Test1 = []

for id in range(len(y)):
    xyPoint = (x[id]-0.1, yerrormax[id]+y[id]+0.2)
    pos_Test1.append(xyPoint)
    textpos_Test1.append(xyPoint)

fig, ax = plt.subplots()
ax.plot(x, y, 'o', color='b', label="Test1")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='b', linewidth=1)
ax.set_ylim(-8, 8)
ax.set_xlabel(r'Puncte de măsură')
ax.set_ylabel(r'Deviația ( $\%$)')

# test2
x = [6]
y = [3.87]
yerrormin = [6.87]
yerrormax = [-0.87]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='r', label="Test2")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='r', linewidth=1)

pos_Test2 = []
textpos_Test2 = []

for id in range(len(y)):
    xyPoint = (x[id]-0.1, yerrormax[id]+y[id]+1.3)
    pos_Test2.append(xyPoint)
    textpos_Test2.append(xyPoint)

# test3
x = [7]
y = [0.72]
yerrormin = [3.72]
yerrormax = [2.28]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='y', label="Test3")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='y', linewidth=1)

pos_Test3 = []
textpos_Test3 = []

for id in range(len(y)):
    xyPoint = (x[id]-0.1, yerrormax[id]+y[id]+0.3)
    pos_Test3.append(xyPoint)
    textpos_Test3.append(xyPoint)

# test5
x = [8, 9]
y = [0.37, 0.89]
yerrormin = [2.37, 4.89]
yerrormax = [1.63, 3.11]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='g', label="Test5")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='g', linewidth=1)

pos_Test5 = []
textpos_Test5 = []

for id in range(len(y)):
    xyPoint = (x[id]-0.1, yerrormax[id]+y[id]+0.3)
    pos_Test5.append(xyPoint)
    textpos_Test5.append(xyPoint)

# test6
x = [10, 11, 12]
y = [0.36, -1.93, -0.43]
yerrormin = [3.36, 2.07, 4.57]
yerrormax = [2.64, 5.93, 5.43]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='crimson', label="Test6")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='crimson', linewidth=1)

pos_Test6 = []
textpos_Test6 = []

for id in range(len(y)):
    xyPoint = (x[id]-0.1, yerrormax[id]+y[id]+0.3)
    pos_Test6.append(xyPoint)
    textpos_Test6.append(xyPoint)

# test7 numere random pe x cum trebuie, de fapt, la toate si la final doar denumite punctele in grafic
x = [13, 14, 15, 16]
y = [1.03, 2.31, 2.16, 1.80]
yerrormin = [3.03, 6.31, 6.16, 4.80]
yerrormax = [0.97, 1.69, 1.84, 1.2]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='indigo', label="Test7")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='indigo', linewidth=1)

pos_Test7 = []
textpos_Test7 = []

for id in range(len(y)):
    if(id < (len(y)/2)):
        xyPoint1 = (x[id]-0.5, yerrormax[id]+y[id]+(id+0.3)*0.4)
        pos_Test7.append(xyPoint1)
        textpos_Test7.append(xyPoint1)
    else:
        xyPoint2 = (x[id]-0.5, y[id]-yerrormin[id]-(id-0.6)*0.6)
        pos_Test7.append(xyPoint2)
        textpos_Test7.append(xyPoint2)

l7 = len(pos_Test7)-1
pos_Test7[l7] = (x[l7], -3.8)
textpos_Test7[l7] = (x[l7], -3.8)

# test8 numere random pe x cum trebuie, de fapt, la toate si la final doar denumite punctele in grafic
x = [17, 18, 19, 20]
y = [2.63, 2.95, 0.57, 2.06]
yerrormin = [5.63, 5.95, 3.57, 5.06]
yerrormax = [0.37, 0.05, 2.43, 0.94]
yerror = [yerrormin, yerrormax]
ax.plot(x, y, 'o', color='darkred', label="Test8")
plt.errorbar(x, y, yerr=yerror, fmt='o', color='darkred', linewidth=1)

pos_Test8 = []
textpos_Test8 = []

for id in range(len(y)):
    if(id < (len(y)/2)):
        xyPoint1 = (x[id]-0.5, yerrormax[id]+y[id]+(id+0.3)*0.6)
        pos_Test8.append(xyPoint1)
        textpos_Test8.append(xyPoint1)
    else:
        xyPoint2 = (x[id]-0.5, y[id]-yerrormin[id]-(id-0.6)*0.6)
        pos_Test8.append(xyPoint2)
        textpos_Test8.append(xyPoint2)

# function to annotate points
# function takes as input the text to be annotated, and its coresponding coordinates)


def anno(text, pos, textpos, xcolor):
    for id in range(len(text)):
        plt.annotate(text[id], xy=pos[id], xytext=textpos[id], color=xcolor)


anno(text_Test1, pos_Test1, textpos_Test1, 'b')
anno(text_Test2, pos_Test2, textpos_Test2, 'r')
anno(text_Test3, pos_Test3, textpos_Test3, 'y')
anno(text_Test5, pos_Test5, textpos_Test5, 'g')
anno(text_Test6, pos_Test6, textpos_Test6, 'crimson')
anno(text_Test7, pos_Test7, textpos_Test7, 'indigo')
anno(text_Test8, pos_Test8, textpos_Test8, 'brown')

# ax.set_title('Plot Title')
ax.legend(ncol=4)
ax.grid(axis='y', linestyle='--', color='silver')
plt.savefig("multiple.pdf", bbox_inches='tight')

# tikzplotlib.clean_figure()
tikzplotlib.save("../latexPlot/plot.tex")
