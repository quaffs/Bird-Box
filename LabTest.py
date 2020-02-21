from sklearn.ensemble import BaggingClassifier
import wave
import numpy as np
from scipy.io.wavfile import read
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import pickle

cardcall = np.load('CardCalls.npy')
noncall = np.load('NonCalls.npy')
robcall = np.load('RobinCalls.npy')

#print(cardcall, noncall)
call = np.vstack([cardcall, noncall, robcall])

ones = np.ones((182,), dtype=int)
zeros = np.zeros((460+200,), dtype=int)
numbers = np.hstack([ones, zeros])

X = np.array(call)

y = np.array(numbers) # 1 = Cardinal, 0 = NOT Cardinal

# filename = 'finalized_model.sav'
# realclf = BaggingClassifier().fit(X, y)
# pickle.dump(realclf, open(filename, 'wb'))
#clf = svm.SVC()
#clf.fit(X, y)

print("here")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.66, random_state=41)
filename = 'finalized_model.sav'
clf = pickle.load(open(filename, 'rb'))

m = clf.score(X_test, y_test)

print(m)

y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

tn, fp, fn, tp = confusion_matrix(y, y_test).ravel()
print(tn, fp, fn, tp)
#print(clf.support_vectors_)

