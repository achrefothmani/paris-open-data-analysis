from models import EspaceVert
import requests
import json
from database import SessionLocal, engine, Base

db = SessionLocal()

Base.metadata.create_all(bind=engine)

data = requests.get("https://opendata.paris.fr/api/records/1.0/search/?dataset=espaces_verts&rows=2171").json()["records"]

for row in data:
    record = EspaceVert(
        annee_ouverture=row["fields"]["annee_ouverture"] if "annee_ouverture" in row['fields'] else None,
        type_ev=row["fields"]["type_ev"] if "type_ev" in row['fields'] else None,
        adresse_codepostal=row["fields"]["adresse_codepostal"] if "adresse_codepostal" in row['fields'] else None,
        surface_totale_reelle=row["fields"]["surface_totale_reelle"] if "surface_totale_reelle" in row['fields'] else None,
        nom=row["fields"]["nom_ev"] if "nom_ev" in row['fields'] else None,
        categorie=row["fields"]["categorie"] if "categorie" in row['fields'] else None
    )
    db.add(record)
db.commit()

db.close()

print("Data inserted successfully")
