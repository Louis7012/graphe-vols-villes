import random
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

vols = [
    ("Paris", "Londres", 450),
    ("Paris", "Madrid", 1050),
    ("Paris", "Rome", 1100),
    ("Paris", "Amsterdam", 520),
    ("Londres", "Berlin", 930),
    ("Londres", "Dublin", 460),
    ("Madrid", "Lisbonne", 625),
    ("Madrid", "Barcelone", 505),
    ("Rome", "Milan", 600),
    ("Rome", "Athenes", 1260),
    ("Berlin", "Varsovie", 575),
    ("Berlin", "Prague", 350),
    ("Amsterdam", "Copenhague", 620),
    ("Copenhague", "Stockholm", 525),
    ("Athenes", "Istanbul", 560),
    ("Milan", "Vienne", 625),
    ("Vienne", "Prague", 330),
    ("Barcelone", "Rome", 850)
]

for ville1, ville2, distance in vols:
    G.add_edge(ville1, ville2, weight=distance)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(13, 9))
nx.draw_networkx_nodes(G, pos, node_size=2200)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=9)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

plt.title("Réseau de vols entre villes")
plt.axis("off")
plt.tight_layout()
plt.show()

depart = "Paris"
arrivee = "Istanbul"

chemin = nx.shortest_path(G, source=depart, target=arrivee, weight="weight")
distance = nx.shortest_path_length(G, source=depart, target=arrivee, weight="weight")

print("Plus court chemin de", depart, "à", arrivee, ":")
print(" -> ".join(chemin))
print("Distance totale :", distance, "km")

arbre_minimal = nx.minimum_spanning_tree(G, algorithm="kruskal", weight="weight")
poids_total = arbre_minimal.size(weight="weight")

print("
Arêtes de l'arbre couvrant minimal :")
for u, v, data in arbre_minimal.edges(data=True):
    print(f"{u} - {v} : {data['weight']} km")
print("Poids total :", int(poids_total), "km")

centralite_degre = nx.degree_centrality(G)
centralite_intermediaire = nx.betweenness_centrality(G, weight="weight")

ville_degre_max = max(centralite_degre, key=centralite_degre.get)
ville_intermediaire_max = max(centralite_intermediaire, key=centralite_intermediaire.get)

print("
Ville la plus connectée :", ville_degre_max)
print("Ville la plus stratégique :", ville_intermediaire_max)


def marche_aleatoire(graphe, ville_depart, nb_etapes):
    ville_actuelle = ville_depart
    parcours = [ville_actuelle]

    for _ in range(nb_etapes):
        voisins = list(graphe.neighbors(ville_actuelle))
        if not voisins:
            break
        ville_actuelle = random.choice(voisins)
        parcours.append(ville_actuelle)

    return parcours


parcours = marche_aleatoire(G, "Paris", 10)
print("
Simulation de déplacement :")
print(" -> ".join(parcours))
