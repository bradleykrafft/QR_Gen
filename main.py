
import streamlit as st
from file_placements import *

st.title("Easy QR")

data = st.text_input("Enter link to convert to QR code.")
save_file_as = st.text_input("Enter a name for the file.")
if 'file_location' not in st.session_state:
    st.session_state['file_location'] = "C:\\Users\\public\\downloads"

button= st.button("Select Location to Save.")
if button:
    st.session_state['file_location'] = get_file_path()


if st.button("Click To Gen"):
    qr_code_gen(data,st.session_state['file_location'],save_file_as)
    st.success("File saved at: ")


