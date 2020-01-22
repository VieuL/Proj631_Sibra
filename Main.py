# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:00:36 2020

@author: vieul
"""
from Classe import *

# =============================================================================
# Importation des données
# =============================================================================

# Importation des données
data_file_name = 'E://0_travail//Proj631_Sibra//data//1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = 'E://0_travail//Proj631_Sibra//data//2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r',encoding = 'utf-8') as f:
        content = f.read()

except OSError:
    # 'File not found' error message.
    print("File not found")

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic

slited_content = content.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

try:
    with open(data_file_name2, 'r',encoding = 'utf-8') as f:
        content2 = f.read()

except OSError:
    # 'File not found' error message.
    print("File not found")


slited_content2 = content2.split("\n\n")
regular_path2 = slited_content2[0]
regular_date_go2 = dates2dic(slited_content2[1])
regular_date_back2 = dates2dic(slited_content2[2])
we_holidays_path2 = slited_content2[3]
we_holidays_date_go2 = dates2dic(slited_content2[4])
we_holidays_date_back2 = dates2dic(slited_content2[5])


# =============================================================================
# Création des graphes
# =============================================================================
ligne1 = Ligne(1)
ligne2 = Ligne(2)


def ajout_arrets_ligne(path,ligne):
    """
    Rajoute l'ensemble des arrets de bus dans un objet de type Ligne
    """
    # Création de tout les arrets
    path = path.replace('+','N')
    path = path.split(' N ')
    
#    for u in range(len(path)):
#        path[u] = path[u].lower()
#    # Ajout des arrets dans le ligne 1
    ligne.set_arrets(path)  

        
def création_var_arret(ligne,pre,date_n_go,date_wk_go):
    """
    Crée des variables de classe Arret et ajoute le nom de l'arret
    
    """
    for i in range(len(ligne.arrets)):
        globals()[str(pre) + str(i)] = Arret(ligne.arrets[i])
        globals()[str(pre) + str(i)].set_heure_normal_go(date_n_go[ligne.arrets[i]])
        globals()[str(pre) + str(i)].set_heure_wk_go(date_wk_go[ligne.arrets[i]])

        


        

    

ajout_arrets_ligne(regular_path,ligne1)
ajout_arrets_ligne(regular_path2,ligne2)
l1 = création_var_arret(ligne1,'varl1_',regular_date_go,we_holidays_date_go)
l2 = création_var_arret(ligne2,'varl2_',regular_date_go2,we_holidays_date_go2)



































