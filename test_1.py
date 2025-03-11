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



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from st_aggrid import AgGrid, GridOptionsBuilder

##############################################
# 1. 다국어 번역 사전 (UI 텍스트용)
##############################################
translations = {
    "ko": {
        "select_language": "언어 선택",
        "password_prompt": "비밀번호를 입력하세요",
        "password_error": "비밀번호가 올바르지 않습니다.",
        "title": "결근율 대시보드",
        "description": "엑셀 파일의 각 시트를 활용한 대시보드입니다. 사이드바에서 원하는 시트를 선택해보세요.",
        "page_select": "페이지 선택",
        "detail": "Detail 데이터",
        "team_summary1": "팀 요약 1",
        "team_summary2": "팀 요약 2",
        "detail_distribution": "결근율 분포",
        "team_summary1_average": "팀별 결근율 요약",
        "team_summary2_comparison": "팀별 결근율 비교",
        "kpi_average": "평균 결근율",
        "kpi_max": "최대 결근율",
        "kpi_min": "최소 결근율",
        "top5_chart_title": "결근율 상위 5",
        "interactive_table": "상세 데이터 (인터랙티브 테이블)",
        "top5_table": "상위 5 결근율 데이터"
    },
    "en": {
        "select_language": "Select Language",
        "password_prompt": "Enter the password",
        "password_error": "Incorrect password.",
        "title": "Absence Rate Dashboard",
        "description": "This dashboard utilizes each sheet of the Excel file. Please select the desired sheet from the sidebar.",
        "page_select": "Select Page",
        "detail": "Detail Data",
        "team_summary1": "Team Summary 1",
        "team_summary2": "Team Summary 2",
        "detail_distribution": "Absence Rate Distribution",
        "team_summary1_average": "Team Absence Rate Summary",
        "team_summary2_comparison": "Team Absence Rate Comparison",
        "kpi_average": "Average Absence Rate",
        "kpi_max": "Max Absence Rate",
        "kpi_min": "Min Absence Rate",
        "top5_chart_title": "Top 5 Absence Rates",
        "interactive_table": "Detailed Data (Interactive Table)",
        "top5_table": "Top 5 Absence Rate Data"
    },
    "vi": {
        "select_language": "Chọn ngôn ngữ",
        "password_prompt": "Nhập mật khẩu",
        "password_error": "Mật khẩu không chính xác.",
        "title": "Bảng điều khiển Tỷ lệ vắng mặt",
        "description": "Bảng điều khiển này sử dụng từng sheet của file Excel. Hãy chọn sheet mà bạn muốn từ thanh bên.",
        "page_select": "Chọn trang",
        "detail": "Dữ liệu Detail",
        "team_summary1": "Tóm tắt đội 1",
        "team_summary2": "Tóm tắt đội 2",
        "detail_distribution": "Phân bố tỷ lệ vắng mặt",
        "team_summary1_average": "Tóm tắt tỷ lệ vắng mặt của đội",
        "team_summary2_comparison": "So sánh tỷ lệ vắng mặt theo đội",
        "kpi_average": "Tỷ lệ vắng mặt trung bình",
        "kpi_max": "Tỷ lệ vắng mặt cao nhất",
        "kpi_min": "Tỷ lệ vắng mặt thấp nhất",
        "top5_chart_title": "Top 5 tỷ lệ vắng mặt",
        "interactive_table": "Dữ liệu chi tiết (Bảng tương tác)",
        "top5_table": "Top 5 Tỷ lệ vắng mặt"
    }
}

##############################################
# 2. 언어 선택 & 비밀번호 확인
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
# 3. 데이터 로딩 (pandas + openpyxl 필요)
##############################################
@st.cache_data
def load_data():
    file_path = 'aggregated_absence_rate_by_group.xlsx'
    xls = pd.ExcelFile(file_path)
    detail = pd.read_excel(xls, sheet_name='Detail')
    team1 = pd.read_excel(xls, sheet_name='team summary1')
    team2 = pd.read_excel(xls, sheet_name='team summary2')
    return detail, team1, team2

