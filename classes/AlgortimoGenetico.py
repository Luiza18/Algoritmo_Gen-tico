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

    def __avalia_fitness(self):
        for individuo in self.__populacao:
            individuo.calcula_fitness(self.__tsp)

    def __selecao(self):
        total_fitness = sum(individuo.get_fitness for individuo in self.__populacao)  # Calcula fitness de todos os individuos
        ponto_escolhido = rd.uniform(0, total_fitness)  # Seleciona um ponto aleatório dentro do intervalo
        fitness_atual = 0
        for individuo in self.__populacao: 
            fitness_atual += individuo.get_fitness
            if fitness_atual > ponto_escolhido:
                return cp.deepcopy(individuo)

    def __crossover(self, pai1: Individuo, pai2: Individuo):
        ponto_corte = rd.randint(1, self.__numero_cidades - 1)
        filho1, filho2 = np.zeros(self.__numero_cidades, dtype=int), np.zeros(self.__numero_cidades, dtype=int)

        # Cópia inicial até o ponto de corte
        filho1[:ponto_corte], filho2[:ponto_corte] = pai1.get_cromossomo[:ponto_corte], pai2.get_cromossomo[:ponto_corte]

        # Preencher o restante do cromossomo
        filho1 = self.__preencher_filho(filho1, pai2, ponto_corte)
        filho2 = self.__preencher_filho(filho2, pai1, ponto_corte)

        return Individuo(self.__numero_cidades), Individuo(self.__numero_cidades)

    def __preencher_filho(self, filho, pai: Individuo, pos):
        if pos >= self.__numero_cidades:  # Se o cromossomo estiver completo, retorna o filho
            return filho

        # Adiciona o próximo gene que não esteja presente no cromossomo do filho
        for gene in pai.get_cromossomo:
            if gene not in filho:
                filho[pos] = gene
                return self.__preencher_filho(filho, pai, pos + 1)

    def __mutacao(self, individuo: Individuo):
        # Mutação: troca dois genes aleatórios no cromossomo
        if rd.random() < self.__taxa_mutacao:
            idx1, idx2 = rd.sample(range(self.__numero_cidades), 2)
            individuo.get_cromossomo[idx1], individuo.get_cromossomo[idx2] = individuo.get_cromossomo[idx2], individuo.get_cromossomo[idx1]

    def __evolucao(self):
        # Ordena a população com base no fitness
        self.__populacao.sort(key=lambda individuo: individuo.get_fitness, reverse=True)

        # Mantém a elite
        qtd_elite = int(self.__tamanho_populacao * self.__elite)
        nova_populacao = self.__populacao[:qtd_elite]

        # Gera nova população por cruzamento e mutação
        while len(nova_populacao) < self.__tamanho_populacao:
            pai1 = self.__selecao()
            pai2 = self.__selecao()
            if rd.random() < self.__taxa_cruzamento:
                filho1, filho2 = self.__crossover(pai1, pai2)
                self.__mutacao(filho1)
                self.__mutacao(filho2)
                nova_populacao.extend([filho1, filho2])
            else:
                self.__mutacao(pai1)
                self.__mutacao(pai2)
                nova_populacao.extend([pai1, pai2])

        self.__populacao = nova_populacao[:self.__tamanho_populacao]

    def run(self):
        # Executa o algoritmo genético
        self.__avalia_fitness()

        for geracao in range(self.__geracoes):
            self.__evolucao()
            self.__avalia_fitness()
            melhor_individuo = max(self.__populacao, key=lambda ind: ind.get_fitness)
            if geracao == 1:
                melhor_individuo_inicial = 1 / melhor_individuo.get_fitness
            #print(f"Geração {geracao}: Melhor distância = {1 / melhor_individuo.get_fitness}")

       
        melhor_solucao = max(self.__populacao, key=lambda ind: ind.get_fitness)
        melhor_individuo_final = 1 / melhor_solucao.get_fitness
        ganho = 100 * ((melhor_individuo_inicial - melhor_individuo_final) / melhor_individuo_inicial)
        return melhor_solucao.get_cromossomo, melhor_individuo_final, melhor_individuo_inicial, ganho