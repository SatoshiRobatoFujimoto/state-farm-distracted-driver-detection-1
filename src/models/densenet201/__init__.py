from keras.applications import DenseNet201
from keras.layers import Input, Flatten, Dense, Dropout, GlobalAveragePooling2D, regularizers
from keras.models import Model
from keras_contrib.applications.densenet import DenseNetImageNet121

from models.fc_layers import add_fc_layers


def get_model(summary=False, img_width=150, fc_layers=[4096, 4096], fc_dropout_layers=[0.5, 0.5]):
    # Get back the convolutional part of a VGG network trained on ImageNet
    base_model = DenseNet201(input_tensor=Input(shape=(img_width, img_width, 3)), include_top=False)
    x = GlobalAveragePooling2D(name='avg_pool')(base_model.output)
    x = Dense(10, activation='softmax', kernel_regularizer=regularizers.l2(0.01))(x)
    my_model = Model(input=base_model.input, output=x)
    layers_to_freeze=481
    for i in range(layers_to_freeze):
        my_model.layers[i].trainable = False
    if summary:
        print("---------------------------------------------------------")
        for i, layer in enumerate(my_model.layers):
            print(i, layer.name)
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        my_model.summary()
    return my_model, layers_to_freeze, 2

if __name__ == "__main__":
    model = get_model(True, 224)
    print('Layers', len(model.layers))
