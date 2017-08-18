import json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

with open('gov.txt', 'r') as f:
    records = [json.loads(line) for line in f]



frame = DataFrame(records)

print(frame['tz'][:10])

# 将缺失字段填充为Unknown
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == '']='Unknow'

# 按照值统计频率
tz_counts = clean_tz.value_counts()
# 展示直方图
tz_counts[:10].plot(kind='barh', rot=0)
