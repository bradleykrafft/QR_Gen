
import streamlit as st
from streamlit import session_state

from file_placements import *

st.title("Easy QR")

data = st.text_input("Enter link to convert to QR code.")
save_file_as = st.text_input("Enter a name for the file.") + ".png"

if 'generated_file' not in session_state:
    st.session_state['generated_file'] = io.BytesIO()

# if 'file_location' not in st.session_state:
#     st.session_state['file_location'] = "C:\\Users\\public\\downloads"
# button= st.button("Select Location to Save.")
# if button:
#     st.session_state['file_location'] = get_file_path()
# if st.button("Click To Gen"):
#     qr_code_gen(data,st.session_state['file_location'],save_file_as)
#     st.success("File saved at: ")
if st.button("Generate QR_Code"):
    #img_file = st.write(qr_code_gen(data))
    img_file = qr_code_gen(data)
    st.success("Now download your QR Code :)")

st.download_button("Save QRCode.",
                   data=st.session_state.generated_file,
                   file_name=save_file_as,
                   mime="image/png")


