import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


df = pd.read_csv('Movie_Numpy_Pandas_Visualization/data/movies.csv')
df = pd.DataFrame(df)
plt.rc('font', family='AppleGothic') 


#데이터 백분율
data = {
    '장르': ['공포', '모험', '뮤지컬', '아이맥스', '액션', '아동', '미스터리', '전쟁', '애니메이션', '코미디',
           '스릴러', '판타지', '다큐멘터리', '서부극', '로맨스', '범죄', '드라마', '누와르', 'SF'],
    '1902-1958': [2.5, 3.4, 3.2, 0.0, 1.8, 1.1, 2.7, 3.4, 0.6, 10.1, 5.6, 1.9, 0.2, 2.5, 11.4, 6.4, 24.9, 5.7, 2.0],
    '1959-2015': [5.5, 6.4, 1.8, 0.9, 10.1, 3.0, 3.5, 2.3, 2.3, 19.6, 12.3, 3.7, 2.5, 1.0, 9.0, 7.7, 27.7, 0.2, 4.9]
}


df['year'] = df['title'].apply(lambda x: x.split("(")[-1].split(")")[0])
df = df.drop((df[df['year'] == '    ']['year'].index))
df['year'] = df['year'].astype(int)

# 데이터프레임 생성
df_chat = pd.DataFrame(data)

# 데이터프레임 1958년 이전과 1959년 이후로 나누기
df_1902_1958 = df[(df['year'] >= 1902) & (df['year'] <= 1958)]
df_1959_2015 = df[(df['year'] >= 1959) & (df['year'] <= 2015)]

# 장르별 빈도를 계산하는 함수 정의
def count_genres(df):
    genre_list = []
    for genres in df['genres']:
        genre_list.extend(genres.split('|'))
    return Counter(genre_list)

# 각 기간별 장르별 개수 계산
genre_counts_1902_1958 = count_genres(df_1902_1958)
genre_counts_1959_2015 = count_genres(df_1959_2015)

# 영화 번역
genre_translation = {
    'Drama': '드라마', 'Romance': '로맨스', 'Comedy': '코미디', 'Crime': '범죄', 'Film-Noir': '필름 느와르',
    'Thriller': '스릴러', 'War': '전쟁', 'Adventure': '모험', 'Musical': '뮤지컬', 'Mystery': '미스터리',
    'Horror': '공포', 'Western': '서부극', 'Action': '액션', 'Sci-Fi': 'SF (공상과학)', 'Fantasy': '판타지',
    'Children': '아동', 'Animation': '애니메이션', 'Documentary': '다큐멘터리', 'IMAX': '아이맥스'
}

# 모든 장르를 포함한 리스트 생성
all_genres = set(genre_counts_1902_1958.keys()).union(set(genre_counts_1959_2015.keys()))

#  그래프 크기 설정
plt.figure(figsize=(14, 6))

#  막대 그래프
plt.bar(df_chat['장르'], df_chat['1902-1958'], color = 'skyblue',label='1902-1958', alpha=0.7)
plt.bar(df_chat['장르'], df_chat['1959-2015'], color='pink',label='1959-2015', bottom=df_chat['1902-1958'], alpha=0.7)

# 꺽은선그래프
plt.legend()
plt.plot(df_chat.index, df_chat['1902-1958'], color='skyblue', linestyle='--', marker='o')
plt.plot(df_chat.index, df_chat['1959-2015']+df_chat['1902-1958'], color='pink', linestyle='--', marker='o')

# 라벨과 타이틀 설정
plt.ylim(0, 100)
plt.xlabel('장르')
plt.ylabel('퍼센트')
plt.title('1902년부터 2015년까지 영화 장르별 백분율 비교')

# 범례 표시
plt.legend()

# 그래프 출력
col = ['장르', '1902-1958', '1959-2015']
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # 그래프 여백 조정
plt.show()