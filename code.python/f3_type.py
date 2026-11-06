import os

dossier = "E:/Users/Richard/Python/bac-a-sable.original"

contenu = sorted(os.listdir(dossier))
size = os.path.getsize(dossier)

for nom in contenu:
    chemin = os.path.join(dossier, nom)
    size = os.path.getsize(chemin)
    
    if os.path.isdir(chemin) is False :
        print(f"{nom:15}{size:>10} octets")