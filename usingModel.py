import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.losses import categorical_crossentropy
import tensorflow as tf
import sys
import cv2

# print("Tham so" + sys.argv[1])

# print(I)
# Test
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# x_train = x_train.reshape(-1, 784)
# x_test = x_test.reshape(-1, 784)
# y_train = to_categorical(y_train, num_classes=10)
# y_test = to_categorical(y_test, num_classes=10)


# Test
# id_test = 102
# img = x_test[id_test, :].reshape(1, -1)
# label = np.argmax(y_test[id_test, :])

model = tf.keras.models.load_model('model.h5')
img = cv2.imread('./img.png')
print(img)

predict = model.predict(img)[0]
predict = np.argmax(predict)
print("ket qua du doan: " + str(predict))
print(img)
plt.imshow(img.reshape(28, 28), cmap='gray')
