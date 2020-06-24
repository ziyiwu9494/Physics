import Physics
from numpy import exp, arange, linalg, array, linspace
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

nx = ny = 64
x = linspace(-0.1,0.15,nx)
y = linspace(-0.1,0.15,ny)
X,Y = meshgrid(x, y) # grid of point

env = [
        Physics.Particle([0, 0.045], float("7.3E-9"), 0),
        Physics.Particle([0.045, 0.045], float("-17.5E-9"), 0),
        Physics.Particle([0.045, 0], float("17.5E-9"), 0),
        Physics.Particle([0, 0], float("-7.3E-9"), 0),
    ]

Z = array([[(linalg.norm(Physics.Point([x_val, y_val]).find_electric_field(env).vector) / 100000) if (linalg.norm(Physics.Point([x_val, y_val]).find_electric_field(env).vector) / 100000) < 50 else 0 for x_val, y_val in zip(X_list, Y_list)] for X_list, Y_list in zip(X, Y) ])

im = imshow(Z,cmap=cm.RdBu) # drawing the function
# adding the Contour lines with labels
cset = contour(Z,arange(-1,1.5,0.2),linewidths=2,cmap=cm.Set2)
clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
colorbar(im) # adding the colobar on the right
# latex fashion title
title('Electric Field')
show()