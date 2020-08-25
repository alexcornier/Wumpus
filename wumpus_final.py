############## IMPORTATION DES MODULES NECESSAIRES ####################
from random import choice
import sys

############## CREATION DE LA GROTTE, DU personnage["joueur"] ET DES AUTRES PERSONNAGES ##############
#### Stocker les perso puis les réutiliser tour-par-tour (dico) ####
grotte=[None,[2,3,4], [1,5,8], [1,6,7], [1,7,8], [2,9,10], [3,9,11], [3,4,11], [2,4,10], [5,6,12], [5,8,12], [6,7,12], [9,10,11]]

def creation_personnage():
    personnage={}
    index_liste=range(1,12)
    personnage["joueur"] = choice(index_liste)
    personnage["wumpus"] = choice(index_liste)
    while personnage["wumpus"]==personnage["joueur"]:
        personnage["wumpus"]=choice(index_liste)
    personnage["chauve_souris"]=choice(index_liste)
    while (personnage["joueur"]==personnage["chauve_souris"] or personnage["wumpus"]==personnage["chauve_souris"]) :
        personnage["chauve_souris"]=choice(index_liste)
    personnage["chauve_souris1"]=choice(index_liste)
    while (personnage["joueur"]==personnage["chauve_souris1"] or personnage["wumpus"]==personnage["chauve_souris1"] or personnage["chauve_souris"]==personnage["chauve_souris1"]) :
        personnage["chauve_souris1"]=choice(index_liste)
    personnage["puits"]=choice(index_liste)
    while (personnage["joueur"]==personnage["puits"] or personnage["wumpus"]==personnage["puits"] or personnage["chauve_souris"]==personnage["puits"] or personnage["chauve_souris1"]==personnage["puits"]) :
        personnage["puits"]=choice(index_liste)
    personnage["puits1"]=choice(index_liste)
    while (personnage["joueur"]==personnage["puits1"] or personnage["wumpus"]==personnage["puits1"] or personnage["chauve_souris"]==personnage["puits1"] or personnage["chauve_souris1"]==personnage["puits1"] or personnage["puits"]==personnage["puits1"]):
        personnage["puits1"]=choice(index_liste)
    return personnage


############## ACCUEIL DU JOUEUR ##################
print ("""
.==============================================.
|  __    __                     ___            |
| / / /\ \ \_   _ _ __ ___     / _ \_   _ ___  |
| \ \/  \/ / | | | '_ ` _ \   / /_)/ | | / __| |
|  \  /\  /| |_| | | | | | | / ___/| |_| \__ \ |
|   \/  \/  \__,_|_| |_| |_| \/     \__,_|___/ |
|                                              |
'=============================================='
""")

print("Quel est votre prénom ?")
prenom=input()
print (prenom,"vous êtes tombé(e) dans la grotte du Wumpus !")
print("Vous disposez de 3 flèches pour abattre le Wumpus. Les puits sont distingables par le bruit des gouttes d'eau ; les chauves-souris par leurs battements d'ailes et le Wumpus par son grognement")

############## INFORMATIONS TOUR-PAR-TOUR ##################
def affichageCave(personnage):
    cave=list(range(1,13))
    position=personnage["joueur"]
    for i in range(len(cave)):
        if position==cave[i]:
            cave[i]="J" 

    print("""                                                                                            
                                                                                                      _______
                                                                                                     |       |
                                                                                  ___________________|  """,cave[0],"""  |__________________
                                                                             ____|                   |_______|                  |___    
                                                                            |                            |                          |
                                                                     _______|                         ___|___                       |___________           
                                                                 ___|___            _______        __|       |__         _______             ___|___
                                                                |       |          |       |______|  |  """,cave[3],"""  |  |_______|       |           |       |
                                                                |  """,cave[2],"""  |__________|  """,cave[6],"""  |         |_______|          |  """,cave[7],"""  |___________|  """,cave[1],"""  |
                                                                |_______|          |_______|                            |_______|           |_______|
                                                                    |                  |                                    |                   |
                                                                 ___|___            ___|___                              ___|___             ___|___
                                                                |       |          |       |          _______           |       |           |       |                
                                                                |  """,cave[5],"""  |__________|  """,cave[10],""" |_______  |       |   _______| """,cave[9],"""  |___________|  """,cave[4],"""  |
                                                                |_______|          |_______|      |__|  """,cave[11],""" |__|       |_______|           |_______|     
                                                                    |                                |_______|                                  |
                                                                    |_______                             |                            __________|
                                                                            |                         ___|___                        |
                                                                            |_____                   |       |                   ____|
                                                                                  |__________________|  """,cave[8],"""  |__________________|
                                                                                                     |_______|""")

