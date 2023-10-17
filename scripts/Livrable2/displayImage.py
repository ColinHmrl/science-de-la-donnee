import matplotlib.pyplot as plt

def display_images(X, n):
    plt.figure(figsize=(7, 7))
    # print(X.shape)
    for i in range(n):
        # print(X[i].shape)
        ax = plt.subplot(1, n, i + 1)
        plt.imshow(X[i])
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()