# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:03:52 2020

@author: tvnte
"""

import os
from donnees import *
from fonctions import *





continuer_partie = True #On booléen le continue

print("c'est parti pour une partie de pendu !")

scores = recup_scores() #Fonctions

user = recup_nom_user() #Fonctions
if user not in scores.keys():#si nouvel utilisateur, APRES insertion de la fonction. Ne fonctionne pas dedans (?)
    scores[user] = 0
    
    
while continuer_partie != "n":
    print("{}, vous avez {} pts.".format(user, scores[user]))#On informe le joueur de ses points
    anonymous = choisir_mot() #Fonctions pour insérer la randomisation du mot pour la partie
    print("Mon mot est long de", len(anonymous), "lettres.")#On donne les carac au joueur
    lettres_trouvees = [] #On fait une liste pour regrouper les lettres déjà trouvées. Vide.
    avancement = recup_mot_masque(anonymous, lettres_trouvees)#C'est le début, le joueur n'a pas encore donné de lettre, on lui montre le terrain de jeu.
    chances = nb_coups #Données et les chances. 8 de base
    while anonymous != avancement and chances > 0:# Tant que le mot n'est pas trouvé et que le joueur a encore des chances, il va réessayer.
        print("{} - Encore {} coups".format(avancement, chances))#avant chaque lettre on fait un point avec le joueur.
        attempt = recup_lettre() #Fonctions pour récupérer la 1ère lettre. (puis 2, puis 3, puis N avec la boucle..)
        if attempt in lettres_trouvees:
            print("Déjà dit")
            print(lettres_trouvees)
        elif attempt in anonymous:
            lettres_trouvees.append(attempt)
            print("yes !")
        else:
            print("Dommage !")
            chances -= 1
        avancement = recup_mot_masque(anonymous, lettres_trouvees)
            

    if avancement == anonymous:
        print("GG le mot était : ", anonymous, " !")
    else:
        print("Pendu ! ... C'était \" ", anonymous, "\"")
    
    scores[user] += chances
    
    continuer_partie = input("Encore ? O/N ")
    continuer_partie = continuer_partie.lower()

enregistrer_score(scores) 

print("A la prochaine {} tu as {} pts qui t'attendent !".format(user, scores[user]))
    
    
   

#scores (sans aucune extension) les scores du jeu.
#Ces scores seront sous la forme d'un dictionnaire : en clés, nous aurons
#les noms des joueurs et en valeurs les scores, sous la forme d'entiers.
#Le fichier n'existe pas. Là, on crée un dictionnaire vide, aucun score n'a été trouvé.
#Le joueur n'est pas dans le dictionnaire. Dans ce cas, on l'ajoute avec un score de 0.



#joueur de donner son nom, au début de la partie.
    



#l'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum


#l'ordinateur affiche le mot avec les lettres déjà trouvées.

#Celles qui ne le sont pas encore sont remplacées par des étoiles (*).
#Le joueur a 8 chances.


#Cela permettra au programme d'enregistrer son score.
#il me reste trois coups au moment où je trouve le mot, je gagne trois points.

#qu'une seule lettre à la fois et que le programme doit bien vérifier
#que c'est le cas avant de continuer

#scores (sans aucune extension) les scores du jeu.
#Ces scores seront sous la forme d'un dictionnaire : en clés, nous aurons
#les noms des joueurs et en valeurs les scores, sous la forme d'entiers.
#Le fichier n'existe pas. Là, on crée un dictionnaire vide, aucun score n'a été trouvé.
#Le joueur n'est pas dans le dictionnaire. Dans ce cas, on l'ajoute avec un score de 0.







os.system("pause")










