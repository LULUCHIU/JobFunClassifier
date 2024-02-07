from config import config
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import unicodedata




def df_column_selection (_data, TARGET_col, SELECT_col):
    _data = _data[[SELECT_col, TARGET_col]]

    return (_data)


def basic_clean(text):
  """
  A simple function to clean up the data. All the words that
  are not designated as a stop word is then lemmatized after
  encoding and basic regex parsing are performed.
  """
  wnl = nltk.stem.WordNetLemmatizer()
  stopwords = nltk.corpus.stopwords.words('english')
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return " ".join([wnl.lemmatize(word) for word in words if word not in stopwords])

def preprocessing(_data, TARGET_col, SELECT_col):
   _data = df_column_selection(_data, TARGET_col, SELECT_col)
   _data["text_clean"] = _data[SELECT_col].apply(basic_clean)

   return _data[["text_clean",TARGET_col]]
