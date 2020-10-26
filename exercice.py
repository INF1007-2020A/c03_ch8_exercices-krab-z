#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Écrire un programme qui compare le contenu de deux fichiers et signale la première différence rencontrée.



# TODO: Importez vos modules ici
from os.path import getsize


# TODO: Définissez vos fonction ici
def compare(fichier1, fichier2):
    
    if getsize(fichier1)!=getsize(fichier2):
        print("Les fichiers sont de tailles différentes.") #ou 
    
    with open(fichier1,"r") as f, open(fichier2, "r") as p:
        c=f.read(1)
        k=p.read(2)
        while c!='' and k!='':
            if c!=k:
                position=f.tell()
                print(f"La difference est à la position {position} entre {c} entre {k}")
                break
            c=f.read(1)
            k=p.read(1)        
            
 def nombres(fname):
    with open(fname,mode="r") as f:
        donnees=f.read()
    liste_nombres=sorted([int(mot) for mot in donnees.split() if mot.isdigit()])
   #append(mot)
   #liste_nombres.sort(key=lambda x:int(x))
    print(liste_nombres)
        

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare(fichier1='exemple.txt', fichier2='exemple2.txt')
    nombres(fname="exemple.txt")
