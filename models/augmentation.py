import tensorflow as tf

def augment_data(input_layer, input_shape):
    augmented_layer = tf.keras.Sequential([
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
        tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"),
        tf.keras.layers.experimental.preprocessing.RandomContrast(0.2),
        tf.keras.layers.experimental.preprocessing.RandomZoom(0.2),
        tf.keras.layers.Rescaling(1./255, input_shape=input_shape)
    ])
    
    return augmented_layer(input_layer)