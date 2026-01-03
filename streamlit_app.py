import streamlit as st
import pandas as pd

# =============================
# PAGE CONFIG (WAJIB PALING ATAS)
# =============================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="centered"
)

# =============================
# SESSION STATE
# =============================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# =============================
# SIDEBAR (RESMI)
# =============================
with st.sidebar:
    st.header("⚙️ Pengaturan")
    st.session_state.dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

# =============================
# TEMA WARNA (LOGIC, BUKAN HACK)
# =============================
if st.session_state.dark_mode:
    BG_COLOR = "#0f172a"
    TEXT_COLOR = "#e5e7eb"
    INPUT_COLOR = "#334155"
else:
    BG_COLOR = "#f4f7f9"
    TEXT_COLOR = "#1f2937"
    INPUT_COLOR = "#f1f3f5"

# =============================
# CSS MINIMAL & AMAN
# =============================
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
        }}

        input {{
            background-color: {INPUT_COLOR};
            color: {TEXT_COLOR};
            border-radius: 10px;
        }}

        button {{
            border-radius: 10px;
            padding: 0.5rem 1.2rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# JUDUL
# =============================
st.markdown(
    f"""
    <h1 style="text-align:center; color:{TEXT_COLOR};_
