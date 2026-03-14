# Réseau de Vols entre Villes

## Description du projet

Ce projet consiste à modéliser et analyser un **réseau de vols entre différentes villes européennes** à l’aide de **Python** et de la **théorie des graphes**.

Dans ce modèle :

* Les **villes représentent les nœuds du graphe**
* Les **vols directs représentent les arêtes**
* Les **distances entre les villes représentent le poids des arêtes**

L’objectif est de représenter ce réseau et d’en analyser certaines propriétés afin de mieux comprendre la structure du réseau de transport.

---

# Objectifs

Les objectifs du projet sont :

* modéliser un **réseau de transport sous forme de graphe**
* visualiser un **réseau de vols entre villes**
* analyser les **connexions entre les villes**
* déterminer **la ville la plus connectée**
* calculer **le plus court chemin entre deux destinations**
* analyser la **structure globale du réseau**

---

# Exécution du programme

Le programme va :

1. créer un **graphe représentant les vols entre villes**
2. afficher le **graphe du réseau**
3. analyser certaines propriétés du réseau
4. afficher les résultats dans le terminal

Image du réseau :

![Graphe du réseau](reseaux-vols.png)

---

# Structure du graphe

Chaque liaison aérienne est définie par :

```
(ville_depart, ville_arrivee, distance)
```

Exemple :

```
("Paris", "Londres", 450)
("Paris", "Madrid", 1050)
("Rome", "Athènes", 1260)
```

La distance est exprimée en **kilomètres**.

---

# Fonctionnalités du projet

Le programme permet de :

* créer un **graphe de vols**
* représenter visuellement le **réseau de transport**
* afficher le **nombre de villes et de liaisons**
* identifier les **villes importantes dans le réseau**
* analyser les **chemins possibles entre les villes**

---

# Exemple de résultat

Le programme peut afficher par exemple :

```
Nombre de villes : 15
Nombre de liaisons : 23
Ville la plus connectée : Paris
```

Une visualisation du réseau est également générée.

---

# Auteur

Projet réalisé par **MARTIN--GRENTZINGER Louis**
