import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="포뮬노트 | FormuNote",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최대한 제거해서 원본 HTML 디자인이 그대로 보이도록 처리
st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header[data-testid="stHeader"] {display: none;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

# 같은 폴더에 있는 index.html을 읽어서 그대로 렌더링
html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# scrolling=True + 넉넉한 height로 페이지 전체 내용이 보이도록 함
components.html(html_content, height=3200, scrolling=True)
