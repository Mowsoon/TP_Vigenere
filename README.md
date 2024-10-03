# Cryptage et Analyse de Texte

Ce projet implémente des algorithmes de cryptage et des techniques d'analyse de texte, notamment la méthode de Vigenère, ainsi que des méthodes d'analyse de fréquence et de détection de motifs. Le code est écrit en Python et utilise diverses bibliothèques pour le traitement des chaînes de caractères et des statistiques.

## Fonctionnalités

- **Affichage et formatage des chaînes de caractères** : 
  - La fonction `affiche` permet de saisir une chaîne et de la formater en ne gardant que les caractères alphanumériques en minuscules.
  - La fonction `format` effectue un formatage similaire mais prend une chaîne en paramètre.

- **Cryptage et décryptage** :
  - La fonction `vigenere` permet de crypter et déchiffrer un message en utilisant la méthode de Vigenère.
  
- **Analyse de fréquence** :
  - La fonction `occurence` identifie les séquences de 3 caractères ou plus qui apparaissent plusieurs fois dans une chaîne.
  - La fonction `distance` calcule les distances entre les occurrences d'une séquence donnée.

- **Détection de motifs** :
  - La fonction `liste_diviseurs_commun` détermine les diviseurs communs des distances entre les occurrences.
  - La fonction `repetition` cherche des répétitions de séquences dans un texte donné.

- **Estimation de clé** :
  - La fonction `friedman` utilise l'équation de Friedman pour estimer la taille de la clé d'un texte chiffré.
  - La fonction `trouverCle` permet de trouver la clé en fonction de son estimation.

- **Analyse de probabilité** :
  - Les fonctions `trouverDeuxLettres` et `deuxLettresIdentiques` calculent la probabilité que deux lettres choisies aléatoirement soient identiques.

- **Fonctionnalité Babbage-Kasiki** : 
  - La méthode `methodeBabbageKasiki` permet d'analyser un texte chiffré pour déduire des informations sur la clé utilisée.

## Prérequis

- Python 3.x
- Bibliothèque standard de Python

## Utilisation

1. **Installation** : Clonez le dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-depot.git

