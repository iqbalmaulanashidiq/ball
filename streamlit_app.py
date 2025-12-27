import streamlit as st
import numpy as np
import pandas as pd
import math
import plotly.express as px

# =============================
# TOGGLE MODE
# =============================
mode = st.toggle("🌙 Dark Mode", value=False)

# =============================
# WARNA DYNAMIC
# =============================
if mode:  # Dark Mode
    bg = "#0f172a"
    card = "#1e293b"
    text = "#e5e7eb"
    accent = "#60a5fa"
else:     # Light Mode
    bg = "#f8fafc"
    card = "#ffffff"
    text = "#0f172a"
    accent = "#2563eb"

# =============================
# CSS
# =============================
st.markdown(f"""
<style>
html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background-color: {bg};
    color: {text};
}}

h1 {{
    text-align: center;
    font-weight: 800;
    color: {text};
    margin-bottom: 2rem;
}}

.block-container {{
    padding-top: 2rem;
}}

.stTextInput input,
.stNumberInput input {{
    background: {card};
    color: {text};
    border-radius: 10px;
    border: 1px solid #e5e7eb;
}}

.stButton button {{
    background: {accent};
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    border: none;
}}

.stButton button:hover {{
    opacity: 0.85;
}}

[data-testid="stDataFrame"] {{
    background: transparent !important;
}}

section[data-testid="stSidebar"],
div[data-testid="stDecoration"],
div[data-testid="stToolbar"] {{
    display: none;
}}
</style>
""", unsafe_allow_html=True)

# =============================
# JUDUL & INPUT FUNGSI
# =============================
st.title("🔹 Metode Regula Falsi")
fungsi = st.text_input("Masukkan fungsi f(x)", value="x**3 - x - 2")

# =============================
# INTERVAL
# =============================
st.subheader("2️⃣ Interval")
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("a", value=1.0)
with col2:
    b = st.number_input("b", value=2.0)

# =============================
# VALIDASI FUNGSI
# =============================
def f(x):
    try:
        return eval(fungsi, {"x": x, "np": np, "math": math})
    except:
        return np.nan

fa, fb = f(a), f(b)

if np.isnan(fa) or np.isnan(fb):
    st.error("f(a) atau f(b) tidak valid. Periksa fungsi Anda!")
    valid_interval = False
else:
    st.write(f"f(a) = {fa}")
    st.write(f"f(b) = {fb}")
    valid_interval = fa * fb < 0
    if valid_interval:
        st.success("Interval valid ✓")
    else:
        st.error("Interval tidak valid ❌")

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
# HITUNG AKAR
# =============================
if st.button("🔍 Hitung Akar") and valid_interval:

    a0, b0 = a, b
    fa, fb = f(a0), f(b0)
    xr_old = a0
    data = []

    for i in range(1, int(max_iter) + 1):
        if fb - fa == 0:
            st.error("Pembagi = 0. Metode gagal.")
            break

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
    # TABEL
    # =============================
    df = pd.DataFrame(data, columns=["Iterasi", "a", "b", "xr", "f(xr)", "Error"])
    st.dataframe(df.style.set_properties(**{'background-color': card, 'color': text}), use_container_width=True)

    # =============================
    # GRAFIK INTERAKTIF PLOTLY
    # =============================
    st.subheader("📈 Grafik f(x)")
    x_vals = np.linspace(a - 2, b + 2, 400)
    y_vals = [f(x) for x in x_vals]
    df_plot = pd.DataFrame({"x": x_vals, "f(x)": y_vals})

    fig = px.line(df_plot, x='x', y='f(x)', title="Grafik f(x)")
    fig.update_traces(line_color=accent)
    fig.update_layout(
        plot_bgcolor=bg,
        paper_bgcolor=bg,
        font_color=text,
        xaxis_title="x",
        yaxis_title="f(x)"
    )

    # Tampilkan titik akar
    fig.add_scatter(x=[xr], y=[f(xr)], mode='markers', marker=dict(color='red', size=10), name="Akar")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"**Titik Akar:** x = `{xr}`, f(x) = `{f(xr)}`")
