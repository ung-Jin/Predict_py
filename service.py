import os
import pickle
import pandas as pd
from config import MODEL_DIR



#저장한 파일 불러오기

#인코딩 객체
encoder = None
#학습된 랜덤포레스트 모델
rf_model = None
#학습에 사용한 컬럼 정보
train_col = None


with open(os.path.join(MODEL_DIR, 'sido_encoder.pkl'), 'rb') as f:
    encoder = pickle.load(f)       # 시도 원핫 인코딩 객체

with open(os.path.join(MODEL_DIR, 'rf_model.pkl'), 'rb') as f:
    rf_model = pickle.load(f)      # 학습된 랜덤포레스트 모델

with open(os.path.join(MODEL_DIR, 'train_col.pkl'), 'rb') as f:
    train_col = pickle.load(f)     # 학습에 사용한 컬럼 정보



#예측 실행 함수
def run_predict(data):
    data = {
        '연도': [data.year],
        '월': [data.month],
        '전년동월': [data.last_year],
        '냉방도일': [data.cooling],
        '난방도일': [data.heating],
        '폭염일수(일)': [data.heatwave],
        '한파일수(일)': [data.coldwave],
        '강수량(mm)': [data.rain],
        '평균습도(%)': [data.humidity],
        '시도': [data.region],
    }

    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    new_df = df.copy()

    # 시도 인코딩 (원핫: 컬럼 17개가 생김)
    encoded_cols = encoder.get_feature_names_out(['시도'])
    new_df[encoded_cols] = encoder.transform(df[['시도']])

    # 시도 컬럼 삭제
    new_df.drop(columns=['시도'], inplace=True)

    # 학습 때 컬럼 순서로 맞추기 (train_col 사용)
    new_df = new_df[train_col]

    predict_data = rf_model.predict(new_df)

    result = float(predict_data[0])

    return result