# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:00:51 2020

@author: vieul
"""
import datetime


class Arret:
    def __init__(self, nom_arret, heure_normal_go=[], heure_wk_go=[], heure_normal_back=[], heure_wk_back=[],
                 precedant=[], suivant=[], ligne=int()):
        self.nom_arret = nom_arret
        self.heure_normal_go = heure_normal_go
        self.heure_wk_go = heure_wk_go
        self.heure_normal_back = heure_normal_back
        self.heure_wk_back = heure_wk_back
        self.suivant = suivant
        self.ligne = ligne
        self.precedant = precedant

    # =============================================================================
    # Création des set et des get
    # =============================================================================
    def set_nom(self, nom):
        self.nom_arret = nom

    def set_heure_normal_go(self, liste):
        self.heure_normal_go = liste

    def set_heure_wk_go(self, liste):
        self.heure_wk_go = liste

    def set_heure_normal_back(self, l):
        self.heure_normal_back = l

    def set_heure_wk_back(self, l):
        self.heure_wk_back = l

    def set_suivant(self, l):
        self.suivant = l

    def set_precedant(self, l):
        self.precedant = l

    def set_ligne(self, l):
        self.ligne = l

    def get_nom(self):
        return self.nom_arret

    def get_linge(self):
        return self.ligne

    def get_precenant(self):
        return self.precedant

    def get_suivant(self):
        return self.suivant

    # =============================================================================
    # Création des primitives
    # =============================================================================
    def premier_bus(self, heure, dest, h):
        '''
        Cette fonction prend comme paramètre
         - une heure au format 
         - une destination: Back ou Go
         - une periode: normal ou wk
        '''
        # dest = input('Go: g ou Black : b    :')
        # h = input('Normal: n ou WK: w       :')
        #        heure = datetime.datetime.strptime(he, '%H:%M')

        if dest == 'g' and h == 'n':
            for i in range(len(self.heure_normal_go)):
                if self.heure_normal_go[i] != '-' and heure < self.heure_normal_go[i]:
                    return [self.heure_normal_go[i], i]

        elif dest == 'g' and h == 'w':
            for i in range(len(self.heure_wk_go)):
                if self.heure_wk_go[i] != '-' and heure < self.heure_wk_go[i]:
                    return [self.heure_wk_go[i], i]

        elif dest == 'b' and h == 'n':
            for i in range(len(self.heure_normal_back)):
                if self.heure_normal_back[i] != '-' and heure < self.heure_normal_back[i]:
                    return [self.heure_normal_back[i], i]

        elif dest == 'b' and h == 'w':
            for i in range(len(self.heure_wk_back)):
                if self.heure_wk_back[i] != '-' and heure < self.heure_wk_back[i]:
                    return [self.heure_wk_back[i], i]
        else:
            return print('\n\n\n\n\n','Erreur')

    def difference(self, arret, i, s, h):
        '''
        Cette fonction renvoi le temps d'att entre deux arrets pour un bus donnée
        '''

        if arret.heure_normal_go[i] == '-' and s == 'g' and h == 'n':
            return datetime.timedelta(99999999)
        if arret.heure_wk_go[i] == '-' and s == 'g' and h == 'w':
            return datetime.timedelta(99999999)
        if arret.heure_normal_back[i] == '-' and s == 'b' and h == 'n':
            return datetime.timedelta(99999999)
        if arret.heure_wk_back[i] == '-' and s == 'b' and h == 'w':
            return datetime.timedelta(99999999)

        if s == 'g' and h == 'n':
            return arret.heure_normal_go[i] - self.heure_normal_go[i]
        elif s == 'g' and h == 'w':

            return arret.heure_wk_go[i] - self.heure_wk_go[i]
        elif s == 'b' and h == 'n':
            return arret.heure_normal_back[i] - self.heure_normal_back[i]
        elif s == 'b' and h == 'w':
            return arret.heure_wk_back[i] - self.heure_wk_back[i]

    def tout_les_voisins(self):
        '''
        Prends en paramètre un arret et retourne les voisins de cette arret, si la ligne est sur correspondance alors
        elle renvoie aussi les arrets voisins sur l'aurtre ligne
        '''
        retour = []

        for u in range(len(self.get_linge().get_correspondance())):
            if self.get_linge().get_correspondance()[u][0].get_nom() == self.get_nom():
                v = True
                break
            else:
                v = False

        if v:
            # Dans correspondance de la classe ligne nous avons l'ensemble des arrets qui  sont en commun avec une autre ligne et cette ligne
            # ne faut t'il pas que l'arret suivant dans le cas d'une gare soit son arret suivant, son arret précédent et sont arret de transition

            for i in range(len(self.get_linge().get_correspondance())):
                if self.get_nom() == self.get_linge().get_correspondance()[i][0].get_nom():

                    # Nous récupérons la deusieme ligne
                    deux = self.get_linge().get_correspondance()[i][1]

                    for j in range(len(deux.get_arrets())):
                        if self.get_nom() == deux.get_arrets()[j].get_nom():
                            retour = [deux.get_arrets()[j].get_precenant() + ['b'] + [deux.get_arrets()[j]],
                                      deux.get_arrets()[j].get_suivant() + ['g'] + [deux.get_arrets()[j]],
                                      self.get_precenant() + ['b'] + [self], self.get_suivant() + ['g'] + [self]]

        else:
            for u in range(len(self.get_precenant())):
                a = [self.get_precenant()[u]] + ['b'] + [self]

                retour.append(a)
            for u in range(len(self.get_suivant())):
                a = [self.get_suivant()[u]] + ['g'] + [self]
                retour.append(a)
        return retour

    def calcule_temps_arret_suivant(self, periode, heure):
        '''
        calcule le temps pour tout les arrets suivants, sur la ligne en cours ou non
        '''
        voisin = self.tout_les_voisins()
        retoune = []
        for i in range(len(voisin)):
            bus_num = voisin[i][2].premier_bus(heure, voisin[i][1], periode)
            retoune.append([voisin[i][2].difference(voisin[i][0], bus_num[1], voisin[i][1], periode), voisin[i][0]])
        return retoune


class Ligne:
    def __init__(self, nom=int(), arrets=[], correspondance=[]):
        self.nom = nom
        self.arrets = arrets
        self.correspondance = correspondance

    def set_nom(self, nom):
        self.nom = nom

    def set_arrets(self, l):
        self.arrets = l

    def set_correspondance(self, l):
        self.correspondance = l

    def get_arrets(self):
        return self.arrets

    def get_correspondance(self):
        return self.correspondance

    def ajout_correspondance(self, ligne2):
        '''
        Recherche les arrets en commun entre deux lignes
        '''

        l = []
        for i in range(len(self.arrets)):
            for j in range(len(ligne2.arrets)):
                if self.arrets[i].get_nom() == ligne2.arrets[j].get_nom():
                    if self.arrets[i] not in self.correspondance or ligne2.arrets[j] not in ligne2.correspondance:
                        l.append([self.arrets[i], ligne2])

        self.set_correspondance(l)
        l = []

    def ajout_arret(self, dic):
        '''
        Ajoute les arrets  de cette ligne dans la liste arrets
        '''

        l = []
        for t in dic.values():
            if t.ligne.nom == self.nom:
                l.append(t)
        self.set_arrets(l)
        l = []


class Voyage:
    def __init__(self, reseau, depart,ld, arrivee,la, moment=str(), he=str):
        self.reseau = reseau
        self.depart = depart
        self.ld = ld
        self.arrivee = arrivee
        self.la = la
        self.moment = moment
        self.heure = datetime.datetime.strptime(he, '%H:%M')

        for i in self.reseau.values():
            if self.arrivee == i.get_nom() and self.la == i.get_linge().nom:
                self.arr = i
            if self.depart == i.get_nom() and self.ld == i.get_linge().nom:
                self.dep = i

    def num_bus(self, direct):
        return self.arr.premier_bus(self.heure, direct, self.moment)

    def get_arr(self):
        return self.arr

    def get_dep(self):
        return self.dep

    def get_reseau(self):
        return self.reseau
    def changement_reseaux(self):
        for i in self.reseau.values():
            for j in self.reseau.values():
                if i.get_nom() == j.get_nom():
                    pass




def changement_dic(dic):
    '''
    :param dic: Donne en paramètre un dictionnaire avec l'ensemble des données pour le réseau
    :return: Créer un nouveau dictionnaire avec l'ensemble des arrets et comme valeur un temps considéré comme l'infinie
    '''

    ndic = dic.values()
    ndic = list(ndic)
    d = {}
    for i in range(len(ndic)):
        d[ndic[i]] = datetime.timedelta(99999999)
    return d

def changement_dic_parcour(dic):
    '''
    :param dic: Donne en paramètre un dictionnaire avec l'ensemble des données pour le réseau
    :return: Créer un nouveau dictionnaire avec l'ensemble des arrets et comme valeur un temps considéré comme l'infinie
    '''

    ndic = dic.values()
    ndic = list(ndic)
    d = {}
    for i in range(len(ndic)):
        d[ndic[i]] = []
    return d

def plus_cours(voyage, dist = {}, etape=Arret(''), visite=[], parcour = {}):
    '''
    :param voyage: Classe Voyage
    :param dist: Dictionnaire des distances
    :param etape: etapes en cours
    :param visite: liste des etapes visitée
    :return: le temps le plus cours entre le point de départ et le point d'arrivé
    '''
    # Condition de fin :
    if voyage.get_arr().get_nom() == etape.get_nom():
        return dist[etape], parcour[voyage.get_arr()]
    # Si aucun noeud n'a été visite
    if len(visite) == 0:
        # On donne comme première etape le debut du voyage
        dist = changement_dic(voyage.reseau)
        parcour = changement_dic_parcour(voyage.reseau)
        etape = voyage.get_dep()
        # on inisialise la distance pour cette etape a 0
        dist[etape] = datetime.timedelta()
        temps = voyage.heure
    else:
        temps = voyage.heure + dist[etape]
    # On calcule les temps pour tous les arrets de l'etape en cours et on donne les voisins
    # Dans [0] il y a le temps et dans [1] le voisin
    v = etape.calcule_temps_arret_suivant('n', temps)
    for voisin in v:
        if voisin[1] not in visite:
            dist_voisin = dist.get(voisin[1]) # , datetime.timedelta(99999999)
            candidat_dist = dist[etape] + voisin[0]
            if candidat_dist < dist_voisin:
                #Ici il faut faire le sauvegarde du trajet
                sauve = parcour[etape] + [voisin[1]]
                parcour[voisin[1]] = sauve
                dist[voisin[1]] = candidat_dist
                # print('l etape en cours : ', etape.get_nom(), etape.get_linge().nom)
                # print('le voisin : ', voisin[1].get_nom(),voisin[1].get_linge().nom)
                # print('la distance est de: ', dist[voisin[1]],'\n')
    visite.append(etape)
    non_visites = dict((s, dist.get(s, datetime.timedelta(99999999))) for s in voyage.reseau.values() if s not in visite)
    noeud_plus_proche = min(non_visites, key=non_visites.get)
    return plus_cours(voyage=voyage, dist=dist, etape=noeud_plus_proche, visite=visite, parcour=parcour)

def le_plus_cours(v):
    '''

    :param v: Classe voyage
    :return: Rien
    Cette fonction sert juste a mettre en forme la fonction : plus_cours
    '''
    try:
        a = plus_cours(v)
        print('Le temps de trajet est estimé à :',a[0], ' min')
        print('Les arrets sont :')
        for i in a[1]:
            print(i.get_nom())
        return ''
    except:
        return ('problème de heure')


def moins_arc(voyage, dist = {}, etape=Arret(''), visite=[], parcour = {}):
    '''
    :param voyage: Classe Voyage
    :param dist: Dictionnaire des distances
    :param etape: etapes en cours
    :param visite: liste des etapes visitée
    :return: le temps le plus cours entre le point de départ et le point d'arrivé
    '''

    # Condition de fin :
    if voyage.get_arr().get_nom() == etape.get_nom():
        return dist[etape], parcour[voyage.get_arr()]
    # Si aucun noeud n'a été visite
    if len(visite) == 0:
        # On donne comme première etape le debut du voyage
        dist = changement_dic(voyage.reseau)
        parcour = changement_dic_parcour(voyage.reseau)
        etape = voyage.get_dep()
        # for i in dist.keys():
        #     dist[i] = int(0)
        # on inisialise la distance pour cette etape a 0
        dist[etape] = datetime.timedelta()
        temps = voyage.heure
        # print(dist)
        # print('la')
    else:
        temps = voyage.heure + dist[etape]
    # On calcule les temps pour tous les arrets de l'etape en cours et on donne les voisins
    # Dans [0] il y a le temps et dans [1] le voisin
    v = etape.calcule_temps_arret_suivant('n', temps)
    for i in v:
        i[0] = datetime.timedelta(seconds = 1 )
    for voisin in v:
        if voisin[1] not in visite:
            dist_voisin = dist.get(voisin[1]  , datetime.timedelta(99999999))
            candidat_dist = dist[etape] + voisin[0]

            if candidat_dist < dist_voisin:
                #Ici il faut faire le sauvegarde du trajet
                sauve = parcour[etape] + [voisin[1]]
                parcour[voisin[1]] = sauve
                dist[voisin[1]] = candidat_dist
                # print('l etape en cours : ', etape.get_nom(), etape.get_linge().nom)
                # print('le voisin : ', voisin[1].get_nom(),voisin[1].get_linge().nom)
                # print('la distance est de: ', dist[voisin[1]],'\n')
    visite.append(etape)
    non_visites = dict((s, dist.get(s, datetime.timedelta(99999999))) for s in voyage.reseau.values() if s not in visite)
    noeud_plus_proche = min(non_visites, key=non_visites.get)
    return moins_arc(voyage=voyage, dist=dist, etape=noeud_plus_proche, visite=visite, parcour=parcour)

def le_moins_arc(v):
    try:
        a = moins_arc(v)
        aa = str(a[0]).split(':')
        print('Il y a',int(aa[2]), 'arrets entre vous et votre destination')
        print('Les arrets sont :')
        for i in a[1]:
            print(i.get_nom())
        return ''
    except:
        return ('problème de heure')