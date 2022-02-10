## height :int , width:int , leaves = liste de liste , wind : str 
import numpy as np
def count_leaves(hauteur:int, profondeur:int, feuille:list, vent:str) :
    """
    example : hauteur = profondeur = 4
    feuille = np.random.randint(0 , 3, size=(hauteur, profondeur))
    mouvement = "RRD" --> les 3 premieres lignes + 2 premieres colonnes
    """
    grille = np.zeros((hauteur, profondeur))
    feuille = np.array(feuille)
    for mouvement in vent :
        print(mouvement)
        if mouvement == "R" :
            grille[:, 1: ] = feuille[:, :profondeur-1]
            grille[: , 0] = 0
        if mouvement == "L" :
            grille[:, :profondeur -1 ] = feuille[:, 1:]
            grille[: , -1] = 0
            
        if mouvement == "U" :
            grille[: hauteur -1 , :] = feuille[1:,:]
            grille[-1 , :] = 0
        if mouvement == "D" :
            grille[1: , :] = feuille[:hauteur-1,:]
            grille[0 , :] = 0
        # mise à jour de l'emplacement des feuilles
        feuille = grille
    return feuille.sum()
