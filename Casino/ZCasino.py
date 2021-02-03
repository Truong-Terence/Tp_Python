# -*- coding: utf-8 -*-


                            # Programme de la roulette

#Imports
import os
from random import  *
from math import *

#Ajout des booléens
pairroulette = False
pairjoueur = False

#Partie joueur
#Variable de la bourse hors boucle
argent = 1000
argent = int(argent)

#Boucle de base pour rejouer tant qu'on a de l'argent
while 0 < argent:

    #Boucle d'input avec les essais et le retour si mauvaise saisie.
    while 0 < argent:
        bet = input("La roulette va de 0 à 49. Faites vos jeux ! Vous pariez sur le : ")
        mise = input("Maintenant, déposez votre mise : ")
        mise = int(mise)
        
      #Bloc try pour le test du bloc qui suit 
        try:
            bet = int(bet)
            mise = int(mise)
            assert 0 <= bet < 50#assert : conditions imposées
            assert 0 < mise
        except NameError:#Relevée d'erreur sans stopper le programme
            print("La valeur n'a pas été définie.")
            continue#Retour boucle pour garder le contrôle sur les exceptions
        except ValueError:
            print("Vous n'avez pas saisi un nombre")
            continue
        except AssertionError:
            print("Cela ne fait pas partie de vos choix")
            continue
        if mise > argent:#Condition supplémentaire avant de continuer le programme
            print("Pas de ça chez nous !")
            continue
        else:#Si pas d'erreur de saisie, opération sur l'argent de base et fin de la boucle
            print("Vous avez misé", mise, "$ sur le", bet, "!")
            argent -= mise
            break
        
    
    #Partie random
    
    a = randrange(50)# Random de 0 à 49. Pour un dé : randrange(1, 7) de 1 à 6
    
    if bet % 2 == 0:#Si le joueuer à parier sur un nombre pair
        pairjoueur = False#Application du booléen
    else:
        pairjoueur = True
    
    if a % 2 == 0:#Idem pour la randomisation, ajour des couleurs au pair/impair
        pairroulette = False
        print("La roulette annonce :", a, " noir.")
    else:
        pairroulette = True
        print("La roulette annonce :", a, " rouge")
    
    if bet == a:
        gain = mise*3
        print("Woaw ! Vous empochez trois fois la mise, soit : ", mise, "$")
    elif pairroulette == 0 and pairjoueur == 0:#Si les deux sont pairs donc noirs.
        gain = ceil(mise/2)#Arrondi au suppérieur
        print("Noir, récupérez la moitié de la mise : ", mise, "$")
    elif pairroulette == 1 and pairjoueur == 1:#Idem impair rouge
        gain = ceil(mise/2)#Mise à jour de la valeur du gain
        print("Rouge, récupérez la moitié de la mise : ", mise, "$")
    else:
        print("Perdu ! File les ", mise, "$ baltringue !")
        gain = 0
    
    argent += gain#Mise à jour du portefeuille
    print("Portefeuille : ", argent, "$")

    while 1:#Boucle de retry ou de mauvaise réponse
        reponse = input("Rejouer ? (o ou n) ")
        if reponse == "o":
            print("Okey !")
            break
        elif reponse == "n":
            print("Okey ... :\'( ")
            break
        else:
            print("T'es con ou quoi ?")
            continue
        
    if reponse == "n":#Fermeture programme
        break
    


os.system("pause")#Ne ferme pas le programme automatiquement








 