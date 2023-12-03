class Node:
    def __init__(self, name):
        self.name = name
        self.orbitors = []
        self.orbiting = None

    def add_orbitor(self, node):
        self.orbitors.append(node)

    def orbit(self, node):
        self.orbiting = node


class Galaxy:
    def __init__(self):
        self.nodes = {}
        self.center = None

    def get_or_add_node(self, node_name):
        if node_name in self.nodes.keys():
            return self.nodes[node_name]
        self.nodes[node_name] = Node(node_name)
        return self.nodes[node_name]

    def get_num_direct_orbits(self):
        if len(self.nodes.keys()) == 0:
            raise ("No center of galaxy")

        count = 0
        for v in self.nodes.values():
            count += len(v.orbitors)
        return count

    def get_num_indirect_orbits(self):

        if len(self.nodes.keys()) == 0:
            raise ("No center of galaxy")

        count = 0
        for v in self.nodes.values():
            curr = v.orbiting
            while curr != None and curr.orbiting != None:
                count += 1
                curr = curr.orbiting

        return count

    def get_min_transfers(self, me, to):
        my_orbits = {}
        count = -1
        curr = me.orbiting
        while curr != None:
            count += 1
            my_orbits[curr.elevation] = count
            curr = curr.orbiting

        count = -1
        curr = to.orbiting
        while curr != None:
            count += 1
            if curr.elevation in my_orbits:
                return my_orbits[curr.elevation] + count
            curr = curr.orbiting

        raise (f"No path to node {to} from {me}")


if __name__ == "__main__":

    galaxy = Galaxy()
    with open("../input/input_6.txt") as f:
        for line in f:
            [item, orbitor] = line.split(")")
            item_node = galaxy.get_or_add_node(item.strip())
            orbitor_node = galaxy.get_or_add_node(orbitor.strip())

            item_node.add_orbitor(orbitor_node)
            orbitor_node.orbit(item_node)

            galaxy.get_or_add_node(item_node)
            galaxy.get_or_add_node(orbitor_node)

            if item == "COM":
                galaxy.center = item_node

    directs = galaxy.get_num_direct_orbits()
    indirects = galaxy.get_num_indirect_orbits()
    transfers = galaxy.get_min_transfers(
        galaxy.get_or_add_node("YOU"), galaxy.get_or_add_node("SAN")
    )

    print(
        f"Direct orbits: {directs}, Indirect orbits: {indirects}, Total: {directs + indirects}"
    )
    print(f"Min transfers {transfers}")
