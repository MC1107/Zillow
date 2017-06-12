#import packages
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#read un data
train = pd.read_csv('../input/train_2016.csv', parse_dates=["transactiondate"])
properties = pd.read_csv('../input/properties_2016.csv')