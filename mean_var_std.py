import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        le = int(np.sqrt(len(list)))
        arr = np.array(list)
        arr = arr.reshape(le, le)
        calculation = {
            'mean': [[0, 0, 0], [0, 0, 0], 0],
            'variance': [[0, 0, 0], [0, 0, 0], 0],
            'standard deviation': [[0, 0, 0], [0, 0, 0], 0],
            'max': [[0, 0, 0], [0, 0, 0], 0],
            'min': [[0, 0, 0], [0, 0, 0], 0],
            'sum': [[0, 0, 0], [0, 0, 0], 0]
        }
        for i in range(le):
            calculation['mean'][0][i] = np.mean(arr[:, i])
            calculation['variance'][0][i] = np.var(arr[:, i])
            calculation['standard deviation'][0][i] = np.std(arr[:, i])
            calculation['max'][0][i] = np.max(arr[:, i])
            calculation['min'][0][i] = np.min(arr[:, i])
            calculation['sum'][0][i] = np.sum(arr[:, i])
        for i in range(le):
            calculation['mean'][1][i] = np.mean(arr[i, :])
            calculation['variance'][1][i] = np.var(arr[i, :])
            calculation['standard deviation'][1][i] = np.std(arr[i, :])
            calculation['max'][1][i] = np.max(arr[i, :])
            calculation['min'][1][i] = np.min(arr[i, :])
            calculation['sum'][1][i] = np.sum(arr[i, :])
        calculation['mean'][2] = np.mean(list)
        calculation['variance'][2] = np.var(list)
        calculation['standard deviation'][2] = np.std(list)
        calculation['max'][2] = np.max(list)
        calculation['min'][2] = np.min(list)
        calculation['sum'][2] = np.sum(list)
        return calculation