import os
import matplotlib.pyplot as plt

# Vérifier si le dossier 'resultats' existe, sinon le créer
if not os.path.exists('resultats'):
    os.makedirs('resultats')

# Données d'exécution
taille_fichiers = ['10k', '100k', '500k', '1M']
temps_import = [0.01, 0.08, 0.48, 0.97]
temps_tri = [0.00, 0.02, 0.16, 0.27]
temps_filtrage = [0.00, 0.00, 0.02, 0.02]
temps_stats = [0.00, 0.00, 0.01, 0.01]

# Création des graphiques
plt.figure(figsize=(10, 6))

plt.plot(taille_fichiers, temps_import, label='Temps d\'importation', marker='o')
plt.plot(taille_fichiers, temps_tri, label='Temps de tri', marker='o')
plt.plot(taille_fichiers, temps_filtrage, label='Temps de filtrage', marker='o')
plt.plot(taille_fichiers, temps_stats, label='Temps de calcul des stats', marker='o')

plt.xlabel('Taille des fichiers CSV')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Temps d\'exécution pour différentes tailles de fichiers')
plt.legend()
plt.grid(True)

# Sauvegarder le graphique
plt.savefig('resultats/temps_execution.png')
plt.show()

