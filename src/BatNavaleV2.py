import numpy as np
import random

def initialiserEcran():
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)

    for i in range(65,75):
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
        print(chr(i),"|   |   |   |   |   |   |   |   |   |   |")
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
    
def afficheGrilleJoueur(A):
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)
    k=65
    for i in range(10):
        B=[]
        for j in range(10):
            if A[i][j]==0:
                B.append(" ")
            if A[i][j]==1:
                B.append("B")
            elif A[i][j]==2:
                B.append("T")
            elif A[i][j]==3:
                B.append("S")
            elif A[i][j]==4:
                B.append("C")
            elif A[i][j]==5:
                B.append("P")
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )
        print(chr(k),"|",B[0],"|",B[1],"|",B[2],"|",B[3],"|",B[4],"|",B[5],"|",B[6],"|",B[7],"|",B[8],"|",B[9],"|")
        k+=1
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )


def placerBateauJoueur(A):
    i=1
    while i<=5:
        if i==1:
            NomBateau="Barque"
        elif i==2:
            NomBateau="Torpilleur"
        elif i==3:
            NomBateau="Sous-marin"
        elif i==4:
            NomBateau="Croiseur"
        else:
            NomBateau="Porte-avion"
        print("\n Où voulez-vous placer votre", NomBateau,"(", i, "case(s) ) ?")
        abscisse=input("Ligne (lettre): ")
        a=ord(abscisse)-ord("A")
        ordonnee=int(input("Colonne (chiffre): "))
        b=ordonnee-1  #b=0 pour "A", b=1 pour "B",...
        choix=input("Horizontale(H)/ Verticale(V): ")
        n=0
        if choix=="H":
            if b+i-1<=9 and 0<=a<=9 and 0<=b<=9:     #verifie si le dernier terme est dans la liste et si les coordonnées sont correctes
                for k in range(i):
                    if A[a][b+k]==0:
                        n+=1   #afin de savoir si toutes les cases sont vides
                if n==i:  #si c'est vide on peut les remplir
                    for k in range(i):
                        A[a][b+k]=i
                else: 
                    print("\n Des cases sont déjà prises, recommencez.")
                    i-=1      #sinon on recommence i (comme on ajoute +1 plus tard alors je retire -1 pour compenser)
            else: 
                print("\n Il n'y a pas assez de cases pour le placer, recommencez.")
                i-=1
        elif choix=="V":
            if a+i-1<=9 and 0<=a<=9 and 0<=b<=9:
                for k in range(i):
                    if A[a+k][b]==0:
                        n+=1
                if n==i:
                    for k in range(i):
                        A[a+k][b]=i
                else: 
                    print("\n Des cases sont déjà prises, recommencez.")
                    i-=1
            else: 
                print("\n Il n'y a pas assez de cases pour le placer, recommencez.")
                i-=1
        else:
            print("Votre saisie est incorrect, recommencez.")
            i-=1
        i+=1
        afficheGrilleJoueur(A)
        


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

    
def afficheEcransDouble(EcranJoueur,EcranOrdi):
    i=1
    print("   ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9,"        ",i, " ",i+1, " ",i+2, " ",i+3, " ",i+4, " ",i+5, " ",i+6, " ",i+7, " ",i+8, " ",i+9)
    k=65
    for n in range(10):
        B=[] #pour les lignes du joueur
        C=[] #pour les lignes de l'ordi
        for m in range(10):
            if EcranJoueur[n][m]==0:
                B.append(" ")
            elif EcranJoueur[n][m]==1:
                B.append("B")
            elif EcranJoueur[n][m]==2:
                B.append("T")
            elif EcranJoueur[n][m]==3:
                B.append("S")
            elif EcranJoueur[n][m]==4:
                B.append("C")
            elif EcranJoueur[n][m]==5:
                B.append("P")
            elif EcranJoueur[n][m]==10:
                B.append("*")
            elif EcranJoueur[n][m]==11:
                B.append("+")
            else:      #EcranJoueur[n][m]==12:
                B.append("X")
                
            if EcranOrdi[n][m]==0:
                C.append(" ")
            elif EcranOrdi[n][m]==10:
                C.append("*")
            elif EcranOrdi[n][m]==11:
                C.append("+")
            else:      #EcranOrdi[n][m]==12:
                C.append("X")
    
        print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ","  ","  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print(chr(k),"|",C[0],"|",C[1],"|",C[2],"|",C[3],"|",C[4],"|",C[5],"|",C[6],"|",C[7],"|",C[8],"|",C[9],"|","   ",chr(k),"|",B[0],"|",B[1],"|",B[2],"|",B[3],"|",B[4],"|",B[5],"|",B[6],"|",B[7],"|",B[8],"|",B[9],"|")
        k+=1
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ","  ","  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " )


def jouer(Jeu,JeuInitial,E,i,j,B,T,S,C,P):
    elmt=Jeu[i][j]
    if elmt==1:
        message="Coulé !"
        print(message) #on a touché la barque
        Jeu[i][j]=100
    elif elmt==2:
        Jeu[i][j]=100
        if T==0:
            message="Coulé !"
            print(message)
        else: 
            message="Touché !"
            print(message)
    elif elmt==3:
        Jeu[i][j]=100
        if S==0:
            message="Coulé !"
            print(message)
        else: 
            message="Touché !"
            print(message)
    elif elmt==4:
        Jeu[i][j]=100
        if C==0:
            message="Coulé !"
            print(message)
        else: 
            message="Touché !"
            print(message)
    elif Jeu[i][j]==5:
        Jeu[i][j]=100
        if P==0:
            message="Coulé !"
            print(message)
        else: 
            message="Touché !"
            print(message)
    elif Jeu[i][j]==0:
        Jeu[i][j]=100
        message="Manqué !"
        print(message)
    else: #c'est-a-dire si Jeu==100
        message="Manqué, case déjà jouée.."
        print(message)
    print("\n")
    
    if message=="Manqué !":
        E[i][j]=10
    if message=="Touché !":
        E[i][j]=11
    if message=="Coulé !":
        for n in range(10):
            for m in range(10):
                if JeuInitial[n][m]==elmt:
                    E[n][m]=12
    afficheEcransDouble(EcranJoueur,EcranOrdi)
    if P==0 and C==0 and S==0 and T==0 and B==0:
        return True
    else: return False
    
 
#Bataille Navale Version 2:  

EcranOrdi=np.zeros((10,10))
JeuOrdi=np.zeros((10,10))
JeuJoueur=np.zeros((10,10))
initialiserEcran()
placerBateauJoueur(JeuJoueur)
JeuJoueurInitial=JeuJoueur.copy()
EcranJoueur=JeuJoueur.copy()
placerBateauOrdi(JeuOrdi)
JeuOrdiInitial=JeuOrdi.copy()
PorteAvionOrdi=5
CroiseurOrdi=4
SousMarinOrdi=3
TorpilleurOrdi=2
BarqueOrdi=1
PorteAvionJoueur=5
CroiseurJoueur=4
SousMarinJoueur=3
TorpilleurJoueur=2
BarqueJoueur=1
FinJeu=False
QuiJoue=random.randint(1,2) #j'ai decide que le joueur joue pour les nombres pairs et l'ordi les nombres impairs
print("\n")
afficheEcransDouble(EcranJoueur,EcranOrdi)
while (FinJeu==False):
    if QuiJoue%2==0:
        print("\n Dans quelle case voulez-vous jouer?")
        abscisse=input("Ligne (lettre): ")
        i=ord(abscisse)-ord("A")
        ordonnee=int(input("Colonne (chiffre): "))
        print("\n")
        j=ordonnee-1
        if i>=0 and i<=9 and j>=0 and j<=9:
            if JeuOrdi[i][j]==1:
                BarqueOrdi-=1
            elif JeuOrdi[i][j]==2:
                TorpilleurOrdi-=1
            elif JeuOrdi[i][j]==3:
                SousMarinOrdi-=1
            elif JeuOrdi[i][j]==4:
                CroiseurOrdi-=1
            elif JeuOrdi[i][j]==5:
                PorteAvionOrdi-=1
            FinJeu=jouer(JeuOrdi,JeuOrdiInitial,EcranOrdi,i,j,BarqueOrdi,TorpilleurOrdi,SousMarinOrdi,CroiseurOrdi,PorteAvionOrdi)
            JoueurSuivant=input("\n Pour continuer appuyez sur 'Entrer'...")
        else: 
            print("Votre tir n'est pas correct, veuillez rejouer. ")
            QuiJoue-=1   #car il y a une incrémentation de +1 après
    else:
        print("\n\n L'ordinateur joue:\n")
        i=random.randint(0,9)
        j=random.randint(0,9)
        if JeuJoueur[i][j]==1:
            BarqueJoueur-=1
        elif JeuJoueur[i][j]==2:
            TorpilleurJoueur-=1
        elif JeuJoueur[i][j]==3:
                SousMarinJoueur-=1
        elif JeuJoueur[i][j]==4:
            CroiseurJoueur-=1
        elif JeuJoueur[i][j]==5:
            PorteAvionJoueur-=1
        FinJeu=jouer(JeuJoueur,JeuJoueurInitial,EcranJoueur,i,j,BarqueJoueur,TorpilleurJoueur,SousMarinJoueur,CroiseurJoueur,PorteAvionJoueur)
        JoueurSuivant=input("\n Pour continuer appuyez sur 'Entrer'...")
    QuiJoue+=1
if QuiJoue%2==0:   #c'est a dire si le jeu s'est fini par l'ordinateur
    print("L'ordinateur a gagné !!!")
else: print("Vous avez gagné, félicitations !!!")

