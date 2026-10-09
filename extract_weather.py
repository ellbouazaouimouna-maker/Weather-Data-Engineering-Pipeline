import csv
from pathlib import Path

import json
from urllib.request import urlopen
from urllib.parse import urlencode
resultats = []
villes = {
    "Casablanca": (33.59, -7.62),
    "Rabat": (34.02, -6.84),
    "Marrakech": (31.63, -8.00),
    "Fes": (34.06, -4.98),
    "Tanger": (35.76, -5.83)
}

for ville, (latitude, longitude) in villes.items():

    params = urlencode({
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Africa/Casablanca"
    })

    url = "https://api.open-meteo.com/v1/forecast?" + params

    with urlopen(url, timeout=20) as response:
        data = json.load(response)

    meteo = data["current"]

    print("\n=== METEO", ville.upper(), "===")
    print("Date :", meteo["time"])
    print("Temperature :", meteo["temperature_2m"], "°C")
    print("Humidite :", meteo["relative_humidity_2m"], "%")
    print("Vitesse du vent :", meteo["wind_speed_10m"], "km/h")
    resultats.append({
        "ville": ville,
        "date_observation": meteo["time"],
        "temperature": meteo["temperature_2m"],
        "humidite": meteo["relative_humidity_2m"],
        "vitesse_vent": meteo["wind_speed_10m"]
    })
dossier_data = Path(__file__).resolve().parent / "data"
dossier_data.mkdir(exist_ok=True)

fichier_csv = dossier_data / "weather_raw.csv"

with open(fichier_csv, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=resultats[0].keys())
    writer.writeheader()
    writer.writerows(resultats)

print("\nDonnees sauvegardees dans :", fichier_csv)