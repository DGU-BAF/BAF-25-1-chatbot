import pandas as pd
import re


# 이모티콘 및 특수문자 제거 함수
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'ㅇ', '', text) # 특수문자 제거
        text = re.sub(r'ㅁ', '', text)
        text = re.sub(r'[\U00010000-\U0010FFFF]', '', text, flags=re.UNICODE)  # 이모티콘 제거
    return text


# 데이터 불러오기
df = pd.read_csv('ONEROOM/직방데이터셋.csv', encoding = 'CP949')
df = df.astype(str).applymap(clean_text)

# 처리된 데이터 저장
df.to_csv('ONEROOM/직방데이터셋_제거.csv', index=False,encoding="utf-8-sig")
print("이모티콘과 특수문자 제거 완료!")
print(df.head())