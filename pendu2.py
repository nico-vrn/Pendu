from random import choice
import os

def dessinPendu(nb):
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]

liste_mots=''
lg_restant=''
mot=''
lettre=''
mot_deja_pris=[]
score=0
score1=0
score2=0
parti=0

def user():
    global username1
    global username2
    if nombrej=='solo':
        username1=input('Choisi ton pseudo joueur1?:')
    else:
        username1=input('Choisi ton pseudo joueur1?:')
        username2=input('Choisi ton pseudo joueur2?:')
        if username2==username1:
            print('ce nom est déjà pris')
            user()

def choisir_mot():
    global liste_mots
    global mot
    fichier = open('fr.txt', "r") #ouvre le fichier
    contenuFichier = fichier.read() #lis le contenu
    fichier.close() #le ferme
    contenuFichier = contenuFichier.lower().replace("é", "e").replace("è", "e").replace("ë", "e").replace(
        "à", "a").replace("ç", "c").replace("ê", "e").replace("â", "a").replace("î", "i").replace("ï", "i").replace("ô","o")
    liste_mots = contenuFichier.split("\n") #en fait une liste en splitant
    if nombrej=='solo':
        mot=choice(liste_mots) #mot dans la liste en aléatoire
        if mot in mot_deja_pris:
            choisir_mot()
        else:
            mot_deja_pris.append(mot)

    else:
        print('a {} de choisir un mot,'.format(username1))
        choix=input('choisis un mot qui existe (sans majuscule ni accent):').lower()
        if choix in mot_deja_pris:
            print('tu as déjà choisi ce mot')
            choisir_mot()
        elif choix in liste_mots:
            print('Ce mot est correct, commençons')
            mot=choix
            mot_deja_pris.append(mot)
        else:
            print('Le mot {} n\'existe pas, réessai'.format(choix))
            choisir_mot()

def lettre_saisie():
    global lettre
    global coups
    lettre1=input('Tape une lettre:').lower()
    if len(lettre1)>1 or not lettre1.isalpha():
        print('Cette lettre n\'est pas valide')
        lettre_saisie()
    else:
        coups +=1
        lettre=lettre1

def bonne_lettre(lettre,mot):
    global erreur
    if lettre in lettre_dite:
        return 'tu as déjà proposer ceci'
    elif lettre in mot:
        lettre_trouvees.append(lettre)
        lettre_dite.append(lettre)
        return 'Bien joué'
    elif not lettre in mot:
        lettre_dite.append(lettre)
        erreur +=1
        return 'mauvaise lettre'

def masquer_mot(mot):
    mot_masquer=''
    for lettre in mot:
        if lettre in lettre_trouvees:
            mot_masquer+=lettre
        else:
            mot_masquer+='_'
    return mot_masquer

def champion(mot):
    global lg_restant
    lg1=len(mot)
    lg2=0
    lg_restant=len(mot)
    for lettre in mot:
        if lettre in lettre_trouvees:
            lg2 +=1
            lg_restant-=1
        else:
            pass
    return lg1==lg2

def rejouera(end):
    global gagner, username1, username2, score, score1, score2, parti
    if nombrej=='solo':
        if gagner:
            score+=1
            print('Tu as gagné! en {} coups, tu as augmenter ton score est de {}'.format(coups, score))
            rejouer=input('veux tu rejouer? (oui ou non):')
        else:
            print('Tu as perdu en {} coups, ton score de {} n\'a pas changer.. le mot était \'{}\' réessai'.format(coups, score, mot))
            rejouer=input('veux tu réessayer? (oui ou non):')

    else:
        if gagner:
            if parti==0:
                score2+=1
                print('Tu as gagné! en {} coups, le score de {} est de {} et le score de {} est de {}'.format(coups, username1, score1, username2, score2))
            else:
                score1+=1
                print('Tu as gagné! en {} coups, le score de {} est de {} et le score de {} est de {}'.format(coups, username2, score1, username1, score2))
            rejouer=input('voulez-vous continuer? (oui ou non):')
        else:
            if parti==0:
                score1+=1
                print('Tu as perdu en {} coups, le score de {} n\'a pas changer mais {} est maintenant à {}.. le mot était \'{}\' réessayez'.format(coups,username2, username1, score1, mot))
            else:
                score2+=1
                print('Tu as perdu en {} coups, le score de {} n\'a pas changer mais {} est maintenant à {}.. le mot était \'{}\' réessayez'.format(coups,username2, username1, score2, mot))
            rejouer=input('voulez-vous réessayer? (oui ou non):')

    if rejouer=='oui':
        if nombrej=='solo':
            os.system('cls')
            print('nouvelle partie!!')
            gagner=True
        else:
            os.system('cls')
            print('nouvelle parti, ON CHANGE LES ROLES!')
            username1, username2= username2, username1
            gagner=True
            if parti==1:
                parti=0
            else:
                parti=1
    elif rejouer!='oui' and rejouer!='non':
        print('ce n\'est pas valide')
        rejouera(end)
    else:
        print('a bientôt!')
        end=False
        exit()
        return end


print('Bienvenue sur le jeu du pendu!')
def nombre():
    global nombrej
    nombrej=input('tu veux jouer seul ou a deux? (solo, duo):')
    if nombrej!='solo' and nombrej!='duo':
        print('ce n\'est pas valable')
        nombre()

nombre()
user()
gagner=True
end=True
while end!=False :
    choisir_mot()
    print(mot)
    coups=0
    lettre_trouvees=[]
    lettre_dite=[]
    erreur=0
    while not champion(mot) and gagner:
        if nombrej=='solo':
            print('Tu peux commencer {}, voici le mot à trouver {}, il reste {} lettres à trouver'.format(username1, masquer_mot(mot), lg_restant))
        else:
            print('a {}, voici le mot à trouver: {}, il reste {} lettres à trouver'.format(username2, masquer_mot(mot), lg_restant))
        lettre_saisie()
        print(bonne_lettre(lettre,mot))
        champion(mot)
        print(dessinPendu(erreur))
        if erreur==6:
            gagner=False

    if gagner:
        end=rejouera(end)
    else:
        end=rejouera(end)
