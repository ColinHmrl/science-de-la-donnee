import matplotlib.pyplot as plt


# Affichage de nos métriques sous forme de graphique  
def display(accuracy, loss):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    bars = plt.bar(range(len(accuracy)), list(accuracy.values()), align='center', color=colors, alpha=0.8, width=0.5)
    plt.xticks(range(len(accuracy)), list(accuracy.keys()))

    plt.title('Accuracy for each test set')
    plt.show()

    plt.bar(range(len(loss)), list(loss.values()), align='center', color=colors, alpha=0.8, width=0.5)
    plt.xticks(range(len(loss)), list(loss.keys()))
    plt.title('Loss for each test set')
    plt.show()