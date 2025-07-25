import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor  # Bisa diganti jika pakai model lain

# --- Load Model ---
# Ganti dengan path model kamu jika sudah ada
# model = joblib.load('model.pkl')

# Dummy model (ganti dengan model asli kamu)
model = RandomForestRegressor()
model.fit(np.random.rand(100, 7), np.random.rand(100))  # dummy training agar tidak error

# --- Setup ---
st.title("Prediksi Inflasi Indonesia")

# --- Sidebar Inputs ---
st.header("Input Parameter")

tahun = st.selectbox("Tahun", list(range(2020, 2031)))
bulan = st.selectbox("Bulan", list(range(1, 13)))  # bulan sudah di-encode, cukup 1 bulan

harga_beras = st.number_input("Harga Beras", min_value=0.0, format="%.2f")
harga_bbm = st.number_input("Harga BBM", min_value=0.0, format="%.2f")
bi_rate = st.number_input("BI Rate", min_value=0.0, format="%.2f")
nilai_tukar = st.number_input("Nilai Tukar IDR/USD", min_value=0.0, format="%.2f")
inflasi_inti = st.number_input("Inflasi Inti", min_value=0.0, format="%.2f")

# --- Validasi & Prediksi ---
if st.button("Prediksi Inflasi"):
    # Bentuk dataframe input
    input_data = pd.DataFrame({
        "Tahun": [tahun],
        "Bulan": [bulan],
        "Harga_Beras": [harga_beras],
        "Harga_BBM": [harga_bbm],
        "BI_Rate": [bi_rate],
        "Nilai_Tukar": [nilai_tukar],
        "Inflasi_Inti": [inflasi_inti]
    })

    try:
        prediksi = model.predict(input_data)[0]
        st.subheader("Hasil Prediksi")
        st.success(f"Prediksi Inflasi: {prediksi:.2f}%")

        st.subheader("Data yang Dimasukkan")
        st.table(input_data)

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses prediksi: {e}")
