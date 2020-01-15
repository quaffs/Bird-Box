# A basic sample of a SKlearn, should be able to show basic layout of how the python script is going to work
# Contact Ryan with any questions

from sklearn import svm
import wave # WAV reader
import numpy as np
from scipy.io.wavfile import read # WAV reader

bj1_1 = bj1_1.flatten() # Audio files come in as 2D arrays. SKlearn can only handle 1D arrays so all audio arrays must be flattened

X = np.array() # X is the array of arrays for input data. Each audio file will be an array in X (which will be a big 2D array)

y = [] # y is the labeling of the X data. It is a 1D array with 1 = Cardinal, 0 = NOT Cardinal

clf = svm.SVC() # buliding of algorithm. SVM is just one statistical anaylsis we could try to get better results
clf.fit(X, y) # fiting of algorithm to X and y

print(clf.predict([bj1_3])) # prediticion of another sound file to test (not the most efficent way to test)
print(clf.predict([card1_3]))

print(clf.support_vectors_) # printing of weights and biases as numbers