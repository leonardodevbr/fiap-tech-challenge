import random
import folium
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from deap import base, creator, tools, algorithms

locations = [
    (-11.694470747614645, -41.467859022939486),
    (-11.690149164483545, -41.47077254135551),
    (-11.691881475894112, -41.469221170245),
    (-11.692844243607777, -41.47189919759093),
    (-11.689319334022683, -41.47394114860833),
    (-11.689306173121015, -41.470325887716925),
    (-11.696172707088513, -41.46846174384558),
    (-11.69388086833337, -41.47286482599258),
    (-11.703544917154318, -41.470151813890034),
    (-11.702541689936462, -41.470664076402336),
    (-11.708965409656692, -41.47427736972155),
    (-11.689416330363684, -41.47474109801829),
    (-11.690619934729517, -41.46734090266138),
    (-11.692074283024706, -41.46695680947676),
    (-11.689792457305051, -41.4701063735906),
    (-11.697557132774259, -41.4689977688212),
    (-11.694009136397373, -41.46477217404899),
    (-11.691059774723337, -41.47465287331417),
]

NUM_LOCATIONS = len(locations)

def distance(individual):
    total_distance = 0
    for i in range(len(individual)):
        city1 = locations[individual[i - 1]]
        city2 = locations[individual[i]]
        total_distance += geodesic(city1, city2).km
    return (total_distance,)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(NUM_LOCATIONS), NUM_LOCATIONS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", distance)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def random_route_distance(locations, n=1000):
    distances = []
    for _ in range(n):
        route = random.sample(range(len(locations)), len(locations))
        dist = distance(route)[0]
        distances.append(dist)
    return sum(distances) / len(distances), min(distances)

def main():
    pop = toolbox.population(n=200)
    algorithms.eaSimple(pop, toolbox, cxpb=0.8, mutpb=0.2, ngen=200, verbose=True)

    best = tools.selBest(pop, k=1)[0]
    best_distance = distance(best)[0]

    print("\n✅ Melhor rota encontrada:", best)
    print(f"✅ Distância total da melhor rota: {best_distance:.2f} km")

    media_aleatoria, melhor_aleatoria = random_route_distance(locations)
    print(f"\n🔀 Média distância rota aleatória: {media_aleatoria:.2f} km")
    print(f"🔀 Melhor distância rota aleatória: {melhor_aleatoria:.2f} km")

    mapa = folium.Map(location=[-11.694470747614645, -41.467859022939486], zoom_start=14)

    for lat, lon in locations:
        folium.Marker([lat, lon]).add_to(mapa)

    rota = [locations[i] for i in best + [best[0]]]
    folium.PolyLine(rota, color="blue", weight=2.5, opacity=1).add_to(mapa)

    mapa.save("rota_otimizada_cafarnaum.html")
    print("✅ Mapa salvo em 'rota_otimizada_cafarnaum.html'")

    lat, lon = zip(*rota)
    plt.figure(figsize=(10, 8))
    plt.plot(lon, lat, marker='o')
    plt.title("Rota otimizada por Algoritmo Genético (Cafarnaum-BA)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()