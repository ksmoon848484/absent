# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # 다국어 번역 딕셔너리
# translations = {
#     "ko": {
#         "password_prompt": "비밀번호를 입력하세요",
#         "password_error": "비밀번호가 올바르지 않습니다.",
#         "title": "결근율 대시보드",
#         "description": "엑셀 파일의 각 시트를 활용한 대시보드입니다. 사이드바에서 원하는 시트를 선택해보세요.",
#         "page_select": "페이지 선택",
#         "detail": "Detail 데이터",
#         "detail_distribution": "결근율 분포",
#         "team_summary1": "팀 요약 1",
#         "team_summary1_average": "팀별 평균 결근율",
#         "team_summary2": "팀 요약 2",
#         "team_summary2_comparison": "팀별 데이터 비교",
#         "select_language": "언어 선택"
#     },
#     "en": {
#         "password_prompt": "Enter the password",
#         "password_error": "Incorrect password.",
#         "title": "Absence Rate Dashboard",
#         "description": "This dashboard utilizes each sheet of the Excel file. Please select the desired sheet from the sidebar.",
#         "page_select": "Select Page",
#         "detail": "Detail Data",
#         "detail_distribution": "Absence Rate Distribution",
#         "team_summary1": "Team Summary 1",
#         "team_summary1_average": "Average Absence Rate by Team",
#         "team_summary2": "Team Summary 2",
#         "team_summary2_comparison": "Team Data Comparison",
#         "select_language": "Select Language"
#     },
#     "vi": {
#         "password_prompt": "Nhập mật khẩu",
#         "password_error": "Mật khẩu không chính xác.",
#         "title": "Bảng điều khiển tỷ lệ vắng mặt",
#         "description": "Bảng điều khiển này sử dụng từng sheet của file Excel. Hãy chọn sheet mà bạn muốn từ thanh bên.",
#         "page_select": "Chọn trang",
#         "detail": "Dữ liệu Detail",
#         "detail_distribution": "Phân bố tỷ lệ vắng mặt",
#         "team_summary1": "Tóm tắt đội 1",
#         "team_summary1_average": "Tỷ lệ vắng mặt trung bình theo đội",
#         "team_summary2": "Tóm tắt đội 2",
#         "team_summary2_comparison": "So sánh dữ liệu theo đội",
#         "select_language": "Chọn ngôn ngữ"
#     }
# }

# # 사이드바에 언어 선택 추가
# language_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
# selected_language_name = st.sidebar.selectbox("Select Language / 언어 선택 / Chọn ngôn ngữ", list(language_options.keys()))
# lang_code = language_options[selected_language_name]
# t = translations[lang_code]

# # 비밀번호 입력 (비밀번호: hwkqip)
# password = st.text_input(t["password_prompt"], type="password")
# if password != "hwkqip":
#     st.error(t["password_error"])
#     st.stop()

# # 데이터 로딩 함수 (캐시 사용)
# @st.cache_data
# def load_data():
#     file_path = 'aggregated_absence_rate_by_group.xlsx'
#     xls = pd.ExcelFile(file_path)
#     detail = pd.read_excel(xls, sheet_name='Detail')
#     team1 = pd.read_excel(xls, sheet_name='team summary1')
#     team2 = pd.read_excel(xls, sheet_name='team summary2')
#     return detail, team1, team2

# # 엑셀 데이터 불러오기
# detail_df, team1_df, team2_df = load_data()

# # 대시보드 타이틀 및 설명
# st.title(t["title"])
# st.write(t["description"])

# # 페이지(시트) 선택
# pages = {
#     t["detail"]: "Detail",
#     t["team_summary1"]: "team summary1",
#     t["team_summary2"]: "team summary2"
# }
# selected_page = st.sidebar.radio(t["page_select"], list(pages.keys()))
# sheet_name = pages[selected_page]

# # 각 페이지별 데이터 및 시각화 표시
# if sheet_name == "Detail":
#     st.header(t["detail"])
#     st.dataframe(detail_df)
#     st.subheader(t["detail_distribution"])
#     # 예시: '결근율' 컬럼을 기준으로 히스토그램 시각화 (컬럼명이 실제와 다를 경우 수정 필요)
#     if "결근율" in detail_df.columns:
#         fig, ax = plt.subplots()
#         ax.hist(detail_df["결근율"].dropna(), bins=20)
#         ax.set_xlabel("결근율")
#         ax.set_ylabel("빈도")
#         st.pyplot(fig)
        
# elif sheet_name == "team summary1":
#     st.header(t["team_summary1"])
#     st.dataframe(team1_df)
#     st.subheader(t["team_summary1_average"])
#     # 예시: '팀'과 '평균 결근율' 컬럼을 활용한 막대 차트 (컬럼명이 실제와 다를 경우 수정 필요)
#     if "팀" in team1_df.columns and "평균 결근율" in team1_df.columns:
#         fig, ax = plt.subplots()
#         ax.bar(team1_df["팀"], team1_df["평균 결근율"])
#         ax.set_xlabel("팀")
#         ax.set_ylabel("평균 결근율")
#         st.pyplot(fig)

# elif sheet_name == "team summary2":
#     st.header(t["team_summary2"])
#     st.dataframe(team2_df)
#     st.subheader(t["team_summary2_comparison"])
#     # 예시: '팀'과 '결근율' 컬럼을 활용한 선 그래프 (컬럼명이 실제와 다를 경우 수정 필요)
#     if "팀" in team2_df.columns and "결근율" in team2_df.columns:
#         fig, ax = plt.subplots()
#         ax.plot(team2_df["팀"], team2_df["결근율"], marker='o')
#         ax.set_xlabel("팀")
#         ax.set_ylabel("결근율")
#         st.pyplot(fig)




    
#     # 상위 5 데이터 및 시각화 (예: AREA 컬럼을 레이블로 사용)
#     show_top5(team2_df, "Absence Rate (%)", label_col="AREA")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

##############################################
# 1. 다국어 번역 딕셔너리
##############################################
translations = {
    "ko": {
        "password_prompt": "비밀번호를 입력하세요",
        "password_error": "비밀번호가 올바르지 않습니다.",
        "title": "결근율 대시보드",
        "description": "엑셀 파일의 각 시트를 활용한 대시보드입니다. 사이드바에서 원하는 시트를 선택해보세요.",
        "page_select": "페이지 선택",
        "detail": "Detail 데이터",
        "detail_distribution": "결근율 분포",
        "team_summary1": "팀 요약 1",
        "team_summary1_average": "팀별 평균 결근율",
        "team_summary2": "팀 요약 2",
        "team_summary2_comparison": "팀별 데이터 비교",
        "select_language": "언어 선택"
    },
    "en": {
        "password_prompt": "Enter the password",
        "password_error": "Incorrect password.",
        "title": "Absence Rate Dashboard",
        "description": "This dashboard utilizes each sheet of the Excel file. Please select the desired sheet from the sidebar.",
        "page_select": "Select Page",
        "detail": "Detail Data",
        "detail_distribution": "Absence Rate Distribution",
        "team_summary1": "Team Summary 1",
        "team_summary1_average": "Average Absence Rate by Team",
        "team_summary2": "Team Summary 2",
        "team_summary2_comparison": "Team Data Comparison",
        "select_language": "Select Language"
    },
    "vi": {
        "password_prompt": "Nhập mật khẩu",
        "password_error": "Mật khẩu không chính xác.",
        "title": "Bảng điều khiển tỷ lệ vắng mặt",
        "description": "Bảng điều khiển này sử dụng từng sheet của file Excel. Hãy chọn sheet mà bạn muốn từ thanh bên.",
        "page_select": "Chọn trang",
        "detail": "Dữ liệu Detail",
        "detail_distribution": "Phân bố tỷ lệ vắng mặt",
        "team_summary1": "Tóm tắt đội 1",
        "team_summary1_average": "Tỷ lệ vắng mặt trung bình theo đội",
        "team_summary2": "Tóm tắt đội 2",
        "team_summary2_comparison": "So sánh dữ liệu theo đội",
        "select_language": "Chọn ngôn ngữ"
    }
}

##############################################
# 2. 사이드바: 언어 선택 및 비밀번호 보호
##############################################
language_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
selected_language_name = st.sidebar.selectbox("Select Language / 언어 선택 / Chọn ngôn ngữ", list(language_options.keys()))
lang_code = language_options[selected_language_name]
t = translations[lang_code]

password = st.text_input(t["password_prompt"], type="password")
if password != "hwkqip":
    st.error(t["password_error"])
    st.stop()

