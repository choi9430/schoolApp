import streamlit as st
import itertools

# 앱 제목
st.title("수행 평가 점수 계산기")

# 영역 점수 입력 받기
st.subheader("각 영역의 가능한 배점을 입력하세요")

# 영역 이름 목록
areas = ["영역1", "영역2", "영역3", "영역4", "영역5"]

# 각 영역에 대해 사용자에게 배점 입력
area_scores = {}
for area in areas:
    # 각 영역마다 사용자에게 가능한 배점을 입력하도록 요청
    score_input = st.text_input(f"{area}의 가능한 배점을 입력하세요 (쉼표로 구분):", "")
    area_scores[area] = score_input

# 각 영역에 대해 점수 선택
scores = {}
for area, score_list in area_scores.items():
    # 쉼표로 구분된 값을 리스트로 변환
    possible_scores = [int(x) for x in score_list.split(",") if x.strip().isdigit()]
    if possible_scores:  # 유효한 배점이 있는 경우에만
        scores[area] = possible_scores

# 합계 가능 점수 계산 버튼
if st.button("합계 가능 점수"):
    # 모든 가능 점수를 저장할 집합
    possible_sums = set()

    # 각 영역의 점수 조합 계산
    score_combinations = list(itertools.product(*scores.values()))  # 각 영역 점수의 Cartesian product
    for combination in score_combinations:
        possible_sums.add(sum(combination))  # 각 조합의 합계를 추가

    possible_sums = sorted(possible_sums)  # 정렬하여 출력
    st.subheader("가능한 합계 점수 리스트")
    st.write(possible_sums)

# 사용자 친화적인 메시지
st.write("※ 각 영역의 가능한 배점은 쉼표로 구분하여 입력해야 합니다.")