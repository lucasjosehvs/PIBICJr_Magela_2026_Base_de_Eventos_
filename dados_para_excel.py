import csv
import time

csvEntrada_N = r''
csvEntrada_NA = r''
csvEntrada_NPA = r''
csvEntrada_NCA = r''

def main():
    inicio = time.time()

    # Criação dos quantificadores
    frequencia_1 = 0
    frequencia_2 = 0
    frequencia_3 = 0
    frequencia_4 = 0
    frequencia_5 = 0
    frequencia_6a10 = 0
    frequencia_11a50 = 0
    frequencia_51a100 = 0
    frequencia_101a500 = 0
    frequencia_501a1000 = 0
    frequencia_1001a5000 = 0
    frequencia_5001a10000 = 0
    frequencia_10001a50000 = 0
    frequencia_50001a100000 = 0
    frequencia_mais100000 = 0

    # Abertura do arquivo de NOME|OCORRENCIAS para leitura e contagem
    with open(csvEntrada_N, newline='', encoding='utf-8', mode='r') as f1:
    
        leitor = csv.reader(f1, delimiter='|')

        cabecalho = next(leitor)
        indice = cabecalho.index("OCORRENCIAS-EVENTO")

        # Contagem de ocorrências
        for linha in leitor:

            ocorrencias = int(linha[indice])

            if ocorrencias == 1:
                frequencia_1 += 1
            elif ocorrencias == 2:
                frequencia_2 += 1
            elif ocorrencias == 3:
                frequencia_3 += 1
            elif ocorrencias == 4:
                frequencia_4 += 1
            elif ocorrencias == 5:
                frequencia_5 += 1
            elif ocorrencias <= 10:
                frequencia_6a10 += 1
            elif ocorrencias <= 50:
                frequencia_11a50 += 1
            elif ocorrencias <= 100:
                frequencia_51a100 += 1
            elif ocorrencias <= 500:
                frequencia_101a500 += 1
            elif ocorrencias <= 1000:
                frequencia_501a1000 += 1
            elif ocorrencias <= 5000:
                frequencia_1001a5000 += 1
            elif ocorrencias <= 10000:
                frequencia_5001a10000 += 1
            elif ocorrencias <= 50000:
                frequencia_10001a50000 += 1
            elif ocorrencias <= 100000:
                frequencia_50001a100000 += 1
            else:
                frequencia_mais100000 += 1

       # Relatório da contagem
        tempo_ex = time.time() - inicio
        print(f'\n========== NOME ==========\n')
        print(f' Tempo de execução 1: {tempo_ex:.2f} s\n OCORRÊNCIAS:')
        print(f'-> 1: {frequencia_1}')
        print(f'-> 2: {frequencia_2}')
        print(f'-> 3: {frequencia_3}')
        print(f'-> 4: {frequencia_4}')
        print(f'-> 5: {frequencia_5}')
        print(f'-> 6 a 10: {frequencia_6a10}')
        print(f'-> 11 a 50: {frequencia_11a50}')
        print(f'-> 51 a 100: {frequencia_51a100}')
        print(f'-> 101 a 500: {frequencia_101a500}')
        print(f'-> 501 a 1.000: {frequencia_501a1000}')
        print(f'-> 1.001 a 5.000: {frequencia_1001a5000}')
        print(f'-> 5.001 a 10.000: {frequencia_5001a10000}')
        print(f'-> 10.001 a 50.000: {frequencia_10001a50000}')
        print(f'-> 50.001 a 100.000: {frequencia_50001a100000}')
        print(f'-> Mais que 100.000: {frequencia_mais100000}')

    inicio = time.time()

    # Variáveis zeradas para nova contagem
    frequencia_1 = 0
    frequencia_2 = 0
    frequencia_3 = 0
    frequencia_4 = 0
    frequencia_5 = 0
    frequencia_6a10 = 0
    frequencia_11a50 = 0
    frequencia_51a100 = 0
    frequencia_101a500 = 0
    frequencia_501a1000 = 0
    frequencia_1001a5000 = 0
    frequencia_5001a10000 = 0
    frequencia_10001a50000 = 0

    # Abertura do arquivo de NOME|ANO|OCORRENCIAS para leitura e contagem
    with open(csvEntrada_NA, newline='', encoding='utf-8', mode='r') as f2:
    
            leitor = csv.reader(f2, delimiter='|')
    
            cabecalho = next(leitor)
            indice = cabecalho.index("OCORRENCIAS-EVENTO-ANO")
    
            # Contagem de ocorrências
            for linha in leitor:
    
                ocorrencias = int(linha[indice])
    
                if ocorrencias == 1:
                    frequencia_1 += 1
                elif ocorrencias == 2:
                    frequencia_2 += 1
                elif ocorrencias == 3:
                    frequencia_3 += 1
                elif ocorrencias == 4:
                    frequencia_4 += 1
                elif ocorrencias == 5:
                    frequencia_5 += 1
                elif ocorrencias <= 10:
                    frequencia_6a10 += 1
                elif ocorrencias <= 50:
                    frequencia_11a50 += 1
                elif ocorrencias <= 100:
                    frequencia_51a100 += 1
                elif ocorrencias <= 500:
                    frequencia_101a500 += 1
                elif ocorrencias <= 1000:
                    frequencia_501a1000 += 1
                elif ocorrencias <= 5000:
                    frequencia_1001a5000 += 1
                elif ocorrencias <= 10000:
                    frequencia_5001a10000 += 1
                else:
                    frequencia_10001a50000 += 1
           
            tempo_ex = time.time() - inicio
            print(f'\n========== NOME | ANO ==========\n')
            print(f' Tempo de execução 1: {tempo_ex:.2f} s\n OCORRÊNCIAS:')
            print(f'-> 1: {frequencia_1}')
            print(f'-> 2: {frequencia_2}')
            print(f'-> 3: {frequencia_3}')
            print(f'-> 4: {frequencia_4}')
            print(f'-> 5: {frequencia_5}')
            print(f'-> 6 a 10: {frequencia_6a10}')
            print(f'-> 11 a 50: {frequencia_11a50}')
            print(f'-> 51 a 100: {frequencia_51a100}')
            print(f'-> 101 a 500: {frequencia_101a500}')
            print(f'-> 501 a 1.000: {frequencia_501a1000}')
            print(f'-> 1.001 a 5.000: {frequencia_1001a5000}')
            print(f'-> 5.001 a 10.000: {frequencia_5001a10000}')
            print(f'-> 10.001 a 50.000: {frequencia_10001a50000}')

    inicio = time.time()

    # Variáveis zeradas para nova contagem
    frequencia_1 = 0
    frequencia_2 = 0
    frequencia_3 = 0
    frequencia_4 = 0
    frequencia_5 = 0
    frequencia_6a10 = 0
    frequencia_11a50 = 0
    frequencia_51a100 = 0
    frequencia_101a500 = 0
    frequencia_501a1000 = 0
    frequencia_1001a5000 = 0
    frequencia_5001a10000 = 0
    frequencia_10001a50000 = 0

    # Abertura do arquivo de NOME|PAIS|ANO|OCORRENCIAS para leitura e contagem
    with open(csvEntrada_NPA, newline='', encoding='utf-8', mode='r') as f3:
    
            leitor = csv.reader(f3, delimiter='|')
    
            cabecalho = next(leitor)
            indice = cabecalho.index("OCORRENCIAS-EVENTO-PAIS-ANO")
    
            # Contagem de ocorrências
            for linha in leitor:
    
                ocorrencias = int(linha[indice])
    
                if ocorrencias == 1:
                    frequencia_1 += 1
                elif ocorrencias == 2:
                    frequencia_2 += 1
                elif ocorrencias == 3:
                    frequencia_3 += 1
                elif ocorrencias == 4:
                    frequencia_4 += 1
                elif ocorrencias == 5:
                    frequencia_5 += 1
                elif ocorrencias <= 10:
                    frequencia_6a10 += 1
                elif ocorrencias <= 50:
                    frequencia_11a50 += 1
                elif ocorrencias <= 100:
                    frequencia_51a100 += 1
                elif ocorrencias <= 500:
                    frequencia_101a500 += 1
                elif ocorrencias <= 1000:
                    frequencia_501a1000 += 1
                elif ocorrencias <= 5000:
                    frequencia_1001a5000 += 1
                elif ocorrencias <= 10000:
                    frequencia_5001a10000 += 1
                else:
                    frequencia_10001a50000 += 1
           
            tempo_ex = time.time() - inicio
            print(f'\n========== NOME | PAIS | ANO ==========\n')
            print(f' Tempo de execução 1: {tempo_ex:.2f} s\n OCORRÊNCIAS:')
            print(f'-> 1: {frequencia_1}')
            print(f'-> 2: {frequencia_2}')
            print(f'-> 3: {frequencia_3}')
            print(f'-> 4: {frequencia_4}')
            print(f'-> 5: {frequencia_5}')
            print(f'-> 6 a 10: {frequencia_6a10}')
            print(f'-> 11 a 50: {frequencia_11a50}')
            print(f'-> 51 a 100: {frequencia_51a100}')
            print(f'-> 101 a 500: {frequencia_101a500}')
            print(f'-> 501 a 1.000: {frequencia_501a1000}')
            print(f'-> 1.001 a 5.000: {frequencia_1001a5000}')
            print(f'-> 5.001 a 10.000: {frequencia_5001a10000}')
            print(f'-> 10.001 a 50.000: {frequencia_10001a50000}')

    inicio = time.time()

    # Variáveis zeradas para nova contagem
    frequencia_1 = 0
    frequencia_2 = 0
    frequencia_3 = 0
    frequencia_4 = 0
    frequencia_5 = 0
    frequencia_6a10 = 0
    frequencia_11a50 = 0
    frequencia_51a100 = 0
    frequencia_101a500 = 0
    frequencia_501a1000 = 0
    frequencia_1001a5000 = 0
    frequencia_5001a10000 = 0
    frequencia_10001a50000 = 0

    # Abertura do arquivo de NOME|CIDADE|ANO|OCORRENCIAS para leitura e contagem
    with open(csvEntrada_NCA, newline='', encoding='utf-8', mode='r') as f4:
    
            leitor = csv.reader(f4, delimiter='|')
    
            cabecalho = next(leitor)
            indice = cabecalho.index("OCORRENCIAS-EVENTO-CIDADE-ANO")
    
            # Contagem de ocorrências
            for linha in leitor:
    
                ocorrencias = int(linha[indice])
    
                if ocorrencias == 1:
                    frequencia_1 += 1
                elif ocorrencias == 2:
                    frequencia_2 += 1
                elif ocorrencias == 3:
                    frequencia_3 += 1
                elif ocorrencias == 4:
                    frequencia_4 += 1
                elif ocorrencias == 5:
                    frequencia_5 += 1
                elif ocorrencias <= 10:
                    frequencia_6a10 += 1
                elif ocorrencias <= 50:
                    frequencia_11a50 += 1
                elif ocorrencias <= 100:
                    frequencia_51a100 += 1
                elif ocorrencias <= 500:
                    frequencia_101a500 += 1
                elif ocorrencias <= 1000:
                    frequencia_501a1000 += 1
                elif ocorrencias <= 5000:
                    frequencia_1001a5000 += 1
                elif ocorrencias <= 10000:
                    frequencia_5001a10000 += 1
                else:
                    frequencia_10001a50000 += 1
           
            tempo_ex = time.time() - inicio
            print(f'\n========== NOME | CIDADE | ANO ==========\n')
            print(f' Tempo de execução 1: {tempo_ex:.2f} s\n OCORRÊNCIAS:')
            print(f'-> 1: {frequencia_1}')
            print(f'-> 2: {frequencia_2}')
            print(f'-> 3: {frequencia_3}')
            print(f'-> 4: {frequencia_4}')
            print(f'-> 5: {frequencia_5}')
            print(f'-> 6 a 10: {frequencia_6a10}')
            print(f'-> 11 a 50: {frequencia_11a50}')
            print(f'-> 51 a 100: {frequencia_51a100}')
            print(f'-> 101 a 500: {frequencia_101a500}')
            print(f'-> 501 a 1.000: {frequencia_501a1000}')
            print(f'-> 1.001 a 5.000: {frequencia_1001a5000}')
            print(f'-> 5.001 a 10.000: {frequencia_5001a10000}')
            print(f'-> 10.001 a 50.000: {frequencia_10001a50000}')
        
if __name__ == '__main__':
    main()
