import pandas as pd

# Simpel data cleaning script voor mijn iNaturalist subset
# Dit script leest een CSV in, schoont hem op en slaat hem weer op.

# Inladen van data (vervang 'sample_species.csv' als jouw bestand anders heet)
df = pd.read_csv("../data/sample_species.csv")

# Lege soortnamen verwijderen
df = df.dropna(subset=["species"])

# Alleen planten houden
df = df[df["kingdom"] == "Plantae"]

# Schoongemaakte dataset opslaan
df.to_csv("../data/clean_species.csv", index=False)

print("Schoonmaken afgerond! Aantal overgebleven soorten:", len(df))

