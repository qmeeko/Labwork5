import matplotlib.pyplot as plt
import numpy as np

#1
x=np.linspace(1,16,16)
y=np.linspace(1,16,16)
x, y = np.meshgrid(x, y)
z=np.power(x,0.25)+np.power(y,0.25)

fig=plt.figure(figsize=(1,100))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#2
x=np.linspace(1,10,10)
y=np.linspace(1,10,10)
x, y = np.meshgrid(x, y)
z=np.power(x,2)-np.power(y,2)

fig=plt.figure(figsize=(1,100))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init( azim=60)

plt.show()

#3
x=np.linspace(1,10,10)
y=np.linspace(1,10,10)
x, y = np.meshgrid(x, y)
z=2*x+3*y

fig=plt.figure(figsize=(1,100))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#4
x=np.linspace(1,10,10)
y=np.linspace(1,10,10)
x, y = np.meshgrid(x, y)
z=np.power(x,2)+np.power(y,2)

fig=plt.figure(figsize=(1,100))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init( azim=270)

plt.show()

#5
x=np.linspace(1,10,10)
y=np.linspace(1,10,10)
x, y = np.meshgrid(x, y)
z=2+2*x+2*y-np.power(x,2)-np.power(y,2)

fig=plt.figure(figsize=(1,100))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init( azim=60)

plt.show()