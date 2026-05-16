import numpy as np
import random


def placerBateauOrdi(A):
    i=1
    while i<=5:
        a=random.randint(0,9)
        b=random.randint(0,9)
        choix=random.randint(0,1) #0 pour verticale,1 pour horizontale
        n=0
        if choix==1:
            if b+i-1<=9:     #verifie si le dernier terme est dans la liste
                for k in range(i):
                    if A[a][b+k]==0:
                        n+=1   #afin de savoir si toutes les cases sont vides
                if n==i:  #si c'est vide on peut les remplir
                    for k in range(i):
                        A[a][b+k]=i
                else: i-=1      #sinon on recommence i (comme on ajoute +1 plus tard alors je retire -1 pour compenser)
            else: i-=1
        else:
            if a+i-1<=9:
                for k in range(i):
                    if A[a+k][b]==0:
                        n+=1
                if n==i:
                    for k in range(i):
                        A[a+k][b]=i
                else: i-=1
            else: i-=1
        i+=1


def initialiserEcran():
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)

    for i in range(65,75):
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
        print(chr(i),"|   |   |   |   |   |   |   |   |   |   |")
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )


#La fonction qui suit m'a permis de suivre l'évolution de la grille de l'ordi pendant
#que j'éditais mon programme
#Elle n'intervient pas dans le programme du jeu
def afficheGrilleOrdi(A):
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)
    k=65
    for i in range(10):
        B=[]
        for j in range(10):
            if A[i][j]==0:
                B.append(" ")
            else:
        #if A[i][j]==1 or A[i][j]==2 or A[i][j]==3 or A[i][j]==4 or A[i][j]==5:
                B.append("@")
    
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
        print(chr(k),"|",B[0],"|",B[1],"|",B[2],"|",B[3],"|",B[4],"|",B[5],"|",B[6],"|",B[7],"|",B[8],"|",B[9],"|")
        k+=1
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )


    
def afficheEcran(E):
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)
    k=65
    for n in range(10):
        B=[]
        for m in range(10):
            if E[n][m]==0:
                B.append(" ")
            elif E[n][m]==1:
                B.append("*")
            elif E[n][m]==2:
                B.append("+")
            else:      #E[n][m]==3:
                B.append("X")
    
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
        print(chr(k),"|",B[0],"|",B[1],"|",B[2],"|",B[3],"|",B[4],"|",B[5],"|",B[6],"|",B[7],"|",B[8],"|",B[9],"|")
        k+=1
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )


def jouerJoueur(Jeu,JeuInitial,E,i,j):
    elmt=Jeu[i][j]
    if elmt==0:
        message="Manqué"
        print(message)
        Jeu[i][j]=100
    elif elmt==1:
        message="Coulé"
        print(message) #on a touché la barque
        Jeu[i][j]=100
    elif elmt==2:
        Jeu[i][j]=100
        if Torpilleur==0:
            message="Coulé"
            print(message)
        else: 
            message="Touché"
            print(message)
    elif elmt==3:
        Jeu[i][j]=100
        if SousMarin==0:
            message="Coulé"
            print(message)
        else: 
            message="Touché"
            print(message)
    elif elmt==4:
        Jeu[i][j]=100
        if Croiseur==0:
            message="Coulé"
            print(message)
        else: 
            message="Touché"
            print(message)
    elif elmt==5:
        Jeu[i][j]=100
        if PorteAvion==0:
            message="Coulé"
            print(message)
        else: 
            message="Touché"
            print(message)
    else: #c'est-a-dire si Jeu[i][j]==100
        message="Manqué, vous aviez déjà joué cette case.."
        print(message)
    print("\n")
    
    if message=="Manqué":
        E[i][j]=1
    if message=="Touché":
        E[i][j]=2
    if message=="Coulé":
        for n in range(10):
            for m in range(10):
                if JeuInitial[n][m]==elmt:
                    E[n][m]=3
    
    afficheEcran(E)
    if PorteAvion==0 and Croiseur==0 and SousMarin==0 and Torpilleur==0 and Barque==0:
        return True
    else: return False
    
    
#Bataille Navale Version 1:
    
Jeu=np.zeros((10,10))
Ecran=np.zeros((10,10))
placerBateauOrdi(Jeu)
JeuInitial=Jeu.copy()
initialiserEcran()
PorteAvion=5
Croiseur=4
SousMarin=3
Torpilleur=2
Barque=1
FinJeu=False
while(FinJeu==False):
    print("\n Dans quelle case voulez-vous jouer?")
    abscisse=input("Ligne (lettre): ")
    i=ord(abscisse)-ord("A")
    ordonnee=int(input("Colonne (chiffre): "))
    print("\n")
    j=ordonnee-1
    if 0<=i<=9 and 0<=j<=9: #vérifie si les coordonées sont dans le tableau
        if Jeu[i][j]==1:
            Barque-=1
        elif Jeu[i][j]==2:
            Torpilleur-=1
        elif Jeu[i][j]==3:
            SousMarin-=1
        elif Jeu[i][j]==4:
            Croiseur-=1
        elif Jeu[i][j]==5:
            PorteAvion-=1
        FinJeu=jouerJoueur(Jeu,JeuInitial,Ecran,i,j)
    else: print("Votre tir n'est pas correct, veuillez rejouer. ")
print("\n Le jeu est fini.")
        
