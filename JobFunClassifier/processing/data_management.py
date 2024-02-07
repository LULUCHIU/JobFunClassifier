from config import config
import pandas as pd

def load_dataset(file_name):
    _data = pd.read_excel(config.DATAPATH + file_name)
    return _data
