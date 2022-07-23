import pyqrcode
import png

link = "https://www.bing.com"

qr_code = pyqrcode.create(link)
qr_code.png(r"D:\Python_Prpjects\18_QR_Code\instagram.png", scale=5)
