"""
Ce module gère les Sounds du jeu en utilisant la bibliothèque pygame.
Il contient la classe SoundManager qui permet de charger et de jouer des Sounds.
"""

import pygame


class SoundManager :
    def __init__(self):
        pygame.init()
        self.sounds = {
            'A_vos_ordre': pygame.mixer.Sound("Sounds/A_vos_ordres.mp3"),
            'Attendre': pygame.mixer.Sound("Sounds/Attendre.mp3"),
            'Au_Combat': pygame.mixer.Sound("Sounds/Au_Combat.mp3"),
            'Blop': pygame.mixer.Sound("Sounds/Blop.mp3"),
            'Boomerang' : pygame.mixer.Sound("Sounds/Boomerang.mp3"),
            'Boule_feu' : pygame.mixer.Sound("Sounds/Boule_feu.dat.mp3"),
            'Casser_mur' : pygame.mixer.Sound("Sounds/Casser_mur.mp3"),
            'Combat' : pygame.mixer.Sound("Sounds/Combat.mp3"),
            'Combat_v2' : pygame.mixer.Sound("Sounds/Combat_v2.mp3"),
            'Combat_v3' : pygame.mixer.Sound("Sounds/Combat_v3.mp3"),
            'Combat_v4' : pygame.mixer.Sound("Sounds/Combat_v4.mp3"),
            'Coup_marteau' : pygame.mixer.Sound("Sounds/Coup_marteau.mp3"),
            'Coup_poing' : pygame.mixer.Sound("Sounds/Coup_poing.mp3"),
            'EcraSounds_ennemi': pygame.mixer.Sound("Sounds/Ecrasons_ennemi.mp3"),
            'En_avant': pygame.mixer.Sound("Sounds/En_Avant.mp3"),
            'Explosion': pygame.mixer.Sound("Sounds/Explosion.mp3"),
            'Feu' : pygame.mixer.Sound("Sounds/Feu.mp3"),
            'Fin_jeu' : pygame.mixer.Sound("Sounds/Fin_jeu.mp3"),
            'Fleche' : pygame.mixer.Sound("Sounds/Fleche.mp3"),
            'Foudre' : pygame.mixer.Sound("Sounds/Foudre.mp3"),
            'Foudre_v2' : pygame.mixer.Sound("Sounds/Foudre_v2.mp3"),
            'Griffes' : pygame.mixer.Sound("Sounds/Griffes.mp3"),
            'Laser' : pygame.mixer.Sound("Sounds/Laser.mp3"),
            'Pistolet_silencieux' : pygame.mixer.Sound("Sounds/Pistolet_silencieux.mp3"),
            'Projectile' : pygame.mixer.Sound("Sounds/Projectile.mp3"),
            'Protection' : pygame.mixer.Sound("Sounds/Protection.mp3"),
            'Revolver' : pygame.mixer.Sound("Sounds/Revolver.mp3"),
            'Sabre' : pygame.mixer.Sound("Sounds/Sabre.mp3"),
            'Soin' : pygame.mixer.Sound("Sounds/Soin.mp3"),
            'Tir_1_coup' : pygame.mixer.Sound("Sounds/Tir_1_coup.mp3"),
            'Tir_rafale' : pygame.mixer.Sound("Sounds/Tir_rafale.mp3"),
            'Tir_rafale_v2': pygame.mixer.Sound("Sounds/Tir_rafale_v2.mp3"),
            'Musique_lancement' : pygame.mixer.Sound("Sounds/The_Avengers.mp3")
        }

    def bruit(self, name):
        if name in self.sounds:
            if name == 'Musique_lancement':
                self.sounds[name].play(-1)
            else :
                #self.sounds['Musique_lancement'].pause()
                self.sounds[name].play()
                #self.sounds['Musique_lancement'].unpause()
        else:
            print(f"Son {name} introuvable.")    