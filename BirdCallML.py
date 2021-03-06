from sklearn.ensemble import BaggingClassifier
import wave
import numpy as np
from scipy.io.wavfile import read
from sklearn.model_selection import train_test_split
import pickle

cardcall = np.load('CardCalls.npy')
noncall = np.load('NonCalls.npy')
robcall = np.load('RobinCalls.npy')

#print(cardcall, noncall)
call = np.vstack([cardcall, noncall, robcall])

ones = np.ones((149,), dtype=int)
zeros = np.zeros((147+200,), dtype=int)
numbers = np.hstack([ones, zeros])

X = np.array(call)

y = np.array(numbers) # 1 = Cardinal, 0 = NOT Cardinal

#clf = svm.SVC()
#clf.fit(X, y)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)
clf = BaggingClassifier().fit(X, y)

#m = clf.score(X_test, y_test)

#print(m)

#print(clf.support_vectors_)

filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))
