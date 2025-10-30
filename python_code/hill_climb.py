import random

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][path[0]]
    return cost

def hill_climb(n, tries=1000):
    path = list(range(n))
    best = path_cost(path)

    for _ in range(tries):
        new_path = path[:]
        i, j = random.sample(range(n), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]

        new_cost = path_cost(new_path)
        if new_cost < best:
            path, best = new_path, new_cost

    return path, best

best_path, best_cost = hill_climb(4)
print("Best path:", best_path)
print("Best cost:", best_cost)
