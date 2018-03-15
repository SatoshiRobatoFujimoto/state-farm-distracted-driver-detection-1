'''
This program is used to detect the driver's status (10 statuses) by using a small convolutional neural network, which
is trained fram scatch using the training images.
'''


from data_generator import get_train_datagen, get_validation_datagen
from models.simple_model import get_model

model = get_model()


#this is the generator that will read images found in sub-folders of 'data/train',
#and indefinitely generate batches of augmented image data
train_generator=get_train_datagen()

# this is the  generator for validation data
validation_generator=get_validation_datagen()

# train the convolutional neural network
model.fit_generator(generator=train_generator, epochs=20,
                    validation_data=validation_generator)

# save the weights
model.save_weights('driver_state_detection_small_CNN.h5')

