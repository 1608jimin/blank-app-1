import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
# 기존 코드: st.title("My First App")
# 수정 코드:
st.title("🏫 우리반 알림장")
st.write("우리 반의 중요한 소식을 확인하세요!")
import streamlit as st

# --- 1. 앱 초기 설정 ---

# st.set_page_config를 사용하여 페이지 제목과 아이콘을 설정합니다.
# 이 코드는 스크립트에서 한 번만, 그리고 다른 Streamlit 명령어보다 먼저 호출되어야 합니다.
st.set_page_config(
    page_title="MBTI 학습 유형 진단",
    page_icon="🧠",
)

# --- 2. 세션 상태 초기화 ---

# st.session_state를 사용하여 사용자의 답변과 진단 결과를 저장합니다.
# 이렇게 하면 사용자가 위젯과 상호작용할 때마다 상태가 초기화되는 것을 방지할 수 있습니다.
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'mbti_result' not in st.session_state:
    st.session_state.mbti_result = ""

# --- 3. 앱 제목 및 설명 ---

st.title("🧑‍💻 MBTI 학습 유형 진단 🧠")
st.write(
    "아래의 간단한 질문들을 통해 자신의 학습 스타일과 선호하는 학습 환경을 알아보세요."
)
st.write("---")


# --- 4. MBTI 질문 및 결과 데이터 ---

# 각 MBTI 지표별 질문 목록
questions = {
    'EI': '1. 여러 사람과 함께 공부하는 것이 혼자 공부하는 것보다 더 즐겁다.',
    'SN': '2. 새로운 것을 배울 때, 실제 사례나 경험을 통해 배우는 것을 선호한다.',
    'TF': '3. 과제 수행 시, 논리적이고 객관적인 기준을 따르는 것이 중요하다.',
    'JP': '4. 학습 계획을 세울 때, 미리 체계적으로 계획을 세우고 따르는 편이다.',
    'EI_2': '5. 토론 수업에서 적극적으로 의견을 내기보다는 주로 듣는 편이다.',
    'SN_2': '6. 추상적인 이론이나 개념을 탐구하는 것에 흥미를 느낀다.',
    'TF_2': '7. 팀 프로젝트에서 동료의 감정을 고려하여 조화로운 관계를 유지하는 것이 더 중요하다.',
    'JP_2': '8. 갑작스러운 과제나 계획 변경에 유연하게 대처할 수 있다.'
}

# MBTI 유형별 학습 스타일 설명
learning_styles = {
    'ISTJ': '체계적이고 사실 기반의 학습을 선호합니다. 조용하고 질서 있는 환경에서 집중력이 높습니다.',
    'ISFJ': '구체적이고 실용적인 정보를 바탕으로 학습하며, 다른 사람을 돕는 과정에서 학습 동기가 부여됩니다.',
    'INFJ': '통찰력과 의미를 중시하며, 개념들 사이의 연관성을 파악하는 데 능숙합니다. 독립적인 학습 환경을 선호합니다.',
    'INTJ': '논리적이고 분석적인 사고를 바탕으로 복잡한 이론을 탐구하는 것을 즐깁니다. 높은 기준을 가지고 스스로 학습합니다.',
    'ISTP': '직접 경험하고 문제를 해결하는 과정에서 가장 잘 배웁니다. 유연하고 실용적인 접근 방식을 선호합니다.',
    'ISFP': '조화로운 환경에서 미적 감각과 가치를 탐구하는 학습을 즐깁니다. 협력적인 분위기에서 능률이 오릅니다.',
    'INFP': '자신의 가치와 신념에 부합하는 내용을 학습할 때 동기가 부여됩니다. 창의적이고 상상력이 풍부합니다.',
    'INTP': '논리적이고 비판적인 사고로 아이디어를 분석하는 것을 즐깁니다. 지적 호기심이 강하고 독립적인 학습을 선호합니다.',
    'ESTP': '활동적이고 경험 중심의 학습을 선호합니다. 실제 문제를 해결하며 배우는 것에 능숙합니다.',
    'ESFP': '사람들과 교류하며 재미있고 활동적인 환경에서 학습할 때 가장 효과적입니다. 실용적인 정보에 관심이 많습니다.',
    'ENFP': '열정적이고 창의적으로 다양한 가능성을 탐구하는 것을 즐깁니다. 협력적인 환경에서 아이디어를 공유하며 배웁니다.',
    'ENTP': '지적인 도전을 즐기며, 논쟁과 토론을 통해 아이디어를 발전시키는 것을 선호합니다. 복잡한 문제를 해결하는 데 능숙합니다.',
    'ESTJ': '논리적이고 체계적으로 목표를 달성하는 학습을 선호합니다. 명확한 규칙과 구조가 있는 환경에서 능률이 오릅니다.',
    'ESFJ': '다른 사람들과 협력하고 소통하며 배우는 것을 즐깁니다. 조화로운 분위기 속에서 학습 동기가 부여됩니다.',
    'ENFJ': '사람들과의 관계를 통해 배우고 성장하는 것을 중시합니다. 다른 사람을 이끌고 영감을 주며 학습 효과를 높입니다.',
    'ENTJ': '전략적이고 목표 지향적인 학습을 선호합니다. 효율적인 방식으로 지식을 습득하고 이를 실제 상황에 적용하는 데 능숙합니다.'
}

