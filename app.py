import streamlit as st

# Mengatur judul tab browser
st.set_page_config(page_title="Aplikasi pertamaku", page_icon="+")

# menampilkan judul dan teks di web
st.title("Aplikasi Streamlit pertamaku!")
st.write("Halo dunia! jika kamu bisa melihat halaman ini, berarti kamu sudah **berhasil** meng-upload dan mendeploy aplikasi streamlit ari GitHub.")

st.divider() # Garis Pembatas

# input sederhana
nama = st.text_input("Siapa Namamu?")

# tombol interaktif
if st.button("klik saya!"):
    if nama:
         st.succes(f"halo, {nama}! Selamat belajar streamlit. kamu hebat !")
         st.ballons() # Memunculkan animasi balon
    else:
        st.warning("isi namamu dulu di kotak atas ya!")