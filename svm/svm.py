import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd 
dataset= pd.read_csv('heartdisease.csv')
X = dataset.iloc[:,[2,3]].values
Y=dataset.iloc[:,4].values
