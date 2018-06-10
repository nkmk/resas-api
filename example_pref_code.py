import json
import urllib.request
import pprint
import pandas as pd

with open('setting/api_key_sample.json') as f:
    print(f.read())
# {"X-API-KEY":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

with open('setting/api_key_sample.json') as f:
    api_key_sample = json.load(f)

print(api_key_sample)
# {'X-API-KEY': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}

print(type(api_key_sample))
# <class 'dict'>

with open('setting/api_key.json') as f:
    api_key = json.load(f)

url = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'

req = urllib.request.Request(url, headers=api_key)

print(type(req))
# <class 'urllib.request.Request'>

with urllib.request.urlopen(req) as response:
    data = response.read()

print(type(data))
# <class 'bytes'>

d = json.loads(data.decode())

pprint.pprint(d)
# {'message': None,
#  'result': [{'prefCode': 1, 'prefName': '北海道'},
#             {'prefCode': 2, 'prefName': '青森県'},
#             {'prefCode': 3, 'prefName': '岩手県'},
#             {'prefCode': 4, 'prefName': '宮城県'},
#             {'prefCode': 5, 'prefName': '秋田県'},
#             {'prefCode': 6, 'prefName': '山形県'},
#             {'prefCode': 7, 'prefName': '福島県'},
#             {'prefCode': 8, 'prefName': '茨城県'},
#             {'prefCode': 9, 'prefName': '栃木県'},
#             {'prefCode': 10, 'prefName': '群馬県'},
#             {'prefCode': 11, 'prefName': '埼玉県'},
#             {'prefCode': 12, 'prefName': '千葉県'},
#             {'prefCode': 13, 'prefName': '東京都'},
#             {'prefCode': 14, 'prefName': '神奈川県'},
#             {'prefCode': 15, 'prefName': '新潟県'},
#             {'prefCode': 16, 'prefName': '富山県'},
#             {'prefCode': 17, 'prefName': '石川県'},
#             {'prefCode': 18, 'prefName': '福井県'},
#             {'prefCode': 19, 'prefName': '山梨県'},
#             {'prefCode': 20, 'prefName': '長野県'},
#             {'prefCode': 21, 'prefName': '岐阜県'},
#             {'prefCode': 22, 'prefName': '静岡県'},
#             {'prefCode': 23, 'prefName': '愛知県'},
#             {'prefCode': 24, 'prefName': '三重県'},
#             {'prefCode': 25, 'prefName': '滋賀県'},
#             {'prefCode': 26, 'prefName': '京都府'},
#             {'prefCode': 27, 'prefName': '大阪府'},
#             {'prefCode': 28, 'prefName': '兵庫県'},
#             {'prefCode': 29, 'prefName': '奈良県'},
#             {'prefCode': 30, 'prefName': '和歌山県'},
#             {'prefCode': 31, 'prefName': '鳥取県'},
#             {'prefCode': 32, 'prefName': '島根県'},
#             {'prefCode': 33, 'prefName': '岡山県'},
#             {'prefCode': 34, 'prefName': '広島県'},
#             {'prefCode': 35, 'prefName': '山口県'},
#             {'prefCode': 36, 'prefName': '徳島県'},
#             {'prefCode': 37, 'prefName': '香川県'},
#             {'prefCode': 38, 'prefName': '愛媛県'},
#             {'prefCode': 39, 'prefName': '高知県'},
#             {'prefCode': 40, 'prefName': '福岡県'},
#             {'prefCode': 41, 'prefName': '佐賀県'},
#             {'prefCode': 42, 'prefName': '長崎県'},
#             {'prefCode': 43, 'prefName': '熊本県'},
#             {'prefCode': 44, 'prefName': '大分県'},
#             {'prefCode': 45, 'prefName': '宮崎県'},
#             {'prefCode': 46, 'prefName': '鹿児島県'},
#             {'prefCode': 47, 'prefName': '沖縄県'}]}

with open('download/pref_code_list.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)

df = pd.io.json.json_normalize(d['result'])
print(df.head())
#    prefCode prefName
# 0         1      北海道
# 1         2      青森県
# 2         3      岩手県
# 3         4      宮城県
# 4         5      秋田県

s_code = df.set_index('prefCode')['prefName']
print(s_code.head())
# prefCode
# 1    北海道
# 2    青森県
# 3    岩手県
# 4    宮城県
# 5    秋田県
# Name: prefName, dtype: object

print(s_code[13])
# 東京都

# print(s_code[100])
# KeyError: 100

d_code = df.set_index('prefCode')['prefName'].to_dict()

print(d_code[13])
# 東京都

# print(d_code[100])
# KeyError: 100

print(d_code.get(13))
# 東京都

print(d_code.get(100))
# None

s_name = df.set_index('prefName')['prefCode']
print(s_name.head())
# prefName
# 北海道    1
# 青森県    2
# 岩手県    3
# 宮城県    4
# 秋田県    5
# Name: prefCode, dtype: int64

print(s_name['東京都'])
# 13

d_name = df.set_index('prefName')['prefCode'].to_dict()

print(d_name['東京都'])
# 13

print(d_name.get('東京都'))
# 13

df.to_csv('download/pref_code_list.csv', index=None)

df_from_csv = pd.read_csv('download/pref_code_list.csv')
print(df_from_csv.head())
#    prefCode prefName
# 0         1      北海道
# 1         2      青森県
# 2         3      岩手県
# 3         4      宮城県
# 4         5      秋田県
