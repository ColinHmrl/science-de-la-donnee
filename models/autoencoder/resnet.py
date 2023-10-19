import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2DTranspose, Reshape, UpSampling2D, GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50

def build(IMG_SIZE):
    # Define the input layer
    input_shape = (IMG_SIZE, IMG_SIZE, 3)
    
    # Define the encoder model
    encoder_input_layer = Input(shape=input_shape)
    encoder = ResNet50(input_tensor=encoder_input_layer, include_top=False)
    for layer in encoder.layers:
        layer.trainable = False
    encoder_model = Model(inputs=encoder_input_layer, outputs=encoder.output)


    x = GlobalAveragePooling2D()(encoder_model.output)
    x = Dense(1024, activation='relu')(x)
    x = Dense(8 * 8 * 2048, activation='relu')(x)  # Adjust based on your specific ResNet50 variant
    
    x = Reshape((8, 8, 2048))(x)  # Adjust based on your specific ResNet50 variant
    x = Conv2DTranspose(1024, (3, 3), activation='relu', padding='same')(x)
    x = Conv2DTranspose(512, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same')(x)  # Output with the same shape as input

    decoder = Model(encoder_model.output, decoded, name='decoder')
    decoder_model = Model(inputs=encoder_model.output, outputs=decoded)

    autoencoder_input = Input(shape=input_shape)
    encoded = encoder_model(autoencoder_input)
    decoded = decoder_model(encoded)
    
    autoencoder = Model(inputs=autoencoder_input, outputs=decoded)
    autoencoder.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

    autoencoder.summary()
    return autoencoder
