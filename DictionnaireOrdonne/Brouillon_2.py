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
        self.dico = {}
        self.keys = []
        self.values = []
        
        for cle, valeur in data.items():
            self.keys.append(cle)
            self.values.append(valeur)

        
     
    def __getitem__(self, key):
        """Méthode appelée lorsqu'on fait item[index]"""
        return self.dico
    
    def __setitem__(self, key, value):
        """Méthode appelée lorsqu'on écrit item(index] = valeur"""
    
        self.dico[key] = value
                
        self.keys.append(key)
        self.values.append(value)
        
        self.dico = dict(zip(self.keys,self.values))
        
        
    def reverse(self):
        
        _dico_reverse = dict(zip(self.keys,self.values))
        
        dico_reverse = {k: v for k, v in sorted(_dico_reverse.items(), reverse = True, key=lambda item: item[1])}
        return dico_reverse
    
    def sort(self):
        
        _dico_sorted = dict(zip(self.keys,self.values))
        
        dico_sorted = {k: v for k, v in sorted(_dico_sorted.items(), key=lambda item: item[1])}
        return dico_sorted

    def __len__(self):
        
        
        return len(self.keys)
    
    def __add__(self, ajout_item):
        

        
        added_keys = self.keys + ajout_item.keys
        added_values = self.values + ajout_item.values
        
        dico_added = dict(zip(added_keys,added_values))
        
        return dico_added
    
    
    def __repr__(self):
        
        
        
        self.dico = dict(zip(self.keys,self.values))
        return repr(dict(self.dico))

    """La méthode spéciale de représentation affiche le self._Livre_d_or définit dans init"""
     

    

keys = list()
values = list()


                 
    # /!\ envoie dans 2 listes : keys  et values /!\ doivent être liées
    
    #Paramètre Vide
    
    #Paramètre constructeur
    
    #Valeurs en paramètre
    
    
    
    #Keys ou Valeurs doivent êtres récupérées, modifiées, supprimées
    
    #Si existe => écrasé. Sinon créée // recherche possible par "CLE IN DICTIONNAIRE"
    
    #len(dictionnaire), print(dictionnaire)
    
"""def sort():#clé
    
def reverse():#clé
    
#parcourue : for clé in dictionnaire

def key():
    
def value():

def items():
    
    
#dico1 + dico2"""




        
fruits = DictionnaireOrdonne()    
print("FRUITS VIDE = ", fruits)

fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print("FRUITS AVEC UN INDEX = ", fruits)

print("SORTED = ",fruits.sort())

legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
print("LEGUMES AVEC **DATA = ", legumes,)
print("LEN LEGUMES = ", len(legumes))

print("REVERSE LEG = ",legumes.reverse())

fruits = fruits + legumes
print("FRUITS + LEGEUMES = ", fruits)

#del fruits['haricot']
#print("DEL = ", 'haricot' in fruits)
#print("HARICOT ? = ",legumes['haricot'])

#for cle in legumes:
#     print("CLE LEGUMES = ", cle)


#for nom, qtt in legumes.items():
#     print("{0} ({1})".format(nom, qtt))

#print(legumes.keys())

#print(legumes.values())

print("\nLISTE KEY FRUITS = ", fruits.keys, type(keys))
print("LISTE VALUES FRUITS = ", fruits.values, type(values))
print("LISTE KEYS LULUMES = ", legumes.keys, type(keys))
print("LISTE VALUES LULUMES = ", legumes.values, type(values))





















#os.system("pause")
