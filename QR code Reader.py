from pyzbar.pyzbar import decode
from PIL import Image
print("Welcome to QR code reader")

img = Image.open("qrcode.png")
d = decode(img)

print(d[0].data.decode())