import numpy as np
from classes.TSP import TSP


class Individuo:
    def __init__(self, numero_cidades):
        self.__numero_cidades = numero_cidades
        self.__cromossomo = self.__gerar_cromossomo()
        self.__fitness = 0

    @property
    def get_cromossomo(self):
        return self.__cromossomo

    @property
    def get_fitness(self):
        return self.__fitness

    def __gerar_cromossomo(self): #permutação das cidades
        chromosome = np.arange(self.__numero_cidades)
        np.random.shuffle(chromosome)
        return chromosome

    def calcula_fitness(self, tsp_problem : TSP):
        self.__fitness = 1 / tsp_problem.calcular_distancia(self.__cromossomo)