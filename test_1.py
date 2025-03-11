import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 다국어 번역 딕셔너리
translations = {
    "ko": {
        "password_prompt": "비밀번호를 입력하세요",
        "password_error": "비밀번호가 올바르지 않습니다.",
        "title": "결근율 대시보드",
        "description": "엑셀 파일의 각 시트를 활용한 대시보드입니다. 사이드바에서 원하는 시트를 선택해보세요.",
        "page_select": "페이지 선택",
        "detail": "Detail 데이터",
        "team_summary1": "팀 요약 1",
        "team_summary2": "팀 요약 2",
        "select_language": "언어 선택"
    },
    "en": {
        "password_prompt": "Enter the password",
        "password_error": "Incorrect password.",
        "title": "Absence Rate Dashboard",
        "description": "This dashboard utilizes each sheet of the Excel file. Please select the desired sheet from the sidebar.",
        "page_select": "Select Page",
        "detail": "Detail Data",
        "team_summary1": "Team Summary 1",
        "team_summary2": "Team Summary 2",
        "select_language": "Select Language"
    },
    "vi": {
        "password_prompt": "Nhập mật khẩu",
        "password_error": "Mật khẩu không chính xác.",
        "title": "Bảng điều khiển tỷ lệ vắng mặt",
        "description": "Bảng điều khiển này sử dụng từng sheet của file Excel. Hãy chọn sheet mà bạn muốn từ thanh bên.",
        "page_select": "Chọn trang",
        "detail": "Dữ liệu Detail",
        "team_summary1": "Tóm tắt đội 1",
        "team_summary2": "Tóm tắt đội 2",
        "select_language": "Chọn ngôn ngữ"
    }
}

# 사이드바에 언어 선택 추가
language_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
selected_language_name = st.sidebar.selectbox("Select Language / 언어 선택 / Chọn ngôn ngữ", list(language_options.keys()))
lang_code = language_options[selected_language_name]
t = translations[lang_code]

# 비밀번호 입력 (비밀번호: hwkqip)
password = st.text_input(t["password_prompt"], type="password")
if password != "hwkqip":
    st.error(t["password_error"])
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

# 엑셀 데이터 불러오기
detail_df, team1_df, team2_df = load_data()

# 대시보드 타이틀 및 설명
st.title(t["title"])
st.write(t["description"])

# 페이지(시트) 선택
pages = {
    t["detail"]: "Detail",
    t["team_summary1"]: "team summary1",
    t["team_summary2"]: "team summary2"
}
selected_page = st.sidebar.radio(t["page_select"], list(pages.keys()))
sheet_name = pages[selected_page]

# 선택한 시트의 테이블만 표시
if sheet_name == "Detail":
    st.header(t["detail"])
    st.dataframe(detail_df)
elif sheet_name == "team summary1":
    st.header(t["team_summary1"])
    st.dataframe(team1_df)
elif sheet_name == "team summary2":
    st.header(t["team_summary2"])
    st.dataframe(team2_df)
