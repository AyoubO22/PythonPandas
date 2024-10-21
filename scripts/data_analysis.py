import pandas as pd
import time

# Fonction pour mesurer le temps d'exécution
def mesurer_temps(fonction):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultat = fonction(*args, **kwargs)
        end_time = time.time()
        print(f"Temps d'exécution de {fonction.__name__}: {end_time - start_time:.2f} secondes")
        return resultat
    return wrapper

@mesurer_temps
def importer_donnees(file_path):
    return pd.read_csv(file_path)

@mesurer_temps
def trier_donnees(df, colonne):
    return df.sort_values(by=colonne)

@mesurer_temps
def filtrer_donnees(df, condition):
    return df.query(condition)

@mesurer_temps
def calculer_statistiques(df, colonnes):
    return df[colonnes].mean(), df[colonnes].sum()

# Fonction principale pour exécuter les tests
def executer_tests(file_path):
    df = importer_donnees(file_path)

    # Tri des données
    df_trie = trier_donnees(df, 'colonne_a_trier')

    # Filtrage des données
    df_filtre = filtrer_donnees(df_trie, 'colonne_condition > 500')

    # Calcul des statistiques
    moyennes, sommes = calculer_statistiques(df_filtre, ['colonne1', 'colonne2'])
    print("Moyennes :", moyennes)
    print("Sommes :", sommes)

# Exemple d'utilisation
if __name__ == "__main__":
    for taille in ['donnees/synthétiques_10000.csv',
                   'donnees/synthétiques_100000.csv',
                   'donnees/synthétiques_500000.csv',
                   'donnees/synthétiques_1000000.csv']:
        print(f"\nTests sur {taille}:")
        executer_tests(taille)
