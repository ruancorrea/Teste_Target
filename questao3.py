"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""


import json
import numpy as np

def lendo_arquivo_json (path):
    with open(path, encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
  
    return dados



def analise(dados):
    min = np.inf
    minAcimaZero = np.inf
    max = -1
    valores = []
    valoresAcimaZero = []
    for d in dados:
    #print(d['valor']) 
        valores.append(d['valor'])
        if d['valor'] < min:
            min = d['valor']

        if d['valor'] > 0:
            valoresAcimaZero.append(d['valor'])
            if d['valor'] < minAcimaZero:
                minAcimaZero = d['valor']
    
        if d['valor'] > max:
            max = d['valor']

    media = np.mean(valores)
    mediaAcimaZero = np.mean(valoresAcimaZero)

    qtdDias = 0
    for v in valores:
        if v > media:
            qtdDias += 1

    qtdDiasAcimaZero = 0
    for v in valoresAcimaZero:
        if v > mediaAcimaZero:
            qtdDiasAcimaZero += 1

    #print(f"valor minimo: {min}")
    print(f"- Valor mínimo considerando apenas dias com faturamento: $ {minAcimaZero}")
    print(f"- Valor máximo: $ {max}")
    #print(f"Tiveram {qtdDias} no mês que foram superiores à média mensal {media}")
    print(f"- Tiveram {qtdDiasAcimaZero} no mês que foram superiores à média mensal $ {mediaAcimaZero}, considerando só dias que houve faturamento")


path = "dados.json"
dados = lendo_arquivo_json(path)
print("Análise com o arquivo JSON:")
analise(dados)