# --- 5. 질문 폼(Form) 생성 ---

# st.form을 사용하면 여러 위젯을 그룹화하고 '제출' 버튼을 한 번만 눌러 모든 입력을 처리할 수 있습니다.
# 이는 각 라디오 버튼을 클릭할 때마다 앱이 재실행되는 것을 방지해 줍니다.
with st.form("mbti_form"):
    st.subheader("아래 질문에 답변해주세요.")

    user_answers = {}
    # 질문 목록을 순회하며 라디오 버튼을 생성합니다.
    for key, question in questions.items():
        user_answers[key] = st.radio(
            question,
            ('예', '아니오'),
            key=f"q_{key}",  # 각 위젯에 고유한 key를 부여합니다.
            horizontal=True, # 버튼을 가로로 정렬합니다.
            label_visibility='collapsed' # 질문이 라벨 역할을 하므로 라벨은 숨깁니다.
        )
    
    # st.form_submit_button은 폼 내부에 위치해야 합니다.
    submitted = st.form_submit_button("결과 확인하기")


# --- 6. 결과 처리 및 표시 ---

# '결과 확인하기' 버튼이 눌렸을 때 실행될 로직
if submitted:
    st.session_state.submitted = True
    st.session_state.user_answers = user_answers

    # MBTI 지표 계산 로직
    # 각 지표별로 점수를 계산하여 최종 유형을 결정합니다.
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    # EI
    if user_answers['EI'] == '예': scores['E'] += 1
    else: scores['I'] += 1
    if user_answers['EI_2'] == '아니오': scores['E'] += 1
    else: scores['I'] += 1

    # SN
    if user_answers['SN'] == '예': scores['S'] += 1
    else: scores['N'] += 1
    if user_answers['SN_2'] == '예': scores['N'] += 1
    else: scores['S'] += 1

    # TF
    if user_answers['TF'] == '예': scores['T'] += 1
    else: scores['F'] += 1
    if user_answers['TF_2'] == '아니오': scores['T'] += 1
    else: scores['F'] += 1
    
    # JP
    if user_answers['JP'] == '예': scores['J'] += 1
    else: scores['P'] += 1
    if user_answers['JP_2'] == '아니오': scores['J'] += 1
    else: scores['P'] += 1

    # 최종 MBTI 유형 결정
    mbti = ""
    mbti += "E" if scores['E'] > scores['I'] else "I"
    mbti += "S" if scores['S'] > scores['N'] else "N"
    mbti += "T" if scores['T'] > scores['F'] else "F"
    mbti += "J" if scores['J'] > scores['P'] else "P"
    
    st.session_state.mbti_result = mbti

# 세션 상태에 결과가 있으면 (즉, 제출 버튼이 눌렸으면) 결과를 표시합니다.
if st.session_state.submitted:
    st.write("---")
    st.subheader("🎉 진단 결과")

    result = st.session_state.mbti_result
    
    # 결과가 유효한지 확인 후 표시합니다.
    if result in learning_styles:
        st.info(f"당신의 MBTI 학습 유형은 **{result}** 입니다.")
        st.write(learning_styles[result])
    else:
        st.error("결과를 계산하는 데 문제가 발생했습니다. 다시 시도해주세요.")

    # 다시 진단하기 버튼
    if st.button("다시 진단하기"):
        # 세션 상태를 초기화하여 처음부터 다시 시작할 수 있도록 합니다.
        st.session_state.submitted = False
        st.session_state.user_answers = {}
        st.session_state.mbti_result = ""
        st.rerun() # 페이지를 새로고침하여 초기 상태로 되돌립니다.
        
