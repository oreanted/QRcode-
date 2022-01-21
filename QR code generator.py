from qrcode import QRCode
import pyqrcode 

print("Welcome to QR code generator:")

msg = input("Type to Secret message : ")
code = pyqrcode.create(msg)

code.png("qrcode1.png", scale= 5)
print("QR code generated succesfully ")