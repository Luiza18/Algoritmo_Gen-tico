import PySimpleGUI as sg
from classes.AlgortimoGenetico import AlgoritmoGenetico
from classes.TSP import TSP

TAMANHO_POPULACAO =  20
NUMERO_GERACOES =  50
TAXA_CRUZAMENTO =  0.8
TAXA_MUTACAO =  0.1
IG =  0.2

class Interface:
    def __init__(self):
        self.layout = [
            [sg.Text('Número de Cidades:'), sg.InputText(key='num_cidades')],
            [sg.Text('Distância Mínima:'), sg.InputText(key='min_dist')],
            [sg.Text('Distância Máxima:'), sg.InputText(key='max_dist')],
            [sg.Button('Executar')]
            #[sg.Text('', key='output')]
        ]
        self.window = sg.Window('Algoritmo Genético para TSP', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Executar':
                
                num_cidades = int(values['num_cidades'])
                min_dist = int(values['min_dist'])
                max_dist = int(values['max_dist'])
               
                # Cria a instância do problema TSP e do algoritmo genético
                tsp = TSP(min_dist, max_dist, num_cidades)
                algoritmo_genetico = AlgoritmoGenetico(num_cidades, TAMANHO_POPULACAO, TAXA_CRUZAMENTO, TAXA_MUTACAO, NUMERO_GERACOES, IG, tsp)

                # Executa o algoritmo
                melhor_caminho, melhor_distancia, distancia_inicial, ganho = algoritmo_genetico.run()
                sg.popup(
                    f'Melhor distância inicial: {distancia_inicial:.2f}\n'
                    f'Melhor solução: {melhor_caminho}\n'
                    f'Melhor distância final: {melhor_distancia:.2f}\n'
                    f'Ganho: {ganho:.2f}%'
                    )

        self.window.close()
