import matplotlib.pyplot as plt
import pandas as pd

def sampleSize_category(_data, TARGET_col, FigSize = (5,5)):
    fig = plt. figure(figsize=FigSize)
    _data[TARGET_col].value_counts().plot.bar()
    plt.show()
    print(_data[TARGET_col].value_counts())

def tokenFreq_category(_data,TARGET_col,label="Accounting",TOP = 30,FigSize = (10,6)):
    fig = plt.figure(figsize=FigSize)
    _data[_data[TARGET_col]== label]["text_clean"].str.split().explode().value_counts().head(TOP).plot.bar()
    plt.title(label)
    plt.show()
