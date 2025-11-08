# Système Intelligent de Gestion du Trafic
Intelligent Traffic Management System

[`Github Repo Link of Proposed System`](https://github.com/mihir-m-gandhi/Adaptive-Traffic-Signal-Timer)
[`Github Repo Link of Module1`](https://github.com/Ha-lm31/VehicleDetection.git)
- CMD
```
python --version
sudo apt-get update -y 
sudo apt-get install -y libgl1
python models.py
python main.py
python eval1.py
python RST1.py
python GST1.py
python ATST1.py
python TST1.py
python analyse.py
cd Module1
cd ..

git status
git add .
git commit -m "8tt commit"
git push -u origin main --force
git push -u origin main \ 

```

## Developped System

### Module de détection de véhicule
`Vehicle Detection Module`
Module1: 

En ce module, on prend un ensemble de données depuis Roboflow, on applique sur elle quelque modèle de YOLO récent pour détecter les types et nombres de véhicules dans un images, à conditions que on cont que les véhicules qui viens vers la CCTV.
Après, on compare les résultats pour aqquir le meillieur modèl.

### Module de commutation de signal
`Signal Switching Module` 

En a utiliser le meme principe.

### Module de simulation
`Simulation Module`

On a faire 5 cas : 

ATST : defaultRed, defaultGreen, defaultYellow, defaultMinimum, defaultMaximum, setTime(greenTime)
ATST : defaultRed, defaultGreen, defaultYellow, defaultMinimum, defaultMaximum, setTime(defaultGreen)

GST1 : defaultRed,defaultRed1, defaultRed2, defaultGreen, defaultYellow, defaultMinimum, defaultMaximum, setTime(greenTime)
GST2 : defaultRed, defaultRed1, defaultRed2, defaultGreen, defaultYellow, defaultMinimum, defaultMaximum, setTime(greenTime -1), 
RST : defaultRed, defaultGreen, defaultYellow, defaultMinimum, defaultMaximum, setTime(defaultGreen)
