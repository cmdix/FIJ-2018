# on importe la librairie qui contient plusieurs fonctions aléatoires
import random

# on initialise nos différentes variables
entree = -1
reponse = random.randrange(100) # on utilise la fonction randrang qui permet de choisir un nombre entre 0 et le nombre zntre (), ici 100
compteur = 10

# Tant que entree est differente de reponse et que compteur est plus grand que 0....
while entree != reponse and compteur > 0 :
  # on changer la valeur de entree avec celle tapée au clavier. Attention, convertion en int
  entree = int(input("écrit un chiffre:")) 

  if entree < reponse :
    print("+ grand")
  elif entree > reponse :
    print("+ petit")
  else :
    print("bien joue !!! tu as a la bonne reponse")
    
  # Attention a changer la valeur du compteur pour evite un boucle infinie
  compteur = compteur -1

