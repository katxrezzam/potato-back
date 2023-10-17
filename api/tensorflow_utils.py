import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']


def get_route():
    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.dirname(current_path)
    images_path = os.path.join(parent_path, 'images')
    return images_path


def predict(img_name):
    try:
        # model = load_model('potato_pretrain_model.h5')
        model = load_model('crop_classification.keras')
        image_path = get_route() + '\\' + img_name
        img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        prediction = model.predict(img_array)
        score = tf.nn.softmax(prediction[0])
        return class_names[np.argmax(score)], 100 * np.max(score)
    except Exception as e:
        print(e)
        return "Error"
