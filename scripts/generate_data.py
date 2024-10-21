import os
import pandas as pd
import numpy as np

# Paramètres de génération
nombre_de_lignes = [10000, 100000, 500000, 1000000]  # tailles de datasets
colonnes = ['id', 'colonne_a_trier', 'colonne_condition', 'colonne1', 'colonne2', 'colonne_cible']

# Chemin du dossier
directory = 'donnees'

# Vérifier si le dossier existe, sinon le créer
if not os.path.exists(directory):
    os.makedirs(directory)

# Boucle pour créer les fichiers CSV de différentes tailles
for n in nombre_de_lignes:
    # Générer des données synthétiques
    data = {
        'id': range(1, n + 1),
        'colonne_a_trier': np.random.rand(n) * 1000,  # Valeurs aléatoires entre 0 et 1000
        'colonne_condition': np.random.randint(1, 1000, size=n),  # Valeurs entre 1 et 1000
        'colonne1': np.random.rand(n) * 100,  # Valeurs aléatoires
        'colonne2': np.random.rand(n) * 200,  # Valeurs aléatoires
        'colonne_cible': np.random.choice(['A', 'B', 'C', 'D'], size=n)  # Catégories
    }
    # Créer un DataFrame
    df = pd.DataFrame(data)

    # Sauvegarder en CSV dans le dossier "donnees"
    df.to_csv(f'{directory}/synthétiques_{n}.csv', index=False)
    print(f'Fichier CSV généré: synthétiques_{n}.csv')