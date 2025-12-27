import streamlit as st
import numpy as np
import pandas as pd
import math

# =============================
# TOGGLE MODE
# =============================
mode = st.toggle("🌙 Dark Mode", value=False)

# =============================
# CSS DINAMIS
# =============================
if mode:  # DARK MODE
    bg = "#0f172a"
    card = "#0f172a"
    text = "#e5e7eb"
    accent = "#38bdf8"
else:     # LIGHT MODE
    bg = "#f8fafc"
    card = "#f8fafc"
    text = "#0f172a"
    accent = "#2563eb"

st.markdown(f"""
<style>
    html, body, [class*="css"] {{
        background-color: {bg};
        color: {text};
    }}

    h1 {{
        text-align: center;
        color: {accent};
        font-family: 'Georgia', serif;
    }}

    h2, h3 {{
        color: {accent};
    }}

    /* Hilangkan box putih Streamlit */
    section[data-testid="stSidebar"],
    div[data-testid="stDataFrame"],
    div[data-testid="stTable"] {{
        background: transparent !important;
        box-shadow: none !important;
    }}

    /* Input styling */
    input {{
        background-color: transparent !important;
        color: {text} !important;
        border-radius: 8px;
    }}

    /* Button */
    button {{
        border-radius: 10px;
        background-color: {accent} !important;
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

# =============================
# TITLE
# =============================
st.markdown("<h1>Kalkulator SPNL – Regula Falsi</h1>", unsafe_allow_html=True)

# =============================
# INPUT FUNGSI
# =============================
st.subheader("1️⃣ Persamaan f(x)")
fungsi = st.text_input(
    "Contoh: x**3 - x - 2",
    value="x**3 - x - 2"
)

# =============================
# INTERVAL
# =============================
st.subheader("2️⃣ Interval")
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
st.success("Interval valid ✓") if valid_interval else st.error("Interval tidak valid")

# =============================
# PARAMETER
# =============================
st.subheader("3️⃣ Parameter")
col1, col2 = st.columns(2)
with col1:
    max_iter = st.number_input("Maksimum Iterasi", value=50)
with col2:
    tol = st.number_input("Toleransi Error", value=1e-6, format="%.10f")

# =============================
# HITUNG
# =============================
if st.button("🔍 Hitung Akar") and valid_interval:

    a0, b0 = a, b
    fa, fb = f(a0), f(b0)
    xr_old = a0
    data = []

    for i in range(1, int(max_iter) + 1):
        xr = (a0 * fb - b0 * fa) / (fb - fa)
        fxr = f(xr)
        err = abs(xr - xr_old)

        data.append([i, a0, b0, xr, fxr, err])

        if err < tol:
            break

        if fa * fxr < 0:
            b0, fb = xr, fxr
        else:
            a0, fa = xr, fxr

        xr_old = xr

    # =============================
    # HASIL
    # =============================
    st.subheader("📌 Hasil")
    st.write(f"**Akar ≈** `{xr}`")
    st.write(f"**Error akhir:** `{err}`")
    st.write(f"**Iterasi:** `{len(data)}`")

    # =============================
    # TABEL (TANPA BACKGROUND PUTIH)
    # =============================
    df = pd.DataFrame(
        data,
        columns=["Iterasi", "a", "b", "xr", "f(xr)", "Error"]
    )
    st.dataframe(df, use_container_width=True)

    # =============================
    # GRAFIK STREAMLIT
    # =============================
    st.subheader("📈 Grafik f(x)")
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

