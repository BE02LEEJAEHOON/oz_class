# 데이터 분석의 핵심: Pandas

Pandas는 panel data analysis를 줄여서 표현한 것으로, 데이터 조작 및 분석을 위한 파이썬 패키지입니다. 원래는 금융 데이터 분석을 위해 만들어졌으며, 데이터 조작 및 분석을 쉽게 할 수 있는 기능을 제공합니다.

## Pandas 특징:
- DataFrame(Excel, CSV와 유사한 형태의 자료형)을 통해 테이블 형태의 데이터 다룸
- SQL과 유사한 데이터 조회, 분석, 수정이 가능
- Numpy 기반으로 개발되어 있어 대용량 데이터 처리 시 속도가 빠름

## Pandas 함수:
1. 파일 로드 및 저장:
   - `read_csv`, `read_excel`, `read_html`, `to_csv`, `to_excel`
   
2. 데이터 확인:
   - `df.shape`, `df.info`, `df.columns`, `df.dtypes`, `df.head`, `df.tail`
   
3. 값 정렬:
   - `sort_index()`: 인덱스 순서대로 정렬
   - `sort_values(by="컬럼 값")`: 지정된 컬럼 값에 따라 정렬
     - `ascending=False`: 내림차순 정렬
     
4. Null 데이터(NaN) 처리:
   - `isnull()`: 데이터의 Null 여부 확인
   - `fillna()`: Null 데이터를 다른 값으로 채움
   - `dropna()`: Null 데이터를 제거
   
5. 특정 column/row 삭제:
   - `df.drop(['column_name'], axis=1)`: 특정 컬럼 삭제
   - `df.drop(['row'])`: 특정 행 삭제
   
6. 특정 column 이름 변경:
   - `df.rename(columns={'A':'B'})`
   
7. DataFrame 2개 합치기:
   - `pd.concat([df1, df2])`
   
8. 중복 관리:
   - 중복 확인: `df.duplicated`
   - 중복 제거: `df.drop_duplicates`

## Pandas 구성:
- Series: 1차원 데이터셋으로 1개의 컬럼 값으로 구성
- DataFrame: 2차원 데이터셋으로 컬럼과 행으로 구성
- Index: Series와 DataFrame의 고유한 키 값

## 기술 통계 (Descriptive Statistics):
- 변수의 평균, 표준편차, 최댓값, 최솟값 등을 보고자 할 때 사용하는 분석
- Pandas를 통해 자동으로 계산 가능

주요 기술 통계량:
- `count`: null을 제외한 데이터 개수
- `min`, `max`: 최솟값, 최댓값
- `sum`: 합
- `cumprod`: 누적합
- `mean`: 평균값
- `median`: 중앙값
- `quantile`: 분위수
- `var`: 표본분산
- `std`: 표준편차
- `describe`: 요약통계량

평균, 분산, 표준편차는 데이터의 분포와 변동성을 나타내는 중요한 통계량입니다.

Pandas 설치 및 import:
```python
%pip install pandas
import pandas as pd
```