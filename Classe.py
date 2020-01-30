# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:00:51 2020

@author: vieul
"""
import datetime

class Arret:
    def __init__(self, nom_arret, heure_normal_go = [], heure_wk_go = [], heure_normal_back = [], heure_wk_back = [], precedant = [], suivant = [], ligne = int()):
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
    def set_nom(self,nom):
        self.nom_arret = nom
        
    def set_heure_normal_go(self,liste):
        self.heure_normal_go = liste
        
    def set_heure_wk_go(self,liste):
        self.heure_wk_go = liste
        
    def set_heure_normal_back(self,l):
        self.heure_normal_back= l
        
    def set_heure_wk_back(self,l):
        self.heure_wk_back = l
        
    def set_suivant(self,l):
        self.suivant = l
    
    def set_precedant(self,l):
        self.precedant = l
    
    def set_ligne(self,l):
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
    def premier_bus(self,heure,dest,h):
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
                if self.heure_normal_go[i] != '-' and  heure < self.heure_normal_go[i]:               
                    return [self.heure_normal_go[i],i]
        
        elif dest == 'g' and h == 'w':
            for i in range(len(self.heure_wk_go)):
                if self.heure_wk_go[i] != '-' and heure < self.heure_wk_go[i]:
                    return [self.heure_wk_go[i],i]
        
        elif dest == 'b' and h == 'n' :
            for i in range(len(self.heure_normal_back)):
                if self.heure_normal_back[i] != '-' and heure < self.heure_normal_back[i]:
                    return [self.heure_normal_back[i],i]
        
        elif dest == 'b' and h == 'w' :
            for i in range(len(self.heure_wk_back)):
                if self.heure_wk_back[i] != '-' and heure < self.heure_wk_back[i]:
                    return [self.heure_wk_back[i],i]
        else:
            print ('Erreur')
    
    
    
    
    def difference(self,arret,i,s,h):
        '''
        Cette fonction renvoi le temps d'att entre deux arrets pour un bus donnée
        '''
        if s == 'g' and h == 'n' :
            return  arret.heure_normal_go[i] - self.heure_normal_go[i]
        elif s == 'g' and h == 'w' :
            return arret.heure_wk_go[i] - self.heure_wk_go[i]
        elif s == 'b' and h == 'n' :
            return arret.heure_normal_back[i] - self.heure_normal_back[i]
        elif s =='b' and h == 'w' :
            return arret.heure_wk_back[i] - self.heure_wk_back[i] 
        
  
    
    
    def tout_les_voisins(self):
        '''
        Prends en paramètre un arret et retourne les voisins de cette arret, si la ligne est sur correspondance alors elle renvoie aussi les arrets voisins sur l'aurtre ligne
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
            # Il y a un problème dans le cas d'une fourche
            
            for i in range(len(self.get_linge().get_correspondance())):
                if self.get_nom() == self.get_linge().get_correspondance()[i][0].get_nom():
                    
                    #Nous récupérons la deusieme ligne
                    deux = self.get_linge().get_correspondance()[i][1]
                    
                    for j in range(len(deux.get_arrets())):
                        if self.get_nom() == deux.get_arrets()[j].get_nom():
                            
                            retour = [deux.get_arrets()[j].get_precenant() + ['b'] + [deux.get_arrets()[j]], deux.get_arrets()[j].get_suivant() + ['g'] + [deux.get_arrets()[j]] , self.get_precenant() +  ['b'] + [self],self.get_suivant() + ['g'] + [self]]
        else:
            for u in range(len(self.get_precenant())):
                
                a =  [self.get_precenant()[u]] + ['b'] + [self]
                
                retour.append(a)
            for u in range(len(self.get_suivant())):
                 
                 a = [self.get_suivant()[u]] + ['g'] + [self]
                 retour.append(a)
        return retour


    
    def calcule_temps_arret_suivant(self,periode,heure):
        '''
        calcule le temps pour tout les arrets suivants, sur la ligne en cours ou non
        '''
        voisin = self.tout_les_voisins()
        retoune = []
        for i in range(len(voisin)):
            bus_num = voisin[i][2].premier_bus(heure,voisin[i][1],periode)
            retoune.append([voisin[i][2].difference(voisin[i][0],bus_num[1],voisin[i][1],periode),voisin[i][0]])
        return retoune
    
    
    
    
      
class Ligne:
    def __init__(self ,nom = int(), arrets = [], correspondance = []):
        self.nom = nom
        self.arrets = arrets
        self.correspondance = correspondance
        
    def set_nom(self,nom):
        self.nom = nom
        
    def set_arrets(self,l):
        self.arrets = l
        
    def set_correspondance(self,l):
        self.correspondance = l
        
    def get_arrets(self):
        return self.arrets
    def get_correspondance(self):
        return self.correspondance
    
    
    
    
    def ajout_correspondance(self,ligne2) :
        '''
        Recherche les arrets en commun entre deux lignes
        '''
        
        l = []
        for i in range(len(self.arrets)):
            for j in range(len(ligne2.arrets)):
                if self.arrets[i].get_nom() == ligne2.arrets[j].get_nom() :
                    if self.arrets[i] not in self.correspondance or ligne2.arrets[j] not in ligne2.correspondance:
                        l.append([self.arrets[i],ligne2])
                    
        self.set_correspondance(l)
        l = []
                        
                        
        
        
    def ajout_arret(self,dic) :
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
    def __init__(self ,reseau, depart, arrivee, moment = str(),he = str):
        self.reseau = reseau
        self.depart = depart
        self.arrivee = arrivee
        self.moment = moment
        self.heure = datetime.datetime.strptime(he, '%H:%M')
        for i in self.reseau.values():
            if self.arrivee == i.get_nom():
                self.arr = i
            if self.depart == i.get_nom():
                self.dep = i

    def num_bus(self,direct):
        return self.arr.premier_bus(self.heure,direct,self.moment)
    
 
    def get_arr(self):
        return self.arr
    def get_dep(self):
        return self.dep
    def get_reseau(self) :
        return self.reseau
    
    
    
    
    def direction_plus_cours(self):
        '''
        Cette fonction nous donne la direction pour faire le trajet entre deux arrets et qu'elles lignes il faut prendre
        '''
        ligne_depart = self.dep.ligne.nom
        ligne_arrivee = self.arr.ligne.nom
        j = 0
        
        
        if ligne_arrivee == ligne_depart:
            
            if self.dep.ligne.get_arrets().index(self.dep) < self.arr.ligne.get_arrets().index(self.arr):
                s = 'g'
                self.trajet = self.dep.ligne.get_arrets()[self.dep.ligne.get_arrets().index(self.dep):self.arr.ligne.get_arrets().index(self.arr)+1]
                
            elif self.dep.ligne.get_arrets().index(self.dep) == self.arr.ligne.get_arrets().index(self.arr):
                return('deja a destination')
                
            else: 
                s = 'b'
                self.trajet = self.dep.ligne.get_arrets()[self.arr.ligne.get_arrets().index(self.arr):self.dep.ligne.get_arrets().index(self.dep)+1]
            
            for i in range(len(self.trajet)) :
                if self.trajet[i] == self.dep.ligne.get_arrets():
                    j = 1
                    
            if j == 0:
            #Si il n'y a pas d'arret
                bus_num = self.num_bus(s)
                res = self.dep.difference(self.arr,bus_num[1],s,self.moment)
                return res
                
        else:
            pass
        
def changement_dic(dic):
    """
    :param dic: le dictionaire avec tout les arrets
    :return: un nouveau dictionaire avec comme keys un objet arret et comme value la valeur infini
    cette fonction est utilisé pour l'algo dijktra
    """
    ndic = dic.values()
    ndic = list(ndic)
    d = {}
    for i in range(len(ndic)):
        d[ndic[i]] = float('inf')

      
def plus_cours(voyage,dist,etape = Arret(''),visite = []):
    # !!! Attention !!! il y a deux noeud gare a voire si cela va poser problème
    # Condition de fin :
    # Quand on traite le noeud de fin alors nous avons fini nous retrournons donc la distance ici un temps
    if voyage.get_arr() == etape:
        return dist[voyage.get_arr()]

    # Si aucun noeud n'a été visité
    if len(visite) == 0  :
        #On donne comme première etape le debut du voyage
        etape = voyage.get_dep()

        # on inisialise la distance pour cette etape a 0
        dist[etape] = datetime.timedelta()


    # On calcule les temps pour tous les arrets de l'etape en cours et on donne les voisins
    # Dans [0] il y a le temps et dans [1] le voisin
    v = etape.calcule_temps_arret_suivant('n',voyage.heure)
    # print(etape)
    # print('\n\n\n')
    # print(dist[etape])
    # print('\n\n\n')
    for voisin in v:
        if voisin[1] not in visite:
            dist_voisin = dist.get(voisin[1], datetime.timedelta(99999999))
            candidat_dist = dist[etape] + voisin[0]
            if candidat_dist < dist_voisin:
                dist[voisin[1]] = candidat_dist
    visite.append(etape)
    non_visites = dict((s, dist.get(s, datetime.timedelta(99999999))) for s in voyage.reseau.values() if s not in visite)
    noeud_plus_proche = min(non_visites, key = non_visites.get)

    return plus_cours(voyage=voyage, dist=dist, etape=noeud_plus_proche, visite=visite)