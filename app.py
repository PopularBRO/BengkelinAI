from pathlib import Path
import streamlit as st

# BengkelinAI Streamlit wrapper
# IMPORTANT: load the website from its real static-file URL, not as srcdoc.
# This preserves the document URL so relative CSS, JS, images, and page links
# resolve from /app/static/ correctly.

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
ENTRY_FILE = STATIC_DIR / "index.html"
STATIC_ENTRY_URL = "/app/static/index.html"

st.set_page_config(
    page_title="BengkelinAI | One App for All Your Vehicle Needs",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the Streamlit shell unobtrusive. The website itself is rendered by
# the original HTML/CSS/JavaScript files inside the iframe.
st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        background: #F4F7F9 !important;
      }
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      footer, #MainMenu {
        visibility: hidden !important;
        height: 0 !important;
      }
      .block-container {
        max-width: 100% !important;
        padding: 0 !important;
      }
      iframe {
        display: block;
        width: 100% !important;
        border: 0 !important;
        border-radius: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Validate the website package before opening it.
required_files = [
    ENTRY_FILE,
    STATIC_DIR / "style.css",
    STATIC_DIR / "script.js",
    STATIC_DIR / "assets" / "logo-bengkelinai.png",
]
missing = [str(path.relative_to(BASE_DIR)) for path in required_files if not path.is_file()]
if missing:
    st.error("Beberapa file website tidak ditemukan di repository.")
    st.write("File yang belum ada:")
    for item in missing:
        st.code(item)
    st.info("Pastikan folder static beserta seluruh isinya ikut di-upload ke GitHub.")
    st.stop()

# Render the real static HTML URL. This is the key fix:
# index.html keeps /app/static/ as its base URL, so style.css,
# script.js, assets/logo-bengkelinai.png, and relative page links work.
st.iframe(
    STATIC_ENTRY_URL,
    height=1250,
    width="stretch",
    alt="Website BengkelinAI",
)
