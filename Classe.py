# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:00:51 2020

@author: vieul
"""

class Arret:
    def __init__(self, nom_arret, heure_normal_go = [], heure_wk_go = [], heure_normal_back = [], heure_wk_back = [], precedant = [], suivant = [], ligne = str()):
        self.nom_arret = nom_arret
        self.heure_normal_go = heure_normal_go
        self.heure_wk_go = heure_wk_go
        self.heure_normal_back = heure_normal_back
        self.heure_wk_back = heure_wk_back      
        self.suivant = suivant
        self.ligne = ligne

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
        
    def set_suivant(self,liste):
        self.suivant = liste
        
    def set_ligne(self,l):
        self.ligne = l
        
        
    def get_nom(self):
        return self.nom_arret
    
    
    
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
        
        
        

