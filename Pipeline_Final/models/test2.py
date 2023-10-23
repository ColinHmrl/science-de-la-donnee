import tensorflow as tf
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, Dropout, add
from keras import regularizers, Model

def build(img_size):
    image = Input(shape=(img_size,img_size,3))

    # Encoder
    l1 = Conv2D(64, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(image)     
    l2 = Conv2D(64, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l1)

#     l3 = MaxPooling2D(padding='same')(l2)
    l3 = Dropout(0.3)(l2)
    l4 = Conv2D(128, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l3)
    l5 = Conv2D(128, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l4)

#     l6 = MaxPooling2D(padding='same')(l5)
    l7 = Conv2D(256, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l5)

    #Decoder
#     l8 = UpSampling2D()(l7)
    l9 = Conv2D(128, (3,3), padding='same', activation='relu',
            activity_regularizer=regularizers.l1(10e-10))(l7)
    l10 = Conv2D(128, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l9)

    l11 = add([l5,l10])
#     l12 = UpSampling2D()(l11)
    l13 = Conv2D(64, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l11)
    l14 = Conv2D(64, (3,3), padding='same', activation='relu',
                activity_regularizer=regularizers.l1(10e-10))(l13)

    l15 = add([l14,l2])

    decoded = Conv2D(3, (3,3), padding='same', activation='relu',
                    activity_regularizer=regularizers.l1(10e-10))(l15)
    model = Model(image, decoded)
    
    model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])
    return model
