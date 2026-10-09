import csv
from pathlib import Path

dossier = Path(__file__).resolve().parent / "data"

fichier_entree = dossier / "weather_raw.csv"
fichier_sortie = dossier / "weather_clean.csv"

donnees_nettoyees = []
doublons = set()

with open(fichier_entree, "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    for ligne in lecteur:
        ville = ligne["ville"].strip()
        date = ligne["date_observation"].strip()

        if not ville or not date:
            continue

        cle = (ville, date)

        if cle in doublons:
            continue

        doublons.add(cle)

        donnees_nettoyees.append({
            "ville": ville,
            "date_observation": date,
            "temperature": float(ligne["temperature"]),
            "humidite": float(ligne["humidite"]),
            "vitesse_vent": float(ligne["vitesse_vent"])
        })

colonnes = [
    "ville",
    "date_observation",
    "temperature",
    "humidite",
    "vitesse_vent"
]

with open(fichier_sortie, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=colonnes)
    writer.writeheader()
    writer.writerows(donnees_nettoyees)

print("Transformation terminee !")
print("Nombre de lignes :", len(donnees_nettoyees))
print("Fichier cree :", fichier_sortie)