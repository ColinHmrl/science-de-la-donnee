import tensorflow as tf

def build_homemade(input_shape, num_classes):
    classic_model = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal', input_shape=(input_shape, 3)),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),


        tf.keras.layers.Rescaling(1./255, input_shape=(input_shape, 3)),

        tf.keras.layers.Conv2D(16, 3, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.4),

        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.4),

        tf.keras.layers.Dense(num_classes, activation='softmax')
        ])