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
        "description": "엑셀 파일의 각 시트를 활용한 대시보드입니다.",
        "page_select": "페이지 선택",
        "detail": "Detail 데이터",
        "team_summary1": "팀 요약 1",
        "team_summary2": "팀 요약 2",
        "total_absent_info": "Total Absent Information",
        "tab_select": "탭 선택",
        "abs_rate_tab": "Absence Rate Info",
        "prs_tab": "5PRS Validation Info",
        "month_select": "월 선택 (2월 / 3월)",
        "language_select": "언어 선택"
    },
    "en": {
        "password_prompt": "Enter the password",
        "password_error": "Incorrect password.",
        "title": "Absence Rate Dashboard",
        "description": "This dashboard utilizes Excel files to display data.",
        "page_select": "Select Page",
        "detail": "Detail Data",
        "team_summary1": "Team Summary 1",
        "team_summary2": "Team Summary 2",
        "total_absent_info": "Total Absent Information",
        "tab_select": "Select Tab",
        "abs_rate_tab": "Absence Rate Info",
        "prs_tab": "5PRS Validation Info",
        "month_select": "Select Month (Feb / Mar)",
        "language_select": "Select Language"
    },
    "vi": {
        "password_prompt": "Nhập mật khẩu",
        "password_error": "Mật khẩu không chính xác.",
        "title": "Bảng điều khiển tỷ lệ vắng mặt",
        "description": "Bảng điều khiển này sử dụng file Excel để hiển thị dữ liệu.",
        "page_select": "Chọn trang",
        "detail": "Dữ liệu Detail",
        "team_summary1": "Tóm tắt đội 1",
        "team_summary2": "Tóm tắt đội 2",
        "total_absent_info": "Total Absent Information",
        "tab_select": "Chọn Tab",
        "abs_rate_tab": "Absence Rate Info",
        "prs_tab": "5PRS Validation Info",
        "month_select": "Chọn tháng (2/3)",
        "language_select": "Chọn ngôn ngữ"
    }
}

##############################################
# 2. 사이드바: 언어 선택 (라디오 버튼) 및 비밀번호 보호
##############################################
lang_options = {"Korean": "ko", "English": "en", "Vietnamese": "vi"}
selected_lang = st.sidebar.radio("Language / " + translations["en"]["language_select"], list(lang_options.keys()))
lang_code = lang_options[selected_lang]
t = translations[lang_code]

password = st.sidebar.text_input(t["password_prompt"], type="password")
if password != "hwkqip":
    st.error(t["password_error"])
    st.stop()

##############################################
# 3. 사이드바: 탭 선택 (메인 탭을 사이드바로 이동)
##############################################
tab_choice = st.sidebar.radio(t["tab_select"], [t["abs_rate_tab"], t["prs_tab"]])

##############################################
# 4. "Absence Rate (%)" 전처리 함수
##############################################
def convert_absence_rate(df, col="Absence Rate (%)"):
    if col in df.columns:
        # "%" 문자 제거 후 숫자형으로 변환
        df[col] = pd.to_numeric(df[col].astype(str).str.replace("%", "", regex=False).str.strip(), errors="coerce")
    return df

