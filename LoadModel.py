import pickle
import sklearn
import numpy as np

filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict([np.zeros(882000)])
print(result)
result = loaded_model.predict([np.ones(882000)])
print(result)
