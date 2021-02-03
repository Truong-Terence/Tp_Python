# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:37:14 2020

@author: tvnte
"""

#import os


class DictionnaireOrdonne:
    """Classe enveleoppe d'un dictionnaire."""
    
     
    
    def __init__(self, dico = {}, **data):
        """La méthode accepte 0 ou x paramètres. De base le dictionnaire dico_vide est vide."""
        self._keys = []
        self._values = []
        
        for cle, valeur in data.items():
            self._keys.append(cle)
            self._values.append(valeur)    
        
        self.dico = dict(zip(self._keys,self._values))

    def __getitem__(self, index):
        """Méthode appelée lorsqu'on fait item[index]"""

        self._keys = tuple(self._keys)
        self._values = tuple(self._values)

        
        return self._keys[index]
    
    def __setitem__(self, key, value):
        """Méthode appelée lorsqu'on écrit item[index] = valeur"""
        self._keys.append(key)
        self._values.append(value)
        
        self.dico = dict(zip(self._keys,self._values))
        
        


    def reverse(self):
        """Méthode qui zip les listes en un set. elle trie le set dans l'ordre inverse et renvoie les listes dézippées"""
        result = zip(self._keys, self._values)
        result_set = set(result)
        
        list_sorted = sorted(result_set, key=lambda x: x[1], reverse = True)
        self._keys, self._values = zip(*list_sorted)
        
        
    def sort(self):
        """Méthode qui zip les listes en un set. elle trie le set dans l'ordre et renvoie les listes dézippées"""
        result = zip(self._keys, self._values)
        result_set = set(result)
        
        list_sorted = sorted(result_set, key=lambda x: x[1])
        self._keys, self._values = zip(*list_sorted)

    def __len__(self):
        """Méthode qui retourne la longueur de la liste keys de l'attribut appelé"""
        
        return len(self._keys)
    
    
    def __add__(self, ajout_item):
        """Ajoute à la liste des keys la keys de l'item ajouté. Elle procède de même pour la liste des values"""
        
        
        self._keys += ajout_item._keys
        self._values += ajout_item._values
        
        self.dico = dict(zip(self._keys,self._values))
        
        return self
    
    def __delitem__(self, index):
        """Méthode qui zip les deux listes de l'attribut. Elle créé à partir de ce set 2 nouvelles listes, récupère l'index de l'élément à supprimer.
        Elle supprime ensuite l'élément indexé de ces 2 listes puis remlace les listes originelles."""
        result = zip(self._keys, self._values)
        result_set = set(result)
        
        keys = [ i for i, j in result_set ]
        values = [ j for i, j in result_set ]
 
        x = keys.index(index)
 
        del keys[x]
        del values[x]
            
        self._keys = keys
        self._values = values
        
        self.dico = dict(zip(self._keys,self._values))
    
    def keys(self):
        
        return list(self._keys)
        
    
    def values(self):
        
        return list(self._values)
    
    
    def items(self):
        
        item = list(zip(self._keys,self._values))
        
        return item

        
    def __repr__(self):
        """La méthode spéciale de représentation affiche le self.dico  qui zip les listes définies dans init"""
        
        return repr(dict(self.dico))
    

keys = list()
values = list()
    

        
fruits = DictionnaireOrdonne()    
print("FRUITS VIDE = ", fruits)

fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print("FRUITS AVEC UN INDEX = ", fruits)

fruits.sort()
print("FRUITS.SORT = ",fruits)


legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
print("LEGUMES AVEC **DATA = ", legumes,)
print("LEN LEGUMES = ", len(legumes))

legumes.reverse()
print("REVERSE LEG = ",legumes)

fruits = fruits + legumes
print("FRUITS + LEGEUMES = ", fruits)

del fruits['haricot']
print("FRUITS W/O HARICOT", fruits)
print("DEL = ", 'haricot' in fruits)
#print("HARICOT ? = ",legumes['haricot'])

for cle in legumes:
     print("CLE LEGUMES = ", cle)


for nom, qtt in legumes.items():
     print("{0} ({1})".format(nom, qtt))

print(legumes.keys())

print(legumes.values())





















#os.system("pause")
