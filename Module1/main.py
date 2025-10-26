import os
from detect import detect

# 📁 Chemins principaux
BASE_DIR = r"/workspaces/Final/Module1"
MODEL_DIR = os.path.join(BASE_DIR, "models")
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
RESULT_DIR = os.path.join(BASE_DIR, "result")

# Vérifie les dossiers
if not os.path.exists(MODEL_DIR):
    print(f"❌ Le dossier '{MODEL_DIR}' est introuvable.")
    exit()

if not os.path.exists(DATASET_DIR):
    print(f"❌ Le dossier '{DATASET_DIR}' est introuvable.")
    exit()

os.makedirs(RESULT_DIR, exist_ok=True)

# 🔍 Liste tous les fichiers .pt dans models/
model_files = [f for f in os.listdir(MODEL_DIR) if f.endswith(".pt")]

if not model_files:
    print(f"⚠️ Aucun modèle (.pt) trouvé dans '{MODEL_DIR}'.")
    exit()

# 🔁 Applique chaque modèle trouvé
for model_name in model_files:
    model_path = os.path.join(MODEL_DIR, model_name)
    print(f"\n🚀 Exécution du modèle : {model_name}")
    detect(model_path, DATASET_DIR, RESULT_DIR)

print("\n✅ Tous les modèles disponibles ont été testés.")
