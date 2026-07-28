import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("CONTACT 📞")
st.divider()

st.header("HUBUNGI SAYA UNTUK MEMBUAT SESUATU YANG LUAR BIASA ")
st.markdown("""Punya ide proyek 3D Rigging,  atau sekadar ingin berdiskusi seputar dunia animation pipeline dan tech? Jangan ragu untuk menyapa! Layar DM dan kotak masuk saya selalu terbuka untuk peluang baru. """)

st.success("🟢 **Status:** *Open for Freelance Projects & Collaborations!*")

col_info, col_form = st.columns([4, 4])

with col_info:
    with st.container(border=True):
        st.markdown("Hubungi Saya Melalui:")
        st.markdown("**Email:** dzaky.luanda2006@gmail.com")
        st.markdown("**Instagram:** Click Melalui Link Dibawah Ini Untuk Detailnya ⬇️")
        st.link_button("Instagram", "https://www.instagram.com/kyy.3d?igsh=MTI0aWdhY3c5b3I2Zw==", icon="📱")
        st.markdown("**Linkedin:** Click Melalui Link Dibawah Ini Untuk Detailnya ⬇️")
        st.link_button("Linkedin", "https://www.linkedin.com/in/dzaky-luanda-8b2735253/", icon="💼")
        st.download_button(
            label=" Download CV / Resume (PDF)",
            data=open("CV Dzaky Aqiilah Luanda.pdf", "rb"),
            file_name="CV Dzaky Aqiilah Luanda.pdf",
            use_container_width=True
        )
        st.divider()
        st.markdown("**Jam Response:** Pasti Segera akan saya Balas dalam Waktu 1 x 24 jam")
        
wb_discord = st.secrets["web_discord"]

def send_to_discord(nama, email, subjek, pesan):
    form = {
        "embeds": [
            {
                "title": f"📩 Pesan Baru dari Website: {subjek}",
                "color": 3447003,  # Warna biru
                "fields": [
                    {"name": "👤 Nama", "value": nama, "inline": True},
                    {"name": "📧 Email", "value": email, "inline": True},
                    {"name": "💬 Pesan", "value": pesan, "inline": False},
                ],
            }
        ]
    }
    response = requests.post(wb_discord, json = form)
    return response.status_code == 204

with col_form:
    with st.container(border=True):
        st.markdown("Anda Bisa langsung menghubungi saya melalu Form Dibawah ini")

        with st.form(key="Form Kerjasama", clear_on_submit=True):
            nama = st.text_input("Nama: ", placeholder="Masukan Nama")
            email = st.text_input("Email: ",placeholder="Pastikan masukkan email dengan lengkap")
            subjek = st.selectbox(
            "Tujuan Pemesanan",
            ["Freelance 3D Rigging", "Recruitment", "Diskusi", "Lainnya"]
            )
            pesan = st.text_area("Pesan: ", placeholder="Tuliskan disini")
            submit = st.form_submit_button("Kirim", use_container_width=True)

            if submit:
                if nama and email and pesan:
                    # Memanggil fungsi send_to_discord
                    success = send_to_discord(nama, email, subjek, pesan)
                    
                    if success:
                        st.toast(f"Terima kasih, {nama}! Pesan Anda berhasil terkirim.", icon= "😍")
                    else:
                        st.error("Gagal mengirim pesan. Silakan periksa koneksi internet Anda.")
                else:
                    st.warning("Mohon isi semua kolom (Nama, Email, dan Pesan) sebelum mengirim.")

st.divider()
cprev, cnext = st.columns(2)

with cprev:
    st.page_link("pages/2_Portofolio.py", label="Kembali", icon="⬅️")

with cnext:
    st.page_link("Home.py", label="Kembali Ke Home", icon="➡️", icon_position="right")