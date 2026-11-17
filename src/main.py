from entendendo_algoritmos.bellman_ford import bellman_ford, reconstruct_path


def exe():
    edges = [
        ("A", "B", 6),
        ("A", "C", 7),
        ("B", "C", 8),
        ("B", "D", 5),
        ("B", "E", -4),
        ("C", "D", -3),
        ("C", "E", 9),
        ("D", "B", -2),
        ("E", "A", 2),
        ("E", "D", 7),
    ]

    vertices = ["A", "B", "C", "D", "E"]

    distances, parents = bellman_ford(vertices, edges, "A")
    print(distances)
    print(parents)

    path = reconstruct_path(parents, "A", "E")
    print(path)
    print(distances["E"])


if __name__ == "__main__":
    exe()
