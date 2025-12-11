import streamlit as st
import numpy as np
import pandas as pd
import math

# =============================
# MENU PILIHAN FONT UNTUK TITLE
# =============================
font_choice = st.sidebar.selectbox(
    "Pilih Font Title",
    ["Poppins", "Arial", "Georgia", "Times New Roman", "Courier New", "Roboto"]
)

# CSS import Google Font (jika perlu)
google_font_url = {
    "Poppins": "Poppins",
    "Roboto": "Roboto",
    "Arial": "",
    "Georgia": "",
    "Times New Roman": "",
    "Courier New": ""
}

if google_font_url[font_choice] != "":
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family={google_font_url[font_choice].replace(' ', '+')}:wght@400;600&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# =============================
# CUSTOM CSS DENGAN FONT TITLE
# =============================
st.markdown(f"""
<style>
    body {{
        background: #f4f7f9;
    }}

    h1 {{
        font-family: '{font_choice}', sans-serif !important;
        text-align: center;
        color: #1976D2;
        margin-bottom: 30px;
    }}

    .card {{
        padding: 20px;
        background: white;
        border-radius: 12px;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }}
</style>
""", unsafe_allow_html=True)

# =============================
# TITLE
# =============================
st.markdown(f"<h1>Kalkulator SPNL - Metode Regula Falsi</h1>", unsafe_allow_html=True)

# =============================
# STEP 1
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 1: Masukkan Persamaan f(x)")
fungsi = st.text_input("Contoh: x**3 - x - 2", value="x**3 - x - 2")
st.markdown("</div>", unsafe_allow_html=True)

# =============================
# STEP 2
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 2: Pilih Interval")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("a", value=1.0)
with col2:
    b = st.number_input("b", value=2.0)

def f(x):
    return eval(fungsi)

fa = f(a)
fb = f(b)

st.write(f"f(a) = {fa}")
st.write(f"f(b) = {fb}")

if fa * fb > 0:
    st.error("Interval tidak valid! f(a) dan f(b) tidak bertanda berbeda.")
else:
    st.success("Interval valid ✓")

st.markdown("</div>", unsafe_allow_html=True)

# =============================
# STEP 3
# =============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Step 3: Pengaturan Lanjut")

col1, col2 = st.columns(2)
with col1:
    max_iter = st.number_input("Maksimum Iterasi", value=50)
with col2:
    tol = st.number_input("Toleransi Error", value=0.000001, format="%.10f")

hitung_button = st.button("Hitung Akar")
st.markdown("</div>", unsafe_allow_html=True)

# =============================
# METODE REGULA FALSI
# =============================
if hitung_button:

    if fa * fb > 0:
        st.error("Perhitungan dibatalkan: interval tidak valid.")
    else:
        a0, b0 = a, b
        fa = f(a0)
        fb = f(b0)
        xr_old = 0
        data_iterasi = []

        for i in range(1, max_iter + 1):
            xr = (a0 * fb - b0 * fa) / (fb - fa)
            fxr = f(xr)
            error = abs(xr - xr_old)

            data_iterasi.append([i, a0, b0, xr, fxr, error])

            if error < tol:
                break

            if fa * fxr < 0:
                b0 = xr
                fb = fxr
            else:
                a0 = xr
                fa = fxr

            xr_old = xr

        # Hasil
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Hasil Perhitungan")
        st.success(f"""
        **Akar mendekati:** {xr}  
        **Error akhir:** {error}  
        **Total iterasi:** {len(data_iterasi)}  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        # Tabel
        df = pd.DataFrame(data_iterasi,
            columns=["Iterasi", "a", "b", "xr", "f(xr)", "Error"])
        
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Tabel Iterasi")
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Grafik
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Grafik Fungsi f(x)")

        x_vals = np.linspace(a - 2, b + 2, 400)
        y_vals = [f(x) for x in x_vals]

        fig, ax = plt.subplots(figsize=(7,4))
        ax.plot(x_vals, y_vals, label="f(x)")
        ax.axhline(0, color='black', linewidth=1)
        ax.scatter([xr], [f(xr)], color='red', label="Akar", zorder=5)

        ax.set_title("Grafik Fungsi")
        ax.legend()
        st.pyplot(fig)

        st.markdown("</div>", unsafe_allow_html=True)
