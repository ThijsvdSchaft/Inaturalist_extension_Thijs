# iNaturalist / Plantle – Mijn individuele technische opdracht

Dit is mijn persoonlijke bijdrage binnen het iNaturalist / Plantle project voor de minor **Big Data & Design** (HU).

Mijn groepsgenoten hebben het originele Plantle-algoritme gebouwd.  
In deze repository laat ik **mijn eigen technische werk** zien — dus echt mijn aandeel binnen het project.

## Wat ik zelf heb gedaan

Deze repo bevat mijn individuele onderdelen:
- een kleine plantendataset geselecteerd en opgeschoond
- twee eigen visualisaties gemaakt (Matplotlib)
- een simpele ML-stap uitgevoerd (KMeans clustering)
- een uitbreiding gebouwd voor Plantle: *difficulty mode* op basis van de ML-clusters
- een technisch document waarin ik uitleg wat ik heb gedaan en waarom

Alles in deze repo is dus **mijn eigen werk**, gebaseerd op de bestaande code uit de groep.

## 📁 Structuur van deze repository

```
inaturalist-extension-thijs/
│
├── data/
│   └── clean_species.csv + andere dataset-bestanden
│
├── code/
│   ├── data_cleaning.py
│   ├── visualisaties.py
│   ├── ml_clustering.py
│   └── uitbreiding_plantle.py
│
└── docs/
    └── technisch_document.md
```

##  Benodigde libraries

Voor deze scripts heb je alleen een paar basis-libraries nodig:

```
pandas
matplotlib
scikit-learn
```

Installeren (optioneel):

```
pip install pandas matplotlib scikit-learn
```

## Starten

1. Download of clone deze repository  
2. Voer de scripts uit in de map **/code**  
3. De visualisaties worden automatisch geopend  
4. In het technisch document staat een volledige uitleg van mijn stappen

## Over dit project

Dit project is onderdeel van de module *Tech Class* binnen de minor.  
De focus ligt op:
- data gebruik & visualisatie  
- machine learning toepassen op beginner-niveau  
- experimenteren met nieuwe libraries  
- eigen features toevoegen aan een datagedreven platform  

## Auteur

Thijs  
Hogeschool Utrecht – CMD / Minor Big Data & Design
