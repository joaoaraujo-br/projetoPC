from datetime import datetime
import matplotlib.pyplot as plt
import os

def read_prices(file_name, product):
    with open(file_name, 'r') as file:
        file_content = file.readlines()

    x = []
    y = []

    #           remove column titles
    for line in file_content[1:]:
        # remove '\n' char from the end and transform into list
        line = line[:-1].split(',')

        y.append(float(line[product]))
        x.append(datetime.strptime(line[0], '%d/%m/%Y'))
    
    return x, y

while True:
    os.system('clear')
    print('Histórico de preços:')
    print('[1] Processador')
    print('[2] Memória')
    print('[3] Placa-mãe')
    print('[4] SSD')
    print('[5] Fonte de alimentação')
    print('[6] Total')
    print('Outra tecla para sair')

    choice = int(input())
    
    if choice < 1 or choice > 6:
        break
    else:
        x, y = read_prices('prices.csv', choice)
        plt.plot(x, y)

        if choice == 1:
            plt.title('Preco Ryzen 5 3400g em funcao do tempo')
        if choice == 2:
            plt.title('Preco RAM DDR4 8GB em funcao do tempo')
        if choice == 3:
            plt.title('Preco Asus 450m em funcao do tempo')
        if choice == 4:
            plt.title('Preco SSD WD 240GB em funcao do tempo')
        if choice == 5:
            plt.title('Preco Fonte EVGA 400w em funcao do tempo')
        if choice == 6:
            plt.title('Preco total em funcao do tempo')
        
        plt.show()