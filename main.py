import random
import folium
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from deap import base, creator, tools, algorithms

class PizzaDeliveryOptimization:
    def __init__(self, delivery_points, population_size=200, generations=200):
        self.delivery_points = delivery_points
        self.population_size = population_size
        self.generations = generations
        self.toolbox = base.Toolbox()
        self._setup_genetic_algorithm()

    def _setup_genetic_algorithm(self):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        self.toolbox.register("indices", random.sample, range(len(self.delivery_points)), len(self.delivery_points))
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.indices)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", self._route_distance)
        self.toolbox.register("mate", tools.cxOrdered)
        self.toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def _route_distance(self, individual):
        total_distance = sum(
            geodesic(self.delivery_points[individual[i - 1]], self.delivery_points[individual[i]]).km
            for i in range(len(individual))
        )
        return (total_distance,)

    def random_route_stats(self, n=1000):
        distances = [
            self._route_distance(random.sample(range(len(self.delivery_points)), len(self.delivery_points)))[0]
            for _ in range(n)
        ]
        return sum(distances) / n, min(distances)

    def optimize_route(self):
        pop = self.toolbox.population(n=self.population_size)
        algorithms.eaSimple(pop, self.toolbox, cxpb=0.8, mutpb=0.2, ngen=self.generations, verbose=True)

        best_route = tools.selBest(pop, k=1)[0]
        best_distance = self._route_distance(best_route)[0]
        return best_route, best_distance

    def plot_results(self, best_route, map_file="rota_otimizada_pizzaria.html"):
        optimized_route = [self.delivery_points[i] for i in best_route + [best_route[0]]]

        # Mapa interativo
        mapa = folium.Map(location=self.delivery_points[0], zoom_start=14)
        for lat, lon in self.delivery_points:
            folium.Marker([lat, lon]).add_to(mapa)

        folium.PolyLine(optimized_route, color="red", weight=2.5, opacity=1).add_to(mapa)
        mapa.save(map_file)
        print(f"✅ Mapa salvo em '{map_file}'")

        # Gráfico estático
        lat, lon = zip(*optimized_route)
        plt.figure(figsize=(10, 8))
        plt.plot(lon, lat, marker='o')
        plt.title("Rota Otimizada para Entregas - Pizzaria Delivery (Cafarnaum-BA)")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(True)
        plt.show()


def main():
    delivery_points = [
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

    optimizer = PizzaDeliveryOptimization(delivery_points)
    best_route, best_distance = optimizer.optimize_route()

    print("\n✅ Melhor rota encontrada:", best_route)
    print(f"✅ Distância total da melhor rota: {best_distance:.2f} km")

    avg_random, best_random = optimizer.random_route_stats()
    print(f"\n🔀 Média distância rota aleatória: {avg_random:.2f} km")
    print(f"🔀 Melhor distância rota aleatória: {best_random:.2f} km")

    optimizer.plot_results(best_route)


if __name__ == "__main__":
    main()