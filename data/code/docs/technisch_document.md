# Technisch Document – Individuele Bijdrage (Thijs)
Minor Big Data & Design – Tech Class  
Hogeschool Utrecht

Dit document beschrijft **mijn eigen technische bijdrage** binnen het iNaturalist project van de UX-challenge.  
Mijn groepsgenoot Berend heeft het originele Plantle-algoritme gebouwd. Ik heb dit **niet** gemaakt en claim dat ook niet.

In deze opdracht laat ik zien:
- mijn eigen dataselectie & opschoning  
- mijn eigen visualisaties  
- mijn eigen machine learning experiment  
- mijn eigen uitbreiding op Plantle  
- mijn reflectie op het leerproces  

---

# 1. Achtergrond van het platform

Voor deze opdracht werken we met data van **iNaturalist**.  
Dat is een wereldwijd platform waar gebruikers foto’s van planten en dieren uploaden en feedback krijgen over de soort.

Het platform gebruikt:
- community-data (crowdsourcing)  
- automatisch soortherkenning via machine learning  
- een open data-structuur

**Bron:**  
iNaturalist developer documentation: https://www.inaturalist.org/pages/developers

Waarom dit relevant is voor de opdracht:  
Het laat zien hoe een **datagedreven platform** werkt en hoe data terugkomt in functies, games of analyses zoals Plantle.

---

# 2. Wat het Plantle-algoritme doet

Plantle is een Wordle-achtige game, maar dan met plantennamen.  
Gebruiker moet de juiste soort raden. Het systeem geeft kleurfeedback die aangeeft of de letters goed staan of niet.

Het originele algoritme:
- kiest elke dag een plantensoort  
- vergelijkt input met het juiste antwoord  
- geeft feedback per letter  
- is gemaakt door mijn groepsgenoot Berend  

Mijn werk begint **ná het bestaande algoritme**.  
Ik heb gekeken hoe ik vanuit data een **uitbreiding** kon maken die iets toevoegt aan het spel.

---

# 3. Mijn eigen bijdrage – Data, Visualisaties, ML & Uitbreiding

## 3.1 Dataset selectie en opschoning

Ik wilde een kleine, overzichtelijke dataset waarmee ik:
- visualisaties kon maken  
- een simpele ML-stap kon uitvoeren  
- logische moeilijkheidsgradaties kon bepalen voor mijn uitbreiding  

Daarom koos ik voor een subset van plantensoorten uit iNaturalist.  
Ik heb alleen kolommen gehouden die voor mij relevant waren:
- species (naam van de plant)  
- kingdom (alleen Plantae)  
- category  
- frequency / count  

### Opschoning
Ik heb lege waarden verwijderd en alles gefilterd op kingdom = "Plantae".

```python
import pandas as pd

df = pd.read_csv("data/sample_species.csv")

df = df.dropna(subset=["species"])
df = df[df["kingdom"] == "Plantae"]

df.to_csv("data/clean_species.csv", index=False)

print("Schoonmaken afgerond. Aantal soorten:", len(df))
```

**Waarom deze dataset werkt voor mijn doel:**  
- Kleine dataset → goed te begrijpen  
- Duidelijke labels  
- Perfect om clusters of grafieken van te maken  
- Direct bruikbaar om de moeilijkheid van woorden te bepalen in Plantle  

---

## 3.2 Visualisaties (criterium 1)

Ik heb twee eigen visualisaties gemaakt om de dataset beter te begrijpen.

### 📊 Visualisatie 1 – Top 10 meest voorkomende plantensoorten

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean_species.csv")

top = df["species"].value_counts().head(10)

plt.figure(figsize=(8,5))
top.plot(kind="bar")
plt.title("Top 10 voorkomende plantensoorten")
plt.xlabel("Soort")
plt.ylabel("Aantal observaties")
plt.tight_layout()
plt.show()
```

**Wat ik eruit haalde:**  
Ik zag welke soorten heel vaak voorkomen, wat handig is voor spelbalans: te veel voorkomende soorten zijn makkelijker te raden.

---

### 📊 Visualisatie 2 – Verdeling per categorie

```python
cat_counts = df["category"].value_counts()

