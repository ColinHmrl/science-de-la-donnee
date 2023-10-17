import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2DTranspose, Reshape, UpSampling2D
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


    decoder_input_layer = Input(shape=(encoder.output.shape[1], encoder.output.shape[2], encoder.output.shape[3]))    
    decoder = Conv2DTranspose(256, (3, 3), activation='relu', padding='same')(decoder)
    decoder = Conv2DTranspose(128, (3, 3), activation='relu', padding='same')(decoder)
    decoder = Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(decoder)
    decoder = Conv2DTranspose(32, (3, 3), activation='relu', padding='same')(decoder)
    decoded_output = Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same')(decoder)
    decoder_model = Model(inputs=decoder_input_layer, outputs=decoded_output)

    autoencoder_input = Input(shape=(input_shape,input_shape,3))
    encoded = encoder_model(autoencoder_input)
    decoded = decoder_model(encoded)
    
    autoencoder = Model(inputs=autoencoder_input, outputs=decoded)
    autoencoder.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

    return autoencoder
