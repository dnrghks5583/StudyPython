from keras.preprocessing.image import ImageDataGenerator
import numpy as np

path = 'C:\\Sources\\StudyPython\\day7\\pic'

trainData = ImageDataGenerator()

trainDataSet = trainData.flow_from_directory(
    path + '2\\',
    # batch_size = 32,
    target_size = (128, 128),
    class_mode = 'categorical'
)