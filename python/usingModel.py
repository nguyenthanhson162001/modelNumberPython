import tensorflow as tf
import numpy as np
import cv2
import sys
model = tf.keras.models.load_model('model.h5')

im = cv2.imread(sys.argv[1], 0)

dim = (28, 28)
resized = cv2.resize(im, dim,)
# plt.imshow(resized, cmap='gray')

resized = resized.reshape(-1, 784)

predict = model.predict(resized)[0]
predict = np.argmax(predict)
print("ket qua du doan: " + str(predict))
