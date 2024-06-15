import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


df = pd.read_csv('Movie_Numpy_Pandas_Visualization/data/movies.csv')
df = pd.DataFrame(df)

#데이터값이 존재하지않는 결측값 제거
df['year'] = df['title'].apply(lambda x: x.split("(")[-1].split(")")[0])
df = df.drop((df[df['year'] == '    ']['year'].index))
df['year'] = df['year'].astype(int)

# 모든 장르를 저장할 세트와 리스트 생성
unique_genres = set()
genre_list = []

# 각 영화의 장르를 세트와 리스트에 추가하고 빈도 계산
for genres in df['genres']:
    genre_split = genres.split('|')
    unique_genres.update(genre_split)  # 세트에 추가
    genre_list.extend(genre_split)  # 리스트에 추가

# 각 장르의 빈도를 계산
genre_counts = Counter(genre_list)

# 장르 빈도순으로 정렬
sorted_genre_counts = dict(sorted(genre_counts.items(), key=lambda x: x[1], reverse=True))

# 파이차트 장르 한글로 번역화
genre_translation = {
    'Drama': '드라마', 'Romance': '로맨스', 'Comedy': '코미디', 'Crime': '범죄', 'Film-Noir': '누와르',
    'Thriller': '스릴러', 'War': '전쟁', 'Adventure': '모험', 'Musical': '뮤지컬', 'Mystery': '미스터리',
    'Horror': '공포', 'Western': '서부극', 'Action': '액션', 'Sci-Fi': 'SF', 'Fantasy': '판타지',
    'Children': '아동', 'Animation': '애니메이션', 'Documentary': '다큐멘터리', 'IMAX': '아이맥스'
}
genres_ko = [genre_translation.get(genre, genre) for genre in sorted_genre_counts.keys()]
counts = list(sorted_genre_counts.values())


# 파이 차트 설정
plt.rc('font', family='AppleGothic')  
plt.figure(figsize=(60, 10))
plt.title('1902년부터 2015년까지 영화 장르 분포')

# 파이 차트 생성
plt.pie(counts, labels=genres_ko, autopct='%1.1f%%', pctdistance= 0.9, startangle=0)
plt.show()









