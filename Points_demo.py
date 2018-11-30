"""
Created on 30/11/2018
@author: baptiste
for Python 3.7.0

Script élémentaire de démonstration. 
Utilisation de la classe Point pour représenter :
 - les sommets d'un carré contenu dans le plan Oxy
 - les sommets d'une cube projetés dans le plan Oxy avec un effet de perspective
"""

import matplotlib.pyplot as plt
import numpy as np
import copy

import Points_def as ptdef

e1 = np.array((1., 0.))
e2 = np.array((0., 1.))

A = ptdef.Point(np.array((0., 0.)), name='A')
B = ptdef.Point(e1, name='B')
C = ptdef.Point(e1+e2, name='C')
D = ptdef.Point(e2, name='D')

carre = [A, B, C, D]
carre_colors = [(66, 134, 244), #blue
                (71, 255, 172), #green
                (255, 106, 38), #orange
                (244, 65, 232) #pink
                ]
grey = (160, 160, 160)

norm_rgb = lambda c : (c[0]/255, c[1]/255, c[2]/255)
carre_colors = [norm_rgb(c) for c in carre_colors]
grey = norm_rgb(grey)

print("On definit le carré unitaire par ses quatres sommets.")
for pt in carre : 
    print(pt)

plt.figure()
plt.axis('equal')
for pt, col in zip(carre, carre_colors):
    pt.plot(color=col)


#Translations pour créer un effet de perspective
cube = copy.copy(carre)
t_vect = np.array((0.2, 0.4))
for pt in carre:
    cube.append(ptdef.translation(pt, t_vect))

cube_colors = copy.copy(carre_colors)
for c in carre_colors:
    nuance = [(val+ 2 * g_val)/3 for val,g_val in zip(c, grey)]
    cube_colors.append(nuance)

plt.figure()
plt.axis('equal')
for pt, col in zip(cube, cube_colors):
    pt.plot(color=col)
plt.pause(0.1)
plt.show()