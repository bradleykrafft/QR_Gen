import qrcode
# import wx
import PIL
import base64
import io
import os
from pathlib import Path
from PIL import Image


# def get_file_path():
#     app = wx.App(False)
#     frame = wx.Frame(None, -1, "Hidden Frame")  # Create a hidden frame for the dialog
#
#     # Create a directory dialog
#     dialog = wx.DirDialog(frame, "Choose a directory", style=wx.DD_DEFAULT_STYLE)
#
#     if dialog.ShowModal() == wx.ID_OK:  # If the user selects a directory
#         selected_directory = dialog.GetPath()  # Get the selected directory as a string
#
#         dialog.Destroy()  # Destroy the dialog to free resources
#         frame.Destroy()  # Destroy the hidden frame
#         return selected_directory


def qr_code_gen(link : str):
    # selected_dir = file_path
    # normalized_path = Path(selected_dir)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    byte_stream = io.BytesIO()
    img.save(byte_stream, format='PNG')
    byte_data = byte_stream.getvalue()
    return byte_data


