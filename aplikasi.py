import streamlit as st

st.title("🏍️ Aplikasi Penghitung Waktu Baku Produksi Motor")

st.markdown("""
Aplikasi ini digunakan untuk menghitung **waktu baku** berdasarkan:
- Waktu siklus (cycle time)
- Faktor kelonggaran (allowance factor)
""")

# Input dari pengguna
ct = st.number_input("⏱️ Masukkan Waktu Siklus (dalam detik):", min_value=0.0, value=60.0)
af_percent = st.number_input("📉 Masukkan Faktor Kelonggaran (dalam persen):", min_value=0.0, value=15.0)

# Konversi persen ke desimal
af = af_percent / 100

# Hitung waktu baku
waktu_baku = ct * (1 + af)

# Output hasil
st.subheader("📊 Hasil Perhitungan:")
st.write(f"**Waktu Baku = {ct} × (1 + {af:.2f}) = {waktu_baku:.2f} detik**")

# Penjelasan tambahan
st.info("Waktu baku adalah waktu standar yang digunakan untuk satu siklus kerja, termasuk waktu kelonggaran.")
