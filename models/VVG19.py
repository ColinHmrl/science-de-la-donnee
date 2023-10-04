import tensorflow as tf


def build(input_shape, num_classes):
    backbone = tf.keras.applications.VGG19(weights='imagenet', include_top=False, input_shape=(input_shape[0],input_shape[1], 3))

    for layer in backbone.layers:
        layer.trainable = False

    x = tf.keras.layers.Flatten()(backbone.output)
    x = tf.keras.layers.Dense(512, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    
    if num_classes == 2:
        output = tf.keras.layers.Dense(1, activation='sigmoid')(x)
        loss = tf.keras.losses.BinaryCrossentropy(from_logits=False)
    else:
        output = tf.keras.layers.Dense(num_classes, activation='softmax')(x)
        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)

    model = tf.keras.models.Model(inputs=backbone.input, outputs=output)

    model.compile(optimizer='adam',
              loss=loss,
              metrics=['accuracy', 'AUC', 'Precision', 'Recall', 'TruePositives', 'TrueNegatives', 'FalsePositives', 'FalseNegatives'])
    
    
    return model