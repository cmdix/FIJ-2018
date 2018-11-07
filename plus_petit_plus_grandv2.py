import random

reponse = random.randrange(100)

continuer = True 

while continuer == True :

  entree = int ( input("Entrez un nombre"))

  if reponse < entree :
    print("plus bas" )

  elif reponse > entree :
    print("plus haut")
  else :
    print("bien joue")
