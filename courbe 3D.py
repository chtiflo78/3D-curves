import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# courbe 1 en sin(x)/x
X= np.arange(-10, 10, 0.25)
Y= np.arange(-10, 10, 0.25)
X,Y=np.meshgrid(X,Y)

R=np.sqrt(X**2+Y**2)
Z=np.sin(R)/(R+0.1)

fig=plt.figure('sin(x)/x')
ax=Axes3D(fig)
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=cm.viridis)

# courbe 2 en 1/x
X= np.arange(-0.5, 0.5, 0.05)
Y= np.arange(-0.5, 0.5, 0.05)
X,Y=np.meshgrid(X,Y)

R=np.sqrt(X**2+Y**2)
Z=-1/(R/10+0.01)

fig=plt.figure('1/x')
ax=Axes3D(fig)
ax.plot_wireframe(X,Y,Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()


        

