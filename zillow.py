#import packages
import numpy as np 
#import pandas as pd #data structures
import matplotlib.pyplot as plt
import seaborn as sns #visulizations



#read in data
train = pd.read_csv('../input/train_2016.csv', parse_dates=["transactiondate"])
properties = pd.read_csv('../input/properties_2016.csv')

#explore train's shape
train.shape
train.head

