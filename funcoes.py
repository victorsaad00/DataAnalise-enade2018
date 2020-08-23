import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dicionarios as dic
import funcoes as func
import seaborn as sns

# Essa funcao faz um grafico no estilo 'pizza'/'pie' com 
# os argumentos que sao passados. Para cada coluna, um grafico.
# A coluna e selecionada a partir da variavel data_index.
def dict_pie_graphic(data, dict, data_index):
        
        graf_data = data.iloc[:,data_index].value_counts().sort_index() # Ler todos os elementos da coluna,
                                                                        # conta quantos elementos cada linha possui e ordena-os

        plt.figure(figsize=(4,4))
        plt.pie(graf_data, labels = dict.keys(),autopct='%1.1f%%')
        plt.legend(graf_data, labels = dict.values(), ncol=1, bbox_to_anchor =(1, 0, 0.5, 1))
        plt.show()

# Funcao que relaciona duas colunas, conta e coloca em ordem
def dataRelation(data, col1, col2, tittle):
        print(tittle)
        return data[[col1, col2]].value_counts().sort_index()

# Funcao que gera grafico de homens e mulheres por quantidade em cada curso.
def grafico_curso_por_MxH(data):
    
        curs_rows = data.CO_GRUPO.unique() # Cria uma lista com todos os rows ( codigos dos grupos ) 
        FM_data_cur =  data[['TP_SEXO','CO_GRUPO']].value_counts().sort_index().to_numpy() # cria uma lista com a quantidade de mulheres e homens por curso. [0:]

        x_index = np.arange(len(curs_rows)) 
        bar_width = 0.4 # Esteticamente falando, essa variavel foi criada p/ separar as barras dos homens e das mulheres.
        
        F = FM_data_cur[0:len(curs_rows)] # Quantidade de mulheres por curso
        H = FM_data_cur[len(curs_rows):]  # Quantidade de homens por curso


        # Plots do grafico
        plt.bar(x_index + bar_width, F,width = bar_width,  label = "Mulheres")
        plt.bar(x_index, H,width = bar_width,  label = 'Homens')
        
        plt.xlabel('Codigo do curso')
        plt.ylabel('Quantidade de pessoas')
        
        plt.legend()
       
        