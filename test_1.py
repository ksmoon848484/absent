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
        "select_language": "언어 선택",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "total_absent_info": "Total Absent Information",
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
        "select_language": "Select Language",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "total_absent_info": "Total Absent Information",
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
        "select_language": "Chọn ngôn ngữ",
        "tab1_name": "Absence Rate Info",
        "tab2_name": "5PRS Validation Info",
        "total_absent_info": "Total Absent Information",
        "month_select": "Chọn tháng (2/3)"
    }
}

##############################################
# 2. 사이드바: 언어 선택 & 비밀번호
##############################################
language_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
selected_language_name = st.sidebar.selectbox(
    "Select Language / 언어 선택 / Chọn ngôn ngữ",
    list(language_options.keys())
)
lang_code = language_options[selected_language_name]
t = translations[lang_code]

password = st.text_input(t["password_prompt"], type="password")
if password != "hwkqip":
    st.error(t["password_error"])
    st.stop()

##############################################
# 3. 2월/3월 구분 로딩 함수 (결근율 엑셀)
##############################################
@st.cache_data
def load_absence_data(month: str):
    """
    month: "February" or "March"
    GitHub Raw URL을 실제 경로로 변경해 주세요.
    """
    if month == "February":
        url = "https://raw.githubusercontent.com/사용자명/저장소명/main/aggregated_absence_rate_by_group_Feb.xlsx"
    else:
        url = "https://raw.githubusercontent.com/사용자명/저장소명/main/aggregated_absence_rate_by_group_Mar.xlsx"

    xls = pd.ExcelFile(url)
    detail = pd.read_excel(xls, sheet_name='Detail')
    team1 = pd.read_excel(xls, sheet_name='team summary1')
    team2 = pd.read_excel(xls, sheet_name='team summary2')
    return detail, team1, team2

##############################################
# 4. 2월/3월 구분 로딩 함수 (Total Absent CSV)
##############################################
@st.cache_data
def load_total_absent_info(month: str):
    """
    month: "February" or "March"
    GitHub Raw URL을 실제 경로로 변경해 주세요.
    """
    if month == "February":
        url = "https://raw.githubusercontent.com/사용자명/저장소명/main/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Feb.csv"
    else:
        url = "https://raw.githubusercontent.com/사용자명/저장소명/main/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Mar.csv"

    df = pd.read_csv(url)
    return df

##############################################
# 5. 5PRS Validation (Inspector, TQC_ID) 로딩 함수
##############################################
@st.cache_data
def load_5prs_data():
    """
    GitHub Raw URL을 실제 경로로 변경해 주세요.
    """
    inspector_url = "https://raw.githubusercontent.com/사용자명/저장소명/main/Inspector_summary.csv"
    tqc_id_url = "https://raw.githubusercontent.com/사용자명/저장소명/main/TQC_ID_summary.csv"

    inspector_df = pd.read_csv(inspector_url)
    tqc_id_df = pd.read_csv(tqc_id_url)
    return inspector_df, tqc_id_df

##############################################
# 6. 메인 UI: 2개 탭 (Tab)
##############################################
st.title(t["title"])
st.write(t["description"])

tab1, tab2 = st.tabs([t["tab1_name"], t["tab2_name"]])

###############################
# 탭 1: Absence Rate Info
###############################
with tab1:
    # 6-1) 2월/3월 라디오 버튼
    month_selected = st.radio(
        t["month_select"],
        ("February", "March"),
        horizontal=True
    )

    # 6-2) 엑셀 파일 로딩 (Detail, team summary1, team summary2)
    detail_df, team1_df, team2_df = load_absence_data(month_selected)

    # 6-3) 페이지(시트) 선택 (Detail, team summary1, team summary2, Total Absent Info)
    pages = {
        t["detail"]: "Detail",
        t["team_summary1"]: "team summary1",
        t["team_summary2"]: "team summary2",
        t["total_absent_info"]: "total_absent_info"
    }
    selected_page = st.radio(t["page_select"], list(pages.keys()))
    sheet_name = pages[selected_page]

    if sheet_name == "Detail":
        st.header(t["detail"])
        st.dataframe(detail_df)

    elif sheet_name == "team summary1":
        st.header(t["team_summary1"])
        st.dataframe(team1_df)

    elif sheet_name == "team summary2":
        st.header(t["team_summary2"])
        st.dataframe(team2_df)

    elif sheet_name == "total_absent_info":
        st.header(t["total_absent_info"])
        # 2월/3월 Total Absent CSV 로딩
        absent_df = load_total_absent_info(month_selected)
        st.dataframe(absent_df)

###############################
# 탭 2: 5PRS Validation Info
###############################
with tab2:
    inspector_df, tqc_id_df = load_5prs_data()
    st.subheader("Inspector Summary")
    st.dataframe(inspector_df)

    st.subheader("TQC ID Summary")
    st.dataframe(tqc_id_df)
