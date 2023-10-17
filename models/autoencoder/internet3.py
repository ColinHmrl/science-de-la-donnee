import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras import regularizers, Model

def build(input_encoder):
     
    inputs = keras.Input(shape=(input_encoder, input_encoder, 3), name='input_layer')
    # Block 1
    x = layers.Conv2D(32, kernel_size=3, strides= 1, padding='same', name='conv_1')(inputs)
    x = layers.BatchNormalization(name='bn_1')(x)
    x = layers.LeakyReLU(name='lrelu_1')(x)
    
    # Block 2
    x = layers.Conv2D(64, kernel_size=3, strides= 2, padding='same', name='conv_2')(x)
    x = layers.BatchNormalization(name='bn_2')(x)
    x = layers.LeakyReLU(name='lrelu_2')(x)
    
    # Block 3
    x = layers.Conv2D(64, 3, 2, padding='same', name='conv_3')(x)
    x = layers.BatchNormalization(name='bn_3')(x)
    x = layers.LeakyReLU(name='lrelu_3')(x)
     
    # Block 4
    x = layers.Conv2D(64, 3, 1, padding='same', name='conv_4')(x)
    x = layers.BatchNormalization(name='bn_4')(x)
    x = layers.LeakyReLU(name='lrelu_4')(x)

    # Block 1
    x = layers.Conv2DTranspose(64, 3, strides= 1, padding='same',name='conv_transpose_1')(x)
    x = layers.BatchNormalization(name='dn_1')(x)
    x = layers.LeakyReLU(name='drelu_1')(x)
     
    # Block 2
    x = layers.Conv2DTranspose(64, 3, strides= 2, padding='same', name='conv_transpose_2')(x)
    x = layers.BatchNormalization(name='dn_2')(x)
    x = layers.LeakyReLU(name='drelu_2')(x)
    
    # Block 3
    x = layers.Conv2DTranspose(32, 3, 2, padding='same', name='conv_transpose_3')(x)
    x = layers.BatchNormalization(name='dn_3')(x)
    x = layers.LeakyReLU(name='drelu_3')(x)
    
    # Block 4
    outputs = layers.Conv2DTranspose(3, (3,3),padding='same', activation='relu',
                    activity_regularizer=regularizers.l1(10e-10), name='conv_transpose_4')(x)
    model = tf.keras.Model(inputs, outputs, name="Decoder")

    model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
    
    return model