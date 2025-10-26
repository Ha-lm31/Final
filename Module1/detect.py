import os
import json
from ultralytics import YOLO

# 🚗 Classes de véhicules à détecter
TARGET_CLASSES = ["car", "truck", "bus", "rickshaw", "bicycle"]

def count_vehicles(model, image_path):
    """Compte les véhicules détectés dans une image"""
    results = model.predict(source=image_path, conf=0.4, verbose=False)
    detections = results[0]
    counts = {cls: 0 for cls in TARGET_CLASSES}

    if detections and hasattr(detections, "names"):
        for box in detections.boxes:
            cls_id = int(box.cls[0])
            cls_name = detections.names[cls_id]
            if cls_name in counts:
                counts[cls_name] += 1

    return counts


def detect(model_path, dataset_dir, result_dir):
    """Applique un modèle YOLO sur toutes les images du dossier dataset"""
    image_files = [f for f in os.listdir(dataset_dir)
                   if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not image_files:
        print(f"⚠️ Aucune image trouvée dans '{dataset_dir}'.")
        return

    model_name = os.path.basename(model_path)
    result_path = os.path.join(result_dir, model_name.replace(".pt", ".json"))

    # ⏩ Si le résultat existe déjà, on saute
    if os.path.exists(result_path):
        print(f"⏩ {result_path} existe déjà, modèle ignoré.")
        return

    print(f"\n🔍 Application du modèle : {model_name}")
    model = YOLO(model_path)
    results_data = []

    for idx, img_name in enumerate(image_files):
        img_path = os.path.join(dataset_dir, img_name)
        counts = count_vehicles(model, img_path)
        results_data.append({
            "id-img": img_name,
            **counts
        })
        print(f"  ✅ {img_name} ({idx+1}/{len(image_files)})")

    # 💾 Sauvegarde du résultat JSON
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(results_data, f, ensure_ascii=False, indent=4)

    print(f"💾 Résultats enregistrés dans : {result_path}\n")
    print("🎯 Détection terminée avec succès.")
