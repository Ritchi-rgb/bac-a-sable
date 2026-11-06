import os

dossier = "E:/Users/Richard/Python/bac-a-sable.original"

contenu = sorted(os.listdir(dossier))

for nom in contenu:
    chemin = os.path.join(dossier, nom)

    if os.path.isdir(chemin):
        print(f"[D] {nom}")
    else:
        print(f"[F] {nom}")