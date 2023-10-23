import tensorflow as tf
from tensorflow import keras
from keras_cv.layers import RandomGaussianBlur
from random import randint, seed

def process(image):
    image = tf.cast(image/255. ,tf.float32)
    return image

def add_noise(img, noise_factor=25, blur_factor=5):
    r = tf.experimental.numpy.random.randint(1, 4)
    noised_img = img
    # if r == 1:
    #     noised_img = RandomGaussianBlur(kernel_size=3, factor=(0.5, 2))(img)
    # elif r == 2:
    #     noise = tf.random.normal(shape=tf.shape(img), mean=0.0, stddev=noise_factor/255, dtype=tf.float32)
    #     noised_img = tf.cast(img, tf.float32) + noise
    # elif r == 3:
    noise = tf.random.normal(shape=tf.shape(img), mean=0.0, stddev=noise_factor/255, dtype=tf.float32)
    noised_img = tf.cast(img, tf.float32) + noise
    noised_img = RandomGaussianBlur(kernel_size=2, factor=(0.5, blur_factor))(noised_img)
    return noised_img, img