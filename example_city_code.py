import json
import urllib.parse
import urllib.request
import pprint
import pandas as pd

url_base = 'https://opendata.resas-portal.go.jp/api/v1/cities'

p = {'prefCode': 13}
url = url_base + '?' + urllib.parse.urlencode(p)
print(url)
# https://opendata.resas-portal.go.jp/api/v1/cities?prefCode=13

pref_code = 13
url = url_base + '?prefCode=' + str(pref_code)
print(url)
# https://opendata.resas-portal.go.jp/api/v1/cities?prefCode=13

with open('setting/api_key.json') as f:
    api_key = json.load(f)

req = urllib.request.Request(url, headers=api_key)

with urllib.request.urlopen(req) as response:
    data = response.read()

d = json.loads(data.decode())

pprint.pprint(d, width=100)
# {'message': None,
#  'result': [{'bigCityFlag': '3', 'cityCode': '13101', 'cityName': '千代田区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13102', 'cityName': '中央区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13103', 'cityName': '港区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13104', 'cityName': '新宿区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13105', 'cityName': '文京区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13106', 'cityName': '台東区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13107', 'cityName': '墨田区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13108', 'cityName': '江東区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13109', 'cityName': '品川区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13110', 'cityName': '目黒区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13111', 'cityName': '大田区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13112', 'cityName': '世田谷区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13113', 'cityName': '渋谷区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13114', 'cityName': '中野区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13115', 'cityName': '杉並区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13116', 'cityName': '豊島区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13117', 'cityName': '北区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13118', 'cityName': '荒川区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13119', 'cityName': '板橋区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13120', 'cityName': '練馬区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13121', 'cityName': '足立区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13122', 'cityName': '葛飾区', 'prefCode': 13},
#             {'bigCityFlag': '3', 'cityCode': '13123', 'cityName': '江戸川区', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13201', 'cityName': '八王子市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13202', 'cityName': '立川市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13203', 'cityName': '武蔵野市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13204', 'cityName': '三鷹市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13205', 'cityName': '青梅市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13206', 'cityName': '府中市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13207', 'cityName': '昭島市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13208', 'cityName': '調布市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13209', 'cityName': '町田市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13210', 'cityName': '小金井市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13211', 'cityName': '小平市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13212', 'cityName': '日野市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13213', 'cityName': '東村山市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13214', 'cityName': '国分寺市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13215', 'cityName': '国立市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13218', 'cityName': '福生市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13219', 'cityName': '狛江市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13220', 'cityName': '東大和市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13221', 'cityName': '清瀬市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13222', 'cityName': '東久留米市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13223', 'cityName': '武蔵村山市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13224', 'cityName': '多摩市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13225', 'cityName': '稲城市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13227', 'cityName': '羽村市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13228', 'cityName': 'あきる野市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13229', 'cityName': '西東京市', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13303', 'cityName': '瑞穂町', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13305', 'cityName': '日の出町', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13307', 'cityName': '檜原村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13308', 'cityName': '奥多摩町', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13361', 'cityName': '大島町', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13362', 'cityName': '利島村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13363', 'cityName': '新島村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13364', 'cityName': '神津島村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13381', 'cityName': '三宅村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13382', 'cityName': '御蔵島村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13401', 'cityName': '八丈町', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13402', 'cityName': '青ヶ島村', 'prefCode': 13},
#             {'bigCityFlag': '0', 'cityCode': '13421', 'cityName': '小笠原村', 'prefCode': 13}]}

l = []
url_base = 'https://opendata.resas-portal.go.jp/api/v1/cities'

for pref_code in range(1, 48):
    url = url_base + '?prefCode=' + str(pref_code)
    req = urllib.request.Request(url, headers=api_key)
    with urllib.request.urlopen(req) as response:
        data = response.read()
    d = json.loads(data.decode())
    l.append(pd.io.json.json_normalize(d['result']))

df_all = pd.concat(l, ignore_index=True)

print(df_all.head())
#   bigCityFlag cityCode cityName  prefCode
# 0           2    01100      札幌市         1
# 1           1    01101   札幌市中央区         1
# 2           1    01102    札幌市北区         1
# 3           1    01103    札幌市東区         1
# 4           1    01104   札幌市白石区         1

print(df_all.shape)
# (1920, 4)

print(df_all.dtypes)
# bigCityFlag    object
# cityCode       object
# cityName       object
# prefCode        int64
# dtype: object

