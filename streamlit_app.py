import streamlit as st
import pandas as pd

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================
# STATE DARK MODE
# =============================
if "dark" not in st.session_state:
    st.session_state.dark = False

# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown("## ⚙️ Pengaturan")
    st.session_state.dark = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark
    )

# =============================
# WARNA
# =============================
if st.session_state.dark:
    BG = "#0f172a"
    TEXT = "#e5e7eb"
    INPUT = "#334155"
else:
    BG = "#f4f7f9"
    TEXT = "#1f2937"
    INPUT = "#f1f3f5"

# =============================
# CSS FINAL (ANTI KOTAK PUTIH)
# =============================
st.markdown(f"""
<style>

/* RESET */
* {{
    box-shadow: none !important;
}}

/* BACKGROUND */
.stApp {{
    background-color: {BG};
    color: {TEXT};
}}

/* SIDEBAR */
section[data-testid="stSidebar"] {{
    background-color: {BG} !important;
    border-right: none !important;
}}

/* HAPUS CONTAINER PUTIH */
div[data-testid="stContainer"],
div[data-testid="stVerticalBlock"],
div[data-testid="stForm"] {{
    background: transparent !important;
    border: none !important;
}}

/* BLOK KOSONG (KUNCI) */
div[data-testid="stVerticalBlock"]:has(> div:empty) {{
    display: none !important;
}}

/* MARKDOWN KOSONG */
div[data-testid="stMarkdown"]:empty {{
    display: none !important;
}}

/* INPUT */
input {{
    background-color: {INPUT} !important;
    color: {TEXT} !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 12px !important;
}}

/* BUTTON */
button {{
    background-color: #1976D2 !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 10px 22px !important;
}}

/* PADDING ATAS */
.block-container {{
    padding-top: 28px;
}}

</style>
""", unsafe_allow_html=True)

# =============================
# JUDUL
# =============================
st.markdown(f"""
<h1 style="
    text-align:center;
    font-family:Georgia;
    margin-bottom:25px;
    color:{TEXT};">
Kalkulator SPNL – Metode Regula Falsi
</h1>
""", unsafe_allow_html=True)

# =============================
# INPUT
# =============================
st.subheader("Step 1: Masukkan Persamaan f(x)")
fungsi = st.text_input(
    label="Persamaan",
    placeholder="Contoh: x**3 - x - 2"
)

st.subheader("Step 2: Interval Awal")
a = st.number_input("Nilai a", value=1.0)
b = st.number_input("Nilai b", value=2.0)

st.subheader("Step 3: Parameter Iterasi")
tol = st.number
