
import streamlit as st
from pandas.core.ops.docstrings import reverse_op
from streamlit import session_state

from file_placements import *

st.title("Easy QR")

data = st.text_input("Enter link to convert to QR code.")
save_file_as = st.text_input("Enter a name for the file.")

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
    img = qr_code_gen(data)
    st.write(img)
    # img.seek(0)
    #st.session_state.generated_file = Image.open(img)
    st.session_state.generated_file = img
    # st.write(st.session_state.generated_file)
    st.success("Now download your QR Code :)")
#
# image_bytes.seek(0)
# reopened_image = Image.open(image_bytes)
# reopened_image.show()
st.download_button(label="Download QRCode.",
                   data=st.session_state.generated_file,
                   file_name=f"{save_file_as}.png",
                   mime="image/png")


