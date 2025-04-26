import random
import math

# Step 1: Generate random points and clusters
def generate_data(filename="data.txt"):
    with open(filename, "w") as f:
        f.write("Points:\n")
        for _ in range(100):
            x, y = random.randint(0, 19), random.randint(0, 19)
            f.write(f"{x} {y}\n")
        f.write("Centers:\n")
        for _ in range(10):
            x, y = random.randint(0, 19), random.randint(0, 19)
            f.write(f"{x} {y}\n")

# Step 2: Read points and centers
def read_data(filename="data.txt"):
    points, centers = [], []
    with open(filename, "r") as f:
        lines = f.readlines()
        mode = None
        for line in lines:
            line = line.strip()
            if line == "Points:":
                mode = "points"
            elif line == "Centers:":
                mode = "centers"
            elif line:
                x, y = map(int, line.split())
                if mode == "points":
                    points.append((x, y))
                elif mode == "centers":
                    centers.append((x, y))
    return points, centers

# Step 3: Manhattan distance
def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# Step 4: K-Means clustering using Manhattan distance
def k_means(points, centers, iterations=5):
    for _ in range(iterations):
        clusters = [[] for _ in centers]
        for p in points:
            distances = [manhattan(p, c) for c in centers]
            min_index = distances.index(min(distances))
            clusters[min_index].append(p)
        # Recalculate centers
        for i, cluster in enumerate(clusters):
            if cluster:  # Avoid division by zero
                avg_x = sum(p[0] for p in cluster) / len(cluster)
                avg_y = sum(p[1] for p in cluster) / len(cluster)
                centers[i] = (round(avg_x), round(avg_y))
    return clusters, centers

# Step 5: Matrix visualization
def visualize(clusters, centers, size=20):
    grid = [["." for _ in range(size)] for _ in range(size)]

    # Mark points
    for idx, cluster in enumerate(clusters):
        symbol = chr(65 + idx)  # A, B, C, ..., J
        for x, y in cluster:
            grid[y][x] = symbol

    # Mark centers
    for x, y in centers:
        grid[y][x] = "#"

    for row in reversed(grid):  # Print from top to bottom
        print(" ".join(row))

# Main program
generate_data()
points, centers = read_data()
clusters, centers = k_means(points, centers)
visualize(clusters, centers)