print(df_all.query('bigCityFlag == "2"'))
#      bigCityFlag cityCode cityName  prefCode
# 0              2    01100      札幌市         1
# 265            2    04100      仙台市         4
# 529            2    11100    さいたま市        11
# 602            2    12100      千葉市        12
# 724            2    14100      横浜市        14
# 743            2    14130      川崎市        14
# 751            2    14150     相模原市        14
# 785            2    15100      新潟市        15
# 1020           2    22100      静岡市        22
# 1024           2    22130      浜松市        22
# 1065           2    23100     名古屋市        23
# 1183           2    26100      京都市        26
# 1220           2    27100      大阪市        27
# 1245           2    27140       堺市        27
# 1294           2    28100      神戸市        28
# 1451           2    33100      岡山市        33
# 1482           2    34100      広島市        34
# 1627           2    40100     北九州市        40
# 1635           2    40130      福岡市        40
# 1742           2    43100      熊本市        43

print(df_all.query('bigCityFlag == "1" & prefCode == 14'))
#     bigCityFlag cityCode  cityName  prefCode
# 725           1    14101    横浜市鶴見区        14
# 726           1    14102   横浜市神奈川区        14
# 727           1    14103     横浜市西区        14
# 728           1    14104     横浜市中区        14
# 729           1    14105     横浜市南区        14
# 730           1    14106  横浜市保土ケ谷区        14
# 731           1    14107    横浜市磯子区        14
# 732           1    14108    横浜市金沢区        14
# 733           1    14109    横浜市港北区        14
# 734           1    14110    横浜市戸塚区        14
# 735           1    14111    横浜市港南区        14
# 736           1    14112     横浜市旭区        14
# 737           1    14113     横浜市緑区        14
# 738           1    14114    横浜市瀬谷区        14
# 739           1    14115     横浜市栄区        14
# 740           1    14116     横浜市泉区        14
# 741           1    14117    横浜市青葉区        14
# 742           1    14118    横浜市都筑区        14
# 744           1    14131    川崎市川崎区        14
# 745           1    14132     川崎市幸区        14
# 746           1    14133    川崎市中原区        14
# 747           1    14134    川崎市高津区        14
# 748           1    14135    川崎市多摩区        14
# 749           1    14136    川崎市宮前区        14
# 750           1    14137    川崎市麻生区        14
# 752           1    14151    相模原市緑区        14
# 753           1    14152   相模原市中央区        14
# 754           1    14153    相模原市南区        14

s_code = df_all.set_index('cityCode')['cityName']
print(s_code.head())
# cityCode
# 01100       札幌市
# 01101    札幌市中央区
# 01102     札幌市北区
# 01103     札幌市東区
# 01104    札幌市白石区
# Name: cityName, dtype: object

print(s_code['14100'])
# 横浜市

s_name = df_all.set_index('cityName')['cityCode']
print(s_name.head())
# cityName
# 札幌市       01100
# 札幌市中央区    01101
# 札幌市北区     01102
# 札幌市東区     01103
# 札幌市白石区    01104
# Name: cityCode, dtype: object

print(s_name['横浜市'])
# 14100

df_all.to_csv('download/city_code_list.csv', index=None)

df_all.to_json('download/city_code_list.json', orient='records', force_ascii=False)

with open('download/city_code_list.json') as f:
    data_json = json.load(f)

print(type(data_json))
# <class 'list'>

pprint.pprint(data_json[:5])
# [{'bigCityFlag': '2', 'cityCode': '01100', 'cityName': '札幌市', 'prefCode': 1},
#  {'bigCityFlag': '1', 'cityCode': '01101', 'cityName': '札幌市中央区', 'prefCode': 1},
#  {'bigCityFlag': '1', 'cityCode': '01102', 'cityName': '札幌市北区', 'prefCode': 1},
#  {'bigCityFlag': '1', 'cityCode': '01103', 'cityName': '札幌市東区', 'prefCode': 1},
#  {'bigCityFlag': '1', 'cityCode': '01104', 'cityName': '札幌市白石区', 'prefCode': 1}]

print(len(data_json))
# 1920

df_from_json = pd.read_json('download/city_code_list.json')
print(df_from_json.head())
#    bigCityFlag  cityCode cityName  prefCode
# 0            2      1100      札幌市         1
# 1            1      1101   札幌市中央区         1
# 2            1      1102    札幌市北区         1
# 3            1      1103    札幌市東区         1
# 4            1      1104   札幌市白石区         1

print(df_from_json.shape)
# (1920, 4)
