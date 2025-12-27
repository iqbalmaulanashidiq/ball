import streamlit as st
import numpy as np
import pandas as pd
import math

# =============================
# CUSTOM CSS
# =============================
st.markdown("""
<style>
    body {
        background: #f4f7f9;
    }
    h1 {
        font-family: 'Georgia', serif !important;
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
</style>
""", unsafe_allow_html=True)

# =============================
# TITLE
# =============================
st.markdown("<h1>Kalkulator SPNL - Metode Regula Falsi</h1>", unsafe_allow_html=True)

# =============================
# INPUT FUNGSI
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 1: Masukkan Persamaan f(x)")
fungsi = st.text_input(
    "Contoh: x**3 - x - 2\nGunakan math / np jika perlu",
    value="x**3 - x - 2"
)
st.markdown("</div>", unsafe_allow_html=True)

# =============================
# INTERVAL
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 2: Pilih Interval")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("a", value=1.0)
with col2:
    b = st.number_input("b", value=2.0)

def f(x):
    try:
        return eval(fungsi, {"x": x, "np": np, "math": math})
    except:
        return np.nan

fa, fb = f(a), f(b)
st.write(f"f(a) = {fa}")
st.write(f"f(b) = {fb}")

valid_interval = fa * fb < 0
if valid_interval:
    st.success("Interval valid ✓")
else:
    st.error("Interval tidak valid")

st.markdown("</div>", unsafe_allow_html=True)

# =============================
# PARAMETER
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 3: Pengaturan Lanjut")

col1, col2 = st.columns(2)
with col1:
    max_iter = st.number_input("Maksimum Iterasi", value=50)
with col2:
    tol = st.number_input("Toleransi Error", value=1e-6, format="%.10f")

hitung_button = st.button("Hitung Akar")
st.markdown("</div>", unsafe_allow_html=True)

# =============================
# REGULA FALSI
# =============================
if hitung_button and valid_interval:

    a0, b0 = a, b
    fa, fb = f(a0), f(b0)
    xr_old = a0
    data_iterasi = []

    for i in range(1, int(max_iter) + 1):
        xr = (a0 * fb - b0 * fa) / (fb - fa)
        fxr = f(xr)
        error = abs(xr - xr_old)

        data_iterasi.append([i, a0, b0, xr, fxr, error])

        if error < tol:
            break

        if fa * fxr < 0:
            b0, fb = xr, fxr
        else:
            a0, fa = xr, fxr

        xr_old = xr

    # =============================
    # HASIL
    # =============================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Hasil Perhitungan")
    st.success(f"""
    **Akar mendekati:** {xr}  
    **Error akhir:** {error}  
    **Total iterasi:** {len(data_iterasi)}
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # =============================
    # TABEL ITERASI
    # =============================
    df = pd.DataFrame(
        data_iterasi,
        columns=["Iterasi", "a", "b", "xr", "f(xr)", "Error"]
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Tabel Iterasi")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # =============================
    # GRAFIK (STREAMLIT NATIVE)
    # =============================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Grafik Fungsi f(x)")

    x_vals = np.linspace(a - 2, b + 2, 400)
    y_vals = [f(x) for x in x_vals]

    df_plot = pd.DataFrame({
        "x": x_vals,
        "f(x)": y_vals
    })

    st.line_chart(df_plot.set_index("x"))

    st.markdown(f"""
    **Titik Akar:**  
    x = `{xr}`  
    f(x) = `{f(xr)}`
    """)

    st.markdown("</div>", unsafe_allow_html=True)