def infosJoueur(personnage):
    print("\nVous êtes actuellement dans la grotte",personnage["joueur"])
    print("Les caves adjacentes sont",grotte[personnage["joueur"]][0],'-',grotte[personnage["joueur"]][1],'-',grotte[personnage["joueur"]][2])
    if (grotte[personnage["joueur"]][0]==personnage["puits1"] or grotte[personnage["joueur"]][1]==personnage["puits1"] or grotte[personnage["joueur"]][2]==personnage["puits1"] or grotte[personnage["joueur"]][0]==personnage["puits"] or grotte[personnage["joueur"]][1]==personnage["puits"] or grotte[personnage["joueur"]][2]==personnage["puits"]):
        print (prenom,"ne serait-ce pas le bruit de gouttes d'eau ?")
    if (grotte[personnage["joueur"]][0]==personnage["chauve_souris"] or grotte[personnage["joueur"]][1]==personnage["chauve_souris"] or grotte[personnage["joueur"]][2]==personnage["chauve_souris"] or grotte[personnage["joueur"]][0]==personnage["chauve_souris1"] or grotte[personnage["joueur"]][1]==personnage["chauve_souris1"] or grotte[personnage["joueur"]][2]==personnage["chauve_souris1"]):
        print (prenom,"quelque chose vole à côté !")
    if (grotte[personnage["joueur"]][0]==personnage["wumpus"] or grotte[personnage["joueur"]][1]==personnage["wumpus"] or grotte[personnage["joueur"]][2]==personnage["wumpus"]):
        print("Ce n'est pas pour vous faire peur",prenom,"mais je crois avoir entendu un grognement...")
    print("Votre localisation est indiquée par la lettre J : ")
    affichageCave(personnage)



############## GESTION DES ERREURS ##################
gestion_erreur=range(1,13)

def gestionErreurSaisie(saisie):
    try:
        valeur=int(saisie)
        return valeur
    except ValueError:
        return 0


############## ACTIONS DU JOUEUR ##################
def obtenirChoix():
    print("Que voulez-vous faire",prenom,"? Tirer (T) ou avancer (A) ?")
    choix=input().upper()
    while choix not in ['T','A']:
        choix=input("Euh...C'est A ou T \nTirer (T) ou avancer (A) ? : ").upper()
    return choix


def realiserChoix(personnage):
    action=obtenirChoix()
    if action=='T' and fleche > 0:
        return tirer(personnage)
    else:
        return avancer(personnage)
 


##### DEPLACEMENT #####
def avancer(personnage):
    print("Vers quelle caverne se déplacer",prenom,"? :", grotte[personnage["joueur"]][0],'-',grotte[personnage["joueur"]][1],'ou',grotte[personnage["joueur"]][2])
    choix=None
    while choix not in grotte[personnage["joueur"]]:
        choix=gestionErreurSaisie(input("Choix : "))
        if choix not in gestion_erreur:
            print("Il faut saisir un nombre !")
    if (choix==personnage["chauve_souris"] or choix==personnage["chauve_souris1"]):
        print (prenom,", vous avez été attrapé(e) par une chave-souris ! Vous vous envolez !")
        return caverneChauveSouris(personnage)
    if (choix==personnage["puits1"] or choix==personnage["puits"]):
        print ("...oh non un puits !!!...Cependant,",prenom,"vous êtes sauvé(e), vous vous êtes accroché(e) à une flèche ! Ouf !\n Ah non, elle rompt. Vous êtes mort(e)")
        sys.exit(0)
    if choix==personnage["wumpus"]:
        print("....GRRRRRRRRRRRRRRRRRRRRR \nLe Wumpus vous attrapé ! Il passe à table... \nVous êtes mort(e)")
        sys.exit(0)
    personnage["joueur"]=choix
    return personnage


def caverneChauveSouris(personnage):
    pos_joueur=0
    index_liste=range(1,12)
    pos_joueur=personnage["joueur"]
    personnage["joueur"]=choice(index_liste)
    while pos_joueur==personnage["joueur"]:
        personnage["joueur"]=choice(index_liste)
    return personnage



##### TIR ##### 
def deplacementWumpus(personnage):
    voisin_wumpus=grotte[personnage["wumpus"]]
    personnage["wumpus"]=choice(voisin_wumpus)
    if personnage["wumpus"]==personnage["joueur"]:
        print("Oh, quel tir ! C'est loupé !... \nLe Wumpus se déplace...vers vous !! Il peut passer en cuisine... \nVous êtes mort(e)")
        sys.exit(0)
    else:
        print("Le Wumpus s'est déplacé, mais il ne doit pas être très loin")
    return personnage


def tirer(personnage):
    global fleche
    print("Vers quelle caverne tirer",prenom,"? :", grotte[personnage["joueur"]][0],'-',grotte[personnage["joueur"]][1],'-',grotte[personnage["joueur"]][2])
    choix_tir=None
    while choix_tir not in grotte[personnage["joueur"]]:
        choix_tir=gestionErreurSaisie(input("Choix : "))
        if choix_tir not in gestion_erreur:
            print("Il faut saisir un nombre !")   
    if choix_tir==personnage["joueur"]:
        print(prenom,"vous avez abattu le Wumpus ! Vous êtes libre ! \n Vous avez gagné(e) !")
        sys.exit(0)
    if (personnage["joueur"]==grotte[personnage["joueur"]][0] or personnage["wumpus"]==grotte[personnage["joueur"]][1] or personnage["wumpus"]==grotte[personnage["joueur"]][2]):
        return deplacementWumpus(personnage)
    else:
        print("Et une flèche de gaspillée !")
    fleche=fleche-1
    print(prenom,'il vous reste',fleche,"flèche(s)")
    if fleche==0:
        print(prenom,"vous n'avez plus de flèche. Le Wumpus l'a compris et vous a dévoré. \nVous êtes mort(e)")
        sys.exit(0)
    return fleche


############## PROGRAMME PRINCIPAL ##############
def main():
    a=creation_personnage()
    global fleche
    fleche=3
    while True:
        infosJoueur(a)
        realiserChoix(a)

main()