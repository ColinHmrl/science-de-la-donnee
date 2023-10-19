import tensorflow as tf
from keras.layers import Input, Conv2D, Conv2DTranspose, Dropout, MaxPooling2D, UpSampling2D
from keras.models import Model


def build(img_size):
    input_img = Input(shape=(img_size, img_size, 3))

    # Encoder
    x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_img)
    x = Dropout(0.3)(x)

    x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = Dropout(0.3)(x)
    x = MaxPooling2D((2, 2), padding='same')(x)

    encoded = Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    
    # Decoder    
    x = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(x)

    x = Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(x)

    decoded = Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same')(x)


    autoencoder = Model(input_img, decoded)
    autoencoder.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

    return autoencoder