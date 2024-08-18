import pandas as pd
from collections import Counter
import re

# 카카오톡 채팅방 대화 내용 CSV 파일 로드
file_path = ''  # CSV 파일 경로
df = pd.read_csv(file_path)

# 1. 각 사용자가 보낸 메시지 비율 계산
user_message_counts = df['User'].value_counts()
total_messages = len(df)
user_message_proportions = (user_message_counts / total_messages) * 100

# 메시지 비율을 백분율 형식으로 출력
user_message_proportions_percentage = user_message_proportions.round(2).astype(str) + '%'
print("User message proportions (in percentage):")
print(user_message_proportions_percentage)

# 2. 가장 자주 언급된 단어 식별
# 모든 메시지를 하나의 텍스트로 결합
all_messages = " ".join(df['Message'])

# 텍스트를 토큰화하고 비알파벳 문자 제거
words = re.findall(r'\b\w+\b', all_messages)

# 각 단어의 빈도수 계산
word_counts = Counter(words)

# 가장 빈도수가 높은 상위 50개 단어 가져오기
top_50_words = word_counts.most_common(50)

# 비율로 변환
top_50_words_proportions = [(word, count / total_messages) for word, count in top_50_words]

# 상위 50개 단어와 그 비율 출력
print("\nTop 50 most mentioned words and their proportions:")
for word, proportion in top_50_words_proportions:
    print(f"{word}: {proportion:.2%}")
