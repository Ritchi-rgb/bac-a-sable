import os

dossier = "E:/Users/Richard/Python/bac-a-sable.original"

contenu = sorted(os.listdir(dossier))
size = os.path.getsize(dossier)

for nom in contenu:
    chemin = os.path.join(dossier, nom)
    size = os.path.getsize(chemin)
    
    if os.path.isdir(chemin) is False :
        if size > 1000 and size < 1000000 :
            print(f"{nom:15}{size/1000:>10.2f} Ko")
        elif size > 1000000 :
            print(f"{nom:15}{size/1000000:>10.2f} Mo")
        elif size < 1000 :
            print(f"{nom:15}{size:>10} octets")