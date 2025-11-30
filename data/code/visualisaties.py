import pandas as pd
import matplotlib.pyplot as plt

# Inladen van de schoongemaakte dataset
df = pd.read_csv("../data/clean_species.csv")

# -----------------------------
# Visualisatie 1: Top 10 soorten
# -----------------------------
def plot_top_10_species():
    top = df["species"].value_counts().head(10)

    plt.figure(figsize=(8, 5))
    top.plot(kind="bar")
    plt.title("Top 10 meest voorkomende plantensoorten")
    plt.xlabel("Soort")
    plt.ylabel("Aantal observaties")
    plt.tight_layout()
    plt.show()

# -----------------------------------
# Visualisatie 2: Verdeling categorieën
# -----------------------------------
def plot_category_distribution():
    cat_counts = df["category"].value_counts()

    plt.figure(figsize=(6, 6))
    cat_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Verdeling categorieën binnen de dataset")
    plt.ylabel("")  # pie charts hebben geen y-label nodig
    plt.show()


# -----------------------------
# Run beide visualisaties
# -----------------------------
if __name__ == "__main__":
    print("Visualisatie 1: Top 10 soorten")
    plot_top_10_species()

    print("Visualisatie 2: Categorieverdeling")
    plot_category_distribution()
