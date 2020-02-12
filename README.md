# IsolationForestSklearn
Análisis de anomalías de tráfico utilizando la librería IsolationForest de Sklearn.

Se utilizan los mismos set de datos utilizados con un modelo supervisado https://github.com/damianra/MetodoSupervisadoSklearn

Se entreno el modelo con datos "normales" provenientes del trafico de red, luego se lo volvió a entrenar con datos de trafico alterado por el malware, con el modelo de IsolationForest (https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html) que nos permite detectar anomalías en los datos logramos que se ajuste al comportamiento que deseamos detectar, etiquetando los datos con 1 para normal y -1 para las anomalías.
