import os
import shutil
from ultralytics import YOLO

# 📁 Chemin complet du dossier 'models' (modifie-le si besoin)
models_dir = r"/workspaces/Final/Module1/models"

# Vérifie si le dossier existe avant de commencer
if not os.path.exists(models_dir):
    raise FileNotFoundError(f"❌ Le dossier '{models_dir}' n'existe pas. Crée-le avant d'exécuter ce script.")

print(f"📁 Dossier trouvé : {models_dir}\n")

# 📦 Liste des modèles YOLO à vérifier / télécharger
model_names = [
    # YOLOv8
    "yolov8n.pt", "yolov8s.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt",
    # YOLOv9
    "yolov9t.pt", "yolov9s.pt", "yolov9m.pt", "yolov9c.pt", "yolov9e.pt",
    # YOLOv10
    "yolov10n.pt", "yolov10s.pt", "yolov10m.pt", "yolov10b.pt", "yolov10l.pt", "yolov10x.pt",
    # YOLOv11
    #"yolov11n.pt", "yolov11s.pt", "yolov11m.pt", "yolov11l.pt", "yolov11x.pt",
    # YOLOv12
    #"yolov12n.pt", "yolov12s.pt", "yolov12m.pt", "yolov12l.pt", "yolov12x.pt"
]

print("🔍 Vérification et téléchargement des modèles YOLO...\n")

for model_name in model_names:
    model_path = os.path.join(models_dir, model_name)

    if os.path.exists(model_path):
        print(f"✅ {model_name} déjà présent dans '{models_dir}'.")
        continue

    print(f"⬇️ Téléchargement de {model_name} ...")
    try:
        # Télécharge le modèle via Ultralytics
        model = YOLO(model_name)

        # Si le fichier est téléchargé dans le répertoire courant, on le déplace
        src_path = os.path.join(os.getcwd(), model_name)
        if os.path.exists(src_path):
            shutil.move(src_path, model_path)
        else:
            model.save(model_path)

        print(f"✅ {model_name} enregistré dans '{models_dir}'.\n")

    except Exception as e:
        print(f"❌ Erreur lors du téléchargement de {model_name}: {e}\n")

print("\n🎯 Tous les modèles sont prêts dans le dossier 'C:\\Users\\ot\\Desktop\\ATST\\Module1\\models' ✅")
