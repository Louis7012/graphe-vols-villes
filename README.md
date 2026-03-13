# graphe-vols-villes
# Réseau de Vols entre Villes

## Description du projet

Ce projet consiste à modéliser et analyser un réseau de vols entre différentes villes européennes à l’aide de Python et de la théorie des graphes.

Dans ce modèle :

* **Les villes représentent les nœuds du graphe**
* **Les vols directs représentent les arêtes**
* **Les distances entre les villes représentent le poids des arêtes**

L’objectif est de représenter ce réseau, d’en analyser certaines propriétés et de calculer le **plus court chemin entre deux villes**.

---

## Objectifs

Les objectifs du projet sont :

* modéliser un réseau de transport sous forme de graphe
* visualiser un réseau de vols entre villes
* analyser les connexions entre les villes
* déterminer la ville la plus connectée
* calculer le **plus court chemin entre deux destinations**

---

## Exécution du programme

Le programme va :

1. créer un graphe représentant les vols entre villes
2. afficher des **statistiques du réseau**
3. calculer le **plus court chemin entre Paris et Istanbul**
4. afficher le **graphe du réseau**
5. sauvegarder une image du réseau dans :


**image à rajouter**


---

## Structure du graphe

Chaque liaison aérienne est définie par :

(ville_depart, ville_arrivee, distance)


Exemple :

("Paris", "Londres", 450)
("Paris", "Madrid", 1050)
("Rome", "Athènes", 1260)


La distance est exprimée en **kilomètres**.

---

## Fonctionnalités du projet

Le programme permet de :

* créer un graphe de vols
* afficher le nombre de villes et de liaisons
* déterminer la **ville la plus connectée**
* calculer le **plus court chemin**
* afficher visuellement le réseau de vols
* mettre en évidence le trajet optimal sur le graphe

---

## Exemple de résultat

Le programme peut afficher par exemple :

Nombre de villes : 15
Nombre de liaisons : 23
Ville la plus connectée : Paris
Plus court chemin : Paris -> Rome -> Athènes -> Istanbul
Distance totale : 2920 km

Une visualisation du réseau est également générée.

---

## Auteur

Projet réalisé par **MARTIN--GRENTZINGER Louis**
