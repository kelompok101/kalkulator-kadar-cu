import streamlit as st

# Judul aplikasi
st.title('Kalkulator Cepat Menghitung Kadar Cu')  

st.markdown('---')
        
# Intro Aplikasi
st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu dalam sampel makanan yang sudah dianalisis melalui Spektrofotometri Serapan Atom (SAA)''')

st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)


# Nama kelompok dan anggota tim
nama_kelompok = "Kelompok 6"
anggota_tim = ("1. Andiani Putri Wijayanti (2320507)\n"
               "2. Azizah Lintang Maylya (2320511)\n"
               "3. Dimas Farrel Arunajati (2320519)\n"
               "4. Fadhlurahman Rayyandani Shafwan (2320522)\n"
               "5. Putri Chalis Lestari (2320544)\n"
               "6. Ratu Amalia Zahara (2320551)")

# Tampilkan nama kelompok dan anggota tim dengan pemformatan khusus
st.info(f"Kelompok: {nama_kelompok}")
st.write("Anggota tim:")
st.write(anggota_tim.replace("\n", "\n"))

st.header('Perhitungan kadar c terukur')

st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

y = st.number_input("Masukkan nilai y:", step=0.0001)
st.write("Nilai absorbansi adalah", y)
a = st.number_input("Masukkan nilai a:", step=0.0001)
st.write("Nilai intercept adalah", a)
b = st.number_input("Masukkan nilai b:", step=0.0001)
st.write("Nilai slope adalah", b)

y2 = st.number_input("Masukkan nilai y2:", step=0.0001)
st.write("Nilai absorbansi adalah", y2)
a2 = st.number_input("Masukkan nilai a2:", step=0.0001)
st.write("Nilai intercept adalah", a2)
b2 = st.number_input("Masukkan nilai b2:", step=0.0001)
st.write("Nilai slope adalah", b2)

hitung_x = st.button("Hitung kadar c terukur")

if hitung_x:
    x = (y - a) / b
    x2 = (y2 - a2) / b2
    rata_rata_x = (x + x2) / 2
    st.write(f"Hasil perhitungan x = {rata_rata_x} (mg/L)")

st.header("Cemaran Kadar Cu Dalam Sampel")

st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

c_terukur = st.number_input("Masukkan kadar C terukur (mg/L)", step=0.0001)
st.write("Nilai kadar C terukur adalah", c_terukur)
v = st.number_input("Masukkan nilai V (L):", step=0.0001)
st.write("Nilai volume adalah", v)
FP = st.number_input("Masukkan nilai FP:", step=0.0001)
st.write("Nilai FP adalah", FP)
bobot_sampel = st.number_input("Masukkan nilai bobot sampel (gram):", step=0.0001)
st.write("Nilai bobot sampel adalah", bobot_sampel)

hitung_cu = st.button("Hitung kadar cemaran Cu")

if hitung_cu:
    kadar_cemaran_cu = (c_terukur * v * FP) / (bobot_sampel * 0.001)
    st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm")