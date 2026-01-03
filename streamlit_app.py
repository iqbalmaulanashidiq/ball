import streamlit as st
import numpy as np
import pandas as pd
import math

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Kalkulator SPNL - Regula Falsi",
    layout="centered"
)

# =============================
# CUSTOM CSS (HILANGKAN KOTAK PUTIH)
# =============================
st.markdown("""
<style>

/* Background utama */
.stApp {
    background-color: #f4f7f9;
}

/* Hilangkan semua container putih default */
div[data-testid="stVerticalBlock"],
div[data-testid="stContainer"] {
    background: transparent !important;
    box-shadow: none !important;
    border: none !important;
    padding: 0 !important;
}

/* Hilangkan markdown kosong */
div[data-testid="stMarkdown"]:empty {
    display: none;
}

/* Input styling */
input {
    background-color: #f1f3f5 !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Button styling */
button {
    background-color: #1976D2 !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    border: none !important;
    font-size: 16px !important;
}

/* Hilangkan jarak kosong berlebih */
.block-container {
    padding-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =============================
# JUDUL
# =============================
st.markdown("""
<h1 style="text-align:center; color:#1f2937; font-family:Georgia;">
Kalkulator SPNL - Metode Regula Falsi
</h1>
""", unsafe_allow_html=True)

# =============================
# INPUT
# =============================
st.markdown("### Step 1: Masukkan Persamaan f(x)")
fungsi = st.text_input(
    label=" ",
    placeholder="Contoh: x**3 - x - 2"
)

st.markdown("### Step 2: Masukkan Interval Awal")
a = st.number_input("Nilai a", value=1.0)
b = st.number_input("Nilai b", value=2.0)

st.markdown("### Step 3: Toleransi & Iterasi")
tol = st.number_input("Toleransi Error", value=0.0001)
max_iter = st.number_input("Maksimum Iterasi", value=20, step=1)

# =============================
# FUNGSI REGULA FALSI
# =============================
def regula_falsi(f, a, b, tol, max_iter):
    hasil = []
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return None

    for i in range(1, max_iter + 1):
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)

        hasil.append([i, a, b, c, fc])

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return hasil

# =============================
# PROSES
# =============================
if st.button("Hitung Akar"):
    if fungsi.strip() == "":
        st.warning("Masukkan persamaan terlebih dahulu!")
    else:
        try:
            f = lambda x: eval(fungsi)

            data = regula_falsi(f, a, b, tol, int(max_iter))

            if data is None:
                st.error("f(a) dan f(b) harus berlainan tanda!")
            else:
                df = pd.DataFrame(
                    data,
                    columns=["Iterasi", "a", "b", "c", "f(c)"]
                )
                st.success(f"Akar ditemukan: {df.iloc[-1]['c']}")
                st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
