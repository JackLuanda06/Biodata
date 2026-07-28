import streamlit as st

st.set_page_config(layout="wide")

st.title("PORTOFOLIO 📁")
st.divider()

st.header("3D RIGGING 🦴")
st.subheader("PROJECT 🔥")

col_sr, col_des = st.columns([4,4], vertical_alignment="center")

with col_sr:
     st.video("Showreel.mp4", subtitles=None, width=500)

with col_des:
    st.markdown(
    """
        **Spesialisasi:**
        * *Custom Rig Mechanics* 
        * Optimasi *Joint Orientations* & *Weight Painting*
        * Rig yang siap digunakan untuk Autodesk Maya.
        
        ---
        
        > **Catatan Showreel:**  
        > Sebagian besar proyek besar yang saya kerjakan di studio animasi dilindungi oleh dokumen **NDA (Non-Disclosure Agreement)**, sehingga tidak semua karya dapat dipublikasikan secara bebas di media sosial. Showreel di samping adalah beberapa kompilasi pengerjaan yang dapat saya bagikan.
        """)

col_asa, col_des_asa = st.columns([4,4], vertical_alignment="center")

with col_asa:
     st.image("Poster Asa.png", width=300)

with col_des_asa:
     st.markdown("""
        **Sebagai:**
        * Script Writer 
        * 3D Rigging Artist
                 
        ---
                 
        > **Asa**, seorang gadis disabilitas penjual asongan, hidup sebatang kara di tengah hiruk-pikuk perkotaan yang dingin. 
        > Namun, sore itu menjadi titik balik hidupnya saat dua takdir mempertemukannya sekaligus: sebuah buku misterius milik seorang pria yang terjatuh, dan seekor anjing kecil disabilitas yang terlantar.
    """)

col_mpt, col_des_mpt = st.columns([4,4], vertical_alignment="center")

with col_mpt:
     st.image("Poster Mepet.jpeg", width=300)

with col_des_mpt:
     st.markdown("""
        **Sebagai:**
        * Film Director
        * 3D Rigging Artist
                 
        ---
                 
        > **Lima menit** menuju acara penyuluhan tanpa satu pun materi presentasi yang rampung! 
        > 
        > Lima mahasiswa peserta KKN kini harus berlomba dengan mepetnya waktu. Mereka dipaksa memeras otak untuk menciptakan alasan paling logis dan tepat demi menutupi kelalaian mereka sebelum Pak Kades yang ganas dan kekar datang menuntut pertanggungjawaban.
    """)
st.divider()
st.subheader("SERTIFIKAT 📃")

col_amk, col_walrus = st.columns([4,4], vertical_alignment="center")

with col_amk:
    st.image("SertifikatAmikom.png", caption="Proyek kolaborasi bersama tim saat kelas 10 SMK yang berhasil meraih Juara 1 Kategori Terfavorit dan Juara 2 Umum.")
    st.link_button("Click Me", "https://youtu.be/CZltuDC_OPY?si=8JIhI-M0fsvUkCW7")
with col_walrus:
    st.image("Juara 1 - Walrus Team.jpg", caption="Kompetisi PPATK (2024)Proyek kolaborasi bersama tim yang berhasil meraih Juara 1 Umum.")
    st.link_button("Click Me", "https://youtu.be/33E4YSyUyQI?si=AIWPuJnHLf96PBF2")

st.divider()
st.subheader("PROGRAMING 💻")

col_vid, col_kode = st.columns([4,4], vertical_alignment="center")

with col_vid:
    st.video("AyoNabung.mp4", subtitles=None)

code = """import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#Membuat Judul
st.set_page_config(page_icon="Icon.png", page_title="Catatan Keuangan")
col1, col2, col3 = st.columns(3)
with col2:
    st.image("Logo Gunadar.jpg", use_container_width=True)
st.title("Catatan Keuangan")
st.markdown("Masukkan Rincian Keuangan Anda")

#Membuat Koneksi Ke GSheets
conn = st.connection("gsheets", type=GSheetsConnection)

#Koneksikan Table Dalam Gsheets
existing_data = conn.read(worksheet="Catatan", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

#List Jenis Tabungan dan Bank
tabungan =[
    "Tabungan",
    "Giro",
    "Deposit",
    "Anak",
    "Investasi"
]

bank =[
    "BCA",
    "BRI",
    "BNI",
    "Mandiri",
]

#Window Form Pengguna Baru
with st.form(key="Form Pengguna"):
    nama_pengguna = st.text_input(label="Nama pengguna*")
    jenis_tabungan = st.selectbox("Jenis Tabungan", options=tabungan, index=None)
    bank_tujuan = st.selectbox("Bank Yang Dituju", options=bank, index=None)
    nominal_tabungan = st.text_input("Nominal Bulan Ini")
    tanggal_input = st.date_input(label="Tanggal Hari Ini")
    info_tambahan = st.text_area(label="Informasi")

    st.markdown("*Diperlukan")

    submit_button = st.form_submit_button(label="Submit", type="primary")

    if submit_button:
        #Cek Ketentuan Form
        if not nama_pengguna or not jenis_tabungan:
            st.warning("Data Belum Lengkap")
            st.stop()
        elif existing_data["Nama Pengguna"].astype(str).str.contains(nama_pengguna, na=False).any():
            st.warning("Nama Sudah Terdaftar")
            st.stop()
        else:
            #Membuat kolom baru pada data Gsheet
            data_pengguna = pd.DataFrame(
                [
                    {
                        "Nama Pengguna": nama_pengguna,
                        "Jenis Tabungan": jenis_tabungan,
                        "Bank": bank_tujuan,
                        "Nominal": nominal_tabungan,
                        "Tanggal": tanggal_input.strftime("%Y-%m-%d"),
                        "Info Tambahan": info_tambahan,
                    }
                ]
            )

            update_data = pd.concat([existing_data, data_pengguna], ignore_index=True)

            #Koneksikan GSheet dengan data form
            conn.update(worksheet="Catatan", data=update_data)

            st.success("Data Berhasil Ditambahkan")
            st.balloons()
"""

with col_kode:
        st.markdown("### **Aplikasi Input Data (Streamlit + GSheets API)**")
        st.markdown("""
        Aplikasi web interaktif untuk mengelola dan memasukkan data transaksi secara *real-time* langsung ke backend Google Sheets menggunakan Python.
        
        **Fitur & Tech Stack:**
        * **Frontend:** Streamlit Framework
        * **Database Backend:** Google Sheets API via `streamlit-gsheets`
        * **Fitur:** Validasi form input, klasifikasi jenis tabungan, dan *update* data otomatis.
        """)
with st.expander("🔍 Lihat Source Code Lengkap (Python)"):
     st.code(code)

st.divider()

cprev, cnext = st.columns(2)

with cprev:
    st.page_link("pages/1_AboutMe.py", label="Kembali", icon="⬅️")

with cnext:
    st.page_link("pages/3_Contact.py", label="Lanjut", icon="➡️", icon_position="right")
