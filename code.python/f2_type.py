# Importe le module os pour gérer les dossiers et les fichiers
import os

# Définit le chemin du dossier à parcourir
dossier = "E:/Users/Richard/Python/bac-a-sable.original"

# Récupère la liste des éléments du dossier et les trie par ordre alphabétique
contenu = sorted(os.listdir(dossier))

# Parcourt chaque élément contenu dans le dossier
for nom in contenu:

    # Construit le chemin complet de l'élément (dossier ou fichier)
    chemin = os.path.join(dossier, nom)

    # Vérifie si l'élément est un dossier
    if os.path.isdir(chemin):

        # Affiche [D] suivi du nom du dossier
        print(f"[D] {nom}")

    # Sinon, l'élément est un fichier
    else:

        # Affiche [F] suivi du nom du fichier
        print(f"[F] {nom}")