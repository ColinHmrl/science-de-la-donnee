import tensorflow as tf
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, Dropout, add
import matplotlib.pyplot as plt

def plot_images_with_highlight(predictions, test_set, output_folder_classification, label_value=1):
    # Convertir le test_set en un itérable pour accéder aux images
    test_iterator = iter(test_set)

    # Liste des noms originales des images qui ont une prédiction de 1
    photos = []
    not_photos = []
    # Préparer la mise en page pour l'affichage
    num_images = len(predictions)
    num_rows = int(num_images**0.5)
    num_cols = (num_images + num_rows - 1) // num_rows

    # Créer un subplot pour afficher toutes les images
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(32, 32))

    # Parcourir les prédictions et les images correspondantes
    for prediction, images, ax in zip(predictions, test_iterator, axes.ravel()):
        binary_prediction = 1 if prediction >= 0.5 else 0
    
        # Sélectionner l'image du batch (index 0) et déplier les dimensions
        image = tf.squeeze(images[0], axis=0).numpy().astype("uint8")

        # Récupérer le nom de fichier correspondant à cette image
        filename = test_set.filenames[test_iterator.batch_index - 1]

        # Afficher l'image
        ax.imshow(image)
        if(binary_prediction == 1):
            ax.set_title(prediction[0], color='green')
            photos.append(filename)
        else:
            ax.set_title(prediction[0], color='red')
            not_photos.append(filename)
        ax.axis('off')

    # Supprimer les sous-plots non utilisés
    for i in range(num_images, num_rows * num_cols):
        fig.delaxes(axes.ravel()[i])

    plt.savefig(output_folder_classification+'/classification_results.png', bbox_inches='tight', pad_inches=0)
    plt.show()

    return photos, not_photos