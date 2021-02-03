# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:37:14 2020

@author: tvnte
"""

#import os

def DictionnaireOrdonne(**kwargs):#Permet à la fonction d'avoir de 0 à x arguments
    "Fonction permettant de gérer un dictionnaire"""
    
    DicoVide = {}#Création de la variable DicoVide en tant que dict
    
    for i, j in kwargs.items():#exrtait de kwargs les séquences du dictionnaire sous forme de tuples
        DicoVide[i] = DicoVide.get(i, j)#méthode de recherche
    
    
    return DicoVide

            
            
def constructeur(DicoImport):
        """Fonction permettant de créer un dictionnaire via l'import"""
        
        for i, j in DicoImport.items():
            DicoImport[i] = DicoImport.get(i, j)
            
        return DicoImport




    

Dictionnaire_test = {"chaise" : 2, "papier toilette" : 500, "chaussure" : 3, "porte" : 12}#Exemple de dictionnaire à importer

fruits = DictionnaireOrdonne()
print(fruits, len(fruits))


fruits["Pomme"] = 2
fruits["poires"] = 55

print(fruits, len(fruits), type(fruits))


legumes = DictionnaireOrdonne(Choux = 5, Poireau = 20, Haricot = 250)
print(legumes, len(legumes), type(fruits))

choses = constructeur(Dictionnaire_test)
print(choses, len(choses), type(choses))





    









#os.system("pause")
