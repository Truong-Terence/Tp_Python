# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:14:28 2020

@author: tvnte
"""

from operator import itemgetter

fruits = {"chaise" : 2, "papier toilette" : 500, "chaussure" : 3, "porte" : 12}
Dictionnaire2 = {"Saras" : 4, "kololo" : 12}


def sort():
    for k in sorted(kwargs.items()):
        kwargs[k] = kwargs.get(i, j)
    
    return kwargs




fruits.sort()
print(fruits)



    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        return self.Livre_d_or[index]
        
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        self.Livre_d_or[index] = valeur
            