# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:00:36 2020

@author: vieul
"""
from Classe import *
import datetime

# =============================================================================
# Importation des données
# =============================================================================

# Importation des données
data_file_name = '1_Poisy-ParcDesGlaisins.txt'
data_file_name2 = '2_Piscine-Patinoire_Campus.txt'

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
def transforme_en_heur(liste):
    '''
    Cette fonction prends en paramètre une liste comportant des str aux format HH:MM ou des '-'
    elle retourne une liste avec d'heur de type heur
    !! La package datetime est obligatoire !!
    
    '''
    a = []
    
    for u in liste:
        if u != '-':
            a.append(datetime.datetime.strptime(u, '%H:%M'))
        else: 
            a.append(u)
    return a
        
def creation_var_arret(ligne,pre,date_n_go,date_wk_go,date_n_back,date_wk_back,nligne):
    """
    Cette fonction a pour objectif de crée les variables et les constructeurs de la classe
    Cette fonction prends pour paramètre un objet de type ligne,
    l'ensemble des horraires et le numéro de la ligne
    """
    for i in range(len(ligne.arrets)):
#        datetime.datetime.strptime(date_n_go[ligne.arrets[i]], '%H:%M')
        globals()[str(pre) + str(i)] = Arret(ligne.arrets[i])
        globals()[str(pre) + str(i)].set_heure_normal_go(transforme_en_heur(date_n_go[ligne.arrets[i]]))
        globals()[str(pre) + str(i)].set_heure_wk_go(transforme_en_heur(date_wk_go[ligne.arrets[i]]))
        globals()[str(pre) + str(i)].set_heure_normal_back(transforme_en_heur(date_n_back[ligne.arrets[i]]))
        globals()[str(pre) + str(i)].set_heure_wk_back(transforme_en_heur(date_wk_back[ligne.arrets[i]]))
        if i != len(ligne.arrets)-1:  
            globals()[str(pre) + str(i)].set_suivant([ligne.arrets[i+1]])
        if i != 0:
            globals()[str(pre) + str(i)].set_precedant([ligne.arrets[i-1]])
        globals()[str(pre) + str(i)].set_ligne(nligne)
    
# =============================================================================
# Programme Principal
# =============================================================================

# Création des lignes de bus
ajout_arrets_ligne(regular_path,ligne1)
ajout_arrets_ligne(regular_path2,ligne2)

#Création d'une variable pour chaque arrets
creation_var_arret(ligne1,'varl1_',regular_date_go,we_holidays_date_go,regular_date_back,we_holidays_date_back,1)
creation_var_arret(ligne2,'varl2_',regular_date_go2,we_holidays_date_go2,regular_date_back2,we_holidays_date_back2,2)



# =============================================================================
# Test console
# =============================================================================

#print(varl1_1.nom_arret,varl1_1.heure_normal_go, '\n\n',varl1_1.heure_wk_go,'\n\n',varl1_1.heure_normal_back,'\n\n',varl1_1.heure_wk_back)
#print(varl1_0.suivant,varl1_0.precedant,varl1_0.ligne)
#print(ligne1.arrets)

print(varl1_1.premier_bus('8:22','g','n'))















