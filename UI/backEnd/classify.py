import sys
import warnings
import pickle
import numpy as np
from scipy.io.wavfile import read
warnings.filterwarnings(action='ignore')
# Load in Model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Testing that the model loads and predicts correctly
input_file = sys.argv[1]
print(input_file)
result = read(input_file)
result = np.array(result[1],dtype=float)
result = result.flatten()
if result.size > 882000:
	result = result[0:882000]
elif result.size < 882000:
	result = np.append(result, np.zeros(882000-result.size))
result = loaded_model.predict([result])
print(result[0])
if result[0] == 1:
	classification = "Cardinal"
else:
	classification = "Non-Cardinal"
print(classification)
