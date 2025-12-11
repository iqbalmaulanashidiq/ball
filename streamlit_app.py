import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# CUSTOM CSS (FONT STATIS UNTUK TITLE)
# =============================
st.markdown("""
<style>
    body {
        background: #f4f7f9;
    }

    h1 {
        font-family: 'Georgia', serif !important; /* Ubah font di sini */
        text-align: center;
        color: #1976D2;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        background: white;
        border-radius: 12px;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }

    .stTextInput>div>div>input {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# =============================
# TITLE
# =============================
st.markdown("<h1>Kalkulator SPNL - Metode Regula Falsi</h1>", unsafe_allow_html=True)

# =============
