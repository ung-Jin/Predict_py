from pydantic import BaseModel

class PredictRequest(BaseModel):
    region: str        # 시도명 (예: 경기도)
    year: int
    month: int
    last_year: int     # 전년동월 사용량
    cooling: float     # 냉방도일
    heating: float     # 난방도일
    heatwave: float    # 폭염일수
    coldwave: float    # 한파일수
    rain: float        # 강수량
    humidity: float    # 평균습도