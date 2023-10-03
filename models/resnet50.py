import tensorflow as tf


def build_resnet50(input_shape, num_classes):
    backbone = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(input_shape, 3))

    for layer in backbone.layers:
        layer.trainable = False

    x = tf.keras.layers.Flatten()(backbone.output)
    x = tf.keras.layers.Dense(512, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.5)(x)  
    
    if num_classes == 2:
        output = tf.keras.layers.Dense(1, activation='sigmoid')(x)
    else:
        output = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.models.Model(inputs=backbone.input, outputs=output)

    model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=['accuracy'])
    
    return model