import streamlit as st
import band_utils

st.title("Band name Generator")
song_style = st.sidebar.selectbox("Pick song styles", ("Rock", "Ballad", "Rap", "Latin", "Classic", "Metal"))

response = band_utils.generate_bandname_and_songlist(song_style)
st.header(response["song_name"])
song_names = response["band_name_list"].split(",")
st.write("** Song Names **")
for song in song_names:
    st.write("-- " + song)