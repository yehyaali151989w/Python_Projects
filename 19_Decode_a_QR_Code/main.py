from pyzbar.pyzbar import decode
from PIL import Image

decocdeQR = decode(Image.open(
    r'D:\Python_Prpjects\19_Decode_a_QR_Code\instagram.png'))

print(decocdeQR[0].data.decode('ascii'))
