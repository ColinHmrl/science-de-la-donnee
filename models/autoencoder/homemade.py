import tensorflow as tf
from keras.layers import Input, Conv2D, Conv2DTranspose, Dropout
from keras.models import Model


def build(img_size):
    input_img = Input(shape=(img_size, img_size, 3))

    # Encoder
    x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_img)
    x = Dropout(0.5)(x)

    x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = Dropout(0.5)(x)

    x = Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    x = Dropout(0.5)(x)
    
    x = Conv2D(512, (3, 3), activation='relu', padding='same')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same')(x)
    encoded = Dropout(0.2)(x)

    # Decoder

    x = Conv2D(512, (3, 3), activation='relu', padding='same')(encoded)
    x = Conv2D(512, (3, 3), activation='relu', padding='same')(x)
    
    x = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(x)
    x = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(x)
    
    x = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(x)
    x = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(x)

    x = Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(x)


    decoded = Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same')(x)


    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

    return autoencoder