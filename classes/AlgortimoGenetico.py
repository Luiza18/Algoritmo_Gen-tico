from classes.Individuo import Individuo
import random as rd
import numpy as np
import copy as cp

class AlgoritmoGenetico:
    def __init__(self, numero_cidades, tamanho_populacao, taxa_cruzamento, taxa_mutacao, geracoes, elite, tsp):
        self.__numero_cidades = numero_cidades
        self.__tamanho_populacao = tamanho_populacao
        self.__taxa_cruzamento = taxa_cruzamento
        self.__taxa_mutacao = taxa_mutacao
        self.__geracoes = geracoes
        self.__elite = elite
        self.__tsp = tsp
        self.__populacao = self.__inicializa_populacao()

    def __inicializa_populacao(self):
        return [Individuo(self.__numero_cidades) for _ in range(self.__tamanho_populacao)]

    def avalia_fitness(self):
        for Individuo in self.__populacao:
            Individuo.calcula_fitness(self.__tsp)

    def selecao(self):

        total_fitness = sum(individuo.get_fiteness() for individuo in self.__populacao)
        pick = rd.uniform(0, total_fitness)
        current = 0
        for Individuo in self.__populacao:
            current += Individuo.get_fiteness()
            if current > pick:
                return cp.deepcopy(Individuo)

    #Refazer essa função
    def crossover(self, parent1:Individuo, parent2:Individuo):
        cut_point = rd.randint(1, self.__numero_cidades - 1)
        filho1, filho2 = np.zeros(self.__numero_cidades, dtype=int), np.zeros(self.__numero_cidades, dtype=int)
        filho1[:cut_point], filho2[:cut_point] = parent1.get_cromossomo()[:cut_point], parent2.get_cromossomo()[:cut_point]

        def fill_filho(filho, parent:Individuo):
            pos = cut_point
            for gene in parent.get_cromossomo():
                if gene not in filho:
                    filho[pos] = gene
                    pos += 1
            return filho

        filho1 = fill_filho(filho1, parent2)
        filho2 = fill_filho(filho2, parent1)

        return Individuo(self.__numero_cidades), Individuo(self.__numero_cidades)

    def mutacao(self, Individuo):
        # Mutação: troca dois genes aleatórios no cromossomo
        if rd.random() < self.__taxa_mutacao:
            idx1, idx2 = rd.sample(range(self.n), 2)
            Individuo.get_cromossomo()[idx1], Individuo.get_cromossomo()[idx2] = Individuo.get_cromossomo()[idx2], Individuo.get_cromossomo()[idx1]

    def evolve(self):
        # Ordena a população com base no fitness
        self.population.sort(key=lambda Individuo: Individuo.get_fiteness(), reverse=True)

        # Mantém a elite
        elite_count = int(self.__tamanho_populacao * self.__elite)
        new_population = self.population[:elite_count]

        # Gera nova população por cruzamento e mutação
        while len(new_population) < self.__tamanho_populacao:
            parent1 = self.selecao()
            parent2 = self.selecao()
            if rd.random() < self.__taxa_cruzamento:
                filho1, filho2 = self.crossover(parent1, parent2)
                self.mutate(filho1)
                self.mutate(filho2)
                new_population.extend([filho1, filho2])
            else:
                self.mutate(parent1)
                self.mutate(parent2)
                new_population.extend([parent1, parent2])

        self.population = new_population[:self.__tamanho_populacao]

    def run(self):
        # Executa o algoritmo genético
        self.evaluate_population()
        for gen in range(self.__geracoes):
            self.evolve()
            self.evaluate_population()
            best_Individuo = max(self.__populacao, key=lambda ind: ind.get_fiteness())
            print(f"Geração {gen}: Melhor distância = {1 / best_Individuo.get_fiteness()}")

        best_solution = max(self.__populacao, key=lambda ind: ind.get_fiteness())
        return best_solution.get_cromossomo(), 1 / best_solution.get_fiteness()
