from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ENTRY_FILE = BASE_DIR / "static" / "index.html"

st.set_page_config(
    page_title="BengkelinAI | One App for All Your Vehicle Needs",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the Streamlit shell visually minimal. The actual website is rendered
# from the trusted local HTML project inside the iframe below.
st.markdown(
    """
    <style>
      [data-testid="stAppViewContainer"] {
        background: #f4f7f9;
      }
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      footer {
        display: none !important;
      }
      .block-container {
        max-width: 100% !important;
        padding: 0 !important;
      }
      iframe {
        display: block;
        width: 100%;
        border: 0 !important;
        border-radius: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not ENTRY_FILE.exists():
    st.error("File website tidak ditemukan. Pastikan folder static/index.html tersedia.")
    st.stop()

# Streamlit static serving exposes ./static at /app/static/.
# Relative links inside index.html (other HTML pages, CSS, JS, and images)
# continue to resolve from the same static folder.
st.iframe("/app/static/index.html", height=950, width="stretch")
