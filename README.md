# mulcamp-miniproject
# 프로젝트의 목적
- 본 프로젝트는 서울시 부동산 데이터를 활용하여 대시보드를 개발하는 목적은 부동산 시장 동향을 시각화하고 사용자에게 부동산 투자 결정을 돕기 위함입니다. 이를 통해 사용자는 시장 개요, 가격 및 지역별 동향, 재건축 예측 및 서울시 부동산 시장의 트렌드를 쉽게 파악하고 흐름을 파악할 수 있습니다.

## 팀원 소개
-  김수현 : https://github.com/suhyeon0325
-  송민 : https://github.com/ms2063
-  송준호 : https://github.com/Kongalmengi
-  임예원 : https://github.com/dsmondo
-  한대희 : https://github.com/roklp


# 본 프로젝트에서 사용한 주요 개발환경 요약 
  + Programming Languages : Python(ver. 3.13)
  + Web Framework : Streamlit (ver. 1.31.0)

## 주요 라이브러리 버전
  + [requirements.txt](requirements.txt) 파일 참조

# 데모페이지
- Streamlit에서 구현한 Demo는 다음과 같습니다.
  + [https://app-api-qkxzk2zdlacnuwxcqwxyyq.streamlit.app/](https://mulcamp-miniproject-tsxpry9q44xmqu4hrbtrtj.streamlit.app/)

 ## 주요 기능
 - 본 프로젝트에서 자체 개발 및 활용한 주요 메서드는 다음과 같습니다.

- **`load_data(filepath)`**: 주어진 파일 경로에서 CSV 데이터를 로드합니다. 이 함수는 pandas를 사용하여 데이터를 읽고 DataFrame으로 반환합니다.
- **`type_scatter(df, house_type)`**: 선택된 부동산 유형에 따라 건물 면적과 매매 가격 사이의 관계를 scatter plot으로 보여줍니다. Plotly를 사용하여 시각화합니다.
- **`type_mean(df, year, month, housing_type)`**: 지정된 년도와 월, 그리고 부동산 유형에 따라 자치구별 매매 가격의 평균을 bar chart로 시각화합니다.
- **`house_price_trend(df, sgg_nms, house_type)`**: 선택된 자치구명과 부동산 유형에 따른 거래 가격의 변동 추이를 line chart로 보여줍니다.
- **`main()`**: 사용자 인터페이스를 통해 분석 유형을 선택하고, 해당 분석에 필요한 데이터를 시각화합니다. 이 함수는 Streamlit을 사용하여 대시보드를 구성합니다.

# 발표자료 PDF 
- 발표자료 PDF는 아래와 같습니다.
  + [서울_부동산_시장_인사이트_대시보드.pdf](서울_부동산_시장_인사이트_대시보드.pdf)

# Release Notes
- 개발 릴리스 노트는 `Releases` 클릭하여 확인하여 주시기를 바랍니다.


# License
- 이 프로젝트는 [MIT Licence](LICENSE)에 따라 라이센스가 부여됩니다.