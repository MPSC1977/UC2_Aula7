import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['estelionato', 'mes_ano']]
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head(12))
    print('\nDados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()    

try:
    df_estelionato_mes_ano = df_estelionato.groupby(['mes_ano']).sum().reset_index()
    print(df_estelionato_mes_ano)
    array_estelionato = np.array(df_estelionato_mes_ano['estelionato'])
    
    print('\nCalculando informações sobre padrão de estelionatos...')
    media_estelionato = (np.mean(array_estelionato))
    mediana_estelionato = (np.median(array_estelionato))
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100
    q1 = np.quantile(array_estelionato, 0.25)
    q2 = np.quantile(array_estelionato, 0.50)
    q3 = np.quantile(array_estelionato, 0.75)

    df_mes_ano_acima_q3 = df_estelionato_mes_ano[df_estelionato_mes_ano['estelionato'] > q3]
    df_mes_ano_abaixo_q1 = df_estelionato_mes_ano[df_estelionato_mes_ano['estelionato'] < q1]

    print('\nMEDIDAS DE TENDÊNCIA CENTRAL:')
    print(30*'-')
    print(f'\nA média de estelionatos registrados é de {media_estelionato:.2f}')
    print(f'\nA médiana de estelionatos registrados é de {mediana_estelionato:.2f}')
    print(f'\nÍndice de verificação de tendência central: {distancia_media_mediana:.2f}%')
    
    print('\nMEDIDAS DE POSIÇÃO:')
    print(30*'-')
    print('\nQ1 (25%): ', q1)
    print('\nQ2 (50%): ', q2)
    print('\nQ3 (75%): ', q3)

    print('\nMÊS/ANO COM MAIOR INCIDÊNCIA DE ESTELIONATOS:')
    print(50*'-')
    print(df_mes_ano_acima_q3.sort_values(by='estelionato', ascending=False))

    print('\nMÊS/ANO COM MENOR INCIDÊNCIA DE ESTELIONATOS:')
    print(50*'-')
    print(df_mes_ano_abaixo_q1.sort_values(by='estelionato'))

    print('\nCONCLUSÃO:')
    print('\nAnalisando os dados apresentados, com base nos cálculos estatísticos, verifica-se tendência assimétrica, tendo em vista o padrão heterogêneo do número de ocorrências desse tipo de crime ao longo do tempo.')

except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()