plt.figure(figsize=(6,6))
cat_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Verdeling categorieën binnen de dataset")
plt.show()
```

**Wat ik eruit haalde:**  
Ik kreeg inzicht in hoe divers de dataset was en welke groepen oververtegenwoordigd zijn.

---

## 3.3 Machine Learning stap (criterium 2)

Ik heb gekozen voor een simpele ML-techniek: **KMeans clustering**.  
Die is begrijpelijk en werkt goed op 1 feature.

### Welke feature?
Ik heb gekeken naar de **lengte van plantennamen**.

```python
df["length"] = df["species"].apply(len)
```

### Waarom?
- Korte namen zijn vaak makkelijker ("oak", "ivy")  
- Lange namen zijn vaak moeilijker (bijv. Latijnse namen)  
- Dit past perfect bij een moeilijkheidsmodus voor Plantle  

### KMeans clustering

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df[["length"]])

print(df[["species", "length", "cluster"]].head())
```

### Interpretatie van mijn ML-resultaat
- **Cluster 0** → korte namen → makkelijk  
- **Cluster 1** → gemiddelde lengte → normaal  
- **Cluster 2** → langere namen → moeilijk  

Dit was precies wat ik nodig had voor mijn uitbreiding.

---

## 3.4 Uitbreiding: Difficulty Mode voor Plantle

Ik heb mijn ML-resultaten gebruikt om een **moeilijkheidsmodus** toe te voegen aan het originele Plantle-spel.

### De drie moeilijkheidslevels
- **Makkelijk** → pakt woorden uit cluster 0  
- **Normaal** → pakt woorden uit cluster 1  
- **Moeilijk** → pakt woorden uit cluster 2  

### Code van mijn uitbreiding

```python
import pandas as pd
import random

df = pd.read_csv("data/clean_species.csv")

def get_random_word(difficulty="normaal"):
    if difficulty == "makkelijk":
        subset = df[df["cluster"] == 0]
    elif difficulty == "moeilijk":
        subset = df[df["cluster"] == 2]
    else:
        subset = df[df["cluster"] == 1]

    return random.choice(subset["species"].tolist())

# Test
print("Woord (moeilijk):", get_random_word("moeilijk"))
```

### Wat werkte goed?
- De moeilijkheidslevels voelen logisch aan  
- De ML-groepen maken het systeem objectiever dan handmatig ingedeelde woorden  

### Wat kon beter?
- Soms vallen lange makkelijke soorten toch in “moeilijk”  
- Dit komt omdat de clustering alleen naar **lengte** kijkt  
- Voor een vervolg zou ik misschien meerdere features gebruiken  

---

# 4. Individuele Reflectie

## 4.1 Mijn bijdrage aan data & visualisatie
Ik heb een eigen dataset gekozen en opgeschoond.  
Hierna heb ik twee visualisaties gemaakt die mij hielpen beter inzicht te krijgen in de verdeling van soorten.  
Dit gaf me een goede basis voor de rest van mijn opdracht.

## 4.2 Mijn bijdrage aan het algoritme
Ik heb zelf KMeans gebruikt om een clustering te maken op basis van naam-lengte.  
Dit was nieuw voor mij, maar doordat ik het simpel hield, kon ik het goed begrijpen.  
De ML-uitkomst gebruikte ik in mijn uitbreiding.

## 4.3 Mijn bijdrage aan de uitbreiding
Ik heb een difficulty mode gebouwd op basis van data én ML.  
Dit vond ik het leukste deel, omdat je echt ziet hoe data de game-beleving kan beïnvloeden.  
Soms werkte het niet perfect, maar dat hoort bij experimenteren.

## 4.4 Wat ik heb geleerd in vier weken
- Werken met Pandas, Matplotlib en scikit-learn  
- Hoe je data schoonmaakt en voorbereid  
- Hoe machine learning werkt op basisniveau  
- Hoe je een bestaande applicatie uitbreidt met eigen functies  
- Dat kleine technische stappen al veel impact kunnen hebben in een datagedreven product  

---

# 5. Conclusie

In deze opdracht heb ik laten zien hoe ik met een haalbare dataset, simpele visualisaties en een basis-ML-methode een uitbreiding kon maken die daadwerkelijk iets toevoegt aan Plantle.

Het was leerzaam om te merken dat je ook zonder heel veel ervaring toch een **datagedreven functie** kunt bouwen die waarde toevoegt aan een platform.

