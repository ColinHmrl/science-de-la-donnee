import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2DTranspose, Reshape
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50

def build(input_shape):
    # Define the input layer
    input_layer = Input(shape=input_shape)

    encoder = ResNet50(input_tensor=input_layer, include_top=False)
    for layer in encoder.layers:
        layer.trainable = False
    
    
    
    # Define the encoder model
    encoder_model = Model(inputs=input_layer, outputs=encoder.output)


    decoder_input = Input(shape=input_shape)

    decoder = Conv2DTranspose(512, (3, 3), activation='relu', padding='same')(decoder_input)
    decoder = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(decoder)
    decoder = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(decoder)

    decoded_output = Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same')(decoder)

    decoder_model = Model(inputs=decoder_input, outputs=decoded_output)

    autoencoder_input = Input(shape=input_shape)
    encoded = encoder_model(autoencoder_input)
    decoded = decoder_model(encoded)

    autoencoder = Model(inputs=autoencoder_input, outputs=decoded)
    
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder
