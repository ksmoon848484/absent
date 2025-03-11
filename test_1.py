import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 비밀번호 입력 기능
password = st.text_input("비밀번호를 입력하세요", type="password")
if password != "hwkqip":
    st.error("비밀번호가 올바르지 않습니다.")
    st.stop()

# 데이터 로딩 함수 (캐시 사용)
@st.cache_data
def load_data():
    file_path = 'aggregated_absence_rate_by_group.xlsx'
    xls = pd.ExcelFile(file_path)
    detail = pd.read_excel(xls, sheet_name='Detail')
    team1 = pd.read_excel(xls, sheet_name='team summary1')
    team2 = pd.read_excel(xls, sheet_name='team summary2')
    return detail, team1, team2

# 데이터 불러오기
detail_df, team1_df, team2_df = load_data()

# 대시보드 타이틀
st.title("결근율 대시보드")
st.write("엑셀 파일의 각 시트를 활용한 대시보드입니다. 사이드바에서 원하는 시트를 선택해보세요.")

# 사이드바 네비게이션
page = st.sidebar.radio("페이지 선택", ["Detail", "Team Summary 1", "Team Summary 2"])

# 페이지별 내용 구성
if page == "Detail":
    st.header("Detail 데이터")
    st.dataframe(detail_df)
    st.subheader("결근율 분포")
    # 예시: 히스토그램 시각화 (컬럼 이름은 실제 데이터에 맞게 수정)
    if "결근율" in detail_df.columns:
        fig, ax = plt.subplots()
        ax.hist(detail_df["결근율"].dropna(), bins=20)
        ax.set_xlabel("결근율")
        ax.set_ylabel("빈도")
        st.pyplot(fig)
        
elif page == "Team Summary 1":
    st.header("Team Summary 1")
    st.dataframe(team1_df)
    st.subheader("팀별 평균 결근율")
    # 예시: 막대 차트 (컬럼 이름은 실제 데이터에 맞게 수정)
    if "팀" in team1_df.columns and "평균 결근율" in team1_df.columns:
        fig, ax = plt.subplots()
        ax.bar(team1_df["팀"], team1_df["평균 결근율"])
        ax.set_xlabel("팀")
        ax.set_ylabel("평균 결근율")
        st.pyplot(fig)

elif page == "Team Summary 2":
    st.header("Team Summary 2")
    st.dataframe(team2_df)
    st.subheader("팀별 데이터 비교")
    # 예시: 다른 유형의 시각화 (컬럼 이름은 실제 데이터에 맞게 수정)
    if "팀" in team2_df.columns and "결근율" in team2_df.columns:
        fig, ax = plt.subplots()
        ax.plot(team2_df["팀"], team2_df["결근율"], marker='o')
        ax.set_xlabel("팀")
        ax.set_ylabel("결근율")
        st.pyplot(fig)
