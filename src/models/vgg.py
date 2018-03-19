from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
import numpy as np


def get_model(summary=False, img_width = 150):
    # Get back the convolutional part of a VGG network trained on ImageNet
    vgg_16_model = VGG16(weights='imagenet', include_top=False)
    if summary:
        vgg_16_model.summary()

    for layer in vgg_16_model.layers:
        layer.trainable = False

    input_shape = Input(shape=(img_width, img_width, 3), name='image_input')

    # Use the generated model
    output_vgg16_conv = vgg_16_model(input_shape)

    # Add the fully-connected layers
    x = Flatten(name='flatten')(output_vgg16_conv)
    x = Dense(256, activation='relu', name='fc1')(x)
    x = Dropout(0.5)(x)
    x = Dense(10, activation='softmax', name='predictions')(x)

    # Create your own model
    my_model = Model(input=input_shape, output=x)
    if summary:
        my_model.summary()
    return my_model

if __name__=="__main__":
    get_model(True, 224)