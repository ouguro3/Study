import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.applications import ResNet50, DenseNet121, EfficientNetB0
from keras.optimizers import Adam

# ignoring warnings
import warnings
warnings.simplefilter('ignore')

import os, cv2, json
from PIL import image

TARGET_SIZE = 224

WORK_DIR = '../input/cassava-leaf-disease-classification'
os.listdir(WORK_DIR)

def create_model():
    model = models.Sequential()

    model.add(EfficientNetB0(include_top= False, weights= None,
                             input_shape= (TARGET_SIZE, TARGET_SIZE, 3)))
    
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(5, activation= 'softmax'))

    model.compile(optimizer= Adam(lr = 0.001),
                  loss = "sparse_categorical_crossentropy",
                  metrics= ['acc'])
    return model

model = create_model()
model.summary()

# Prediction

ss = pd.read_csv(os.path.join(WORK_DIR, 'sample_submission.csv'))
print(ss)


