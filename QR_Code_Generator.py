import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border =4,
)


qr.add_data("https://www.youtube.com/watch?v=uW0zmBZpoWM") # add your link here

img =qr.make_image()
img.save("qrcode.jpg")
