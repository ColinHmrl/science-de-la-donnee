from tensorflow import keras
from keras import layers

import sampling_layer
import variational_loss_layer

def build(img_size, latent_dim, loss_weights):
    encoder_inputs    = keras.Input(shape=(img_size, img_size, 3))
    x         = layers.Conv2D(128, 3, strides=1, padding="same", activation="relu")(encoder_inputs)
    x         = layers.Conv2D(256, 3, strides=2, padding="same", activation="relu")(x)
    x         = layers.Conv2D(256, 3, strides=2, padding="same", activation="relu")(x)
    x         = layers.Conv2D(128, 3, strides=1, padding="same", activation="relu")(x)
    x         = layers.Flatten()(x)
    x         = layers.Dense(64, activation="relu")(x)

    z_mean    = layers.Dense(latent_dim, name="z_mean")(x)
    z_log_var = layers.Dense(latent_dim, name="z_log_var")(x)
    z         = sampling_layer.SamplingLayer()([z_mean, z_log_var])

    encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")

    encoder.compile()

    decoder_inputs  = keras.Input(shape=(latent_dim,))
    x       = layers.Dense(56 * 56 * 64, activation="relu")(decoder_inputs)
    x       = layers.Reshape((56, 56, 64))(x)
    x       = layers.Conv2DTranspose(256, 3, strides=1, padding="same", activation="relu")(x)
    x       = layers.Conv2DTranspose(256, 3, strides=2, padding="same", activation="relu")(x)
    x       = layers.Conv2DTranspose(256, 3, strides=2, padding="same", activation="relu")(x)
    x       = layers.Conv2DTranspose(128, 3, strides=1, padding="same", activation="relu")(x)
    outputs = layers.Conv2DTranspose(3,  3, padding="same", activation="sigmoid")(x)

    decoder = keras.Model(decoder_inputs, outputs, name="decoder")
    decoder.compile()

    inputs = keras.Input(shape=(img_size, img_size,3))

    z_mean, z_log_var, z = encoder(inputs)
    outputs              = decoder(z)

    outputs = variational_loss_layer.VariationalLossLayer(loss_weights=loss_weights)([inputs, z_mean, z_log_var, outputs])

    vae=keras.Model(inputs,outputs)

    vae.compile(optimizer='adam', loss=None)
    vae.summary()
    return vae