matrix = [
    [0, 5, 3, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 7],
    [1, 0, 0, 0]
]

# Přístup k hodnotě
vaha = matrix[0][1]   # Vrátí 5


class Graph:
    def __init__(self, n):
        """Konstruktor: n je počet uzlů grafu (0 až n-1)."""
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def reset(self):
        """Vyčistí graf."""
        for r in range(self.n):
            for c in range(self.n):
                self.matrix[r][c] = 0

    def add_edge(self, u, v, weight=1):
        """Přidá orientovanou hranu z u do v."""
        if 0 <= u < self.n and 0 <= v < self.n:
            self.matrix[u][v] = weight
        else:
            print(f"Chyba: Neplatný index uzlu ({u} nebo {v})!")

    def remove_edge(self, u, v):
        """Odstraní hranu u -> v."""
        self.add_edge(u, v, weight=0)

    def get_edge(self, u, v):
        """Vrátí váhu hrany u -> v."""
        return self.matrix[u][v]

    def has_edge(self, u, v):
        """Vrátí True, pokud hrana u -> v existuje."""
        return self.matrix[u][v] > 0

    def get_neighbors(self, u):
        """Vrátí seznam všech uzlů, do kterých vede hrana z u."""
        neighbors = []

        for v in range(self.n):
            if self.matrix[u][v] > 0:
                neighbors.append(v)

        return neighbors

    def out_degree(self, u):
        """Výstupní stupeň uzlu."""
        return len(self.get_neighbors(u))

    def in_degree(self, v):
        """Vstupní stupeň uzlu."""
        count = 0

        for u in range(self.n):
            if self.matrix[u][v] > 0:
                count += 1

        return count

    def print_matrix(self):
        """Vytiskne matici sousednosti."""
        print("    " + "  ".join(f"{c}" for c in range(self.n)))
        print("  +" + "---" * self.n)

        for r in range(self.n):
            row_str = "  ".join(
                f"{self.matrix[r][c]}" for c in range(self.n)
            )
            print(f"{r} | {row_str}")


# Vytvoření grafu
g = Graph(4)

g.add_edge(0, 1, weight=5)
g.add_edge(0, 2, weight=3)
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=7)
g.add_edge(3, 0, weight=1)

g.print_matrix()
print(g.has_edge(0, 1))
print(g.has_edge(1, 0))
print(g.get_neighbors(0))
print(g.out_degree(0))
print(g.in_degree(2))
