#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:30:06 2020

@author: Damian Ramirez

Analisis de anomalias de trafico utilizando la libreria IsolationForest de Sklearn.
Utilizando las muestras de datos del ejemplo supervisado, se modifico el primer
data set quitando el comportamiento del malware para utilizarlo como trafico normal
"""

# Librerias utilizadas
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler
import mglearn
from sklearn.decomposition import PCA

# Dataset base sin malware es el comportamiento que deseamos enseñar a nuestro modelo
dataframe = pd.read_csv('traficoNoSupervisado.csv', index_col = 'Time')

dataframe['Count'] = np.nan

# Se filtran los datos reagrupando los repetidos y se guarda un conteo de ellos en una nueva fila
df = dataframe.groupby(['Time', 'Src Port', 'Dst Port', 'Source', 'Protocol', 'Length']).size().reset_index(name='counts')
dfc= df.copy()

# Se crea un objeto LabelEncoder() para codificar los datos no numéricos y poder escalarlos para crear relaciones y poder graficarlos.
encoder = LabelEncoder()

dfc['Time'] = encoder.fit_transform(dfc['Time'])
dfc['Src Port'] = encoder.fit_transform(dfc['Src Port'])
dfc['Dst Port'] = encoder.fit_transform(dfc['Dst Port'])
dfc['Source'] = encoder.fit_transform(dfc['Source'])
dfc['Protocol'] = encoder.fit_transform(dfc['Protocol'])

x = dfc


esc = x
escala = MinMaxScaler()
escala.fit(esc)
escalada = escala.transform(esc)
pca=PCA(n_components=2)
pca.fit(escalada)
transformada=pca.transform(escalada)

# grafico de los datos
mglearn.discrete_scatter(transformada[:,0], transformada[:,1])

modelo = IsolationForest(n_estimators=100, max_samples=256, contamination=0.02)

modelo.fit(transformada)

predict = modelo.predict(transformada)

"""
Con un nuevo set de datos se volverá a entrenar el modelo, este dataset contiene comportamiento de malware.
"""
dataframe2 = pd.read_csv('trafico_prueba_2016.csv', index_col = 'Time')

dataframe2['Count'] = np.nan

df2 = dataframe2.groupby(['Time', 'Src Port', 'Dst Port', 'Source', 'Protocol', 'Length']).size().reset_index(name='counts')
dfpredict2 = df2.copy()

dfpredict2['Time'] = encoder.fit_transform(dfpredict2['Time'])
dfpredict2['Src Port'] = encoder.fit_transform(dfpredict2['Src Port'])
dfpredict2['Dst Port'] = encoder.fit_transform(dfpredict2['Dst Port'])
dfpredict2['Source'] = encoder.fit_transform(dfpredict2['Source'])
dfpredict2['Protocol'] = encoder.fit_transform(dfpredict2['Protocol'])


escalada2 = escala.transform(dfpredict2)
pca2=PCA(n_components=2)
pca2.fit(escalada2)
transformada2=pca2.transform(escalada2)

mglearn.discrete_scatter(transformada2[:,0], transformada2[:,1])

# Se vuelve a entrenar el modelo con los nuevos datos con malware
predict2 = modelo.fit(transformada2)
pre = modelo.predict(transformada2)
df2["Type"] = pre
print(df2[-50:])

"""
Tercer dataframe con Malware.
Se vuelve a probar el nuevo modelo con otro dataset, realizando los mismos métodos 
para reagrupar, codificar y transformar los datos e implementarlos en el modelo.
"""

dataframe3 = pd.read_csv('trafico_prueba_2017.csv', index_col = 'Time')

dataframe3['Count'] = np.nan

df3 = dataframe3.groupby(['Time', 'Src Port', 'Dst Port', 'Source', 'Protocol', 'Length']).size().reset_index(name='counts')
dfpredict3 = df3.copy()

dfpredict3['Time'] = encoder.fit_transform(dfpredict3['Time'])
dfpredict3['Src Port'] = encoder.fit_transform(dfpredict3['Src Port'])
dfpredict3['Dst Port'] = encoder.fit_transform(dfpredict3['Dst Port'])
dfpredict3['Source'] = encoder.fit_transform(dfpredict3['Source'])
dfpredict3['Protocol'] = encoder.fit_transform(dfpredict3['Protocol'])

escalada3 = escala.transform(dfpredict3)
pca3=PCA(n_components=2)
pca3.fit(escalada3)
transformada3=pca3.transform(escalada3)

mglearn.discrete_scatter(transformada3[:,0], transformada3[:,1])

prediccion = modelo.predict(transformada3)
df3["Type"] = prediccion
print(df3[-40:])