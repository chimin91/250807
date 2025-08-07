import streamlit as st

# 제목
st.title("🎓 MBTI 기반 고등학생 진로 추천 서비스 💡")

# 설명
st.markdown("당신의 **MBTI 유형**을 선택하면, 그에 어울리는 **추천 진로와 이유**를 알려드릴게요! 😎")
st.markdown("---")

# MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
mbti = st.selectbox("📌 당신의 MBTI는 무엇인가요?", mbti_list)

# 진로 추천 딕셔너리
career_dict = {
    "INTJ": {
        "career": ["데이터 과학자 🧠", "전략 컨설턴트 📊"],
        "reason": "논리적이고 미래지향적인 INTJ는 복잡한 문제를 분석하고 전략을 세우는 데 탁월해요. 💡"
    },
    "INTP": {
        "career": ["연구원 🔬", "개발자 💻"],
        "reason": "창의적이고 독창적인 사고를 하는 INTP는 새로운 아이디어를 탐구하는 데 큰 즐거움을 느낍니다. 🚀"
    },
    "ENTJ": {
        "career": ["CEO 🏢", "프로젝트 매니저 📈"],
        "reason": "리더십과 실행력이 강한 ENTJ는 조직을 이끌고 목표를 달성하는 데 강점을 지녀요. 🧭"
    },
    "ENTP": {
        "career": ["스타트업 창업자 🚀", "마케팅 기획자 📣"],
        "reason": "호기심 많고 아이디어 뱅크인 ENTP는 새로운 것을 시도하고 도전하는 데 뛰어납니다. 🎯"
    },
    "INFJ": {
        "career": ["상담사 🧘", "작가 ✍️"],
        "reason": "깊은 통찰과 공감을 가진 INFJ는 사람을 돕는 직업에 잘 어울려요. 💞"
    },
    "INFP": {
        "career": ["예술가 🎨", "심리상담가 🧠"],
        "reason": "감수성이 풍부하고 이상적인 INFP는 내면의 가치를 표현하고 사람을 이해하는 데 관심이 많습니다. 🌈"
    },
    "ENFJ": {
        "career": ["교사 👩‍🏫", "HR 매니저 🤝"],
        "reason": "타인을 이끌고 도와주는 데 탁월한 ENFJ는 교육과 조직관리 분야에서 빛을 발해요. 🌟"
    },
    "ENFP": {
        "career": ["홍보 전문가 📢", "콘텐츠 크리에이터 🎥"],
        "reason": "자유롭고 열정적인 ENFP는 사람과 소통하며 창의적인 콘텐츠를 만드는 데 탁월합니다. 🌟"
    },
    "ISTJ": {
        "career": ["공무원 🏛️", "회계사 🧾"],
        "reason": "책임감 있고 철저한 ISTJ는 안정적인 직업에서 강한 성과를 내요. ✅"
    },
    "ISFJ": {
        "career": ["간호사 🏥", "도서관 사서 📚"],
        "reason": "섬세하고 헌신적인 ISFJ는 남을 도와주는 분야에서 안정감 있게 일할 수 있어요. 🤗"
    },
    "ESTJ": {
        "career": ["경영자 🏢", "군인]()
