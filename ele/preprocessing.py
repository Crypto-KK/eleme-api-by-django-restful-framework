import pandas as pd

data = pd.read_csv('eleme.csv',encoding='utf-8')

data['city'] = data['school'].apply(lambda x: x.split(')')[0].split('(')[1])
data['school'] = data['school'].apply(lambda x: x.split('(')[0])
data['time'] = data['time'].apply(lambda x: str(x).replace('明天',''))
data['contact'] = data['contact'].apply(lambda x: str(x).replace(' ',','))
data = data.applymap(str)
print(data)

data.to_csv('eleme_ok',encoding='utf-8')
print('success')