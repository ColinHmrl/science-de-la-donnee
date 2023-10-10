import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def plot_image(i, predictions_array, true_label, img, class_names):
  true_label, img = true_label[i], img[i]/255.0
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)
  # use softmax to convert the logits to probabilities
  # and take the argmax to get the predicted label
  predictions_array = (tf.nn.softmax(predictions_array))

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(5))
  plt.yticks([])
  predictions_array = (tf.nn.softmax(predictions_array))
  thisplot = plt.bar(range(5), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')