import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_csv('database.csv', sep=';' , engine= 'python')
grouped = data[['casosNovos','obitosNovos']].groupby(data['estado'])

quantitativos = grouped.sum()/2

def plotar(tipo):
   if(tipo == 'Casos'):
       cor = 'y'
       df = quantitativos.sort_values(by=['casosNovos'])
       analiseTipo = list(df['casosNovos'])    
       estado = list(df.index)
   else:
       cor = 'r'
       df = quantitativos.sort_values(by=['obitosNovos'])
       analiseTipo = list(df['obitosNovos'])
       estado = list(df.index)
                    
   fig = plt.figure(figsize=(12, 6))
   ax = fig.add_subplot(111)
   grupos = len(estado)
   indice = np.arange(grupos)
   bar_larg = 0.6
   ax.bar(indice, analiseTipo, bar_larg, color=cor, label=tipo)

   plt.rcParams['xtick.labelsize'] = 15
   plt.rcParams['ytick.labelsize'] = 15
   plt.xlabel(tipo) 
   plt.ylabel('Quantidades de '+str(tipo)) 
   plt.title(str(tipo)+' por estado') 
   plt.xticks(indice , estado)
   plt.legend() 
   plt.tight_layout() 
   plt.savefig(tipo+'.png', format='png')


plotar('Casos')
plotar('Obitos')