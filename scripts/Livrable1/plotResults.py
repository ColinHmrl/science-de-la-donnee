import matplotlib.pyplot as plt
import numpy as np

def plot_image(prediction_array, true_label, img, class_names):
  img = img/255.0
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)
  predicted_label = np.argmax(prediction_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(prediction_array),
                                class_names[true_label]),
                                color=color)

def plot_image_binary(prediction_array, true_label, img, class_names):
  img = img/255.0
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)
  if prediction_array[0] > 0.5:
    pourcentage = np.max(prediction_array)
    predicted_label = 1
  else:
    pourcentage = 1 - np.max(prediction_array)
    predicted_label = 0

  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100* pourcentage,
                                class_names[true_label]),
                                color=color)
  
def plot_value_array(predictions_array, true_label, num_classes):
  plt.grid(False)
  plt.xticks(range(num_classes))
  plt.yticks([])
  thisplot = plt.bar(range(num_classes), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


def plot_value_array_binary(predictions_array, true_label, num_classes):
  plt.grid(False)
  plt.xticks(range(num_classes))
  plt.yticks([])
  predictions_array = [1 - predictions_array[0], predictions_array[0]]
  thisplot = plt.bar(range(num_classes), predictions_array, color="red")
  plt.ylim([0, 1])

  if predictions_array[0] > 0.5:
    predicted_label = 1
  else:
    predicted_label = 0

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


def plot_results(binary, predictions, full_tests_labels, full_tests_images, class_names, save_path, index_start=5000, images_displayed=64, num_rows=45, num_cols=5):

  plt.figure(figsize=(2*2*num_cols, 2*num_rows))
  i = 0
  if binary:
    for image_index in range(index_start, index_start+images_displayed):
      plt.subplot(num_rows, 2*num_cols, 2*i+1)
      plot_image_binary(predictions[image_index], full_tests_labels[image_index], full_tests_images[image_index], class_names)

      plt.subplot(num_rows, 2*num_cols, 2*i+2)
      plot_value_array_binary(predictions[image_index], full_tests_labels[image_index], len(class_names))
      i+=1
  else:
    for image_index in range(index_start, index_start+images_displayed):
        # index = tests_images = i%batch_size + i //batch_size
        plt.subplot(num_rows, 2*num_cols, 2*i-index_start+1)
        plot_image(predictions[image_index], full_tests_labels[image_index], full_tests_images[image_index], class_names)

        plt.subplot(num_rows, 2*num_cols, 2*i+index_start+2)
        plot_value_array(predictions[image_index], full_tests_labels[image_index], len(class_names))

  plt.tight_layout()
  if save_path != None:
    plt.savefig(save_path + "/test_images.png")
  plt.show()