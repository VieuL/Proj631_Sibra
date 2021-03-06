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
    with open(data_file_name, 'r', encoding='utf-8') as f:
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
    with open(data_file_name2, 'r', encoding='utf-8') as f:
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


def arret_suivant(path):
    '''
    Créer les arrets suivant 
    
    '''
    n = path.split(' N ')
    fin = []
    #    ['nom 1 + nom2','nom3','nom4']
    for i in range(len(n)):
        if ' + ' in n[i]:

            a = n[i].split(" + ")

            fin.append([a[0], [n[i + 1]]])
            fin.append([a[1], [n[i + 1]]])
            a = []
        elif i < len(n) - 1:
            fin.append([n[i], [n[i + 1]]])

    return fin


def arret_pre(path):
    '''
    créer une liste avec [arret, arret_suivant]
    
    '''
    n = path.split(' N ')
    fin = []
    for i in range(-1, -len(n), -1):
        if ' + ' in n[i - 1]:
            a = n[i - 1].split(" + ")
            fin.append([n[i], [a[0], a[1]]])
        elif i > -len(n):
            fin.append([n[i], [n[i - 1]]])
    return fin


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


def changement_suivant_pre(data):
    '''
    Cette fonction sert a transformer les arrets suivants et précédant qui sont de type str à un type Arret
    :param data: dictionnaire avec l'ensemble des arrêts
    '''

    # on parcour tous les arrets
    for t in data.values():

        # on parcour tous les arrets
        for w in data.values():

            for i in range(len(w.suivant)):
                if t.get_nom() == w.suivant[i] and t.ligne.nom == w.ligne.nom:
                    w.suivant[i] = t
            for u in range(len(w.precedant)):
                if t.get_nom() == w.precedant[u] and t.ligne.nom == w.ligne.nom:
                    w.precedant[u] = t


def creation_var_arret(ligne, pre, date_n_go, date_wk_go, date_n_back, date_wk_back, path):
    '''

    :param ligne: L'objet de type ligne dont on veut créer les arrets
    :param pre: Le nom du préfixe
    :param date_n_go: la liste des horaires pour une date normal (hors wk ou jf) dans le sens go
    :param date_wk_go: la liste des horaires pour une date de wk  dans le sens go
    :param date_n_back: la liste des horaires pour une date normal (hors wk ou jf) dans le sens back
    :param date_wk_back: la liste des horaires pour une date de wk  dans le sens go
    :param path: liste avec le nom de touts les arrets de la ligne

    Cette fonction a pour objectif de crée les variables et les constructeurs de la classe
    Cette fonction prend pour paramètre un objet de type ligne,
    l'ensemble des horraires et le numéro de la ligne
    '''


    arrets = path.replace('+', 'N')
    arrets = arrets.split(' N ')

    for i in range(len(arrets)):
        # Création de tous les arrets
        data[str(pre) + str(i)] = Arret(arrets[i])
    for m in range(len(arrets)):
        data[str(pre) + str(m)].set_heure_normal_go(transforme_en_heur(date_n_go[arrets[m]]))
        data[str(pre) + str(m)].set_heure_wk_go(transforme_en_heur(date_wk_go[arrets[m]]))
        data[str(pre) + str(m)].set_heure_normal_back(transforme_en_heur(date_n_back[arrets[m]]))
        data[str(pre) + str(m)].set_heure_wk_back(transforme_en_heur(date_wk_back[arrets[m]]))
        data[str(pre) + str(m)].set_ligne(ligne)
        n = arret_suivant(path)
        p = arret_pre(path)

        for j in range(len(n)):
            if arrets[m] == n[j][0]:
                data[str(pre) + str(m)].set_suivant((n[j][1]))

        for k in range(len(p)):
            if arrets[m] == p[k][0]:
                data[str(pre) + str(m)].set_precedant(list(p[k][1]))


# =============================================================================
# Programme Principal
# =============================================================================
#Cette partie du programme peut etre opti facilement
ligne1 = Ligne(1)
ligne2 = Ligne(2)

data = {}

# Création des arrets
creation_var_arret(ligne1, 'varl1_', regular_date_go, we_holidays_date_go, regular_date_back, we_holidays_date_back,
                   regular_path)
creation_var_arret(ligne2, 'varl2_', regular_date_go2, we_holidays_date_go2, regular_date_back2, we_holidays_date_back2,
                   regular_path2)

# on ajoute les arrets dans la ligne
ligne1.ajout_arret(data)
ligne2.ajout_arret(data)

# on remplace les arrets suivant de type str par les arrets de type Arret
changement_suivant_pre(data)

# on recherche les correspondance
ligne1.ajout_correspondance(ligne2)
ligne2.ajout_correspondance(ligne1)

# =============================================================================
# Test console
# =============================================================================



# Test de la création des diff arrets
# for i in data.values():
#     print('num de la ligne : ', i.ligne.nom)
#     print('nom de l arret : ',i.get_nom())
#     print('next stop : ', i.get_suivant())
#     print('previous stop : ', i.get_precenant())
#     print('\n')


v1 = Voyage(data,'France_Barattes',1,'Ponchy',1,'n','10:37')
v2 = Voyage(data,'LYCÉE_DE_POISY',1,'CAMPUS',2,'n','7:40')

le_moins_arc(v1)
print('\n')
le_plus_cours(v2)


