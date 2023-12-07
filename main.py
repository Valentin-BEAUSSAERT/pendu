import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))

#Définir un background 
background1 = pygame.image.load("fond.png")

# Définir les couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Liste des mots possibles
liste_mots = ["nekfeu", "damso", "disiz la peste", "booba", "sopico", "kalash", "lomepal", "vald", "lorenzo", "s-crew", "alpha wann", "freeze corleone", "dinos", "remy", "columbine", "lujipeka", "iam"]

# Choix du mot au hasard
mot = random.choice(liste_mots)
lettres_devinees = ["_"] * len(mot)

# Police pour afficher les lettres
police = pygame.font.SysFont(None, 48)

# Nombre d'erreurs (à gérer dans la logique du jeu)
erreurs = 0

def dessiner_pendu(erreurs):
    # [Le code de dessin du pendu]
    # Base
    if erreurs > 0:
        pygame.draw.line(fenetre, NOIR, (50, 500), (150, 500), 5)
    # Poteau
    if erreurs > 1:
        pygame.draw.line(fenetre, NOIR, (100, 500), (100, 100), 5)
    # Traverse
    if erreurs > 2:
        pygame.draw.line(fenetre, NOIR, (100, 100), (300, 100), 5)
    # Corde
    if erreurs > 3:
        pygame.draw.line(fenetre, NOIR, (300, 100), (300, 150), 5)
    # Tête
    if erreurs > 4:
        pygame.draw.circle(fenetre, NOIR, (300, 180), 30, 5)
    # Corps
    if erreurs > 5:
        pygame.draw.line(fenetre, NOIR, (300, 210), (300, 350), 5)
    # Bras gauche
    if erreurs > 6:
        pygame.draw.line(fenetre, NOIR, (300, 250), (250, 300), 5)
    # Bras droit
    if erreurs > 7:
        pygame.draw.line(fenetre, NOIR, (300, 250), (350, 300), 5)
    # Jambe gauche
    if erreurs > 8:
        pygame.draw.line(fenetre, NOIR, (300, 350), (250, 400), 5)
    # Jambe droite
    if erreurs > 9:
        pygame.draw.line(fenetre, NOIR, (300, 350), (350, 400), 5)

def afficher_mot():
    affichage = " ".join(lettres_devinees)
    texte_surface = police.render(affichage, True, NOIR)
    fenetre.blit(texte_surface, (350, 450))

def ecran_fin(message, couleur):
    fenetre.fill(BLANC)
    texte_surface = police.render(message, True, couleur)
    fenetre.blit(texte_surface, (largeur // 2 - texte_surface.get_width() // 2, hauteur // 2 - texte_surface.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Boucle principale du jeu
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode in mot:
                for i, lettre in enumerate(mot):
                    if lettre == event.unicode:
                        lettres_devinees[i] = lettre
            else:
                erreurs += 1

    # Remplir l'arrière-plan
    fenetre.fill(BLANC)

    # Dessiner le pendu en fonction du nombre d'erreurs
    dessiner_pendu(erreurs)

    # Afficher le mot
    afficher_mot()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Conditions de victoire ou défaite
    if "_" not in lettres_devinees:
        ecran_fin("Gagné!", VERT)
        break
    elif erreurs > 9:
        ecran_fin("Perdu!", ROUGE)
        break
