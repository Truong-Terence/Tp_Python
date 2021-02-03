# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:15:26 2020

@author: tvnte
"""


#Le fichier fonctions.py qui contiendra les fonctions utiles à notre application.
#(Quelles sont les actions de mon programme ? Que puis-je mettre dans des fonctions ?).

import os
from random import *
from donnees import *
import pickle



def recup_scores():
    if os.path.exists(score_book):
        with open(score_book,"rb") as les_scores: 
            mon_depickler = pickle.Unpickler(les_scores)
            scores = mon_depickler.load()
    else:
        scores = {}
    return scores


def enregistrer_score(scores):
    with open(score_book,"wb") as les_scores:
        mon_pickler = pickle.Pickler(les_scores)
        mon_pickler.dump(scores)
        
    
    
def recup_nom_user():
    joueur = input("Say your name : ")
    joueur = joueur.capitalize()
    if not joueur.isalnum or len(joueur) < 3:
        print("Blaz non acceptable")
        return recup_nom_user()
    else:
        return joueur

    
def recup_lettre():
    lettre = input("Donne moi une lettre : ")
    lettre = lettre.lower()
    if not lettre.isalpha() or len(lettre) > 1:
        print("neh")
        return recup_lettre()
    else:
        return lettre


def choisir_mot():
    mot_pendu = choice(liste_mots)
    if not len(mot_pendu) <= 8:
        return choisir_mot()
    else:
        return mot_pendu
    
    
    
    
    
def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque


        
    


