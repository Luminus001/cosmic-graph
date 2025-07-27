# tp_matrix_simulation.py

import networkx as nx
import matplotlib.pyplot as plt

def build_tp_graph():
    G = nx.Graph()

    # Додаємо атом (Сонце) та планети як вершини
    G.add_node("☀️ Сонце", layer="атом")
    planets = ["Меркурій", "Венера", "Земля", "Марс", "Юпітер", "Сатурн", "Уран", "Нептун"]

    for planet in planets:
        G.add_node(planet, layer="планета")
        G.add_edge("☀️ Сонце", planet)

    # Додаємо супутники Землі й Юпітера як "нейтрони"
    moons = {
        "Земля": ["Місяць"],
        "Юпітер": ["Іо", "Європа", "Ганімед", "Каллісто"]
    }

    for planet, moon_list in moons.items():
        for moon in moon_list:
            G.add_node(moon, layer="супутник")
            G.add_edge(planet, moon)

    return G

def visualize_tp_graph(G):
    pos = nx.spring_layout(G, seed=42)
    layers = nx.get_node_attributes(G, 'layer')

    colors = {
        "атом": "#FFD700",        # золоте Сонце
        "планета": "#1E90FF",     # сині планети
        "супутник": "#A9A9A9",    # сірі супутники
    }

    node_colors = [colors.get(layers.get(node, ""), "#ccc") for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=10)
    plt.title("🌌 TP-граф Сонячної системи")
    plt.show()

if __name__ == "__main__":
    G = build_tp_graph()
    visualize_tp_graph(G)
