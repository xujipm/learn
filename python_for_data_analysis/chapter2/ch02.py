# 
# __*__ coding: utf-8 __*__


import json

import pandas as pd
import numpy as np

from pandas import DataFrame, Series


path = r"H:\python\learn\python_for_data_analysis\chapter2\usagov.txt"
#path = "H:\\python\\learn\\python_for_data_analysis\\chapter2\\usagov.txt"
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
print(records[0])
print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
print(tz_counts)
tz_counts[:].plot(kind='barh', rot=0)
input('end')

