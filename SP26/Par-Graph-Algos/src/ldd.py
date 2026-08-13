import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import heapq


def main():
    grid_size = 100
    n_nodes = grid_size * grid_size
    beta = 25.0

    print(f"Initializing {grid_size}x{grid_size} grid ({n_nodes} nodes)...")

    # Generate coordinates for the scatter plot
    x_coords = np.arange(n_nodes) % grid_size
    y_coords = np.arange(n_nodes) // grid_size

    # Sample d(u) ~ Exponential(mean=25)
    np.random.seed(45)  # For reproducible colors and shifts
    d = np.random.exponential(scale=beta, size=n_nodes)

    # Calculate the edge weight from supersource S to u: max(d(v)) - d(u)
    W = np.max(d)
    start_times = W - d

    # Priority Queue: stores tuples of (time, current_node, cluster_center)
    pq = []
    for i in range(n_nodes):
        heapq.heappush(pq, (start_times[i], i, i))

    visited = np.zeros(n_nodes, dtype=bool)

    # Prepare distinct colors using HSV space (random hue, high saturation/value)
    hues = np.random.rand(n_nodes)
    saturations = np.random.uniform(0.6, 1.0, n_nodes)
    values = np.random.uniform(0.7, 1.0, n_nodes)
    hsv_colors = np.column_stack((hues, saturations, values))
    cluster_colors = mcolors.hsv_to_rgb(hsv_colors)

    # Node colors for visualization (default pale gray)
    node_colors = np.full((n_nodes, 3), [0.85, 0.85, 0.85])

    frame_idx = 1
    print("Running parallel LDD BFS...")

    while pq:
        t, u, center = heapq.heappop(pq)

        # If the node is already claimed by a cluster, ignore this path
        if visited[u]:
            continue

        # Mark as visited and color it according to its cluster center
        visited[u] = True
        node_colors[u] = cluster_colors[center]

        # A node "times out" when the path from the supersource S is taken directly to it.
        is_new_cluster = u == center

        if is_new_cluster:
            # Generate the frame for this timeout event
            # HALVED FIGSIZE to tightly pack the fixed-size dots
            plt.figure(figsize=(5, 5))

            # Draw all nodes (visited ones have their cluster color, unvisited are pale gray)
            plt.scatter(x_coords, y_coords, c=node_colors, s=8, edgecolors="none")

            # Highlight the newly timed-out node with a red circle
            # Scaled s=50 slightly so it doesn't bleed too far into neighbors on the tighter grid
            plt.scatter(
                x_coords[u],
                y_coords[u],
                facecolors="none",
                edgecolors="red",
                s=50,
                linewidths=1.2,
            )

            plt.axis("off")
            plt.xlim(-2, grid_size + 1)
            plt.ylim(-2, grid_size + 1)

            filename = f"ldd_frame_{frame_idx:04d}.pdf"
            plt.savefig(filename, format="pdf", dpi=500, bbox_inches="tight")
            plt.close()

            print(f"Saved {filename} (Time: {t:.2f})")
            frame_idx += 1

        # Relax orthogonal neighbors (weight 1)
        if u % grid_size > 0:  # Left
            v = u - 1
            if not visited[v]:
                heapq.heappush(pq, (t + 1.0, v, center))
        if u % grid_size < grid_size - 1:  # Right
            v = u + 1
            if not visited[v]:
                heapq.heappush(pq, (t + 1.0, v, center))
        if u >= grid_size:  # Top
            v = u - grid_size
            if not visited[v]:
                heapq.heappush(pq, (t + 1.0, v, center))
        if u < n_nodes - grid_size:  # Bottom
            v = u + grid_size
            if not visited[v]:
                heapq.heappush(pq, (t + 1.0, v, center))

    # --- FINAL FRAME ---
    print("Generating final decomposition frame...")
    plt.figure(figsize=(5, 5))

    # Draw the final state of all nodes
    plt.scatter(x_coords, y_coords, c=node_colors, s=8, edgecolors="none")
    plt.axis("off")
    plt.xlim(-2, grid_size + 1)
    plt.ylim(-2, grid_size + 1)

    final_filename = "ldd_frame_final.pdf"
    plt.savefig(final_filename, format="pdf", dpi=500, bbox_inches="tight")
    plt.close()

    print(f"Complete. Generated {frame_idx} timeout frames + 1 final frame.")


if __name__ == "__main__":
    main()
