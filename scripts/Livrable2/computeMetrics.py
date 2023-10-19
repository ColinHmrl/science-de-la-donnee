import numpy as np


# Calcule de nos métriques
def compute(autoencoder, datasets):
    accuracy = {}
    loss = {}

    for set_name in datasets:
        loss[set_name], accuracy[set_name] = autoencoder.evaluate(datasets[set_name])

    accuracy['overall'] = np.mean(list(accuracy.values()))
    loss['overall'] = np.mean(list(loss.values()))

    return accuracy, loss