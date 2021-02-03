# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:42:14 2020

@author: tvnte
"""

class DummyUpdater:
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)
 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
 
 
class Passenger(DummyUpdater):
    def __init__(self, iterable=(), **kwargs):
        super().__init__(iterable, **kwargs)
 
 
d = DummyUpdater(first_name="abc")
d2 = Passenger({"first_name": "abc"})
print(d)
print(d2)



def création_dico():
        
        if len(Livre_d_or) == 0:
            for cle, valeur in data.items():
                Livre_d_or[cle] = Livre_d_or.get(cle, valeur)
        else:
            Livre_d_or = {}
            
        return Livre_d_or
    
    
    
    def Dico_Vide():
    
     if bool(Livre_d_or):
                
                Livre_d_or[cle] = Livre_d_or.get(cle, valeur)
            else:
                Livre_d_or = {}