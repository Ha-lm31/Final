import subprocess

# Liste des fichiers à exécuter
scripts = ["GS1.py", "GST2.py", "RST1.py", "ATST1.py", "TST1.py"]

for script in scripts:
    print(f"--- Exécution de {script} ---")
    subprocess.run(["python", script])  # ou ["python3", script] selon ton environnement
    print(f"--- Fin de {script} ---\n")