detail_df, team1_df, team2_df = load_data()

##############################################
# 4. 레이아웃 & UI 기본 설정
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
# 5. AgGrid를 활용한 인터랙티브 테이블
##############################################
def show_aggrid(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    # 페이지네이션, 정렬, 필터, 그룹화 설정
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_default_column(
        editable=False, groupable=True, sortable=True, filter=True
    )
    grid_options = gb.build()
    AgGrid(data, gridOptions=grid_options, theme='light', height=300, fit_columns_on_grid_load=True)

##############################################
# 6. KPI 카드: 평균, 최대, 최소 Absence Rate
##############################################
def show_kpi(data, rate_col: str):
    """
    data: pd.DataFrame
    rate_col: 'Absence Rate (%)' 등, 실제 결근율 컬럼명
    """
    if rate_col in data.columns:
        avg_rate = data[rate_col].mean()
        max_rate = data[rate_col].max()
        min_rate = data[rate_col].min()
        col1, col2, col3 = st.columns(3)
        col1.metric(t["kpi_average"], f"{avg_rate:.2f}")
        col2.metric(t["kpi_max"], f"{max_rate:.2f}")
        col3.metric(t["kpi_min"], f"{min_rate:.2f}")
    else:
        st.warning(f"Column '{rate_col}' not found in the DataFrame.")

##############################################
# 7. 상위 5 데이터 + 시각화
##############################################
def show_top5(data, rate_col: str, label_col: str = None):
    """
    rate_col 기준으로 상위 5개 추출하여 테이블 및 막대 차트 표시.
    label_col을 지정하면 x축 레이블로 사용, 지정하지 않으면 index 사용.
    """
    if rate_col not in data.columns:
        st.warning(f"Column '{rate_col}' not found in the DataFrame.")
        return
    
    top5 = data.nlargest(5, rate_col)
    st.subheader(t["top5_table"])
    st.dataframe(top5)
    
    st.subheader(t["top5_chart_title"])
    fig, ax = plt.subplots()
    if label_col and label_col in top5.columns:
        x_labels = top5[label_col]
    else:
        x_labels = top5.index.astype(str)
    
    ax.bar(x_labels, top5[rate_col])
    ax.set_xlabel(label_col if label_col else "Index")
    ax.set_ylabel(rate_col)
    ax.set_title(t["top5_chart_title"])
    st.pyplot(fig)

##############################################
# 8. 페이지별(시트별) 내용 구성
##############################################
if sheet_name == "Detail":
    # Detail 시트
    st.header(t["detail"])
    
    # 8-1) KPI 카드: "Absence Rate (%)" 기준
    show_kpi(detail_df, "Absence Rate (%)")
    
    # 8-2) 인터랙티브 테이블 (익스팬더에 숨김)
    with st.expander(t["interactive_table"]):
        show_aggrid(detail_df)
    
    # 8-3) 상위 5 (rate_col='Absence Rate (%)', label_col='AREA' 예시)
    show_top5(detail_df, "Absence Rate (%)", label_col="AREA")

elif sheet_name == "team summary1":
    # team summary1 시트
    st.header(t["team_summary1"])
    
    # 8-1) KPI 카드: "Absence Rate (%)" 기준
    show_kpi(team1_df, "Absence Rate (%)")
    
    # 8-2) 인터랙티브 테이블
    with st.expander(t["interactive_table"]):
        show_aggrid(team1_df)
    
    # 8-3) 상위 5
    show_top5(team1_df, "Absence Rate (%)", label_col="AREA")

elif sheet_name == "team summary2":
    # team summary2 시트
    st.header(t["team_summary2"])
    
    # 8-1) KPI 카드: "Absence Rate (%)" 기준
    show_kpi(team2_df, "Absence Rate (%)")
    
    # 8-2) 인터랙티브 테이블
    with st.expander(t["interactive_table"]):
        show_aggrid(team2_df)
    
    # 8-3) 상위 5
    show_top5(team2_df, "Absence Rate (%)", label_col="AREA")
