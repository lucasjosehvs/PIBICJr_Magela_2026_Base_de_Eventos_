import csv
from collections import Counter
import os
import time

csvEntrada = r''
csvSaida = r''

csvConjunto1_ordenado = os.path.join(csvSaida, 'conjuntoN_ordenado.csv')
csvConjunto2_ordenado = os.path.join(csvSaida, 'conjuntoNA_ordenado.csv')
csvConjunto3_ordenado = os.path.join(csvSaida, 'conjuntoNCA_ordenado.csv')
csvConjunto4_ordenado = os.path.join(csvSaida, 'conjuntoNPA_ordenado.csv')

intervaloFlush = 300000

def main():
    os.makedirs(csvSaida, exist_ok=True)
    inicio = time.time()
    totalLinhas = 0
    totalLinhas1 = 0
    totalLinhas2 = 0
    totalLinhas3 = 0
    totalLinhas4 = 0

    # Criação dos quantificadores
    frequencia_evento = Counter()
    frequencia_evento_ano = Counter()
    frequencia_evento_cidade_ano = Counter()
    frequencia_evento_pais_ano = Counter()

    # Abertura dos arquivos para leitura e escrita
    with open(csvEntrada, newline='', encoding='utf-8', mode='r') as f_entrada, \
        open(csvConjunto1_ordenado, newline='', encoding='utf-8', mode='w') as f1, \
        open(csvConjunto2_ordenado, newline='', encoding='utf-8', mode='w') as f2, \
        open(csvConjunto3_ordenado, newline='', encoding='utf-8', mode='w') as f3, \
        open(csvConjunto4_ordenado, newline='', encoding='utf-8', mode='w') as f4:

        leitor = csv.DictReader(f_entrada, delimiter='|')

        # Contagem de ocorrências
        for linha in leitor:

            totalLinhas += 1  

            nome = linha["NOME-DO-EVENTO"]
            ano = linha["ANO-DO-EVENTO"]
            pais = linha["PAIS-DO-EVENTO"]
            cidade = linha["CIDADE-DO-EVENTO"]
    
            frequencia_evento[nome] += 1
            frequencia_evento_ano[(nome, ano)] += 1
            frequencia_evento_cidade_ano[(nome, cidade, ano)] += 1
            frequencia_evento_pais_ano[(nome, pais, ano)] += 1

        # Ordenação das ocorrências
        eventos_ordenados = sorted(
            frequencia_evento,
            key=frequencia_evento.get,
            reverse=True
        )
        evento_ano_ordenados = sorted(
            frequencia_evento_ano,
            key=frequencia_evento_ano.get,
            reverse=True
        )
        evento_cidade_ano_ordenados = sorted(
            frequencia_evento_cidade_ano,
            key=frequencia_evento_cidade_ano.get,
            reverse=True
        )
        evento_pais_ano_ordenados = sorted(
            frequencia_evento_pais_ano,
            key=frequencia_evento_pais_ano.get,
            reverse=True
        )

        # CSV ordenado por frequência de EVENTO
        escritor = csv.DictWriter(f1, delimiter='|', fieldnames= ['NOME-DO-EVENTO', 'OCORRENCIAS-EVENTO'])
        escritor.writeheader()

        for evento in eventos_ordenados:
            escritor.writerow({
                'NOME-DO-EVENTO': evento,
                'OCORRENCIAS-EVENTO':
                    frequencia_evento[evento]
            })
            totalLinhas1 += 1
            
            if totalLinhas1 % intervaloFlush == 0:
                f1.flush()

        # CSV ordenado por frequência de EVENTO-ANO
        escritor = csv.DictWriter(f2, delimiter='|', fieldnames= ['NOME-DO-EVENTO', 'ANO-DO-EVENTO', 'OCORRENCIAS-EVENTO-ANO'])
        escritor.writeheader()

        for evento, ano in evento_ano_ordenados:
            escritor.writerow({
                'NOME-DO-EVENTO': evento,
                'ANO-DO-EVENTO': ano,
                'OCORRENCIAS-EVENTO-ANO':
                    frequencia_evento_ano[(evento, ano)]
            })
            totalLinhas2 += 1
            
            if totalLinhas2 % intervaloFlush == 0:
                f2.flush()

        # CSV ordenado por frequência de EVENTO-CIDADE-ANO
        escritor = csv.DictWriter(f3, delimiter='|', fieldnames= ['NOME-DO-EVENTO', 'CIDADE-DO-EVENTO', 'ANO-DO-EVENTO', 'OCORRENCIAS-EVENTO-CIDADE-ANO'])
        escritor.writeheader()

        for evento, cidade, ano in evento_cidade_ano_ordenados:
            escritor.writerow({
                'NOME-DO-EVENTO': evento,
                'CIDADE-DO-EVENTO': cidade,
                'ANO-DO-EVENTO': ano,
                'OCORRENCIAS-EVENTO-CIDADE-ANO':
                    frequencia_evento_cidade_ano[(evento, cidade, ano)]
            })
            totalLinhas3 += 1
            
            if totalLinhas3 % intervaloFlush == 0:
                f3.flush()

        # CSV ordenado por frequência de EVENTO-PAIS-ANO
        escritor = csv.DictWriter(f4, delimiter='|', fieldnames= ['NOME-DO-EVENTO', 'PAIS-DO-EVENTO', 'ANO-DO-EVENTO', 'OCORRENCIAS-EVENTO-PAIS-ANO'])
        escritor.writeheader()
        
        for evento, pais, ano in evento_pais_ano_ordenados:
            escritor.writerow({
                'NOME-DO-EVENTO': evento,
                'PAIS-DO-EVENTO': pais,
                'ANO-DO-EVENTO': ano,
                'OCORRENCIAS-EVENTO-PAIS-ANO':
                frequencia_evento_pais_ano[(evento, pais, ano)]
            })
            totalLinhas4 += 1
                    
            if totalLinhas4 % intervaloFlush == 0:
                f4.flush()

    tempo_total = time.time() - inicio
    print(f' Tempo de execução: {tempo_total:.2f} s')
    print(f' Total de linhas lidas: {totalLinhas}')
    print(f' Qntd de linhas conjunto EVENTO: {totalLinhas1}')
    print(f' Qntd de linhas conjunto EVENTO-ANO: {totalLinhas2}')
    print(f' Qntd de linhas conjunto EVENTO-CIDADE-ANO: {totalLinhas3}')
    print(f' Qntd de linhas conjunto EVENTO-PAIS-ANO: {totalLinhas4}')

if __name__ == '__main__':
    main()
