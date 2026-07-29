import streamlit as st

st.set_page_config(layout="wide")

col_foto, col_judul = st.columns([1,4], vertical_alignment="center")

with col_foto:
    st.image("Foto Dzaky.jpeg", width=450)

with col_judul:
    st.markdown("""
        <h1 style='margin-bottom: 0px; padding-bottom: 0px;'>Hi, I'm Dzaky Aqiilah Luanda</h1>
        <p style='font-size: 1.3rem; font-weight: bold; margin-top: 5px; color: #ced4da;'>
            Informatics Engineering Student | 3D Rigger | ScriptWriter
        </p>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""
Halo! Saya seorang 3D Rigging Artist yang sangat menyukai seni animasi dengan logika teknis. 

Saya menghabiskan masa studi di SMK Raden Umar Said Kudus dengan fokus pada Animasi 3D termasuk pengalaman berharga magang selama 1 tahun di RUS Animation Studio dan bekerja selama 7 bulan di Shoh Entertainment, Kemudian saya memutuskan untuk melangkah lebih jauh.

Saat ini, saya aktif menempuh kuliah di jurusan Teknik Informatika Universitas Gunadarma. Langkah ini saya ambil untuk memperluas cakrawala keahlian teknis saya pada (programming/scripting), demi menghadirkan solusi rigging yang lebih adaptif, efisien dan siap bersaing di dunia kerja modern.
""")

st.markdown("#### **🧭 Ketahui saya lebih dalam:**")

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_AboutMe.py", label="About Me", icon="👨‍💻")

with col2:
    st.page_link("pages/2_Portofolio.py", label="Portofolio", icon="📁")

with col3:
    st.page_link("pages/3_Contact.py", label="Contact", icon="✉️")