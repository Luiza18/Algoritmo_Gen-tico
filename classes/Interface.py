import PySimpleGUI as sg
from classes.AlgortimoGenetico import AlgoritmoGenetico
from classes.TSP import TSP

TAMANHO_POPULACAO = 20
NUMERO_GERACOES = 50
TAXA_CRUZAMENTO = 0.8
TAXA_MUTACAO = 0.1
IG = 0.2

class Interface:
    def __init__(self):
        self.layout = [
            [sg.Text('Número de Cidades:'), sg.InputText(key='num_cidades', size=(7,7))],
            [sg.Text('Distância Mínima:'), sg.InputText(key='min_dist', size=(7,7))],
            [sg.Text('Distância Máxima:'), sg.InputText(key='max_dist', size=(7,7))],
            [sg.Button('Executar')],
            [sg.Multiline(size=(40, 10), font=('Courier New', 12), disabled=True, no_scrollbar=True, key='-RESULTADO-')]
        ]
        self.window = sg.Window('Algoritmo Genético para TSP', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Executar':
                try:
                    num_cidades = int(values['num_cidades'])
                    min_dist = int(values['min_dist'])
                    max_dist = int(values['max_dist'])

                    if min_dist > max_dist:
                        sg.popup_error('Distância mínima é maior que a distância máxima, por favor corrija!')
                        continue

                    # Cria a instância do problema TSP e do algoritmo genético
                    tsp = TSP(min_dist, max_dist, num_cidades)
                    algoritmo_genetico = AlgoritmoGenetico(num_cidades, TAMANHO_POPULACAO, TAXA_CRUZAMENTO, TAXA_MUTACAO, NUMERO_GERACOES, IG, tsp)

                    # Executa o algoritmo
                    melhor_caminho, melhor_distancia, distancia_inicial, ganho = algoritmo_genetico.run()
                    
                    resultado = (
                        f'Melhor distância inicial: {distancia_inicial:.2f}\n\n'
                        f'Melhor caminho:{melhor_caminho}\n\n'
                        f'Melhor distância final: {melhor_distancia:.2f}\n\n'
                        f'Ganho: {ganho:.2f}%'
                    )
                    self.window['-RESULTADO-'].update(resultado)

                except ValueError:
                    sg.popup_error('Por favor, digite um número válido')
                    self.window['min_dist'].update('')
                    self.window['max_dist'].update('')
                    self.window['num_cidades'].update('')

        self.window.close()
