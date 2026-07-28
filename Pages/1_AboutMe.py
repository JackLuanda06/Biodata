import streamlit as st

st.set_page_config(layout="wide")

st.title("ABOUT ME 👨‍💻")
st.header("GET TO KNOW ME:")
st.divider()

story, skill, experience = st.tabs(["📖 My Story", "🛠️ Skills", "💼 Experience"])

with story:
    st.title("My Story")
    st.markdown("""
    Perjalanan profesional saya dimulai lebih awal sejak masa sekolah di SMK Raden Umar Said Kudus. Pada tahun 2023, saat masih duduk di kelas 11, saya mendapatkan kesempatan luar biasa untuk magang selama satu tahun penuh di RUS Animation Studio sebagai 3D Rigging Artist. Di sana, saya terlibat langsung dalam memproduksi berbagai proyek animasi besar seperti Wakakibo Season 1, La Luz de Aisha, Nyla, dan masih banyak lagi.

    Setahun kemudian, pada tahun 2024, saya lulus dari SMK dengan nilai yang memuaskan dan membawa bekal skill yang sudah matang ditempa oleh industri. Tak lama setelah lulus, tepatnya pada bulan Oktober 2024, saya berhasil mewujudkan salah satu impian terbesar saya sejak sekolah: diterima bekerja di Shoh Entertainment. Selama 7 bulan mendedikasikan diri di sana, saya sangat bersyukur bisa mengasah keahlian teknis ke tingkat yang lebih tinggi, mendapatkan banyak skill baru, sekaligus membangun relasi profesional yang berharga di industri animasi.
    """)

with skill:
    st.title("Skills")
    c1, c2 = st.columns(2)
    with c1:
        st.info("""
        3D Rigging
        * Autodesk Maya 
        * Joint Orientations & Advanced Weight Painting
        * Custom Rig Mechanics 
        """)
    with c2:
        st.success("""
        Programming
        * Python (Scripting untuk Maya)
        * Streamlit Framework & Google Sheets Integration
        """)

with experience:
    st.title("Pengalaman Kerja & Pendidikan")
    
    st.markdown("""
    **Pengalaman Kerja**
                
    1. 3D Rigging Artist = Shoh Entertainment (Oktober 2024 – Mei 2025 · 7 Bulan)
    
    2. 3D Rigging Artist Intern = RUS Animation Studio (2023 – 2024 · 1 Tahun)
    Featured Projects: Wakakibo Season 1, La Luz de Aisha, Nyla.
    
    **Pendidikan**
                    
    1. S1 Teknik Informatika = Universitas Gunadarma (Angkatan 2025 – Sekarang)
    
    2. Animasi 3D = SMK Raden Umar Said Kudus (Lulus 2024)
    """)

st.divider()

cprev, cnext = st.columns(2)

with cprev:
    st.page_link("Home.py", label="Kembali", icon="⬅️")

with cnext:
    st.page_link("pages/2_Portofolio.py", label="Lanjut", icon="➡️", icon_position="right")