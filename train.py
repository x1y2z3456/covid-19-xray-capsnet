import os
import cv2
import numpy as np
import tensorflow as tf


home_directory = os.path.expanduser('~')
base_dir = os.path.abspath(
    f'{home_directory}/Efficient-CapsNet/covid-chestxray-dataset')
to_create = {
    'root': base_dir,
    'train_dir': os.path.join(base_dir, 'train'),
    'test_dir': os.path.join(base_dir, 'test'),
}


def data_load(root_path, scale=(96, 96)):
    categories = os.listdir(root_path)
    x = []
    y = []
    for i, cat in enumerate(categories):
        img_path = os.path.join(root_path, cat)
        images = os.listdir(img_path)
        for image in images:
            img = cv2.imread(os.path.join(img_path, image), 0)
            img = cv2.resize(img, scale)
            x.append(img)
            y.append(i)
    return np.array(x), np.array(y)


x_train, y_train = data_load(to_create.get('train_dir'))
x_test, y_test = data_load(to_create.get('test_dir'))
print(' trainset has length of {}'.format(len(x_train)))
print(' testset has length of {}'.format(len(x_test)))

x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)

train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_data = tf.data.Dataset.from_tensor_slices((x_test, y_test))

print(x_train.shape)
print(y_train.shape)

train_data = train_data.shuffle(506).batch(6)
test_data = test_data.shuffle(506).batch(2)


