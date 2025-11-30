import pandas as pd
import random

# Inladen van dataset met clusters
# Dit is de output van ml_clustering.py
df = pd.read_csv("../data/clustered_species.csv")

# -----------------------------
# Difficulty Mode functie
# -----------------------------
def get_random_word(difficulty="normaal"):
    """
    Retourneert een willekeurige plantensoort op basis van de moeilijkheidsgraad.
    Clusters:
        0 = makkelijke, korte namen
        1 = normale namen
        2 = moeilijke, lange namen
    """

    if difficulty == "makkelijk":
        subset = df[df["cluster"] == 0]
    elif difficulty == "moeilijk":
        subset = df[df["cluster"] == 2]
    else:
        subset = df[df["cluster"] == 1]

    # Omzetten naar lijst en random woord kiezen
    species_list = subset["species"].tolist()
    return random.choice(species_list)

# -----------------------------
# Demo prints
# -----------------------------
if __name__ == "__main__":
    print("Makkelijk woord:", get_random_word("makkelijk"))
    print("Normaal woord:", get_random_word("normaal"))
    print("Moeilijk woord:", get_random_word("moeilijk"))
