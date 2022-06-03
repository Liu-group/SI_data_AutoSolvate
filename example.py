# Script showing the usage of the pkl and csv files in the SI.

import pickle #version 4.0
import sklearn #version 1.0
import numpy as np

#load model pkl and training/test split
model_pkl = open('ML-GB.pkl', 'rb')
training_indices, test_indices, model = pickle.load(model_pkl)

#load SOAP feature from csv file
features_soap=np.loadtxt('features.csv', skiprows=1, delimiter=',')
features_soap.shape

#predict for test set
prediction=model.predict(features_soap[test_indices,:])
