# TP2-REP-MH-VVK


## Expérience avec python

### Environnement
L'environnement utilisé pour la compilation et le calcul en python est décrit ci-dessous :
* Windows10 22H2
* VirtualBox Ubuntu 24.04.1 LTS
* Intel® Core™ i5-10400H × 4
* Python 3.12.3

### Résultat obtenu

Le programme donne des résultat qui oscillent entre 75,5% et 75,8% d'erreur

### Reproduction

Pour reproduire l'expérience : 
* Exécuter le fichier tp2-rep-mh-vvk/repro.py

## Expérience avec Scratch

L'environnement utilisé pour le calcul sur Scratch (à imiter un maximum pour retrouver les mêmes résultats) est :
* Windows 11, version 23H2
* Google Chrome Version 129.0.6668.90
A noter que les calculs s'éxecutent sur les serveurs de Scratch, ce qui rend une imitation de l'environnement moins (voir non) nécessaire.

Pour reproduire le test de l'associativité x(y+z) == (x+y)+z sur Scratch, suivre les étapes suivantes :

1. Télécharger le fichier source "Exo 1.sb3" disponible sur le Git.

2. Se connecter avec le navigateur sur : https://scratch.mit.edu/projects/editor/?tutorial=getStarted

3. Cliquer sur l'icône de fichier puis "Load from your computer".

4. Importer le fichier téléchargé lors de l'étape 1.

5. Cliquer sur le drapeau vert. Le programme génère 1M de triplettes (x,y,z) aléatoires comprises entre 0.0 et 1000.0.

6. Le résultat final s'affiche en haut à droite dans la case "taux". Le taux trouvé est 0.746.

Note : il est possible de changer le nombre de générations de triplettes générées avec le bloc "set nbRep to ...". nboktemoin est une variable qui permet de montrer l'avancer du calcul (elle va de 0 au nombre de nbRep défini).

