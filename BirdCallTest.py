from sklearn import svm
import wave
import numpy as np
from scipy.io.wavfile import read

card1_1 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_1.wav")
card1_1 = np.array(card1_1[1],dtype=float)
card1_2 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_2.wav")
card1_2 = np.array(card1_2[1],dtype=float)
card1_3 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_3.wav")
card1_3 = np.array(card1_3[1],dtype=float)
card1_4 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_4.wav")
card1_4 = np.array(card1_4[1],dtype=float)
card1_5 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_5.wav")
card1_5 = np.array(card1_5[1],dtype=float)
card1_6 = read("Call_Samples/Cardinal Calls/Cardinal Call 1_6.wav")
card1_6 = np.array(card1_6[1],dtype=float)
card3_1 = read("Call_Samples/Cardinal Calls/Cardinal Call 3_1.wav")
card3_1 = np.array(card3_1[1],dtype=float)
card3_2 = read("Call_Samples/Cardinal Calls/Cardinal Call 3_2.wav")
card3_2 = np.array(card3_2[1],dtype=float)
card4_1 = read("Call_Samples/Cardinal Calls/Cardinal Call 4_1.wav")
card4_1 = np.array(card4_1[1],dtype=float)
card4_2 = read("Call_Samples/Cardinal Calls/Cardinal Call 4_2.wav")
card4_2 = np.array(card4_2[1],dtype=float)
card4_3 = read("Call_Samples/Cardinal Calls/Cardinal Call 4_3.wav")
card4_3 = np.array(card4_3[1],dtype=float)
card4_4 = read("Call_Samples/Cardinal Calls/Cardinal Call 4_4.wav")
card4_4 = np.array(card4_4[1],dtype=float)
card4_5 = read("Call_Samples/Cardinal Calls/Cardinal Call 4_5.wav")
card4_5 = np.array(card4_5[1],dtype=float)
card5_1 = read("Call_Samples/Cardinal Calls/Cardinal Call 5_1.wav")
card5_1 = np.array(card5_1[1],dtype=float)


bj1_1 = read("Call_Samples/Non-Cardinal Calls/Blue Jay Call 1_1.wav")
bj1_1 = np.array(bj1_1[1],dtype=float)
bj1_2 = read("Call_Samples/Non-Cardinal Calls/Blue Jay Call 1_2.wav")
bj1_2 = np.array(bj1_2[1],dtype=float)
bj1_3 = read("Call_Samples/Non-Cardinal Calls/Blue Jay Call 1_3.wav")
bj1_3 = np.array(bj1_3[1],dtype=float)

card1_1 = card1_1.flatten()
card1_2 = card1_2.flatten()
card1_3 = card1_3.flatten()
card1_4 = card1_4.flatten()
card1_5 = card1_5.flatten()
card1_6 = card1_6.flatten()
card3_1 = card3_1.flatten()
card3_2 = card3_2.flatten()
card4_1 = card4_1.flatten()
card4_2 = card4_2.flatten()
card4_3 = card4_3.flatten()
card4_4 = card4_4.flatten()
card4_5 = card4_5.flatten()
card5_1 = card5_1.flatten()

print(card1_6.shape[0], card3_1.shape[0], card3_2.shape[0], card4_1.shape[0], card5_1.shape[0])

bj1_1 = bj1_1.flatten()
bj1_2 = bj1_2.flatten()
bj1_3 = bj1_3.flatten()
#bj1_1 = np.append(bj1_1, np.zeros(a.shape[0]-bj1_1.shape[0]))

X = np.array([card1_1, card1_2, card1_3, card1_4, card1_5, card1_6, card3_1, card3_2, card4_1, card4_2, card4_3, card4_4, card4_5, card5_1, bj1_1, bj1_2, bj1_3])

y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0] # 1 = Cardinal, 0 = NOT Cardinal

clf = svm.SVC()
clf.fit(X, y)

print(clf.predict([bj1_3]))
print(clf.predict([card1_3]))

print(clf.support_vectors_)