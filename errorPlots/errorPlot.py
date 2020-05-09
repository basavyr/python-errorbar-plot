import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[-5,-1,0,3,5]
yerrormin=[0.5,0.2,0.1,0.9,1]
yerrormax=[0.7,1,2,3,4]

yerr=[yerrormin,yerrormax]

# errors=[]
# for id in range(len(yerrormin)):
#     dif=yerrormax[id]-yerrormin[id]
#     errors.append(dif)

plt.errorbar(x,y,yerr=yerr,fmt='o')
plt.savefig("plot.pdf",bbox_inches='tight')