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
# =============================================================================
# Création des primitives    
# =============================================================================
    def premier_bus(self,he,dest,h):
        '''
        Cette fonction prend comme paramètre
         - une heure(str) au format HH:MM
         - une destination: Back ou Go
         - une periode: normal ou wk
        '''
        # dest = input('Go: g ou Black : b    :')
        # h = input('Normal: n ou WK: w       :')
        heure = datetime.datetime.strptime(he, '%H:%M')

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
    
    def ajout_correspondance(self,ligne2) :
        for i in range(len(self.arrets)):
            for j in range(len(ligne2.arrets)):
                if self.arrets[i] == ligne2.arrets[j] :
                    if self.arrets[i] not in self.correspondance or ligne2.arrets[j] not in ligne2.correspondance:
                        self.correspondance.append(self.arrets[i])
                        # ligne2.correspondance.append(ligne2.arrets[j])
                        
    
    
    
    
class Voyage:
    def __init__(self ,destination, depart, moment = str()):
        self.destination = destination
        self.depart = depart
        self.moment = moment
        
    
        
        

