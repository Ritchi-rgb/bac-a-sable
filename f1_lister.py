# Récupérer la liste des fichiers et dossiers via os.listdir(chemin)

import os

chemin = "E:/Users/Richard/AppData/Local/Programs/Microsoft VS Code/bac-a-sable"
contenu = os.listdir(chemin)

#print(f"Contenu du répertoire {contenu}\n")
# Afficher chaque élément
for element in contenu:
    print(element)
