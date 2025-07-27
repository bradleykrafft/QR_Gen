import os
import streamlit as st
import qrcode
from streamlit import empty, exception
from pathlib import Path

st.title("Easy QR")

data = st.text_input("Enter link to convert to QR code.")
save_file_as = st.text_input("Enter a name for the file.")

# Generate and save the QR Code as an image
if st.button("Generate QR code."):
    st.write(f"Generating QR code: {data} ")
    try:
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Thickness of the border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        if save_file_as == empty:
             filename = "MY_QRCode"
        folder_path = downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        #folder_path = str(os.path.join(Path.home(), "Downloads"))
        img.save(f"{folder_path}\\{save_file_as}.png")
    except Exception as e:
        print(e)













