import matplotlib.pyplot as plt

plt.figure(figsize=(14, 14))
def plotImages(data_set, class_names):
    for images, labels in data_set.take(1):
        for i in range(14):
            ax = plt.subplot(6, 7, i + 1)
            plt.imshow(images[i] / 255.0)
            plt.title(class_names[labels[i]])
            plt.axis("off")