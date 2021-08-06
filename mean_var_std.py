import numpy as np


def calculate(lis):
    try:
        arr = np.array(lis).reshape(3, 3)
        calculations = {
            "mean": [[], [], []],
            "variance": [[], [], []],
            "standard deviation": [[], [], []],
            "max": [[], [], []],
            "min": [[], [], []],
            "sum": [[], [], []],
        }

        calculations["mean"][0] = list(map(float, arr.sum(axis=0) / 3))
        calculations["mean"][1] = list(map(float, arr.sum(axis=1) / 3))
        calculations["mean"][2] = float(arr.sum() / 9)
        calculations["variance"][0] = list(map(float, np.var(arr, axis=0)))
        calculations["variance"][1] = list(map(float, np.var(arr, axis=1)))
        calculations["variance"][2] = float(np.var(arr))
        calculations["standard deviation"][0] = list(
            map(float, np.std(arr, axis=0)))
        calculations["standard deviation"][1] = list(
            map(float, np.std(arr, axis=1)))
        calculations["standard deviation"][2] = float(np.std(arr))
        calculations["max"][0] = list(map(int, np.max(arr, axis=0)))
        calculations["max"][1] = list(map(int, np.max(arr, axis=1)))
        calculations["max"][2] = np.max(arr)
        calculations["min"][0] = list(map(int, np.min(arr, axis=0)))
        calculations["min"][1] = list(map(int, np.min(arr, axis=1)))
        calculations["min"][2] = np.min(arr)
        calculations["sum"][0] = list(map(int, arr.sum(axis=0)))
        calculations["sum"][1] = list(map(int, arr.sum(axis=1)))
        calculations["sum"][2] = arr.sum()
        return calculations
    except:
        raise ValueError("List must contain nine numbers.")
