"""
Created on 30/11/2018
@author: baptiste
for Python 3.7.0

Définition d'une classe permettant de représenter des points, 
ainsi que d'une fonctions permettant d'effectuer des opérations de translation sur des instances de Point.
"""

import matplotlib.pyplot as plt
import numpy as np

class Point(object):
    """Classe définissant un point caractérisée par :
    - ses coordonnées en 2D ou 3D ;
    - la dimension de l'espace de travail;
    - son nom (optionnel)

    Cette classe possède un attribut de classe qui récapitule toutes les instances créées.
    
    """
    all_pts_in_script = [] 

    def __init__(self, coord=np.array((0., 0.)), name=''):
        """Constructeur de notre classe. Coordonnées importéées sous forme d'un np.array"""
        dim = coord.shape[0]
        self.coord = coord
        self.dim = dim
        self.name = name
        Point.all_pts_in_script.append(self)

    def __repr__(self):#? Je ne m'en sers pas ou vraiment rarement. On supprime ? 
        """Afficher les coordonnées du point."""
        return f"Les coordonnées du point {self.name} sont {self.coord}"

    def plot(self, color="red", size=5):
        """ Représentation du point dans le plan Oxy"""
        plt.plot(self.coord[0], self.coord[1], marker='o', markersize=size, color=color)

def translation(pt, vect):
    """ Translation d'un point, définie par un vecteur de type np.array."""
    new_coord = pt.coord + vect
    return Point(new_coord)
