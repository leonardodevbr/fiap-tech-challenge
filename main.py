import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

NUM_CITIES = 15
random.seed(42)
cities = np.random.rand(NUM_CITIES, 2) * 100

def distance(individual):
    total_distance = 0
    for i in range(len(individual)):
        city1 = cities[individual[i - 1]]
        city2 = cities[individual[i]]
        total_distance += np.linalg.norm(city1 - city2)
    return (total_distance,)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(NUM_CITIES), NUM_CITIES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", distance)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=100)
    algorithms.eaSimple(pop, toolbox, cxpb=0.8, mutpb=0.2, ngen=100, verbose=True)

    best = tools.selBest(pop, k=1)[0]
    print("Melhor rota:", best)
    print("Distância total:", distance(best)[0])

    plt.figure(figsize=(8, 6))
    route = cities[best + [best[0]]]
    plt.plot(route[:, 0], route[:, 1], marker='o', linestyle='-')
    plt.title("Rota otimizada por Algoritmo Genético")
    plt.grid(True)

    def random_route_distance(cities, n=1000):
        distances = []
        for _ in range(n):
            route = np.random.permutation(len(cities))
            dist = distance(route)[0]
            distances.append(dist)
        return np.mean(distances), np.min(distances)

    media_aleatoria, melhor_aleatoria = random_route_distance(cities)
    print("\nMédia distância rota aleatória:", media_aleatoria)
    print("Melhor distância rota aleatória:", melhor_aleatoria)
    print("Distância Algoritmo Genético:", distance(best)[0])

    plt.show()

if __name__ == "__main__":
    main()
