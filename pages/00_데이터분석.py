import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI별 국가 순위", page_icon="🌍")

st.title("🌍 MBTI 유형이 가장 많은 국가 Top 10")
st.write("아래에서 MBTI 유형을 선택하면, 해당 성격 유형이 가장 높은 비율로 나타나는 국가 10개를 시각화해줍니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 유형 리스트
mbti_types = [
    "INFJ", "ISFJ", "INTP", "ISFP", "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP", "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# 사용자 선택
selected_mbti = st.selectbox("🔎 MBTI 유형을 선택하세요:", mbti_types)

# Top 10 국가 추출
top10 = df[["Country", selected_mbti]].sort_values(by=selected_mbti, ascending=False).head(10)

# Altair 차트 생성
chart = alt.Chart(top10).mark_bar().encode(
    x=alt.X(selected_mbti, title=f"{selected_mbti} 비율", scale=alt.Scale(domain=[0, top10[selected_mbti].max()*1.1])),
    y=alt.Y("Country", sort='-x', title="국가"),
    tooltip=["Country", selected_mbti]
).properties(
    width=600,
    height=400,
    title=f"Top 10 Countries with Highest Proportion of {selected_mbti}"
)

st.altair_chart(chart, use_container_width=True)
