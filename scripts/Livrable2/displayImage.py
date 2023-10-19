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

def display_images_single_row(*images):
    """Display images on a single row."""
    plt.figure(figsize=(50, 50))
    for index, image in enumerate(images):
        plt.subplot(1, len(images), index+1)
        plt.imshow(image)
        plt.axis('off')
    plt.show()