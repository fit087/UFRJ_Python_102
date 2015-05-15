# 14/05/2015
# Aula Teorica Igor Leão
# Scientific Libraries: Numpy, Scipy, Matplotlib

import numpy as np
import matplotlib.pyplot as plt

z = np.random.random((100, 2))
x, y = z[:, 0], z[:, 1]
R = np.sqrt(x**2 + y**2)
T = np.arctan2(y, x)

#plt.figure(1)

plt.subplot(121)
plt.plot(x, y)
plt.axis('equal')

plt.ylabel("Ordenadas")
plt.xlabel("Absisas")
plt.title("Coordenadas Retangulares")

plt.subplot(122, polar = True)
#plt.subplot(122)
#plt.axes(polar = True)
#plt.plot(R, T)
plt.plot(T, R)
plt.title("Coordenadas Polares")

#plt.set_title("A line plot on a polar axis", va='bottom')
plt.show(block = False) # impede que o programa se bloque até fechar a janela
                        # da figura.

polar_coord = np.hstack((R, T))

print ("polar_coord")
print (polar_coord)
print ("polar_coord.shape()")
print (polar_coord.shape)


polar_coord2 = np.vstack((R, T))

print ("polar_coord2")
print (polar_coord2)
print ("polar_coord2.shape()")
print (polar_coord2.shape)

polar_coord2 = polar_coord2.T

print ("polar_coord2.T")
print (polar_coord2)
print ("polar_coord2.T.shape()")
print (polar_coord2.shape)