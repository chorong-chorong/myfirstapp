import streamlit as st
import altair as alt
import pandas as pd
import os # 파일 경로를 다루기 위해 os 모듈 임포트

st.set_page_config(layout="wide")

st.title("MBTI 유형별 국가 분포 분석")
st.markdown("특정 MBTI 유형이 가장 많이 나타나는 국가 상위 10개를 시각화합니다.")

# CSV 파일 경로 설정
# 현재 스크립트가 실행되는 디렉토리를 기준으로 파일 경로를 찾습니다.
# Streamlit 클라우드에 배포 시, 이 파일은 GitHub 리포지토리의 루트나 지정된 위치에 있어야 합니다.
file_path = "countriesMBTI_16types.csv"

# CSV 파일 로드
try:
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        # MBTI 유형 컬럼 확인 및 선택
        # 'country' 또는 'Country' 컬럼을 제외한 나머지를 MBTI 유형으로 간주
        mbti_types = [col for col in df.columns if col.lower() not in ['country', 'gdp', 'population']]
        # 만약 컬럼에 GDP, Population 등 다른 통계값이 있다면 함께 제외하는 것이 좋습니다.
        # 정확한 컬럼 이름을 모른다면, 사용자에게 선택하도록 하거나, 휴리스틱을 더 강화할 수 있습니다.
        
        if not mbti_types:
            st.error("MBTI 유형으로 보이는 컬럼을 찾을 수 없습니다. 파일의 컬럼 이름을 확인해주세요.")
            st.stop()

        selected_mbti = st.selectbox("분석할 MBTI 유형을 선택하세요:", mbti_types)

        if selected_mbti:
            # 선택된 MBTI 유형을 기준으로 내림차순 정렬하여 상위 10개 국가 추출
            # 'country' 또는 'Country' 컬럼 중 존재하는 것을 사용
            country_col = None
            if 'country' in df.columns:
                country_col = 'country'
            elif 'Country' in df.columns:
                country_col = 'Country'
            
            if country_col is None:
                st.error("국가 이름을 포함하는 'country' 또는 'Country' 컬럼을 찾을 수 없습니다. 파일의 컬럼 이름을 확인해주세요.")
                st.stop()

            top_10_countries = df.nlargest(10, selected_mbti)[[country_col, selected_mbti]]

            st.subheader(f"'{selected_mbti}' MBTI 유형이 가장 많은 국가 Top 10")
            st.dataframe(top_10_countries.reset_index(drop=True))

            # Altair를 이용한 시각화
            chart = alt.Chart(top_10_countries).mark_bar().encode(
                x=alt.X(selected_mbti, title=f"{selected_mbti} 비율 (%)", axis=alt.Axis(format='.1f')), # 소수점 한자리까지 표시
                y=alt.Y(country_col, sort='-x', title="국가"),
                tooltip=[country_col, alt.Tooltip(selected_mbti, format=".2f")] # 툴팁에 소수점 두자리까지 표시
            ).properties(
                title=f"'{selected_mbti}' MBTI 유형 상위 10개 국가"
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("MBTI 유형을 선택해주세요.")
    else:
        st.error(f"'{file_path}' 파일을 찾을 수 없습니다. 파일이 이 코드와 같은 디렉토리에 있는지 확인해주세요.")
        st.info("Streamlit 클라우드에 배포하는 경우, 이 CSV 파일이 GitHub 리포지토리에 함께 커밋되어야 합니다.")

except Exception as e:
    st.error(f"데이터를 처리하는 중 오류가 발생했습니다: {e}")
    st.warning("파일 형식이 올바른지 확인하거나, 필요한 경우 개발자에게 문의해주세요.")