##############################################
# 5. requests + BytesIO를 이용해 Excel 파일 불러오기 함수 (예외 처리 포함)
##############################################
@st.cache_data
def load_excel_from_github(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        st.error(f"Error loading file from URL:\n{url}\n{e}")
        return None
    return BytesIO(response.content)

##############################################
# 6. 결근율 데이터 로딩 (2월/3월 Excel)
##############################################
@st.cache_data
def load_absence_data(month: str):
    if month == "February":
        url = "https://raw.githubusercontent.com/ksmoon848484/absent/2ddca50bdd054e76c542323bfd7263acc6c496e4/aggregated_absence_rate_by_group_Feb.xlsx"
    else:
        url = "https://raw.githubusercontent.com/ksmoon848484/absent/2ddca50bdd054e76c542323bfd7263acc6c496e4/aggregated_absence_rate_by_group_Mar.xlsx"
    
    data_bytes = load_excel_from_github(url)
    if data_bytes is None:
        return None, None, None
    detail = pd.read_excel(data_bytes, sheet_name='Detail')
    team1 = pd.read_excel(data_bytes, sheet_name='team summary1')
    team2 = pd.read_excel(data_bytes, sheet_name='team summary2')
    # "Absence Rate (%)" 컬럼을 숫자형으로 변환
    detail = convert_absence_rate(detail)
    team1 = convert_absence_rate(team1)
    team2 = convert_absence_rate(team2)
    return detail, team1, team2

##############################################
# 7. Total Absent Information 로딩 (2월/3월 CSV)
##############################################
@st.cache_data
def load_total_absent_csv(month: str):
    if month == "February":
        url = "https://raw.githubusercontent.com/ksmoon848484/absent/c0fc873fb175d937f79ef6b64e8980e0ba51d80f/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Feb.csv"
    else:
        url = "https://raw.githubusercontent.com/ksmoon848484/absent/c0fc873fb175d937f79ef6b64e8980e0ba51d80f/Result_UnapprovedAbsence_AbsenceRate_by_PersonnelNo_Mar.csv"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        st.error(f"Error loading Total Absent CSV from URL:\n{url}\n{e}")
        return None
    df = pd.read_csv(BytesIO(response.content))
    # "Absence Rate (%)" 컬럼도 숫자형으로 변환 (필요하다면)
    df = convert_absence_rate(df)
    return df

##############################################
# 8. 5PRS Validation 데이터 로딩 (CSV)
##############################################
@st.cache_data
def load_5prs_data():
    inspector_url = "https://raw.githubusercontent.com/ksmoon848484/absent/2ddca50bdd054e76c542323bfd7263acc6c496e4/Inspector_summary.csv"
    tqc_id_url = "https://raw.githubusercontent.com/ksmoon848484/absent/2ddca50bdd054e76c542323bfd7263acc6c496e4/TQC_ID_summary.csv"
    try:
        insp_response = requests.get(inspector_url)
        insp_response.raise_for_status()
        inspector_df = pd.read_csv(BytesIO(insp_response.content))
        
        tqc_response = requests.get(tqc_id_url)
        tqc_response.raise_for_status()
        tqc_id_df = pd.read_csv(BytesIO(tqc_response.content))
    except requests.exceptions.HTTPError as e:
        st.error(f"Error loading 5PRS data:\n{e}")
        return None, None
    return inspector_df, tqc_id_df

##############################################
# 9. 메인 UI: 탭별 내용 표시
##############################################
st.title(t["title"])
st.write(t["description"])

if tab_choice == t["abs_rate_tab"]:
    # Absence Rate Info 탭
    month_selected = st.radio(t["month_select"], ("February", "March"), horizontal=True)
    
    detail_df, team1_df, team2_df = load_absence_data(month_selected)
    if detail_df is None:
        st.error("Error loading absence data.")
    else:
        st.header(t["detail"])
        st.dataframe(detail_df.sort_values("Absence Rate (%)"))
        
        st.header(t["team_summary1"])
        st.dataframe(team1_df.sort_values("Absence Rate (%)"))
        
        st.header(t["team_summary2"])
        st.dataframe(team2_df.sort_values("Absence Rate (%)"))
        
        st.header(t["total_absent_info"])
        total_absent_df = load_total_absent_csv(month_selected)
        if total_absent_df is None:
            st.error("Error loading total absent information.")
        else:
            st.dataframe(total_absent_df.sort_values("Absence Rate (%)"))
                
elif tab_choice == t["prs_tab"]:
    # 5PRS Validation Info 탭
    inspector_df, tqc_id_df = load_5prs_data()
    if inspector_df is None or tqc_id_df is None:
        st.error("Error loading 5PRS Validation data.")
    else:
        st.subheader("Inspector Summary")
        st.dataframe(inspector_df)
        st.subheader("TQC ID Summary")
        st.dataframe(tqc_id_df)




