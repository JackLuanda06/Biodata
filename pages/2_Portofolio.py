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
     st.link_button("Click Me", "https://youtu.be/CZltuDC_OPY?si=8JIhI-M0fsvUkCW7")

col_ung, col_des_ung = st.columns([4,4], vertical_alignment="center")

with col_ung:
     st.image("Uang Bersih.jpg", width=300)

with col_des_ung:
     st.markdown("""
        **Sebagai:**
        * Scriptwriter
        * 3D Rigging Artist
                      
        ---
                      
        > Andrew adalah seekor kucing yang bekerja di sebuah perusahaan swasta. Suatu hari di tengah 
        malam yang sunyi, ia lembur mengerjakan pekerjaan tambahan yang harus diselesaikan pada 
        malam itu. Namun, ia tiba tiba mendapatkan perintah dari bosnya yang sangat mencurigakan. 
        Karena itu perintah atasan, Andrew tanpa pikir panjang langsung mematuhi perintah tersebut 
        hingga suatu kejadian tak diinginkan pun terjadi
    """)
     st.link_button("Click Me", "https://youtu.be/33E4YSyUyQI?si=AIWPuJnHLf96PBF2")
     
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
with col_walrus:
    st.image("Juara 1 - Walrus Team.jpg", caption="Kompetisi PPATK (2024)Proyek kolaborasi bersama tim yang berhasil meraih Juara 1 Umum.")

st.divider()
st.subheader("PROGRAMING 💻")

col_vid, col_kode = st.columns([4,4], vertical_alignment="center")

with col_vid:
    st.video("AyoNabung.mp4", subtitles=None)

with col_kode:
        st.markdown("### **Aplikasi Input Data (Streamlit + GSheets API)**")
        st.markdown("""
        Aplikasi web interaktif untuk mengelola dan memasukkan data transaksi secara *real-time* langsung ke backend Google Sheets menggunakan Python.
        
        **Fitur & Tech Stack:**
        * **Frontend:** Streamlit Framework
        * **Database Backend:** Google Sheets API via `streamlit-gsheets`
        * **Fitur:** Validasi form input, klasifikasi jenis tabungan, dan *update* data otomatis.
        """)

st.divider()

cprev, cnext = st.columns(2)

with cprev:
    st.page_link("pages/1_AboutMe.py", label="Kembali", icon="⬅️")

with cnext:
    st.page_link("pages/3_Contact.py", label="Lanjut", icon="➡️", icon_position="right")
