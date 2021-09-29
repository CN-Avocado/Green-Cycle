import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=8,
    error_correction=ERROR_CORRECT_L,
    box_size=5,
    border=8
)
qr.add_data('Goyave')
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")
img.save('qrcode.png')