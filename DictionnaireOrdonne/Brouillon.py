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
        self.keys = []
        self.values = []
        
        for cle, valeur in data.items():
            self.keys.append(cle)
            self.values.append(valeur)    
        
        self.dico = dict(zip(self.keys,self.values))

    def __getitem__(self, index):
        """Méthode appelée lorsqu'on fait item[index]"""

        self.keys = tuple(self.keys)
        self.values = tuple(self.values)

        
        return self.keys[index]
    
    def __setitem__(self, key, value):
        """Méthode appelée lorsqu'on écrit item[index] = valeur"""
        self.keys.append(key)
        self.values.append(value)
        
        self.dico = dict(zip(self.keys,self.values))
        
        


    def reverse(self):
        """Méthode qui zip les listes en un set. elle trie le set dans l'ordre inverse et renvoie les listes dézippées"""
        result = zip(self.keys, self.values)
        result_set = set(result)
        
        list_sorted = sorted(result_set, key=lambda x: x[1], reverse = True)
        self.keys, self.values = zip(*list_sorted)
        
        
    def sort(self):
        """Méthode qui zip les listes en un set. elle trie le set dans l'ordre et renvoie les listes dézippées"""
        result = zip(self.keys, self.values)
        result_set = set(result)
        
        list_sorted = sorted(result_set, key=lambda x: x[1])
        self.keys, self.values = zip(*list_sorted)

    def __len__(self):
        """Méthode qui retourne la longueur de la liste keys de l'attribut appelé"""
        
        return len(self.keys)
    
    
    def __add__(self, ajout_item):
        """Ajoute à la liste des keys la keys de l'item ajouté. Elle procède de même pour la liste des values"""
        
        
        self.keys += ajout_item.keys
        self.values += ajout_item.values
        
        self.dico = dict(zip(self.keys,self.values))
        
        return self
    
    def __delitem__(self, index):
        """Méthode qui zip les deux listes de l'attribut. Elle créé à partir de ce set 2 nouvelles listes, récupère l'index de l'élément à supprimer.
        Elle supprime ensuite l'élément indexé de ces 2 listes puis remlace les listes originelles."""
        result = zip(self.keys, self.values)
        result_set = set(result)
        
        _keys = [ i for i, j in result_set ]
        _values = [ j for i, j in result_set ]
 
        x = _keys.index(index)
 
        del _keys[x]
        del _values[x]
            
        self.keys = _keys
        self.values = _values
        
        self.dico = dict(zip(self.keys,self.values))
    
    def keys(self):
        
        return self.keys
        
    
    def values(self):
        
        return list(self.values)
    
    
    def items():
        
        
        return self

        
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


#for nom, qtt in legumes.items():
#     print("{0} ({1})".format(nom, qtt))

#print(legumes.keys())

#print(legumes.values())

print("\nLISTE KEY FRUITS = ", fruits.keys, type(keys))
print("LISTE VALUES FRUITS = ", fruits.values, type(values))
print("LISTE KEYS LULUMES = ", legumes.keys, type(keys))
print("LISTE VALUES LULUMES = ", legumes.values, type(values))






















#os.system("pause")
