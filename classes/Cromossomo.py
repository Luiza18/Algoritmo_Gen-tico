from numpy import arange, random
from classes.TSP import TSP

#Rever se é possível puxar o numero de cidades na classe TSP

class Cromossomo():
    def __init__(self, min_dist, max_dist,numero_cidades:int):
        self.__numero_cidades = numero_cidades
        self.__comossomo = self.__gerar_cromossomo()
        self.__aptidao = 0
        self.__tsp = TSP(min_dist, max_dist,self.__numero_cidades)


    # Gera uma solução (um caminho)
    def __gerar_cromossomo(self):
        cromossomo = arange(self.__numero_cidades)
        random.shuffle(cromossomo)
        return cromossomo

    #Avalia solução (menor distância, melhor aptidão)
    def calcula_aptidao(self):
        self.__aptidao = 1 / self.__tsp.calcular_distancia(self.__comossomo)
        