from numpy import random

class TSP():
    def __init__(self, min_dist, max_dist,numero_cidades):
        self.__min_dist = min_dist
        self.__numero_cidades = numero_cidades
        self.__max_dist = max_dist
        self.__ditancia_matrix = self.__gerar_problema()

    @property 
    def get_matrix(self):
        return self.__ditancia_matrix

    def __gerar_problema(self):
        matriz = random.randint(self.__min_dist, self.__max_dist, (self.__numero_cidades, self.__numero_cidades))
        
        # Definir a diagonal (distância de uma cidade para ela mesma) como 0
        for i in range(self.__numero_cidades):
            matriz[i][i] = 0
        return matriz

    def calcular_distancia(self, caminho:list):
        distancia = 0

        for i in range(len(caminho) -1):
            distancia += self.__ditancia_matrix[caminho[i]][caminho[i+1]]

        # Retorna ao ponto de partida
        distancia += self.__ditancia_matrix[caminho[-1]][caminho[0]]
        return distancia