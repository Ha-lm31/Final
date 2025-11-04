# pour analyser les résultats

import pandas as pd
import matplotlib.pyplot as plt

# === 1. Lecture du fichier CSV ===
# Assure-toi que sim-resultas.csv est dans le même dossier que ce script
df = pd.read_csv('sim-resultas.csv')

# === 2. Vérification du contenu ===
print("Aperçu des données :")
print(df.head())

# === 3. Calcul du total moyen par 'case' ===
# (au cas où il y a plusieurs lignes pour un même scénario)
df_grouped = df.groupby('case')['total'].mean().reset_index()

# === 4. Création du graphique ===
plt.figure(figsize=(8, 4))

# Tracer chaque système avec une couleur distincte
for i, row in df_grouped.iterrows():
    color = 'g' if 'G' in row['case'] or 'A' in row['case'] else 'r'  # vert pour proposé, rouge pour actuel
    plt.plot(row['case'], row['total'], 'o-', color=color, label=row['case'])

# === 5. Mise en forme du graphique ===
plt.title('Comparison: Current System vs Proposed System')
plt.xlabel('Simulation Cases')
plt.ylabel('Number of vehicles passed per 5 minutes')
plt.ylim(0, df_grouped['total'].max() + 20)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# === 6. Affichage ===
plt.show()
