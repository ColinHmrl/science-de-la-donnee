import tensorflow as tf

def build(input_shape, num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal', input_shape=(input_shape[0],input_shape[1], 3)),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),


        tf.keras.layers.Rescaling(1./255,  input_shape=(input_shape[0],input_shape[1], 3)),

        tf.keras.layers.Conv2D(16, 3, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        ])
    #Binary
    if(num_classes == 2):
        model.add(
            tf.keras.layers.Dense(1, activation='sigmoid')
        )
        model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=['accuracy'])
    # Multi classes
    else: 
        model.add(
            tf.keras.layers.Dense(num_classes, activation='softmax')
        )
        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])
        
    return model