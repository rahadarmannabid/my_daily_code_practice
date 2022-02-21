# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:01:10 2022

@author: Dell
"""

import pandas as pd

messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t',
                           names=["label", "message"])

#Data cleaning and preprocessing
import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
