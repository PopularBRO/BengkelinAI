from pathlib import Path
import re
import streamlit as st

# BengkelinAI Streamlit wrapper
# The original website remains in HTML, CSS, and JavaScript.
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
ENTRY_FILE = STATIC_DIR / "index.html"
STATIC_URL = "/app/static/"

st.set_page_config(
    page_title="BengkelinAI | One App for All Your Vehicle Needs",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit's surrounding canvas minimal. The site itself is rendered
# inside a trusted iframe so its JavaScript and multi-page navigation work.
st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        background: #f4f7f9 !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer,
      #MainMenu { visibility: hidden !important; height: 0 !important; }
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

if not ENTRY_FILE.is_file():
    st.error("Halaman utama tidak ditemukan.")
    st.code(str(ENTRY_FILE))
    st.info("Pastikan folder static berisi index.html, style.css, script.js, dan folder assets.")
    st.stop()

try:
    html = ENTRY_FILE.read_text(encoding="utf-8")
except OSError as exc:
    st.error("Streamlit tidak dapat membaca index.html.")
    st.exception(exc)
    st.stop()

# Because the HTML is embedded in an iframe as srcdoc, relative URLs would
# otherwise resolve against the Streamlit page. Convert local href/src paths
# to the Streamlit static-file endpoint. Keep #anchors and external URLs intact.
URL_ATTR = re.compile(r"(?P<prefix>\b(?:href|src)\s*=\s*)(?P<quote>[\"'])(?P<url>[^\"']+)(?P=quote)", re.IGNORECASE)

def make_static_url(match: re.Match) -> str:
    url = match.group("url").strip()
    lowered = url.lower()
    if (
        url.startswith(("#", "/"))
        or lowered.startswith(("http://", "https://", "data:", "mailto:", "tel:", "javascript:", "blob:"))
    ):
        return match.group(0)
    return f"{match.group('prefix')}{match.group('quote')}{STATIC_URL}{url}{match.group('quote')}"

html = URL_ATTR.sub(make_static_url, html)

# Render the local HTML directly instead of asking the iframe to navigate to
# /app/static/index.html. This avoids a second document-navigation step during
# first load. CSS, JS, images and page links still load from /app/static/.
st.iframe(
    html,
    height=1100,
    width="stretch",
    alt="Website BengkelinAI",
)
