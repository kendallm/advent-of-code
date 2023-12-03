class Grid:
    def __init__(self, default_values):
        self.grid = {}
        self.default = default_values

    def contains(self, coord):
        return coord in self.grid.keys()
    def get(self, coord, bounded=True):
        if coord in self.grid:
            return self.grid[coord]
        if bounded:
            raise KeyError(coord)
        return self.default()

    def put(self, coord, item):
        self.grid[coord] = item

    def items(self):
        return self.grid.items()
    def get_neighbor_coordinates(self, coord, diagonals=True, bounded=True):
        neighbors = []
        (x, y) = coord
        neighbors.append((x, y - 1))
        neighbors.append((x - 1, y))
        neighbors.append((x + 1, y))
        neighbors.append((x, y + 1))

        if diagonals:
            neighbors.append((x - 1, y - 1))
            neighbors.append((x + 1, y - 1))
            neighbors.append((x - 1, y + 1))
            neighbors.append((x + 1, y + 1))
        if bounded:
            neighbors = [x for x in neighbors if x in self.grid.keys()]

        return neighbors