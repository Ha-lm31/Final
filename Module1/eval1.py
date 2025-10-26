import os
import json

# 📁 Dossier contenant les résultats
RESULT_DIR = r"C:\Users\ot\Desktop\ATST\Module1\result"

# Vérification du dossier
if not os.path.exists(RESULT_DIR):
    print(f"❌ Le dossier '{RESULT_DIR}' est introuvable.")
    exit()

# Liste de tous les fichiers JSON dans result/
result_files = [f for f in os.listdir(RESULT_DIR) if f.endswith(".json")]

if not result_files:
    print(f"⚠️ Aucun fichier JSON trouvé dans '{RESULT_DIR}'.")
    exit()

# Dictionnaire pour stocker le total de véhicules par modèle
model_vehicle_counts = {}

for res_file in result_files:
    model_name = res_file.replace(".json", "")
    res_path = os.path.join(RESULT_DIR, res_file)

    try:
        with open(res_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"⚠️ Erreur lecture {res_file} : {e}")
        continue

    total = 0
    for item in data:
        # additionne toutes les valeurs sauf l'ID
        total += sum(v for k, v in item.items() if k != "id-img")

    model_vehicle_counts[model_name] = total

# Trie les modèles par total décroissant
sorted_models = sorted(model_vehicle_counts.items(), key=lambda x: x[1], reverse=True)

# Affichage des résultats
print("\n🚗 Classement des modèles selon le total de véhicules détectés :")
for rank, (model, total) in enumerate(sorted_models, start=1):
    print(f"{rank:>2}. {model:<15} → {total} véhicules détectés")

# Sauvegarde dans un fichier résumé
summary_path = os.path.join(RESULT_DIR, "summary1.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(sorted_models, f, ensure_ascii=False, indent=4)

print(f"\n💾 Résumé enregistré dans : {summary_path}")
