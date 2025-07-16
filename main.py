import streamlit as st

st.set_page_config(page_title="MBTI 한국 배우 추천기 🎬", page_icon="🎭")

st.title("🎭 MBTI별 어울리는 한국 배우 추천기")
st.write("당신의 MBTI를 선택하면, 어울릴 것 같은 한국 배우 3명을 추천해드릴게요! 🎬")

# MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 한국 배우와 이미지 URL
mbti_actors = {
    "INTJ": [
        ("설경구", "https://upload.wikimedia.org/wikipedia/commons/d/db/Seol_Gyeong-gu_at_BIFF_2016.jpg"),
        ("김혜수", "https://upload.wikimedia.org/wikipedia/commons/b/bc/Kim_Hye-soo_in_2018.jpg"),
        ("이선균", "https://upload.wikimedia.org/wikipedia/commons/0/05/Lee_Sun-kyun_BIFF_2016.jpg")
    ],
    "INFP": [
        ("이제훈", "https://upload.wikimedia.org/wikipedia/commons/e/e5/Lee_Je-hoon_in_2017.jpg"),
        ("박보영", "https://upload.wikimedia.org/wikipedia/commons/d/d9/Park_Bo-young_in_July_2018.png"),
        ("이종석", "https://upload.wikimedia.org/wikipedia/commons/4/4a/Lee_Jong-suk_at_Asia_Artist_Awards_2017.png")
    ],
    "ENTP": [
        ("유재석", "https://upload.wikimedia.org/wikipedia/commons/f/f1/Yoo_Jae-suk_from_acrofan.jpg"),
        ("전지현", "https://upload.wikimedia.org/wikipedia/commons/e/ed/Jun_Ji-hyun_at_the_%2710_Asia_Song_Festival.jpg"),
        ("조정석", "https://upload.wikimedia.org/wikipedia/commons/5/56/Jo_Jung-suk_in_2017.jpg")
    ],
    "ISFP": [
        ("정우성", "https://upload.wikimedia.org/wikipedia/commons/f/f6/Jung_Woo-sung_at_the_2020_Blue_Dragon_Awards.png"),
        ("수지", "https://upload.wikimedia.org/wikipedia/commons/d/d3/Suzy_at_a_fan_meeting_in_2017.png"),
        ("박서준", "https://upload.wikimedia.org/wikipedia/commons/6/6f/Park_Seo-joon_in_2019.jpg")
    ]
    # 나머지 MBTI는 필요 시 추가 가능
}

# 사용자 입력
selected_mbti = st.selectbox("👇 당신의 MBTI를 골라주세요", mbti_list)

if selected_mbti:
    st.subheader(f"🎬 {selected_mbti} 타입에게 어울리는 한국 배우")
    if selected_mbti in mbti_actors:
        for name, img_url in mbti_actors[selected_mbti]:
            st.image(img_url, width=200, caption=name)
        
        # 🎈 풍선 효과
        st.balloons()
    else:
        st.info("해당 MBTI에 대한 배우 추천은 아직 준비 중이에요. 다음 업데이트를 기대해주세요! 🚧")

st.write("---")
st.markdown("💡 배우 추천은 재미로만 봐주세요! 더 잘 어울릴 것 같은 배우가 있다면 의견 주세요 😉")
