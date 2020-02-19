import pickle
import numpy as np
from scipy.io.wavfile import read

# Load in Model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Testing that the model loads and predicts correctly
result = read("Cardinal Call 3_1.wav")
result = np.array(result[1],dtype=float)
result = result.flatten()
result = loaded_model.predict([result])
print(result)

result = read("Pileated Call 2_1.wav")
result = np.array(result[1],dtype=float)
result = result.flatten()
result = loaded_model.predict([result])
print(result)
