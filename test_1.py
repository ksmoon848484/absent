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
#         "team_summary1": "팀 요약 1",
#         "team_summary2": "팀 요약 2",
#         "select_language": "언어 선택"
#     },
#     "en": {
#         "password_prompt": "Enter the password",
#         "password_error": "Incorrect password.",
#         "title": "Absence Rate Dashboard",
#         "description": "This dashboard utilizes each sheet of the Excel file. Please select the desired sheet from the sidebar.",
#         "page_select": "Select Page",
#         "detail": "Detail Data",
#         "team_summary1": "Team Summary 1",
#         "team_summary2": "Team Summary 2",
#         "select_language": "Select Language"
#     },
#     "vi": {
#         "password_prompt": "Nhập mật khẩu",
#         "password_error": "Mật khẩu không chính xác.",
#         "title": "Bảng điều khiển tỷ lệ vắng mặt",
#         "description": "Bảng điều khiển này sử dụng từng sheet của file Excel. Hãy chọn sheet mà bạn muốn từ thanh bên.",
#         "page_select": "Chọn trang",
#         "detail": "Dữ liệu Detail",
#         "team_summary1": "Tóm tắt đội 1",
#         "team_summary2": "Tóm tắt đội 2",
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

# # 선택한 시트의 테이블만 표시
# if sheet_name == "Detail":
#     st.header(t["detail"])
#     st.dataframe(detail_df)
# elif sheet_name == "team summary1":
#     st.header(t["team_summary1"])
#     st.dataframe(team1_df)
# elif sheet_name == "team summary2":
#     st.header(t["team_summary2"])
#     st.dataframe(team2_df)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import BytesIO

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
        "team_summary1": "팀 요약 1",
        "team_summary2": "팀 요약 2",
        "total_absent_info": "Total Absent Information",
        "select_language": "언어 선택",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "month_select": "월 선택 (2월 / 3월)"
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
        "total_absent_info": "Total Absent Information",
        "select_language": "Select Language",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "month_select": "Select Month (Feb / Mar)"
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
        "total_absent_info": "Total Absent Information",
        "select_language": "Chọn ngôn ngữ",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "month_select": "Chọn tháng (2/3)"
    }
}

##############################################
# 2. 사이드바: 언어 선택 및 비밀번호 보호
##############################################
language_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
selected_language_name = st.sidebar.selectbox(
    "Select Language / 언어 선택 / Chọn ngôn ngữ", list(language_options.keys())
)
lang_code = language_options[selected_language_name]
t = translations[lang_code]

password = st.text_input(t["password_prompt"], type="password")
if password != "hwkqip":
    st.error(t["password_error"])
    st.stop()

##############################################
# 3. requests + BytesIO를 이용해 Excel 파일 불러오기 함수
##############################################
@st.cache_data
def load_excel_from_github(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return pd.ExcelFile(BytesIO(response.content))

##############################################
# 4. 결근율 데이터 로딩 (2월/3월 Excel)
##############################################
@st.cache_data
def load_absence_data(month: str):
    """
    month: "February" 또는 "March"
    실제 GitHub Raw URL을 사용자의 경로로 변경해 주세요.
    """
    if month == "February":
        url = "https://raw.githubusercontent.com/username/repo/main/aggregated_absence_rate_by_group_Feb.xlsx"
    else:
        url = "https://raw.githubusercontent.com/username/repo/main/aggregated_absence_rate_by_group_Mar.xlsx"
    
    xls = load_excel_from_github(url)
    detail = pd.read_excel(xls, sheet_name='Detail')
    team1 = pd.read_excel(xls, sheet_name='team summary1')
    team2 = pd.read_excel(xls, sheet_name='team summary2')
    return detail, team1, team2

##############################################
# 5. Total Absent Information 로딩 (2월/3월 Excel)
##############################################
@st.cache_data
def load_total_absent_excel(month: str):
    """
    month: "February" 또는 "March"
    실제 GitHub Raw URL을 사용자의 경로로 변경해 주세요.
    """
    if month == "February":
        url = "https://raw.githubusercontent.com/username/repo/main/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Feb.xlsx"
    else:
        url = "https://raw.githubusercontent.com/username/repo/main/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Mar.xlsx"
    
    xls = load_excel_from_github(url)
    # 엑셀 파일의 첫 번째 시트를 불러온다고 가정 (필요에 따라 sheet_name 지정)
    df = pd.read_excel(xls)
    return df

##############################################
# 6. 5PRS Validation 데이터 로딩 (CSV)
##############################################
@st.cache_data
def load_5prs_data():
    """
    실제 GitHub Raw URL을 사용자의 경로로 변경해 주세요.
    """
    inspector_url = "https://raw.githubusercontent.com/username/repo/main/Inspector_summary.csv"
    tqc_id_url = "https://raw.githubusercontent.com/username/repo/main/TQC_ID_summary.csv"
    
    inspector_response = requests.get(inspector_url)
    inspector_response.raise_for_status()
    inspector_df = pd.read_csv(BytesIO(inspector_response.content))
    
    tqc_id_response = requests.get(tqc_id_url)
    tqc_id_response.raise_for_status()
    tqc_id_df = pd.read_csv(BytesIO(tqc_id_response.content))
    
    return inspector_df, tqc_id_df

##############################################
# 7. 메인 UI: 탭(Tab) 구성
##############################################
st.title(t["title"])
st.write(t["description"])

tab1, tab2 = st.tabs([t["tab1_name"], t["tab2_name"]])

###############################
# 탭 1: Absence Rate Info
###############################
with tab1:
    # (1) 2월/3월 라디오 버튼
    month_selected = st.radio(
        t["month_select"],
        ("February", "March"),
        horizontal=True
    )
    
    # (2) 결근율 데이터 로딩 (엑셀)
    detail_df, team1_df, team2_df = load_absence_data(month_selected)
    
    # (3) 페이지(시트) 선택: Detail, team summary1, team summary2, Total Absent Information
    pages = {
        t["detail"]: "Detail",
        t["team_summary1"]: "team_summary1",
        t["team_summary2"]: "team_summary2",
        t["total_absent_info"]: "total_absent_info"
    }
    selected_page = st.radio(t["page_select"], list(pages.keys()))
    sheet_name = pages[selected_page]
    
    if sheet_name == "Detail":
        st.header(t["detail"])
        st.dataframe(detail_df)
    elif sheet_name == "team_summary1":
        st.header(t["team_summary1"])
        st.dataframe(team1_df)
    elif sheet_name == "team_summary2":
        st.header(t["team_summary2"])
        st.dataframe(team2_df)
    elif sheet_name == "total_absent_info":
        st.header(t["total_absent_info"])
        total_absent_df = load_total_absent_excel(month_selected)
        st.dataframe(total_absent_df)

###############################
# 탭 2: 5PRS Validation Info
###############################
with tab2:
    inspector_df, tqc_id_df = load_5prs_data()
    st.subheader("Inspector Summary")
    st.dataframe(inspector_df)
    
    st.subheader("TQC ID Summary")
    st.dataframe(tqc_id_df)