##############################################
# 3. 데이터 로딩 및 전처리 (엑셀 파일 내 "Absence Rate (%)" 컬럼 숫자형 변환)
##############################################
@st.cache_data
def load_data():
    file_path = 'aggregated_absence_rate_by_group.xlsx'
    xls = pd.ExcelFile(file_path)
    detail = pd.read_excel(xls, sheet_name='Detail')
    team1 = pd.read_excel(xls, sheet_name='team summary1')
    team2 = pd.read_excel(xls, sheet_name='team summary2')
    
    # "Absence Rate (%)" 컬럼을 숫자형으로 변환하는 함수
    def convert_absence_rate(df, col_name="Absence Rate (%)"):
        if col_name in df.columns:
            df[col_name] = df[col_name].astype(str).str.replace("%", "", regex=False)
            df[col_name] = pd.to_numeric(df[col_name], errors="coerce")
        return df

    detail = convert_absence_rate(detail, "Absence Rate (%)")
    team1 = convert_absence_rate(team1, "Absence Rate (%)")
    team2 = convert_absence_rate(team2, "Absence Rate (%)")
    
    return detail, team1, team2

detail_df, team1_df, team2_df = load_data()

##############################################
# 4. 개선된 KPI 카드 함수 (더 디테일한 통계 지표 제공)
##############################################
def show_detailed_kpi(df, rate_col: str):
    if rate_col in df.columns:
        mean_val = df[rate_col].mean()
        median_val = df[rate_col].median()
        std_val = df[rate_col].std()
        max_val = df[rate_col].max()
        min_val = df[rate_col].min()
        count_val = df[rate_col].count()

        # 첫 번째 행: 평균, 중앙값, 표준편차
        col1, col2, col3 = st.columns(3)
        col1.metric("Mean Absence Rate", f"{mean_val:.2f}%")
        col2.metric("Median Absence Rate", f"{median_val:.2f}%")
        col3.metric("Std. Deviation", f"{std_val:.2f}")

        # 두 번째 행: 최대, 최소, 데이터 건수
        col4, col5, col6 = st.columns(3)
        col4.metric("Max Absence Rate", f"{max_val:.2f}%")
        col5.metric("Min Absence Rate", f"{min_val:.2f}%")
        col6.metric("Total Records", f"{count_val}")
    else:
        st.warning(f"Column '{rate_col}' not found in the DataFrame.")

##############################################
# 5. 대시보드 기본 UI: 타이틀, 설명, 페이지(시트) 선택
##############################################
st.title(t["title"])
st.write(t["description"])

pages = {
    t["detail"]: "Detail",
    t["team_summary1"]: "team summary1",
    t["team_summary2"]: "team summary2"
}
selected_page = st.sidebar.radio(t["page_select"], list(pages.keys()))
sheet_name = pages[selected_page]

##############################################
# 6. 각 시트별 데이터 및 시각화
##############################################
if sheet_name == "Detail":
    st.header(t["detail"])
    # KPI 카드: "Absence Rate (%)"에 대한 자세한 통계
    show_detailed_kpi(detail_df, "Absence Rate (%)")
    st.dataframe(detail_df)
    st.subheader(t["detail_distribution"])
    if "Absence Rate (%)" in detail_df.columns:
        fig, ax = plt.subplots()
        ax.hist(detail_df["Absence Rate (%)"].dropna(), bins=20)
        ax.set_xlabel("Absence Rate (%)")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

elif sheet_name == "team summary1":
    st.header(t["team_summary1"])
    show_detailed_kpi(team1_df, "Absence Rate (%)")
    st.dataframe(team1_df)
    st.subheader(t["team_summary1_average"])
    # 예시: "팀"과 "평균 결근율" 컬럼 사용 (실제 컬럼명이 다르면 수정 필요)
    if "팀" in team1_df.columns and "평균 결근율" in team1_df.columns:
        fig, ax = plt.subplots()
        ax.bar(team1_df["팀"], team1_df["평균 결근율"])
        ax.set_xlabel("팀")
        ax.set_ylabel("평균 결근율")
        st.pyplot(fig)

elif sheet_name == "team summary2":
    st.header(t["team_summary2"])
    show_detailed_kpi(team2_df, "Absence Rate (%)")
    st.dataframe(team2_df)
    st.subheader(t["team_summary2_comparison"])
    # 예시: "팀"과 "결근율" 컬럼 사용 (실제 컬럼명이 다르면 수정 필요)
    if "팀" in team2_df.columns and "결근율" in team2_df.columns:
        fig, ax = plt.subplots()
        ax.plot(team2_df["팀"], team2_df["결근율"], marker='o')
        ax.set_xlabel("팀")
        ax.set_ylabel("결근율")
        st.pyplot(fig)


