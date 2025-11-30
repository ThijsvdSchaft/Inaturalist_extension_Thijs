import pandas as pd
from sklearn.cluster import KMeans

# Inladen van de schoongemaakte dataset
df = pd.read_csv("../data/clean_species.csv")

# -----------------------------
# Stap 1: Feature maken
# -----------------------------
# Simpele feature: lengte van de soortnaam
df["length"] = df["species"].apply(len)

# -----------------------------
# Stap 2: KMeans clustering
# -----------------------------
# 3 clusters: makkelijk, normaal, moeilijk
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df[["length"]])

# -----------------------------
# Output tonen
# -----------------------------
print("Eerste 10 resultaten met clusters:")
print(df[["species", "length", "cluster"]].head(10))

# -----------------------------
# Optioneel: opslaan
# -----------------------------
df.to_csv("../data/clustered_species.csv", index=False)
print("\nNieuwe dataset opgeslagen als 'clustered_species.csv'")
