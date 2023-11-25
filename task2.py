import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def check_normality(data, column):

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.boxplot(np.log1p(data))
    plt.title(f'Логарифмическая шкала для {column}')

    plt.subplot(1, 2, 2)
    plt.hist(np.log1p(data), bins=19)
    plt.title(f'Гистограмма для {column}')

    plt.show()

def check_ejections(data,column):
    z_scores = (data - np.mean(data)) / np.std(data)

    ejection = data[np.abs(z_scores) > 10]

    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=19)
    plt.scatter(ejection, np.zeros_like(ejection), label='Выбросы')
    plt.title(f'Гистограмма выбросов для {column}')
    plt.legend()
    plt.show()

def replace_ejections(data):
    q_low = data["Rooms"].quantile(0.01)
    q_high = data["Rooms"].quantile(0.99)
    data["Rooms"] = np.where(data["Rooms"] < q_low, q_low, data["Rooms"])
    data["Rooms"] = np.where(data["Rooms"] > q_high, q_high, data["Rooms"])


dataFrame = pd.read_csv("test.csv")
dataSet = dataFrame.sample(n = 1000)

for column in dataSet.columns:
    try:
        check_normality(dataSet[column], column)
    except TypeError:
        print('Значения в столбце имеют тип string')
    else:
        print(f'Количество нулевых значений в столбце {column}: {dataSet[column].isnull().sum()}')
        check_ejections(dataSet[column], column)

dataSet["Id"] = dataSet["Id"].fillna(dataSet["Id"].median())
dataSet["Rooms"] = dataSet["Rooms"].fillna(dataSet["Rooms"].median())
replace_ejections(dataSet)

roomCounter = dataSet['Rooms'].value_counts()
print('Количество квартир по количеству комнат')
print(roomCounter)

pivotTable = pd.pivot_table(dataSet, values='Id', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)
print(pivotTable)

dataSet.to_csv('surname.csv')