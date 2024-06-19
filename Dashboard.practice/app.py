import requests
import pandas as pd
import streamlit as st


# API URL 설정
api_url = "http://openapi.airgwangsan.kr:8080/Gwangsan/getDustDataAPI?apiId=01"

# API 호출
response = requests.get(api_url)
# JSON 데이터를 가져오기
data = response.json()

df = pd.DataFrame(data['response']['items'])
df_unique = df.drop_duplicates(subset=['place'])
def pm_to_color(pm10, pm2_5):
    if pm10 >= 151 and pm2_5 >= 76:
        return '#FF0000'
    elif pm10 >= 81 and pm2_5 >= 36:
        return '#FFFF00'
    elif pm10 >= 31 and pm2_5 >= 16:
        return '#00FF00'
    else:
        return '#A1CCE2'
    
df_unique.loc[:, 'color'] = df_unique.rename(columns={'LATITUDE':'lat', 'LONGITUDE':'lot'})[['PM10', 'PM2_5']].astype(float).apply(lambda x: pm_to_color(x['PM10'], x['PM2_5']), axis=1)
df_unique


map = df_unique.rename(columns={'LATITUDE':'lat', 'LONGITUDE':'lon'})[['place', 'lat', 'lon', 'color']]
map['lat'] = map['lat'].astype(float)
map['lon'] = map['lon'].astype(float)

st.map(map,color='color')

