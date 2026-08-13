import matplotlib.pyplot as plt
import networkx as nx


def get_planar_tree_layout(tree, root=0):
    """
    Calculates a planar layout for a tree.
    X-coordinate = depth (distance from root).
    Y-coordinate = post-order traversal index to prevent edge crossings.
    """
    depths = nx.single_source_shortest_path_length(tree, root)
    directed_tree = nx.bfs_tree(tree, root)

    y_coords = {}
    y_counter = 0

    def assign_y(node):
        nonlocal y_counter
        children = list(directed_tree.successors(node))

        if not children:
            y_coords[node] = y_counter
            y_counter += 1
        else:
            for child in children:
                assign_y(child)
            y_coords[node] = (y_coords[children[0]] + y_coords[children[-1]]) / 2.0

    assign_y(root)
    return {node: (depths[node], y_coords[node]) for node in tree.nodes()}


def main():
    max_nodes = 4096
    print(f"Generating BA graph with {max_nodes} nodes...")
    G = nx.barabasi_albert_graph(max_nodes, 1)

    # 1. Calculate the layout ONCE using the full graph
    print("Calculating global layout...")
    global_pos = get_planar_tree_layout(G, root=0)

    # Calculate global boundaries to lock the camera (add a 5% margin)
    all_x = [pos[0] for pos in global_pos.values()]
    all_y = [pos[1] for pos in global_pos.values()]

    x_margin = (max(all_x) - min(all_x)) * 0.05 if max(all_x) != min(all_x) else 1
    y_margin = (max(all_y) - min(all_y)) * 0.05 if max(all_y) != min(all_y) else 1

    x_lim = (min(all_x) - x_margin, max(all_x) + x_margin)
    y_lim = (min(all_y) - y_margin, max(all_y) + y_margin)

    sizes = [8, 64, 512, 4096]

    for n in sizes:
        print(f"Processing size {n}...")
        sub_G = G.subgraph(range(n)).copy()

        # 2. Extract only the coordinates needed for this subgraph from the global layout
        sub_pos = {node: global_pos[node] for node in sub_G.nodes()}

        plt.figure(figsize=(17, 8.5))

        if sub_G.number_of_edges() > 0:
            nx.draw_networkx_edges(
                sub_G, sub_pos, edge_color="black", width=0.8, alpha=0.7
            )

        plt.axis("off")

        # 3. Lock the axes to the global boundaries so the graph doesn't shift or zoom
        plt.xlim(x_lim)
        plt.ylim(y_lim)

        filename = f"ba_tree_nodes_{n:04d}.pdf"
        plt.savefig(
            filename,
            format="pdf",
            dpi=500,
            orientation="landscape",
            bbox_inches="tight",
        )
        plt.close()

        print(f"Saved {filename}")


if __name__ == "__main__":
    main()
