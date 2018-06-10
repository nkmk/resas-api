import json
import urllib.parse
import urllib.request
import pprint
import pandas as pd

url_base = 'https://opendata.resas-portal.go.jp/api/v1/municipality/taxes/perYear'

p = {'prefCode': 13, 'cityCode': 13103}
url = url_base + '?' + urllib.parse.urlencode(p)
print(url)
# https://opendata.resas-portal.go.jp/api/v1/municipality/taxes/perYear?prefCode=13&cityCode=13103

with open('setting/api_key.json') as f:
    api_key = json.load(f)

req = urllib.request.Request(url, headers=api_key)

with urllib.request.urlopen(req) as response:
    data = response.read()

d = json.loads(data.decode())

pprint.pprint(d)
# {'message': None,
#  'result': {'cityCode': '13103',
#             'cityName': '港区',
#             'data': [{'value': 335, 'year': 2008},
#                      {'value': 326, 'year': 2009},
#                      {'value': 286, 'year': 2010},
#                      {'value': 277, 'year': 2011},
#                      {'value': 254, 'year': 2012},
#                      {'value': 262, 'year': 2013},
#                      {'value': 304, 'year': 2014}],
#             'prefCode': 13,
#             'prefName': '東京都'}}

print(pd.io.json.json_normalize(d['result']))
#   cityCode cityName                                               data  \
# 0    13103       港区  [{'year': 2008, 'value': 335}, {'year': 2009, ...   
#    prefCode prefName  
# 0        13      東京都  

print(pd.io.json.json_normalize(d['result'], record_path='data'))
#    value  year
# 0    335  2008
# 1    326  2009
# 2    286  2010
# 3    277  2011
# 4    254  2012
# 5    262  2013
# 6    304  2014

print(pd.io.json.json_normalize(d['result'], record_path='data',
                                meta=['cityCode', 'cityName', 'prefCode', 'prefName']))
#    value  year cityCode cityName  prefCode prefName
# 0    335  2008    13103       港区        13      東京都
# 1    326  2009    13103       港区        13      東京都
# 2    286  2010    13103       港区        13      東京都
# 3    277  2011    13103       港区        13      東京都
# 4    254  2012    13103       港区        13      東京都
# 5    262  2013    13103       港区        13      東京都
# 6    304  2014    13103       港区        13      東京都

df_city = pd.read_csv('download/city_code_list.csv')

print(df_city.query('prefCode == 40 & bigCityFlag == 1'))
#       bigCityFlag  cityCode  cityName  prefCode
# 1628            1     40101   北九州市門司区        40
# 1629            1     40103   北九州市若松区        40
# 1630            1     40105   北九州市戸畑区        40
# 1631            1     40106  北九州市小倉北区        40
# 1632            1     40107  北九州市小倉南区        40
# 1633            1     40108  北九州市八幡東区        40
# 1634            1     40109  北九州市八幡西区        40
# 1636            1     40131     福岡市東区        40
# 1637            1     40132    福岡市博多区        40
# 1638            1     40133    福岡市中央区        40
# 1639            1     40134     福岡市南区        40
# 1640            1     40135     福岡市西区        40
# 1641            1     40136    福岡市城南区        40
# 1642            1     40137    福岡市早良区        40

a = df_city.query('prefCode == 40 & bigCityFlag == 1')['cityCode'].values

print(a)
# [40101 40103 40105 40106 40107 40108 40109 40131 40132 40133 40134 40135
#  40136 40137]

print(type(a))
# <class 'numpy.ndarray'>

for code in a:
    print(code)
# 40101
# 40103
# 40105
# 40106
# 40107
# 40108
# 40109
# 40131
# 40132
# 40133
# 40134
# 40135
# 40136
# 40137
